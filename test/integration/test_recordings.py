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
from bandwidth.exceptions import ForbiddenException, NotFoundException, UnauthorizedException
from bandwidth.model.call_recording_metadata import CallRecordingMetadata
from bandwidth.model.call_state import CallState
from bandwidth.model.call_state_enum import CallStateEnum
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
    # BW Credentials
    BW_USERNAME = os.environ["BW_USERNAME"]
    BW_PASSWORD = os.environ["BW_PASSWORD"]
    BW_ACCOUNT_ID = os.environ["BW_ACCOUNT_ID"]

    # Manteca Numbers
    MANTECA_ACTIVE_NUMBER = os.environ["MANTECA_ACTIVE_NUMBER"]
    MANTECA_IDLE_NUMBER = os.environ["MANTECA_IDLE_NUMBER"]

    # Manteca
    MANTECA_BASE_URL = os.environ["MANTECA_BASE_URL"]
    MANTECA_STATUS_URL = MANTECA_BASE_URL + "tests/"
    MANTECA_APPLICATION_ID = os.environ["MANTECA_APPLICATION_ID"]

    # Test Environment
    PYTHON_VERSION = os.environ["PYTHON_VERSION"]
    OPERATING_SYSTEM = os.environ["OPERATING_SYSTEM"]
except KeyError as e:
    raise Exception("Environmental variables not found")

MAX_RETRIES = 40
TEST_SLEEP = 5

