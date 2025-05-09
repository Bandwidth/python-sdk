"""
Integration tests for Bandwidth's Voice Conferences API
"""

from cgi import test
import json
import time
from typing import Dict, List, Tuple
import unittest

from hamcrest import assert_that, has_properties, not_none, instance_of, greater_than

import bandwidth
from bandwidth import ApiResponse
from bandwidth.api import calls_api
from bandwidth.models.create_call import CreateCall
from bandwidth.models.create_call_response import CreateCallResponse
from bandwidth.models.call_state import CallState
from bandwidth.models.call_state_enum import CallStateEnum
from bandwidth.models.update_call import UpdateCall
from bandwidth.models.redirect_method_enum import RedirectMethodEnum
from bandwidth.api import conferences_api
from bandwidth.models.conference_state_enum import ConferenceStateEnum
from bandwidth.models.conference_recording_metadata import ConferenceRecordingMetadata
from bandwidth.models.update_conference import UpdateConference
from bandwidth.models.update_conference_member import UpdateConferenceMember
from bandwidth.models.file_format_enum import FileFormatEnum
from bandwidth.rest import RESTClientObject, RESTResponse
from bandwidth.exceptions import ApiException, UnauthorizedException, ForbiddenException, NotFoundException
from test.utils.env_variables import *
from test.utils.call_cleanup import callCleanup


