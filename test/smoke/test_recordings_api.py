"""
Integration test for Bandwidth's Voice Recordings API
"""
import os
from typing import Dict, List, Tuple
import unittest
import time
import json

import bandwidth
from hamcrest import *

from bandwidth import ApiResponse
from bandwidth.api.recordings_api import RecordingsApi
from bandwidth.configuration import Configuration
from bandwidth.exceptions import ForbiddenException, NotFoundException, UnauthorizedException
from bandwidth.models.call_recording_metadata import CallRecordingMetadata
from bandwidth.models.call_state import CallState
from bandwidth.models.call_state_enum import CallStateEnum
from bandwidth.api.calls_api import CallsApi
from bandwidth.models.create_call_response import CreateCallResponse
from bandwidth.models.create_call import CreateCall
from bandwidth.models.file_format_enum import FileFormatEnum
from bandwidth.models.recording_state_enum import RecordingStateEnum
from bandwidth.models.transcribe_recording import TranscribeRecording
from bandwidth.models.transcription import Transcription
from bandwidth.models.update_call import UpdateCall
from bandwidth.models.update_call_recording import UpdateCallRecording
from bandwidth.rest import RESTClientObject, RESTResponse
from test.utils.call_cleanup import callCleanup
from test.utils.env_variables import *


try:
    # BW Credentials
    BW_USERNAME = BW_USERNAME
    BW_PASSWORD = BW_PASSWORD
    BW_ACCOUNT_ID = BW_ACCOUNT_ID

    # Manteca Numbers
    MANTECA_ACTIVE_NUMBER = MANTECA_ACTIVE_NUMBER
    MANTECA_IDLE_NUMBER = MANTECA_IDLE_NUMBER

    # Manteca
    MANTECA_BASE_URL = MANTECA_BASE_URL
    MANTECA_STATUS_URL = MANTECA_BASE_URL + "tests/"
    MANTECA_APPLICATION_ID = MANTECA_APPLICATION_ID

    # Test Environment
    PYTHON_VERSION = PYTHON_VERSION
    OPERATING_SYSTEM = OPERATING_SYSTEM
except KeyError as e:
    raise Exception("Environmental variables not found")

MAX_RETRIES = 40
TEST_SLEEP = 5


