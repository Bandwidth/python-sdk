"""
    Bandwidth

    Bandwidth's Communication APIs  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: letstalk@bandwidth.com
    Generated by: https://openapi-generator.tech
"""


import os
from typing import Dict, List, Tuple
import unittest
import time
import json

import bandwidth
from bandwidth.api.recordings_api import RecordingsApi
from bandwidth.configuration import Configuration
from bandwidth.exceptions import ApiException, ForbiddenException, NotFoundException, UnauthorizedException
from bandwidth.model.call_recording_metadata import CallRecordingMetadata
from bandwidth.model.call_state_enum import CallStateEnum
from bandwidth.model.callback_method_enum import CallbackMethodEnum
from bandwidth.api.calls_api import CallsApi
from bandwidth.model.create_call_response import CreateCallResponse
from bandwidth.model.create_call import CreateCall
from bandwidth.model.file_format_enum import FileFormatEnum
from bandwidth.model.recording_state_enum import RecordingStateEnum
from bandwidth.model.transcribe_recording import TranscribeRecording
from bandwidth.model.transcription import Transcription
from bandwidth.model.update_call import UpdateCall
from bandwidth.model.update_call_recording import UpdateCallRecording
from bandwidth.rest import RESTClientObject, RESTResponse


try:
    BW_USERNAME = os.environ["BW_USERNAME"]
    BW_PASSWORD = os.environ["BW_PASSWORD"]
    BW_ACCOUNT_ID = os.environ["BW_ACCOUNT_ID"]
    BW_VOICE_APPLICATION_ID = os.environ["BW_VOICE_APPLICATION_ID"]
    MANTECA_BASE_CALLBACK_URL = os.environ["MANTECA_BASE_CALLBACK_URL"]
    MANTECA_STATUS_URL = MANTECA_BASE_CALLBACK_URL + "tests/"
    BW_NUMBER = os.environ["BW_NUMBER"]
    USER_NUMBER = os.environ["USER_NUMBER"]
except KeyError as e:
    raise Exception("Environmental variables not found")

MAX_RETRIES = 30