class ConferencesIntegration(unittest.TestCase):
    """
    Voice Conferences API integration test
    """

    def setUp(self):
        """
        Set up for our tests by creating the CallsApi and ConferencesApi instances
        for testing as well as the unauthorized and forbidden credentials for the 4xx tests.
        """
        configuration = bandwidth.Configuration(
            username=BW_USERNAME,
            password=BW_PASSWORD
        )
        api_client = bandwidth.ApiClient(configuration)

        self.calls_api_instance = calls_api.CallsApi(api_client)
        self.conference_api_instance = conferences_api.ConferencesApi(api_client)

        unauthorizedConfiguration = bandwidth.Configuration(
            username='bad_username',
            password='bad_password'
        )
        unauthorized_api_client = bandwidth.ApiClient(unauthorizedConfiguration)
        self.unauthorized_api_instance = conferences_api.ConferencesApi(unauthorized_api_client)

        forbiddenConfiguration = bandwidth.Configuration(
            username=FORBIDDEN_USERNAME,
            password=FORBIDDEN_PASSWORD
        )
        forbidden_api_client = bandwidth.ApiClient(forbiddenConfiguration)
        self.forbidden_api_instance = conferences_api.ConferencesApi(forbidden_api_client)

        # Rest client for interacting with Manteca
        self.rest_client = RESTClientObject(bandwidth.Configuration.get_default_copy())
        configuration = bandwidth.Configuration(
            username=BW_USERNAME,
            password=BW_PASSWORD,
        )

        self.account_id = BW_ACCOUNT_ID
        self.callIdArray = []
        self.testUpdateConf = UpdateConference(
            state=ConferenceStateEnum("active"),
            redirect_url=MANTECA_BASE_URL + "/bxml/pause",
            redirect_method=RedirectMethodEnum("POST"),
            username="mySecretUsername",
            password="mySecretPassword1!",
            redirect_fallback_url=MANTECA_BASE_URL + "/bxml/pause",
            redirect_fallback_method=RedirectMethodEnum("POST"),
            fallback_username="mySecretUsername",
            fallback_password="mySecretPassword1!",
            tag="My Custom Tag",
        )
        self.testUpdateBxml = '<?xml version="1.0" encoding="UTF-8"?><Bxml><SpeakSentence locale="en_US" gender="female" voice="susan">This is test BXML.</SpeakSentence></Bxml>'
        self.testUpdateMember = UpdateConferenceMember(mute=False)
        self.testConfId = "Conf-id"
        self.testMemberId = "Member-Id"
        self.testRecordId = "Recording-Id"
        self.TEST_SLEEP = 3
        self.TEST_SLEEP_LONG = 10
        self.MAX_RETRIES = 40

    def tearDown(self):
        callCleanup(self)

    def assertApiException(self, context: ApiException, expectedException: ApiException, expected_status_code: int):
        """Validates that common API exceptions, (401, 403, and 404) are properly formatted
        Args:
            context (ApiException): Exception to validate
            expected_status_code (int): Expected status code
        """
        assert_that(context.exception, has_properties(
            'status', expected_status_code,
            'body', not_none()
        ))

    def create_conference(self, answer_url: str) -> Tuple[str, str]:
        """
        Create and validate a call between two bandwidth numbers.  Initializes the call with the Manteca
        system.

        Args:
            answer_url (str): The answer url for the call to create.
        Return:
            Tuple[str, str]: A tuple containing the test id created in Manteca to track this call, as well as
                            the call id for the created call.
        """

        # Initialize the call with Manteca
        response = self.rest_client.request(
            method='POST',
            url=MANTECA_BASE_URL + 'tests',
            body={
                'os': OPERATING_SYSTEM,
                'language': 'python' + PYTHON_VERSION,
                'type': 'CONFERENCE'
            }
        )

        # Get the test id from the response
        test_id = response.response.data.decode("utf-8")

        call_body = CreateCall(to=MANTECA_IDLE_NUMBER, var_from=MANTECA_ACTIVE_NUMBER,
                               application_id=MANTECA_APPLICATION_ID, answer_url=answer_url, tag=test_id)

        create_call_response: CreateCallResponse = self.calls_api_instance.create_call(
            BW_ACCOUNT_ID, call_body)

        assert_that(create_call_response, has_properties(
            "call_id", instance_of(str),
            'account_id', BW_ACCOUNT_ID,
            'application_id', MANTECA_APPLICATION_ID,
            'to', MANTECA_IDLE_NUMBER,
            'var_from', MANTECA_ACTIVE_NUMBER
        ))

        time.sleep(self.TEST_SLEEP)
        list_conferences_response = self.conference_api_instance.list_conferences_with_http_info(
            BW_ACCOUNT_ID, name=test_id)

        assert_that(list_conferences_response.status_code, 200)

        # TODO: This is not deterministic; our latest conference may not always be the one we just created due to parallelism.
        # This new solution should guarantee the right conference id is grabbed.
        conference_id = list_conferences_response.data[0].id

        get_conference_response = self.conference_api_instance.get_conference_with_http_info(
            BW_ACCOUNT_ID, conference_id)
        assert_that(get_conference_response.status_code, 200)

        self.callIdArray.append(create_call_response.call_id)

        return (test_id, create_call_response.call_id, conference_id)

    def validate_recording(self, recording: ConferenceRecordingMetadata) -> None:
        assert_that(recording.status, 'complete')
        assert_that(recording.file_format, FileFormatEnum('wav'))

    def get_test_status(self, test_id: str) -> Dict:
        """
        Get the status of the specified test by its id value from Manteca services.

        Args:
            test_id (str): The test id associated with the test to get the status of.

        Returns:
            Dict: The status of the test requested.
        """
        status_url = MANTECA_STATUS_URL + test_id
        response: RESTResponse = self.rest_client.request(
            method='GET',
            url=status_url
        )
        return json.loads(response.response.data)

    def test_conference_and_members(self):
        """
        Tests a successful flow of creating and ending a conference.
        The following endpoints are tested in this flow:
            - list_conferences
            - get_conference_information
            - get_conference_member
            - update_conference_member
            - update_conference_
            - update_conference_bxml
        """

        answer_url = MANTECA_BASE_URL + "bxml/joinConferencePause"
        (test_id, call_id, conference_id) = self.create_conference(answer_url)

        list_conferences_response = self.conference_api_instance.list_conferences_with_http_info(
            BW_ACCOUNT_ID)

        assert_that(list_conferences_response.status_code, 200)
        assert_that(list_conferences_response.data[0].name, instance_of(str))
        assert_that(list_conferences_response.data[0].id, instance_of(str))

        # TODO: Also non-deterministic; we could differentiate by conference name instead? The conference name is set to be the test id by Manteca
        # conferenceId = (list_conferences_response[0][len(list_conferences_response[0])-1].id)

        get_conference_response = self.conference_api_instance.get_conference_with_http_info(
            BW_ACCOUNT_ID, conference_id)
        assert_that(get_conference_response.status_code, 200)
        assert_that(get_conference_response.data.id, conference_id)
        assert_that(get_conference_response.data.name, instance_of(str))
        callId = (get_conference_response.data.active_members[0].call_id)
        self.callIdArray.append(callId)

        get_conference_member_response = self.conference_api_instance.get_conference_member_with_http_info(
            BW_ACCOUNT_ID, conference_id, callId)
        assert_that(get_conference_member_response.status_code, 200)
        assert_that(get_conference_member_response.data.conference_id, conference_id)
        assert_that(get_conference_member_response.data.call_id, callId)

        # time.sleep(self.TEST_SLEEP)
        update_conference_member_response = self.conference_api_instance.update_conference_member_with_http_info(
            BW_ACCOUNT_ID, conference_id, callId, self.testUpdateMember)
        assert_that(update_conference_member_response.status_code, 204)

        # time.sleep(self.TEST_SLEEP)
        update_conference_response = self.conference_api_instance.update_conference_with_http_info(
            BW_ACCOUNT_ID, conference_id, self.testUpdateConf)
        assert_that(update_conference_response.status_code, 204)

        updateBxmlBody = '<?xml version="1.0" encoding="UTF-8"?><Bxml><SpeakSentence locale="en_US" gender="female" voice="susan">This is a test bxml response</SpeakSentence></Bxml>'

        # time.sleep(self.TEST_SLEEP)
        update_conference_bxml_response = self.conference_api_instance.update_conference_bxml_with_http_info(
            BW_ACCOUNT_ID, conference_id, updateBxmlBody)
        assert_that(update_conference_bxml_response.status_code, 204)

        update_call = UpdateCall(state=CallStateEnum('completed'))
        self.calls_api_instance.update_call(
            BW_ACCOUNT_ID, call_id, update_call
        )

    @unittest.skip("PV Issues")
    def test_conference_recordings(self) -> None:
        """
        Tests a successful flow of creating a call with a recording.
        The following endpoints are tested in this flow:
            - list_conference_recordings
            - get_conference_recording
            - download_conference_recording
        """

        answer_url = MANTECA_BASE_URL + "bxml/joinConferencePause"
        (test_id, call_id, conference_id) = self.create_conference(answer_url)

        list_conferences_response = self.conference_api_instance.list_conferences(
            BW_ACCOUNT_ID)

        assert_that(list_conferences_response[1], 200)

        updateBxmlBody = '<?xml version="1.0" encoding="UTF-8"?><Bxml><StartRecording/><SpeakSentence locale="en_US" gender="female" voice="susan">This should be a conference recording.</SpeakSentence><StopRecording/></Bxml>'
        update_conference_bxml_response = self.conference_api_instance.update_conference_bxml_with_http_info(
            BW_ACCOUNT_ID, conference_id, updateBxmlBody)
        assert_that(update_conference_bxml_response.status_code, 204)

        # Poll Manteca to ensure our conference is recorded
        call_status = self.get_test_status(test_id)
        retries = 0
        while call_status['callRecorded'] == False and retries < self.MAX_RETRIES:
            time.sleep(self.TEST_SLEEP)
            call_status = self.get_test_status(test_id)
            retries += 1

        # If we failed to get a recorded conference, fail due to polling timeout
        assert call_status['callRecorded'] == True

        list_conference_recordings_response: ApiResponse = self.conference_api_instance.list_conference_recordings_with_http_info(
            BW_ACCOUNT_ID, conference_id)
        assert_that(list_conference_recordings_response.status_code, 200)

        conference_recordings = list_conference_recordings_response.data
        assert_that(len(conference_recordings), greater_than(0))

        first_recording: ConferenceRecordingMetadata = conference_recordings[0]
        self.validate_recording(first_recording)
        recording_id = first_recording.recording_id

        recording_response: ConferenceRecordingMetadata = self.conference_api_instance.get_conference_recording_with_http_info(
            BW_ACCOUNT_ID, conference_id, recording_id)
        assert_that(recording_response.status_code, 200)
        assert_that(recording_response.data.conference_id, conference_id)
        assert_that(recording_response.data.recording_id, recording_id)
        assert_that(recording_response.data.name, instance_of(str))

        self.validate_recording(recording_response.data)

        recording_media_response = self.conference_api_instance.download_conference_recording(
            BW_ACCOUNT_ID, conference_id, recording_id)
        conference_recording_media = recording_media_response

    def test_list_conferences_unauthorized(self) -> None:
        with self.assertRaises(UnauthorizedException) as context:
            self.unauthorized_api_instance.list_conferences(
                BW_ACCOUNT_ID)

        self.assertApiException(context, UnauthorizedException, 401)

    def test_list_conferences_forbidden(self) -> None:
        with self.assertRaises(ForbiddenException) as context:
            self.forbidden_api_instance.list_conferences(
                BW_ACCOUNT_ID)

        self.assertApiException(context, ForbiddenException, 403)

    def test_get_conferences_unauthorized(self) -> None:
        with self.assertRaises(UnauthorizedException) as context:
            self.unauthorized_api_instance.get_conference(
                BW_ACCOUNT_ID, self.testConfId)

        self.assertApiException(context, UnauthorizedException, 401)

    def test_get_conferences_forbidden(self) -> None:
        with self.assertRaises(ForbiddenException) as context:
            self.forbidden_api_instance.get_conference(
                BW_ACCOUNT_ID, self.testConfId)

        self.assertApiException(context, ForbiddenException, 403)

    def test_get_conferences_not_found(self) -> None:
        with self.assertRaises(NotFoundException) as context:
            self.conference_api_instance.get_conference(
                BW_ACCOUNT_ID, self.testConfId)

        self.assertApiException(context, NotFoundException, 404)

    def test_get_conference_member_unauthorized(self) -> None:
        with self.assertRaises(UnauthorizedException) as context:
            self.unauthorized_api_instance.get_conference_member(
                BW_ACCOUNT_ID, self.testConfId, self.testMemberId)

        self.assertApiException(context, UnauthorizedException, 401)

    def test_get_conference_member_forbidden(self) -> None:
        with self.assertRaises(ForbiddenException) as context:
            self.forbidden_api_instance.get_conference_member(
                BW_ACCOUNT_ID, self.testConfId, self.testMemberId)

        self.assertApiException(context, ForbiddenException, 403)

    def test_get_conference_member_not_found(self) -> None:
        with self.assertRaises(NotFoundException) as context:
            self.conference_api_instance.get_conference_member(
                BW_ACCOUNT_ID, self.testConfId, self.testMemberId)

        self.assertApiException(context, NotFoundException, 404)

    def test_list_conference_recordings_unauthorized(self) -> None:
        with self.assertRaises(UnauthorizedException) as context:
            self.unauthorized_api_instance.list_conference_recordings(
                BW_ACCOUNT_ID, self.testConfId)

        self.assertApiException(context, UnauthorizedException, 401)

    def test_list_conference_recordings_forbidden(self) -> None:
        with self.assertRaises(ForbiddenException) as context:
            self.forbidden_api_instance.list_conference_recordings(
                BW_ACCOUNT_ID, self.testConfId)

        self.assertApiException(context, ForbiddenException, 403)

    def test_get_recording_unauthorized(self) -> None:
        with self.assertRaises(UnauthorizedException) as context:
            self.unauthorized_api_instance.get_conference_recording(
                BW_ACCOUNT_ID, self.testConfId, self.testRecordId)

        self.assertApiException(context, UnauthorizedException, 401)

    def test_get_recording_forbidden(self) -> None:
        with self.assertRaises(ForbiddenException) as context:
            self.forbidden_api_instance.get_conference_recording(
                BW_ACCOUNT_ID, self.testConfId, self.testRecordId)

        self.assertApiException(context, ForbiddenException, 403)

    def test_get_conference_recording_not_found(self) -> None:
        with self.assertRaises(NotFoundException) as context:
            self.conference_api_instance.get_conference_member(
                BW_ACCOUNT_ID, self.testConfId, self.testRecordId)

        self.assertApiException(context, NotFoundException, 404)

    def test_update_conference_unauthorized(self) -> None:
        with self.assertRaises(UnauthorizedException) as context:
            self.unauthorized_api_instance.update_conference(
                BW_ACCOUNT_ID, self.testConfId, self.testUpdateConf)

        self.assertApiException(context, UnauthorizedException, 401)

    def test_update_conference_forbidden(self) -> None:
        with self.assertRaises(ForbiddenException) as context:
            self.forbidden_api_instance.update_conference(
                BW_ACCOUNT_ID, self.testConfId, self.testUpdateConf)

        self.assertApiException(context, ForbiddenException, 403)

    @unittest.skip("PV Issues")
    def test_update_conference_not_found(self) -> None:
        with self.assertRaises(NotFoundException) as context:
            self.conference_api_instance.update_conference(
                BW_ACCOUNT_ID, self.testConfId, self.testUpdateConf)

        self.assertApiException(context, NotFoundException, 404)

    def test_update_conference_bxml_unauthorized(self) -> None:
        with self.assertRaises(UnauthorizedException) as context:
            self.unauthorized_api_instance.update_conference_bxml(
                BW_ACCOUNT_ID, self.testConfId, self.testUpdateBxml)

        self.assertApiException(context, UnauthorizedException, 401)

    def test_update_conference_bxml_forbidden(self) -> None:
        with self.assertRaises(ForbiddenException) as context:
            self.forbidden_api_instance.update_conference_bxml(
                BW_ACCOUNT_ID, self.testConfId, self.testUpdateBxml)

        self.assertApiException(context, ForbiddenException, 403)

    @unittest.skip("PV Issues")
    def test_update_conference_bxml_not_found(self) -> None:
        with self.assertRaises(NotFoundException) as context:
            self.conference_api_instance.update_conference_bxml(
                BW_ACCOUNT_ID, self.testConfId, self.testUpdateBxml)

        self.assertApiException(context, NotFoundException, 404)

    def test_update_conference_member_unauthorized(self) -> None:
        with self.assertRaises(UnauthorizedException) as context:
            self.unauthorized_api_instance.update_conference_member(
                BW_ACCOUNT_ID, self.testConfId, self.testMemberId, self.testUpdateMember)

        self.assertApiException(context, UnauthorizedException, 401)

    def test_update_conference_member_forbidden(self) -> None:
        with self.assertRaises(ForbiddenException) as context:
            self.forbidden_api_instance.update_conference_member(
                BW_ACCOUNT_ID, self.testConfId, self.testMemberId, self.testUpdateMember)

        self.assertApiException(context, ForbiddenException, 403)

    @unittest.skip("PV Issues")
    def test_update_conference_member_not_found(self) -> None:
        with self.assertRaises(NotFoundException) as context:
            self.conference_api_instance.update_conference_member(
                BW_ACCOUNT_ID, self.testConfId, self.testMemberId, self.testUpdateMember)

        self.assertApiException(context, NotFoundException, 404)


if __name__ == '__main__':
    unittest.main()
