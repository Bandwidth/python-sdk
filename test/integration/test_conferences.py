"""
Integration tests for Bandwidth's Voice Voice Conferences API
"""

from test.utils.env_variables import *
from test.utils.call_cleanup import callCleanup
import json
import time
from typing import List, Tuple
import unittest
from hamcrest import assert_that, has_properties, not_none, instance_of, greater_than


import bandwidth
from bandwidth.api import calls_api
from bandwidth.model.create_call import CreateCall
from bandwidth.model.create_call_response import CreateCallResponse
from bandwidth.model.call_state import CallState
from bandwidth.model.call_state_enum import CallStateEnum
from bandwidth.model.update_call import UpdateCall
from bandwidth.model.redirect_method_enum import RedirectMethodEnum
from bandwidth.api import conferences_api
from bandwidth.model.conference_state_enum import ConferenceStateEnum
from bandwidth.model.conference_recording_metadata import ConferenceRecordingMetadata
from bandwidth.model.update_conference import UpdateConference
from bandwidth.model.update_conference_member import UpdateConferenceMember
from bandwidth.model.file_format_enum import FileFormatEnum
from bandwidth.rest import RESTClientObject, RESTResponse
from bandwidth.exceptions import ApiException, UnauthorizedException, ForbiddenException, NotFoundException

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
            username = BW_USERNAME,
            password = BW_PASSWORD
        )
        api_client = bandwidth.ApiClient(configuration)

        # Two Valid API Clients
        self.calls_api_instance = calls_api.CallsApi(api_client)
        self.conference_api_instance = conferences_api.ConferencesApi(api_client)

        # Unauthorized API Client

        unauthorizedConfiguration = bandwidth.Configuration(
             username='bad_username',
             password='bad_password'
        )
        unauthorized_api_client = bandwidth.ApiClient(unauthorizedConfiguration)
        self.unauthorized_api_instance = conferences_api.ConferencesApi(unauthorized_api_client)            
        
        # Forbidden API Client

        forbiddenConfiguration = bandwidth.Configuration(
            username=FORBIDDEN_USERNAME,
            password=FORBIDDEN_PASSWORD
        )
        forbidden_api_client = bandwidth.ApiClient(forbiddenConfiguration)
        self.forbidden_api_instance = conferences_api.ConferencesApi(forbidden_api_client)

        # Rest client for interacting with Manteca
        self.rest_client = RESTClientObject(bandwidth.Configuration.get_default_copy())    
        configuration = bandwidth.Configuration(
            username = BW_USERNAME,
            password = BW_PASSWORD,
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
        
    def tearDown(self):
        callCleanup(self)

    def assertApiException(self, context: ApiException, expectedException: ApiException, expected_status_code: int):
        """Validates that common API exceptions, (401, 403, and 404) are properly formatted
        Args:
            context (ApiException): Exception to validate
            expectedException (ApiException): Expected exception type
            expected_status_code (int): Expected status code
        """
        assert_that(context.exception, has_properties(
            'status', expected_status_code,
            'body', not_none()
        ))

    # Create Conference Call with Manteca

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
        test_id = json.loads(response.data)

        # Make a CreateCall body and assign the appropriate params

        call_body = CreateCall(to=MANTECA_IDLE_NUMBER, _from=MANTECA_ACTIVE_NUMBER, application_id=MANTECA_APPLICATION_ID, answer_url=answer_url, tag=test_id)

        # Make the call
        create_call_response: CreateCallResponse = self.calls_api_instance.create_call(BW_ACCOUNT_ID, call_body)

        # Verify info about the call
        assert_that(create_call_response, has_properties(
            "call_id", instance_of(str),
            'account_id', BW_ACCOUNT_ID,
            'application_id', MANTECA_APPLICATION_ID,
            'to', MANTECA_IDLE_NUMBER,
            '_from', MANTECA_ACTIVE_NUMBER
        ))

        # Getting our ConferenceId and returning the test_id from Manteca and the callId

        list_conferences_response = self.conference_api_instance.list_conferences(BW_ACCOUNT_ID, _return_http_data_only=False)
    
        time.sleep(self.TEST_SLEEP)
        assert_that(list_conferences_response[1], 200)
        conferenceId = (list_conferences_response[0][len(list_conferences_response[0])-1].id)


        get_conference_response = self.conference_api_instance.get_conference(BW_ACCOUNT_ID, conferenceId, _return_http_data_only=False)
        assert_that(get_conference_response[1], 200)       
   
        self.callIdArray.append(create_call_response.call_id)

        return (test_id, create_call_response.call_id)

    def validate_recording(self, recording: ConferenceRecordingMetadata, conference_id: str) -> None:
        """
        Validate the given recording metadata.
        Args:
            recording (ConferenceRecordingMetadata): The recording metadata to validate.
            conference_id (str): The call id associated with the given recording.
        """
        assert_that(recording.status,'complete')
        assert_that(recording.file_format,FileFormatEnum('wav'))

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

        # Create the call
        answer_url = MANTECA_BASE_URL + "/bxml/joinConferencePause"
        (test_id, call_id) = self.create_conference(answer_url)

        # List Conferences
        list_conferences_response = self.conference_api_instance.list_conferences(BW_ACCOUNT_ID, _return_http_data_only=False)

        assert_that(list_conferences_response[1], 200)
        assert_that(list_conferences_response[0][0].name, instance_of(str))
        assert_that(list_conferences_response[0][0].id, instance_of(str))

        conferenceId = (list_conferences_response[0][len(list_conferences_response[0])-1].id)

        # Get Conference Information
        """Validate a Get Conference Information Request
        """
        get_conference_response = self.conference_api_instance.get_conference(BW_ACCOUNT_ID, conferenceId, _return_http_data_only=False)
        assert_that(get_conference_response[1], 200)
        assert_that(get_conference_response[0].id, conferenceId)
        assert_that(get_conference_response[0].name, instance_of(str))
        callId = (get_conference_response[0].active_members[0].call_id)
        self.callIdArray.append(callId)

        # Get Conference Member
        """Validate a GET Conference Member
        """
        get_conference_member_response = self.conference_api_instance.get_conference_member(BW_ACCOUNT_ID, conferenceId, callId,  _return_http_data_only=False)
        assert_that(get_conference_member_response[1], 200)
        assert_that(get_conference_member_response[0].conference_id, conferenceId)
        assert_that(get_conference_member_response[0].call_id, callId)

        # Update Conference Member
        """Validate an Update Conference Member Request
        """

        time.sleep(self.TEST_SLEEP)
        update_conference_member_response = self.conference_api_instance.update_conference_member(BW_ACCOUNT_ID, conferenceId, callId, self.testUpdateMember, _return_http_data_only=False)
        assert_that(update_conference_member_response[1], 204)   

        # Update Conference
        """Validate an Update Conference Request 
        """

        time.sleep(self.TEST_SLEEP)   
        update_conference_response = self.conference_api_instance.update_conference(BW_ACCOUNT_ID, conferenceId, self.testUpdateConf, _return_http_data_only=False)
        assert_that(update_conference_response[1], 204)   


        # Update Conference Bxml
        """Validate an UpdateConferencelBxml Request
        """            
        updateBxmlBody = '<?xml version="1.0" encoding="UTF-8"?><Bxml><SpeakSentence locale="en_US" gender="female" voice="susan">This is a test bxml response</SpeakSentence></Bxml>'

        time.sleep(self.TEST_SLEEP)
        update_conference_bxml_response = self.conference_api_instance.update_conference_bxml(BW_ACCOUNT_ID, conferenceId, updateBxmlBody, _return_http_data_only=False)
        assert_that(update_conference_bxml_response[1], 204)          

        # Kill the call
        update_call = UpdateCall(state=CallStateEnum('completed'))
        self.calls_api_instance.update_call(BW_ACCOUNT_ID, call_id, update_call,  _return_http_data_only=False)

    # Conference Recordings Tests
    def test_conference_recordings(self) -> None:
        """
        Tests a successful flow of creating a call with a recording.
        The following endpoints are tested in this flow:
            - list_conference_recordings
            - get_conference_recording
            - download_conference_recording
        """

        # Create a conference and have it recorded
        answer_url = MANTECA_BASE_URL + "/bxml/joinConferencePause"
        (test_id, call_id) = self.create_conference(answer_url)

        list_conferences_response = self.conference_api_instance.list_conferences(BW_ACCOUNT_ID, _return_http_data_only=False)

        assert_that(list_conferences_response[1], 200)
        conferenceId = (list_conferences_response[0][len(list_conferences_response[0])-1].id)
        
        # Update Conference Bxml
        """Validate an UpdateConferencelBxml Request to start and stop recording
        """            
        updateBxmlBody = '<?xml version="1.0" encoding="UTF-8"?><Bxml><StartRecording/><SpeakSentence locale="en_US" gender="female" voice="susan">This should be a conference recording.</SpeakSentence><StopRecording/></Bxml>'
        update_conference_bxml_response = self.conference_api_instance.update_conference_bxml(BW_ACCOUNT_ID, conferenceId, updateBxmlBody, _return_http_data_only=False)
        assert_that(update_conference_bxml_response[1], 204)   
        
        time.sleep(self.TEST_SLEEP_LONG)

        # List Conference Recordings Endpoint
        list_conference_recordings_response: List[ConferenceRecordingMetadata] = self.conference_api_instance.list_conference_recordings(BW_ACCOUNT_ID, conferenceId, _return_http_data_only=False)
        assert_that(list_conference_recordings_response[1],200)

        # We should get back at least 1 recording
        conference_recordings = list_conference_recordings_response[0]
        assert_that(len(conference_recordings), greater_than(0))

        # Checks on the first recording
        first_recording: ConferenceRecordingMetadata = conference_recordings[0]
        self.validate_recording(first_recording, conferenceId)
        recording_id = first_recording.recording_id

        # Get Single Recording Endpoint
        recording_response: ConferenceRecordingMetadata = self.conference_api_instance.get_conference_recording(BW_ACCOUNT_ID, conferenceId, recording_id, _return_http_data_only=False)
        assert_that(recording_response[1], 200)
        assert_that(recording_response[0].conference_id, conferenceId)
        assert_that(recording_response[0].recording_id, recording_id)
        assert_that(recording_response[0].name, instance_of(str))  

        self.validate_recording(recording_response[0], conferenceId)

        # Download recording media
        recording_media_response = self.conference_api_instance.download_conference_recording(BW_ACCOUNT_ID, conferenceId, recording_id, _preload_content=False)
        conference_recording_media = recording_media_response.data                   

    def test_list_conferences_unauthorized(self) -> None:
         """Validate an unauthorized (401) request
         """ 
         with self.assertRaises(UnauthorizedException) as context:
            self.unauthorized_api_instance.list_conferences(BW_ACCOUNT_ID, _return_http_data_only=False)
 
         self.assertApiException(context, UnauthorizedException, 401)
  
    def test_list_conferences_forbidden(self) -> None:
         """Validate a forbidden (403) request
         """
         with self.assertRaises(ForbiddenException) as context:
            self.forbidden_api_instance.list_conferences(BW_ACCOUNT_ID, _return_http_data_only=False)
 
         self.assertApiException(context, ForbiddenException, 403)
 
    def test_get_conferences_unauthorized(self) -> None:
        """Validate an unauthorized (401) Get Conference Information
        """
        with self.assertRaises(UnauthorizedException) as context:
            self.unauthorized_api_instance.get_conference(BW_ACCOUNT_ID, self.testConfId, _return_http_data_only=False)

        self.assertApiException(context, UnauthorizedException, 401)

    def test_get_conferences_forbidden(self) -> None:
        """Validate a forbidden (403) Get Conference Information request
        """
        with self.assertRaises(ForbiddenException) as context:
            self.forbidden_api_instance.get_conference(BW_ACCOUNT_ID, self.testConfId, _return_http_data_only=False)

        self.assertApiException(context, ForbiddenException, 403)

    def test_get_conferences_not_found(self) -> None:
        """Validate an invalid Get Conference Information Request due to a bad conferenceId
        """
        with self.assertRaises(NotFoundException) as context:
            self.conference_api_instance.get_conference(BW_ACCOUNT_ID, self.testConfId, _return_http_data_only=False)
        
        self.assertApiException(context, NotFoundException, 404)    

    def test_get_conference_member_unauthorized(self) -> None:
        """Validate an unauthorized (401) Get Conference Member
        """  
        with self.assertRaises(UnauthorizedException) as context:
            self.unauthorized_api_instance.get_conference_member(BW_ACCOUNT_ID, self.testConfId, self.testMemberId, _return_http_data_only=False)

        self.assertApiException(context, UnauthorizedException, 401)    

    def test_get_conference_member_forbidden(self) -> None:
        """Validate an forbidden (403) Get Conference Member
        """
        with self.assertRaises(ForbiddenException) as context:
            self.forbidden_api_instance.get_conference_member(BW_ACCOUNT_ID, self.testConfId, self.testMemberId, _return_http_data_only=False)

        self.assertApiException(context, ForbiddenException, 403)

    def test_get_conference_member_not_found(self) -> None:
        """Validate an not found (404) Get Conference Member
        """
        with self.assertRaises(NotFoundException) as context:
            self.conference_api_instance.get_conference_member(BW_ACCOUNT_ID, self.testConfId, self.testMemberId, _return_http_data_only=False)
        
        self.assertApiException(context, NotFoundException, 404)    
    
    def test_list_conference_recordings_unauthorized(self) -> None:
        """Validate an unauthorized (401) request
        """
        with self.assertRaises(UnauthorizedException) as context:
            self.unauthorized_api_instance.list_conference_recordings(BW_ACCOUNT_ID, self.testConfId, _return_http_data_only=False)

        self.assertApiException(context, UnauthorizedException, 401)
    
    def test_list_conference_recordings_forbidden(self) -> None:
        """Validate a forbidden (403) request
        """
        with self.assertRaises(ForbiddenException) as context:          
            self.forbidden_api_instance.list_conference_recordings(BW_ACCOUNT_ID, self.testConfId, _return_http_data_only=False)

        self.assertApiException(context, ForbiddenException, 403)
    
    def test_get_recording_unauthorized(self) -> None:
        """Validate an unauthorized (401) Get Conference Recording
        """  
        with self.assertRaises(UnauthorizedException) as context:
            self.unauthorized_api_instance.get_conference_recording(BW_ACCOUNT_ID, self.testConfId, self.testRecordId, _return_http_data_only=False)

        self.assertApiException(context, UnauthorizedException, 401)

    def test_get_recording_forbidden(self) -> None:
        """Validate an forbidden (403) Get Conference Recording
        """
        with self.assertRaises(ForbiddenException) as context:
            self.forbidden_api_instance.get_conference_recording(BW_ACCOUNT_ID, self.testConfId, self.testRecordId, _return_http_data_only=False)

        self.assertApiException(context, ForbiddenException, 403)     

    def test_get_conference_recording_not_found(self) -> None:
        """Validate an not found (404) Get Conference Recording
        """
        with self.assertRaises(NotFoundException) as context:
            self.conference_api_instance.get_conference_member(BW_ACCOUNT_ID, self.testConfId, self.testRecordId, _return_http_data_only=False)
        
        self.assertApiException(context, NotFoundException, 404)    
    
    def test_update_conference_unauthorized(self) -> None:
        """Validate an unauthorized (401) Update Conference
        """  
        with self.assertRaises(UnauthorizedException) as context:
            self.unauthorized_api_instance.update_conference(BW_ACCOUNT_ID, self.testConfId, self.testUpdateConf, _return_http_data_only=False)

        self.assertApiException(context, UnauthorizedException, 401)

    def test_update_conference_forbidden(self) -> None:
        """Validate an forbidden (403) Update Conference
        """
        with self.assertRaises(ForbiddenException) as context:
            self.forbidden_api_instance.update_conference(BW_ACCOUNT_ID, self.testConfId, self.testUpdateConf, _return_http_data_only=False)

        self.assertApiException(context, ForbiddenException, 403) 

    def test_update_conference_not_found(self) -> None:
        """Validate an not found (404) Update Conference
        """
        with self.assertRaises(NotFoundException) as context:
            self.conference_api_instance.update_conference(BW_ACCOUNT_ID, self.testConfId, self.testUpdateConf, _return_http_data_only=False)
        
        self.assertApiException(context, NotFoundException, 404)    
    
    def test_update_conference_bxml_unauthorized(self) -> None:
        """Validate an unauthorized (401) Update Conference BXML
        """  
        with self.assertRaises(UnauthorizedException) as context:
            self.unauthorized_api_instance.update_conference_bxml(BW_ACCOUNT_ID, self.testConfId, self.testUpdateBxml, _return_http_data_only=False)

        self.assertApiException(context, UnauthorizedException, 401)   

    def test_update_conference_bxml_forbidden(self) -> None:
        """Validate an forbidden (403) Update Conference BXML
        """
        with self.assertRaises(ForbiddenException) as context:
            self.forbidden_api_instance.update_conference_bxml(BW_ACCOUNT_ID, self.testConfId, self.testUpdateBxml, _return_http_data_only=False)

        self.assertApiException(context, ForbiddenException, 403) 

    def test_update_conference_bxml_not_found(self) -> None:
        """Validate an not found (404) Update Conference BXML
        """
        with self.assertRaises(NotFoundException) as context:
            self.conference_api_instance.update_conference_bxml(BW_ACCOUNT_ID, self.testConfId, self.testUpdateBxml, _return_http_data_only=False)
        
        self.assertApiException(context, NotFoundException, 404)    
    
    def test_update_conference_member_unauthorized(self) -> None:
        """Validate an unauthorized (401) Get Conference Member
        """  
        with self.assertRaises(UnauthorizedException) as context:
            self.unauthorized_api_instance.update_conference_member(BW_ACCOUNT_ID, self.testConfId, self.testMemberId, self.testUpdateMember, _return_http_data_only=False)

        self.assertApiException(context, UnauthorizedException, 401)

    def test_update_conference_member_forbidden(self) -> None:
        """Validate an forbidden (403) Get Conference Member
        """
        with self.assertRaises(ForbiddenException) as context:
            self.forbidden_api_instance.update_conference_member(BW_ACCOUNT_ID, self.testConfId, self.testMemberId, self.testUpdateMember, _return_http_data_only=False)

        self.assertApiException(context, ForbiddenException, 403)   

    def test_update_conference_member_not_found(self) -> None:
        """Validate an not found (404) Get Conference Member
        """
        with self.assertRaises(NotFoundException) as context:
            self.conference_api_instance.update_conference_member(BW_ACCOUNT_ID, self.testConfId, self.testMemberId, self.testUpdateMember, _return_http_data_only=False)
        
        self.assertApiException(context, NotFoundException, 404)    


if __name__ == '__main__':
    unittest.main()