class TestRecordings(unittest.TestCase):
    """CreateCall unit test stubs"""

    def setUp(self):
        """
        Set up for our tests by creating the CallsApi and RecordingsApi instances
        for testing.
        """
        configuration = bandwidth.Configuration(
            username = BW_USERNAME,
            password = BW_PASSWORD
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

    def tearDown(self):
        pass

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
            url=MANTECA_BASE_CALLBACK_URL + 'tests',
            body={
                'os': 'macos',
                'language': 'python3.9',
                'type': 'CALL'
            }
        )

        # Get the test id from the response
        test_id = json.loads(response.data)
        # print("Test created in Manteca.")

        # Make a CreateCall body and assign the appropriate params
        call_body = CreateCall(to=USER_NUMBER, _from=BW_NUMBER, application_id=BW_VOICE_APPLICATION_ID, answer_url=answer_url, tag=test_id)

        # Make the call
        create_call_response: CreateCallResponse = self.calls_api_instance.create_call(BW_ACCOUNT_ID, call_body)

        # Verify info about the call
        # print("Call was created.")
        assert len(create_call_response.call_id) == 47    # assert request created and id matches expected length (47)
        assert create_call_response.account_id == BW_ACCOUNT_ID
        assert create_call_response.application_id == BW_VOICE_APPLICATION_ID
        assert create_call_response.to == USER_NUMBER
        assert create_call_response._from == BW_NUMBER
        assert create_call_response.call_url == "https://voice.bandwidth.com/api/v2/accounts/" + \
            BW_ACCOUNT_ID + "/calls/" + create_call_response.call_id

        # Return our test id and call id
        return (test_id, create_call_response.call_id)


    def validate_recording(self, recording: CallRecordingMetadata, call_id: str):
        assert recording.account_id == BW_ACCOUNT_ID
        assert recording.call_id == call_id
        assert recording.application_id == BW_VOICE_APPLICATION_ID
        assert recording.status == 'complete'
        assert recording.file_format == FileFormatEnum('wav')
        # print("Recording Validated.")

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
        return json.loads(response.data)

    def test_successful_call_recording(self):
        """
        Tests a successful flow of creating a call with a recording.
        The following endpoints are tested in this flow:
            - list_call_recordings
            - get_call_recording
            - download_call_recording
            - transcribe_call_recording
            - get_call_transcription
            - delete_call_transcription
            - delete_recording_media
            - delete_recording
        """

        # Create a call
        answer_url = MANTECA_BASE_CALLBACK_URL + '/bxml/startRecording'
        (test_id, call_id) = self.create_and_validate_call(answer_url)

        # Poll Manteca to make sure our call is recorded
        call_status = self.get_test_status(test_id)
        retries = 0
        while call_status['callRecorded'] == False and retries < MAX_RETRIES:
            time.sleep(3)
            call_status = self.get_test_status(test_id)
            # print('Recording poll attempt ' + str(retries))
            # print(json.dumps(call_status, indent=4))
            retries += 1

        # If we failed to get a recorded call, fail due to polling timeout
        assert call_status['callRecorded'] == True
            
        # List Call Recordings Endpoint
        call_recordings: List[CallRecordingMetadata] = self.recordings_api_instance.list_call_recordings(BW_ACCOUNT_ID, call_id)
        
        # We should get back 1 recording
        assert len(call_recordings) == 1
        
        # Checks on the first recording
        first_recording: CallRecordingMetadata = call_recordings[0]
        self.validate_recording(first_recording, call_id)
        recording_id = first_recording.recording_id

        # Get Single Recording Endpoint
        recording: CallRecordingMetadata = self.recordings_api_instance.get_call_recording(BW_ACCOUNT_ID, call_id, recording_id)
        assert recording.recording_id == recording_id
        self.validate_recording(recording, call_id)

        # Download recording media
        recording_response = self.recordings_api_instance.download_call_recording(BW_ACCOUNT_ID, call_id, recording_id, _preload_content=False)
        call_recording_media = recording_response.data
        '''
        Do a verification test on the actual recording data?
        '''
        # # print(call_recording_media)
        # with open("zzzz.wav", "wb") as fp:
        #     fp.write(call_recording_media)

        # Create Transcription Request
        transcription_url = MANTECA_BASE_CALLBACK_URL + "/transcriptions"
        transcribe_recording_request = TranscribeRecording(callback_url=transcription_url,tag=test_id)
        self.recordings_api_instance.transcribe_call_recording(BW_ACCOUNT_ID, call_id, recording_id, transcribe_recording_request)

        # print("Transcription request sent.")
        # Poll Manteca to make sure our call is transcribed
        call_status = self.get_test_status(test_id)
        retries = 0
        while call_status['callTranscribed'] == False and retries < MAX_RETRIES:
            time.sleep(3)
            call_status = self.get_test_status(test_id)
            # print('Transcribe poll attempt ' + str(retries))
            # print(json.dumps(call_status, indent=4))
            retries += 1

        # If we failed to get a transcribed call, fail due to polling timeout (TEMP COMMENTED)
        assert call_status['callTranscribed'] == True

        # Get the transcription
        transcription_list = self.recordings_api_instance.get_call_transcription(BW_ACCOUNT_ID, call_id, recording_id)
        assert len(transcription_list.transcripts) == 1
        transcription = transcription_list.transcripts[0]
        assert isinstance(transcription, Transcription)
        assert isinstance(transcription.text, str)
        assert isinstance(transcription.confidence, float)

        # # Wait (TEMP)
        # time.sleep(10)

        # Delete the transcription
        self.recordings_api_instance.delete_call_transcription(BW_ACCOUNT_ID, call_id, recording_id)
        with self.assertRaises(NotFoundException):
            self.recordings_api_instance.get_call_transcription(BW_ACCOUNT_ID, call_id, recording_id)
        # print("Delete transcription.")

        # Delete Recording media
        delete_recording_response = self.recordings_api_instance.delete_recording_media(BW_ACCOUNT_ID, call_id, recording_id, _return_http_data_only=False)
        # Validate the 204 response
        assert delete_recording_response[1] == 204 
        # print("Deleted Recording Media.")

        # Delete Recording
        self.recordings_api_instance.delete_recording(BW_ACCOUNT_ID, call_id, recording_id)
        call_recordings = self.recordings_api_instance.list_call_recordings(BW_ACCOUNT_ID, call_id)
        assert len(call_recordings) == 0
        # print("Deleted recording")

    def test_successful_update_active_recording(self):
        """
        Tests updating the recording for a call that is currently active.
        Tests the following endpoints:
            - update_call_recording_state
        """
        
        # Create the call
        answer_url = MANTECA_BASE_CALLBACK_URL + "/bxml/startRecordingLoop"
        (test_id, call_id) = self.create_and_validate_call(answer_url)

        # Poll Manteca to make sure our call is alive
        call_status = self.get_test_status(test_id)
        retries = 0
        while call_status['status'] == 'DEAD' and retries < 10:
            time.sleep(3)
            call_status = self.get_test_status(test_id)
            # print('Call status poll attempt ' + str(retries))
            # print(json.dumps(call_status, indent=4))
            retries += 1

        # Make sure the call is alive
        assert call_status['status'] == 'ALIVE'

        # Update the call to pause the recording
        update_call_recording = UpdateCallRecording(RecordingStateEnum('paused'))
        update_response = self.recordings_api_instance.update_call_recording_state(BW_ACCOUNT_ID, call_id, update_call_recording, _return_http_data_only=False)
        assert update_response[1] == 200

        # Update the call to resume the recording
        update_call_recording = UpdateCallRecording(RecordingStateEnum('recording'))
        update_response = self.recordings_api_instance.update_call_recording_state(BW_ACCOUNT_ID, call_id, update_call_recording, _return_http_data_only=False)
        assert update_response[1] == 200

        # Kill the call
        update_call = UpdateCall(state=CallStateEnum('completed'))
        self.calls_api_instance.update_call(BW_ACCOUNT_ID, call_id, update_call)

    def test_list_call_recordings_unauthorized(self):
        # Create a call
        answer_url = MANTECA_BASE_CALLBACK_URL + '/bxml/startRecording'
        (test_id, call_id) = self.create_and_validate_call(answer_url)

        # Poll Manteca to make sure our call is recorded
        call_status = self.get_test_status(test_id)
        retries = 0
        while call_status['callRecorded'] == False and retries < MAX_RETRIES:
            time.sleep(3)
            call_status = self.get_test_status(test_id)
            # print('Recording poll attempt ' + str(retries))
            # print(json.dumps(call_status, indent=4))
            retries += 1

        # If we failed to get a recorded call, fail due to polling timeout
        assert call_status['callRecorded'] == True

        # Use the unauthorized client to try to list recordings
        with self.assertRaises(UnauthorizedException):
            self.unauthorized_recordings_api_instance.list_call_recordings(BW_ACCOUNT_ID, call_id)

    def test_list_call_recordings_invalid(self):
        # Create a call
        answer_url = MANTECA_BASE_CALLBACK_URL + '/bxml/startRecording'
        (test_id, call_id) = self.create_and_validate_call(answer_url)

        # Poll Manteca to make sure our call is recorded
        call_status = self.get_test_status(test_id)
        retries = 0
        while call_status['callRecorded'] == False and retries < MAX_RETRIES:
            time.sleep(3)
            call_status = self.get_test_status(test_id)
            # print('Recording poll attempt ' + str(retries))
            # print(json.dumps(call_status, indent=4))
            retries += 1

        # If we failed to get a recorded call, fail due to polling timeout
        assert call_status['callRecorded'] == True
        
        # Invalid call id
        assert self.recordings_api_instance.list_call_recordings(BW_ACCOUNT_ID, 'not a call id') == []

        # Invalid account id
        with self.assertRaises(ForbiddenException):
            self.recordings_api_instance.list_call_recordings("not an account id", call_id)

        with self.assertRaises(ApiException):
            self.recordings_api_instance.list_call_recordings(1, 2)       


if __name__ == '__main__':
    unittest.main()