class TestRecordings(unittest.TestCase):
    """
    Integration tests for the Recordings API.
    """

    def setUp(self) -> None:
        """
        Set up for our tests by creating the CallsApi and RecordingsApi instances
        for testing.
        """
        configuration = bandwidth.Configuration(
            username=BW_USERNAME,
            password=BW_PASSWORD
        )
        api_client = bandwidth.ApiClient(configuration)

        # Two Valid API Clients
        self.calls_api_instance = CallsApi(api_client)
        self.recordings_api_instance = RecordingsApi(api_client)

        # Unauthorized Recordings API Client
        self.unauthorized_recordings_api_instance = RecordingsApi(
            api_client=bandwidth.ApiClient(Configuration.get_default_copy())
        )

        # Rest client for interacting with Manteca
        self.rest_client = RESTClientObject(Configuration.get_default_copy())

        # Call ID Array
        self.callIdArray = []

    def tearDown(self):
        callCleanup(self)

    def create_and_validate_call(self, answer_url: str) -> Tuple[str, str]:
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
                'type': 'CALL'
            }
        )

        # Get the test id from the response
        test_id = response.response.data.decode("utf-8")

        # Make a CreateCall body and assign the appropriate params
        call_body = CreateCall(to=MANTECA_IDLE_NUMBER, var_from=MANTECA_ACTIVE_NUMBER,
                               application_id=MANTECA_APPLICATION_ID, answer_url=answer_url, tag=test_id)

        # Make the call
        create_call_response: CreateCallResponse = self.calls_api_instance.create_call(
            BW_ACCOUNT_ID, call_body)

        # Verify info about the call
        assert_that(create_call_response, has_properties(
            # assert request created and id matches expected length (47)
            'call_id', has_length(47),
            'account_id', BW_ACCOUNT_ID,
            'application_id', MANTECA_APPLICATION_ID,
            'to', MANTECA_IDLE_NUMBER,
            'var_from', MANTECA_ACTIVE_NUMBER,
            'call_url', "https://voice.bandwidth.com/api/v2/accounts/" + \
            BW_ACCOUNT_ID + "/calls/" + create_call_response.call_id
        ))

        # Adding the call to the callIdArray
        self.callIdArray.append(create_call_response.call_id)

        # Return our test id and call id
        return (test_id, create_call_response.call_id)

    def complete_recorded_call(self) -> Tuple[str, str]:
        """
        Creates and completes an entire recorded call lifecycle.  A call should be completed and fully recorded.

        Return:
            (str, str): A tuple containing the test id to track this call in the Manteca system and the call id
                        associated with the call in Bandwidth services.
        """
        # Create a call
        answer_url = MANTECA_BASE_URL + '/bxml/startRecording'
        (test_id, call_id) = self.create_and_validate_call(answer_url)

        time.sleep(12)
        # Poll Manteca to make sure our call is recorded
        call_status = self.get_test_status(test_id)
        retries = 0
        while call_status['callRecorded'] == False and retries < MAX_RETRIES:
            time.sleep(TEST_SLEEP)
            call_status = self.get_test_status(test_id)
            retries += 1

        # If we failed to get a recorded call, fail due to polling timeout
        assert_that(call_status['callRecorded'], equal_to(True))

        # Return our test_id and call_id
        return (test_id, call_id)

    def validate_recording(self, recording: CallRecordingMetadata, call_id: str) -> None:
        """
        Validate the given recording metadata.

        Args:
            recording (CallRecordingMetadata): The recording metadata to validate.
            call_id (str): The call id associated with the given recording.
        """
        assert_that(recording, has_properties(
            'account_id', BW_ACCOUNT_ID,
            'call_id', call_id,
            'application_id', MANTECA_APPLICATION_ID,
            'status', 'complete',
            'file_format', FileFormatEnum('wav')
        ))

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

    def test_successful_call_recording(self) -> None:
        """
        Tests a successful flow of creating a call with a recording.
        The following endpoints are tested in this flow:
            - list_call_recordings
            - get_call_recording
            - download_call_recording
            - transcribe_call_recording
            - get_recording_transcription
            - delete_recording_transcription
            - delete_recording_media
            - delete_recording
        """

        # Have a recorded call
        (test_id, call_id) = self.complete_recorded_call()

        # List Call Recordings Endpoint
        response: ApiResponse = self.recordings_api_instance.list_call_recordings_with_http_info(
            BW_ACCOUNT_ID,
            call_id
        )
        assert_that(response.status_code, equal_to(200))  # Check response code

        # We should get back 1 recording
        call_recordings: List[CallRecordingMetadata] = response.data
        assert_that(call_recordings, has_length(1))

        # Checks on the first recording
        first_recording: CallRecordingMetadata = call_recordings[0]
        self.validate_recording(first_recording, call_id)
        recording_id = first_recording.recording_id

        # Get Single Recording Endpoint
        recording_response: ApiResponse = self.recordings_api_instance.get_call_recording_with_http_info(
            BW_ACCOUNT_ID,
            call_id,
            recording_id
        )
        assert_that(recording_response.status_code, equal_to(200))  # Check response code

        recording = recording_response.data
        assert_that(recording.recording_id, equal_to(recording_id))
        self.validate_recording(recording, call_id)

        # Download recording media
        recording_media_response = self.recordings_api_instance.download_call_recording(
            BW_ACCOUNT_ID, call_id, recording_id)
        call_recording_media = recording_media_response

        '''
        Do a verification test on the actual recording data?
        '''
        # # print(call_recording_media)
        # with open("zzzz.wav", "wb") as fp:
        #     fp.write(call_recording_media)

        # Create Transcription Request
        transcription_url = MANTECA_BASE_URL + "/transcriptions"
        transcribe_recording_request = TranscribeRecording(
            callback_url=transcription_url, tag=test_id)
        transcription_response = self.recordings_api_instance.transcribe_call_recording_with_http_info(
            BW_ACCOUNT_ID, call_id, recording_id, transcribe_recording_request)
        assert_that(transcription_response.status_code, equal_to(204))  # Check response code

        # Poll Manteca to make sure our call is transcribed
        call_status = self.get_test_status(test_id)
        retries = 0
        while call_status['callTranscribed'] == False and retries < MAX_RETRIES:
            time.sleep(TEST_SLEEP)
            call_status = self.get_test_status(test_id)
            retries += 1

        # If we failed to get a transcribed call, fail due to polling timeout
        assert_that(call_status['callTranscribed'], equal_to(True))

        # Get the transcription
        transcription_response = self.recordings_api_instance.get_recording_transcription_with_http_info(
            BW_ACCOUNT_ID, call_id, recording_id)
        assert_that(transcription_response.status_code, equal_to(200))  # Check response code

        transcription_list = transcription_response.data
        assert_that(transcription_list.transcripts, has_length(1))
        transcription = transcription_list.transcripts[0]
        assert_that(transcription, instance_of(Transcription))
        assert_that(transcription, has_properties(
            'text', instance_of(str),
            'confidence', instance_of(float)
        ))

        # Delete the transcription
        delete_transcription_response = self.recordings_api_instance.delete_recording_transcription_with_http_info(
            BW_ACCOUNT_ID, call_id, recording_id)
        assert_that(delete_transcription_response.status_code, equal_to(204))  # Check response code

        assert_that(calling(self.recordings_api_instance.get_recording_transcription).with_args(
            BW_ACCOUNT_ID, call_id, recording_id), raises(NotFoundException))

        # Delete Recording media
        delete_recording_media_response = self.recordings_api_instance.delete_recording_media_with_http_info(
            BW_ACCOUNT_ID, call_id, recording_id)
        # Validate the 204 response
        assert_that(delete_recording_media_response.status_code, equal_to(204))

        # Delete Recording
        delete_recording_response = self.recordings_api_instance.delete_recording_with_http_info(
            BW_ACCOUNT_ID, call_id, recording_id)
        assert_that(delete_recording_response.status_code, equal_to(204))
        call_recordings = self.recordings_api_instance.list_call_recordings(BW_ACCOUNT_ID, call_id)
        assert_that(call_recordings, has_length(0))

    def test_successful_update_active_recording(self) -> None:
        """
        Tests updating the recording for a call that is currently active.
        Tests the following endpoints:
            - update_call_recording_state
        """

        # Create the call
        answer_url = MANTECA_BASE_URL + "/bxml/startLongRecording"
        (test_id, call_id) = self.create_and_validate_call(answer_url)

        # Poll Manteca to make sure our call is alive
        call_status = self.get_test_status(test_id)
        retries = 0
        while call_status['status'] == 'DEAD' and retries < MAX_RETRIES:
            time.sleep(TEST_SLEEP)
            call_status = self.get_test_status(test_id)
            retries += 1

        # Make sure the call is alive
        assert_that(call_status['status'], equal_to('ALIVE'))

        # Add a sleep to prevent timing issues
        time.sleep(TEST_SLEEP)

        # Update the call to pause the recording
        update_call_recording = UpdateCallRecording(state=RecordingStateEnum('paused'))
        update_response = self.recordings_api_instance.update_call_recording_state_with_http_info(
            BW_ACCOUNT_ID, call_id, update_call_recording)
        assert_that(update_response.status_code, equal_to(200))

        # Update the call to resume the recording
        update_call_recording = UpdateCallRecording(state=RecordingStateEnum('recording'))
        self.recordings_api_instance.update_call_recording_state_with_http_info(
            BW_ACCOUNT_ID, call_id, update_call_recording)
        assert_that(update_response.status_code, equal_to(200))

        # Kill the call
        update_call = UpdateCall()
        update_call.state = CallStateEnum.COMPLETED
        self.calls_api_instance.update_call(BW_ACCOUNT_ID, call_id, update_call)

    def test_4xx_errors(self) -> None:
        """
        Tests invalid flows for several methods
        """

        # Have a recorded call
        (test_id, call_id) = self.complete_recorded_call()

        # List Recordings
        # Use the unauthorized client to try to list recordings (401)
        assert_that(calling(self.unauthorized_recordings_api_instance.list_call_recordings).with_args(
            BW_ACCOUNT_ID, call_id), raises(UnauthorizedException))

        # Invalid account id (403)
        assert_that(calling(self.recordings_api_instance.list_call_recordings).with_args(
            "not an account id", call_id), raises(ForbiddenException))

        # Non-existent call id
        # This should probably be a 404, but actually returns an empty list
        not_found_call_recordings = self.recordings_api_instance.list_call_recordings(
            BW_ACCOUNT_ID, "not a call id")
        assert_that(not_found_call_recordings, equal_to([]))

        # Get Call Recording
        # Get our recording id
        recordings = self.recordings_api_instance.list_call_recordings(BW_ACCOUNT_ID, call_id)
        recording_id = recordings[0].recording_id

        # Use the unauthorized client to try to get a recording (401)
        assert_that(calling(self.unauthorized_recordings_api_instance.get_call_recording).with_args(
            BW_ACCOUNT_ID, call_id, recording_id), raises(UnauthorizedException))

        # Non-existent account id (403)
        assert_that(calling(self.recordings_api_instance.get_call_recording).with_args(
            "not an account id", call_id, recording_id), raises(ForbiddenException))

        # Non-existent recording id (404)
        assert_that(calling(self.recordings_api_instance.get_call_recording).with_args(
            BW_ACCOUNT_ID, call_id, "not a recording id"), raises(NotFoundException))

        # Download Recording
        # Use the unauthorized client to try to download a recording (401)
        assert_that(calling(self.unauthorized_recordings_api_instance.download_call_recording).with_args(
            BW_ACCOUNT_ID, call_id, recording_id), raises(UnauthorizedException))

        # Non-existent account id (403)
        assert_that(calling(self.recordings_api_instance.download_call_recording).with_args(
            "not an account id", call_id, recording_id), raises(ForbiddenException))

        # Non-existent recording id (404)
        assert_that(calling(self.recordings_api_instance.download_call_recording).with_args(
            BW_ACCOUNT_ID, call_id, "not a recording id"), raises(NotFoundException))

        # Transcribe Recording
        # Create a standard TranscribeRecording instance to use
        transcription_url = MANTECA_BASE_URL + "transcriptions"
        transcribe_recording = TranscribeRecording(callback_url=transcription_url, tag=test_id)

        # Use the unauthorized client to request a transcription (401)
        assert_that(calling(self.unauthorized_recordings_api_instance.transcribe_call_recording).with_args(
            BW_ACCOUNT_ID, call_id, recording_id, transcribe_recording), raises(UnauthorizedException))

        # Non existent account id (403)
        assert_that(calling(self.recordings_api_instance.transcribe_call_recording).with_args(
            "not an account id", call_id, recording_id, transcribe_recording), raises(ForbiddenException))

        # Non-existent recording id (404)
        # TODO: This does not work right now as the API is unexpectedly returning a 502 Bad Gateway for this request.
        # with self.assertRaises(NotFoundException):
        #     self.recordings_api_instance.transcribe_call_recording(BW_ACCOUNT_ID, call_id, "not a recording id", transcribe_recording)

        # Get Transcription
        # Actually Create a transcription
        transcription_url = MANTECA_BASE_URL + "transcriptions"
        transcribe_recording = TranscribeRecording(callback_url=transcription_url, tag=test_id)
        self.recordings_api_instance.transcribe_call_recording(
            BW_ACCOUNT_ID, call_id, recording_id, transcribe_recording)

        # Poll Manteca to make sure our call is transcribed
        call_status = self.get_test_status(test_id)
        retries = 0
        while call_status['callTranscribed'] == False and retries < MAX_RETRIES:
            time.sleep(TEST_SLEEP)
            call_status = self.get_test_status(test_id)
            retries += 1

        # If we failed to get a transcribed call, fail due to polling timeout (TEMP COMMENTED)
        assert_that(call_status['callTranscribed'], equal_to(True))

        # Use the unauthorized client to get transcripion (401)
        assert_that(calling(self.unauthorized_recordings_api_instance.get_recording_transcription).with_args(
            BW_ACCOUNT_ID, call_id, recording_id), raises(UnauthorizedException))

        # Non-existent account id (403)
        assert_that(calling(self.recordings_api_instance.get_recording_transcription).with_args(
            "not an account id", call_id, recording_id), raises(ForbiddenException))

        # Non-existent recording id (404)
        assert_that(calling(self.recordings_api_instance.get_recording_transcription).with_args(
            BW_ACCOUNT_ID, call_id, "not a recording id"), raises(NotFoundException))

        # Delete Transcription
        # Use the unauthorized client to delete transcripion (401)
        assert_that(calling(self.unauthorized_recordings_api_instance.delete_recording_transcription).with_args(
            BW_ACCOUNT_ID, call_id, recording_id), raises(UnauthorizedException))

        # Non-existent account id (403)
        assert_that(calling(self.recordings_api_instance.delete_recording_transcription).with_args(
            "not an account id", call_id, recording_id), raises(ForbiddenException))

        # Non-existent recording id (404)
        assert_that(calling(self.recordings_api_instance.delete_recording_transcription).with_args(
            BW_ACCOUNT_ID, call_id, "not a recording id"), raises(NotFoundException))

        # Delete Recording Media
        # Use the unauthorized client to try to delete a recording (401)
        assert_that(calling(self.unauthorized_recordings_api_instance.delete_recording_media).with_args(
            BW_ACCOUNT_ID, call_id, recording_id), raises(UnauthorizedException))

        # Non-existent account id (403)
        assert_that(calling(self.recordings_api_instance.delete_recording_media).with_args(
            "not an account id", call_id, recording_id), raises(ForbiddenException))

        # Non-existent recording id (404)
        assert_that(calling(self.recordings_api_instance.delete_recording_media).with_args(
            BW_ACCOUNT_ID, call_id, "not a recording id"), raises(NotFoundException))

        # Delete Recording
        # Use the unauthorized client to try to delete a recording (401)
        assert_that(calling(self.unauthorized_recordings_api_instance.delete_recording).with_args(
            BW_ACCOUNT_ID, call_id, recording_id), raises(UnauthorizedException))

        # Non-existent account id (403)
        assert_that(calling(self.recordings_api_instance.delete_recording).with_args(
            "not an account id", call_id, recording_id), raises(ForbiddenException))

        # Non-existent recording id (404)
        assert_that(calling(self.recordings_api_instance.delete_recording).with_args(
            BW_ACCOUNT_ID, call_id, "not a recording id"), raises(NotFoundException))

    @unittest.skip("PV Issues")
    def test_invalid_update_call_recording_state(self) -> None:
        """
        Tests invalid flows for update_call_recording_state
        """

        # Create the call
        answer_url = MANTECA_BASE_URL + "/bxml/startLongRecording"
        (test_id, call_id) = self.create_and_validate_call(answer_url)

        # Poll Manteca to make sure our call is alive
        call_status = self.get_test_status(test_id)
        retries = 0
        while call_status['status'] == 'DEAD' and retries < MAX_RETRIES:
            time.sleep(TEST_SLEEP)
            call_status = self.get_test_status(test_id)
            retries += 1

        # Make sure the call is alive
        assert_that(call_status['status'], equal_to('ALIVE'))

        # Common models
        pause_recording = UpdateCallRecording(state=RecordingStateEnum('paused'))
        resume_recording = UpdateCallRecording(state=RecordingStateEnum('recording'))


        # Use the unauthorized client to try to update (401)
        assert_that(calling(self.unauthorized_recordings_api_instance.update_call_recording_state).with_args(
            BW_ACCOUNT_ID, call_id, pause_recording), raises(UnauthorizedException))

        # Non-existent account id (403)
        assert_that(calling(self.recordings_api_instance.update_call_recording_state).with_args(
            "not an account id", call_id, pause_recording), raises(ForbiddenException))

        # Non-existent call id (404)
        assert_that(calling(self.recordings_api_instance.update_call_recording_state).with_args(
            BW_ACCOUNT_ID, "not a call id", pause_recording), raises(NotFoundException))

        # Kill the call
        update_call = UpdateCall(state=CallStateEnum('completed'))
        self.calls_api_instance.update_call(BW_ACCOUNT_ID, call_id, update_call)


if __name__ == '__main__':
    unittest.main()