class TestRecordings(unittest.TestCase):
    """
    Integration tests for the Recordings API.
    """

    global callIdArray
    callIdArray = []

    def setUp(self) -> None:
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

    def tearDown(self) -> None:
        """
           Whenever we create an actual call, we'll add the call_id to the callIdArray. Then when the integration test is done, as part of tearDown we'll:
                Do a get to check is the call status is still active
                    If so, update to completed to end the call
                    If not, pop that callID off the array
                Once we go through the whole array, we clear the array so it's empty for the next integration test.    
           if the status is active, send UpdateCall to change to completed
        """

        if len(callIdArray) > 0:       
            for callId in callIdArray:
                body = UpdateCall(state=CallStateEnum("completed"))
                get_call_response: CallState = self.calls_api_instance.get_call_state(BW_ACCOUNT_ID, callId, _return_http_data_only=False)
                if get_call_response[0].state == 'active':
                    self.calls_api_instance.update_call(BW_ACCOUNT_ID, callId, body, _return_http_data_only=False)
                elif get_call_response[0].state == 'complete':
                    callIdArray.remove(callId)
            callIdArray.clear()
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
            url=MANTECA_BASE_URL + 'tests',
            body={
                'os': OPERATING_SYSTEM,
                'language': 'python' + PYTHON_VERSION,
                'type': 'CALL'
            }
        )

        # Get the test id from the response
        test_id = json.loads(response.data)

        # Make a CreateCall body and assign the appropriate params
        call_body = CreateCall(to=MANTECA_IDLE_NUMBER, _from=MANTECA_ACTIVE_NUMBER, application_id=MANTECA_APPLICATION_ID, answer_url=answer_url, tag=test_id)

        # Make the call
        create_call_response: CreateCallResponse = self.calls_api_instance.create_call(BW_ACCOUNT_ID, call_body)

        # Verify info about the call
        assert len(create_call_response.call_id) == 47    # assert request created and id matches expected length (47)
        assert create_call_response.account_id == BW_ACCOUNT_ID
        assert create_call_response.application_id == MANTECA_APPLICATION_ID
        assert create_call_response.to == MANTECA_IDLE_NUMBER
        assert create_call_response._from == MANTECA_ACTIVE_NUMBER
        assert create_call_response.call_url == "https://voice.bandwidth.com/api/v2/accounts/" + \
            BW_ACCOUNT_ID + "/calls/" + create_call_response.call_id

        # Adding the call to the callIdArray
        callIdArray.append(create_call_response.call_id)

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
        assert call_status['callRecorded'] == True

        # Return our test_id and call_id
        return (test_id, call_id)

    def validate_recording(self, recording: CallRecordingMetadata, call_id: str) -> None:
        """
        Validate the given recording metadata.

        Args:
            recording (CallRecordingMetadata): The recording metadata to validate.
            call_id (str): The call id associated with the given recording.
        """
        assert recording.account_id == BW_ACCOUNT_ID
        assert recording.call_id == call_id
        assert recording.application_id == MANTECA_APPLICATION_ID
        assert recording.status == 'complete'
        assert recording.file_format == FileFormatEnum('wav')

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

    def test_successful_call_recording(self) -> None:
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

        # Have a recorded call
        (test_id, call_id) = self.complete_recorded_call()
            
        # List Call Recordings Endpoint
        response: List[CallRecordingMetadata] = self.recordings_api_instance.list_call_recordings(BW_ACCOUNT_ID, call_id, _return_http_data_only=False)
        assert response[1] == 200 # Check response code
        
        # We should get back 1 recording
        call_recordings = response[0]
        assert len(call_recordings) == 1
        
        # Checks on the first recording
        first_recording: CallRecordingMetadata = call_recordings[0]
        self.validate_recording(first_recording, call_id)
        recording_id = first_recording.recording_id

        # Get Single Recording Endpoint
        recording_response: CallRecordingMetadata = self.recordings_api_instance.get_call_recording(BW_ACCOUNT_ID, call_id, recording_id, _return_http_data_only=False)
        assert recording_response[1] == 200

        recording = recording_response[0]
        assert recording.recording_id == recording_id
        self.validate_recording(recording, call_id)

        # Download recording media
        recording_media_response = self.recordings_api_instance.download_call_recording(BW_ACCOUNT_ID, call_id, recording_id, _preload_content=False)
        call_recording_media = recording_media_response.data

        '''
        Do a verification test on the actual recording data?
        '''
        # # print(call_recording_media)
        # with open("zzzz.wav", "wb") as fp:
        #     fp.write(call_recording_media)

        # Create Transcription Request
        transcription_url = MANTECA_BASE_URL + "/transcriptions"
        transcribe_recording_request = TranscribeRecording(callback_url=transcription_url,tag=test_id)
        transcription_response = self.recordings_api_instance.transcribe_call_recording(BW_ACCOUNT_ID, call_id, recording_id, transcribe_recording_request, _return_http_data_only=False)
        assert transcription_response[1] == 204

        # Poll Manteca to make sure our call is transcribed
        call_status = self.get_test_status(test_id)
        retries = 0
        while call_status['callTranscribed'] == False and retries < MAX_RETRIES:
            time.sleep(TEST_SLEEP)
            call_status = self.get_test_status(test_id)
            retries += 1

        # If we failed to get a transcribed call, fail due to polling timeout
        assert call_status['callTranscribed'] == True

        # Get the transcription
        transcription_response = self.recordings_api_instance.get_call_transcription(BW_ACCOUNT_ID, call_id, recording_id, _return_http_data_only=False)
        assert transcription_response[1] == 200

        transcription_list = transcription_response[0]
        assert len(transcription_list.transcripts) == 1
        transcription = transcription_list.transcripts[0]
        assert isinstance(transcription, Transcription)
        assert isinstance(transcription.text, str)
        assert isinstance(transcription.confidence, float)

        # Delete the transcription
        delete_transcription_response = self.recordings_api_instance.delete_call_transcription(BW_ACCOUNT_ID, call_id, recording_id, _return_http_data_only=False)
        assert delete_transcription_response[1] == 204
        with self.assertRaises(NotFoundException):
            self.recordings_api_instance.get_call_transcription(BW_ACCOUNT_ID, call_id, recording_id)

        # Delete Recording media
        delete_recording_media_response = self.recordings_api_instance.delete_recording_media(BW_ACCOUNT_ID, call_id, recording_id, _return_http_data_only=False)
        # Validate the 204 response
        assert delete_recording_media_response[1] == 204

        # Delete Recording
        delete_recording_response = self.recordings_api_instance.delete_recording(BW_ACCOUNT_ID, call_id, recording_id, _return_http_data_only=False)
        assert delete_recording_response[1] == 204
        call_recordings = self.recordings_api_instance.list_call_recordings(BW_ACCOUNT_ID, call_id)
        assert len(call_recordings) == 0

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

    def test_invalid_list_call_recordings(self) -> None:
        """
        Tests invalid flows for list_call_recordings
        """

        # Have a recorded call
        (test_id, call_id) = self.complete_recorded_call()

        # Use the unauthorized client to try to list recordings (401)
        with self.assertRaises(UnauthorizedException):
            self.unauthorized_recordings_api_instance.list_call_recordings(BW_ACCOUNT_ID, call_id)

        # Invalid account id (403)
        with self.assertRaises(ForbiddenException):
            self.recordings_api_instance.list_call_recordings("not an account id", call_id)    
        
        # Non-existent call id
        # This should probably be a 404, but actually returns an empty list
        assert self.recordings_api_instance.list_call_recordings(BW_ACCOUNT_ID, "not a call id") == []

    def test_invalid_get_call_recording(self) -> None:
        """
        Tests invalid flows for get_call_recording
        """

        # Have a recorded call
        (test_id, call_id) = self.complete_recorded_call()

        # Get our recording id
        recordings = self.recordings_api_instance.list_call_recordings(BW_ACCOUNT_ID, call_id)
        recording_id = recordings[0].recording_id

        # Use the unauthorized client to try to get a recording (401)
        with self.assertRaises(UnauthorizedException):
            self.unauthorized_recordings_api_instance.get_call_recording(BW_ACCOUNT_ID, call_id, recording_id)
        
        # Non-existent account id (403)
        with self.assertRaises(ForbiddenException):
            self.recordings_api_instance.get_call_recording("not an account id", call_id, recording_id)

        # Non-existent recording id (404)
        with self.assertRaises(NotFoundException):
            self.recordings_api_instance.get_call_recording(BW_ACCOUNT_ID, call_id, "not a recording id")

    def test_invalid_download_call_recording(self) -> None:
        """
        Tests invalid flows for download_call_recording
        """

        # Have a recorded call
        (test_id, call_id) = self.complete_recorded_call()

        # Get our recording id
        recordings = self.recordings_api_instance.list_call_recordings(BW_ACCOUNT_ID, call_id)
        recording_id = recordings[0].recording_id

        # Use the unauthorized client to try to download a recording (401)
        with self.assertRaises(UnauthorizedException):
            self.unauthorized_recordings_api_instance.download_call_recording(BW_ACCOUNT_ID, call_id, recording_id)
        
        # Non-existent account id (403)
        with self.assertRaises(ForbiddenException):
            self.recordings_api_instance.download_call_recording("not an account id", call_id, recording_id)

        # Non-existent recording id (404)
        with self.assertRaises(NotFoundException):
            self.recordings_api_instance.download_call_recording(BW_ACCOUNT_ID, call_id, "not a recording id")

    def test_invalid_transcribe_call_recording(self) -> None:
        """
        Tests invalid flows for transcribe_call_recording
        """

        # Have a recorded call
        (test_id, call_id) = self.complete_recorded_call()

        # Get our recording id
        recordings = self.recordings_api_instance.list_call_recordings(BW_ACCOUNT_ID, call_id)
        recording_id = recordings[0].recording_id

        # Create a standard TranscribeRecording instance to use
        transcription_url = MANTECA_BASE_URL + "transcriptions"
        transcribe_recording = TranscribeRecording(callback_url=transcription_url, tag=test_id)

        # Use the unauthorized client to request a transcription (401)
        with self.assertRaises(UnauthorizedException):
            self.unauthorized_recordings_api_instance.transcribe_call_recording(BW_ACCOUNT_ID, call_id, recording_id, transcribe_recording)

        # Non existent account id (403)
        with self.assertRaises(ForbiddenException):
            self.recordings_api_instance.transcribe_call_recording("not an account id", call_id, recording_id, transcribe_recording)

        # Non-existent recording id (404)
        # TODO: This does not work right now as the API is unexpectedly returning a 502 Bad Gateway for this request.
        # with self.assertRaises(NotFoundException):
        #     self.recordings_api_instance.transcribe_call_recording(BW_ACCOUNT_ID, call_id, "not a recording id", transcribe_recording)        


    def test_invalid_get_call_transcription(self) -> None:
        """
        Tests invalid flows for get_call_transcription
        """

        # Have a recorded call
        (test_id, call_id) = self.complete_recorded_call()

        # Get our recording id
        recordings = self.recordings_api_instance.list_call_recordings(BW_ACCOUNT_ID, call_id)
        recording_id = recordings[0].recording_id

        # Create a transcription
        transcription_url = MANTECA_BASE_URL + "transcriptions"
        transcribe_recording = TranscribeRecording(callback_url=transcription_url, tag=test_id)
        self.recordings_api_instance.transcribe_call_recording(BW_ACCOUNT_ID, call_id, recording_id, transcribe_recording)

        # Poll Manteca to make sure our call is transcribed
        call_status = self.get_test_status(test_id)
        retries = 0
        while call_status['callTranscribed'] == False and retries < MAX_RETRIES:
            time.sleep(TEST_SLEEP)
            call_status = self.get_test_status(test_id)
            retries += 1

        # If we failed to get a transcribed call, fail due to polling timeout (TEMP COMMENTED)
        assert call_status['callTranscribed'] == True

        # Use the unauthorized client to get transcripion (401)
        with self.assertRaises(UnauthorizedException):
            self.unauthorized_recordings_api_instance.get_call_transcription(BW_ACCOUNT_ID, call_id, recording_id)

        # Non-existent account id (403)
        with self.assertRaises(ForbiddenException):
            self.recordings_api_instance.get_call_transcription("not an account id", call_id, recording_id)

        # Non-existent recording id (404)
        with self.assertRaises(NotFoundException):
            self.recordings_api_instance.get_call_transcription(BW_ACCOUNT_ID, call_id, "not a recording id")

    def test_invalid_delete_call_transcription(self) -> None:
        """
        Tests invalid flows for delete_call_transcription
        """

        # Have a recorded call
        (test_id, call_id) = self.complete_recorded_call()

        # Get our recording id
        recordings = self.recordings_api_instance.list_call_recordings(BW_ACCOUNT_ID, call_id)
        recording_id = recordings[0].recording_id

        # Create a transcription
        transcription_url = MANTECA_BASE_URL + "transcriptions"
        transcribe_recording = TranscribeRecording(callback_url=transcription_url, tag=test_id)
        self.recordings_api_instance.transcribe_call_recording(BW_ACCOUNT_ID, call_id, recording_id, transcribe_recording)

        # Poll Manteca to make sure our call is transcribed
        call_status = self.get_test_status(test_id)
        retries = 0
        while call_status['callTranscribed'] == False and retries < MAX_RETRIES:
            time.sleep(TEST_SLEEP)
            call_status = self.get_test_status(test_id)
            retries += 1

        # If we failed to get a transcribed call, fail due to polling timeout (TEMP COMMENTED)
        assert call_status['callTranscribed'] == True

        # Use the unauthorized client to delete transcripion (401)
        with self.assertRaises(UnauthorizedException):
            self.unauthorized_recordings_api_instance.delete_call_transcription(BW_ACCOUNT_ID, call_id, recording_id)

        # Non-existent account id (403)
        with self.assertRaises(ForbiddenException):
            self.recordings_api_instance.delete_call_transcription("not an account id", call_id, recording_id)

        # Non-existent recording id (404)
        with self.assertRaises(NotFoundException):
            self.recordings_api_instance.delete_call_transcription(BW_ACCOUNT_ID, call_id, "not a recording id")

    def test_invalid_delete_recording_media(self) -> None:
        """
        Tests invalid flows for delete_recording_media
        """

        # Have a recorded call
        (test_id, call_id) = self.complete_recorded_call()

        # Get our recording id
        recordings = self.recordings_api_instance.list_call_recordings(BW_ACCOUNT_ID, call_id)
        recording_id = recordings[0].recording_id

        # Use the unauthorized client to try to delete a recording (401)
        with self.assertRaises(UnauthorizedException):
            self.unauthorized_recordings_api_instance.delete_recording_media(BW_ACCOUNT_ID, call_id, recording_id)
        
        # Non-existent account id (403)
        with self.assertRaises(ForbiddenException):
            self.recordings_api_instance.delete_recording_media("not an account id", call_id, recording_id)

        # Non-existent recording id (404)
        with self.assertRaises(NotFoundException):
            self.recordings_api_instance.delete_recording_media(BW_ACCOUNT_ID, call_id, "not a recording id")

    def test_invalid_delete_recording(self) -> None:
        """
        Tests invalid flows for delete_recording
        """

        # Have a recorded call
        (test_id, call_id) = self.complete_recorded_call()

        # Get our recording id
        recordings = self.recordings_api_instance.list_call_recordings(BW_ACCOUNT_ID, call_id)
        recording_id = recordings[0].recording_id

        # Use the unauthorized client to try to delete a recording (401)
        with self.assertRaises(UnauthorizedException):
            self.unauthorized_recordings_api_instance.delete_recording(BW_ACCOUNT_ID, call_id, recording_id)
        
        # Non-existent account id (403)
        with self.assertRaises(ForbiddenException):
            self.recordings_api_instance.delete_recording("not an account id", call_id, recording_id)

        # Non-existent recording id (404)
        with self.assertRaises(NotFoundException):
            self.recordings_api_instance.delete_recording(BW_ACCOUNT_ID, call_id, "not a recording id")

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
        assert call_status['status'] == 'ALIVE'

        # Common models
        pause_recording = UpdateCallRecording(RecordingStateEnum('paused'))
        resume_recording = UpdateCallRecording(RecordingStateEnum('recording'))

        # Use the unauthorized client to try to update (401)
        with self.assertRaises(UnauthorizedException):
            self.unauthorized_recordings_api_instance.update_call_recording_state(BW_ACCOUNT_ID, call_id, pause_recording)

        # Non-existent account id (403)
        with self.assertRaises(ForbiddenException):
            self.recordings_api_instance.update_call_recording_state("not an account id", call_id, pause_recording)

        # Non-existent call id (404)
        with self.assertRaises(NotFoundException):
            self.recordings_api_instance.update_call_recording_state(BW_ACCOUNT_ID, "not a call id", pause_recording)        

        # Kill the call
        update_call = UpdateCall(state=CallStateEnum('completed'))
        self.calls_api_instance.update_call(BW_ACCOUNT_ID, call_id, update_call)


if __name__ == '__main__':
    unittest.main()
