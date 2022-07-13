"""
    Bandwidth

    Bandwidth's Communication APIs  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: letstalk@bandwidth.com
    Generated by: https://openapi-generator.tech
"""


import os
import unittest
import time
import json

import bandwidth
from bandwidth.api.recordings_api import RecordingsApi
from bandwidth.configuration import Configuration
from bandwidth.exceptions import NotFoundException
from bandwidth.model.call_recording_metadata import CallRecordingMetadata
from bandwidth.model.callback_method_enum import CallbackMethodEnum
from bandwidth.api.calls_api import CallsApi
from bandwidth.model.create_call_response import CreateCallResponse
from bandwidth.model.create_call import CreateCall
from bandwidth.model.transcribe_recording import TranscribeRecording
from bandwidth.model.transcription import Transcription
from bandwidth.rest import RESTClientObject


try:
    BW_USERNAME = os.environ["BW_USERNAME"]
    BW_PASSWORD = os.environ["BW_PASSWORD"]
    BW_ACCOUNT_ID = os.environ["BW_ACCOUNT_ID"]
    BW_VOICE_APPLICATION_ID = os.environ["BW_VOICE_APPLICATION_ID"]
    #BW_MESSAGING_APPLICATION_ID = os.environ["BW_MESSAGING_APPLICATION_ID"]
    MANTECA_BASE_CALLBACK_URL = os.environ["MANTECA_BASE_CALLBACK_URL"]
    BW_NUMBER = os.environ["BW_NUMBER"]
    USER_NUMBER = os.environ["USER_NUMBER"]
except KeyError as e:
    raise Exception("Environmental variables not found")

class TestRecordings(unittest.TestCase):
    """CreateCall unit test stubs"""

    def setUp(self):
        configuration = bandwidth.Configuration(
            username = BW_USERNAME,
            password = BW_PASSWORD
        )
        api_client = bandwidth.ApiClient(configuration)

        self.calls_api_instance = CallsApi(api_client)
        self.recordings_api_instance = RecordingsApi(api_client)

    def tearDown(self):
        pass

    def test_successful_get_call_recording(self):
        """
        Create a call and retrieve the recording.
        """

        # Initialize the call with Manteca
        rest_client = RESTClientObject(Configuration.get_default_copy())
        response = rest_client.request(
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

        # Make a CreateCall body and assign the appropriate params
        answer_url = MANTECA_BASE_CALLBACK_URL + 'bxml/startRecording'
        call_body = CreateCall(to=USER_NUMBER, _from=BW_NUMBER, application_id=BW_VOICE_APPLICATION_ID, answer_url=answer_url, tag=test_id)


        # Make the call
        create_call_response: CreateCallResponse = self.calls_api_instance.create_call(BW_ACCOUNT_ID, call_body)

        # Verify info about the call
        assert len(create_call_response.call_id) == 47    # assert request created and id matches expected length (47)
        assert create_call_response.account_id == BW_ACCOUNT_ID
        assert create_call_response.application_id == BW_VOICE_APPLICATION_ID
        assert create_call_response.to == USER_NUMBER
        assert create_call_response._from == BW_NUMBER
        assert create_call_response.call_url == "https://voice.bandwidth.com/api/v2/accounts/" + \
            BW_ACCOUNT_ID + "/calls/" + create_call_response.call_id

        call_id = create_call_response.call_id

        # Wait (TEMP)
        time.sleep(60)

        # List Call Recordings Endpoint
        call_recordings = self.recordings_api_instance.list_call_recordings(BW_ACCOUNT_ID, create_call_response.call_id)
        
        # We should get back 1 recording
        assert len(call_recordings) == 1
        
        # Checks on the first recording
        first_recording = call_recordings[0]
        assert first_recording.account_id == BW_ACCOUNT_ID
        assert first_recording.call_id == call_id
        assert first_recording.application_id == BW_VOICE_APPLICATION_ID
        assert first_recording.status == 'complete'
        # assert first_recording.file_format == 'wav'

        # Get Single Recording Endpoint
        recording_id = first_recording.recording_id

        recording: CallRecordingMetadata = self.recordings_api_instance.get_call_recording(BW_ACCOUNT_ID, call_id, recording_id)
        
        assert recording.recording_id == recording_id
        assert recording.account_id == BW_ACCOUNT_ID
        assert recording.call_id == call_id
        assert recording.application_id == BW_VOICE_APPLICATION_ID
        assert recording.status == 'complete'
        # assert recording.file_format == 'wav'

        # Download recording media
        recording_response = self.recordings_api_instance.download_call_recording(BW_ACCOUNT_ID, call_id, recording_id, _preload_content=False)
        call_recording_media = recording_response.data
        
        '''
        Do a verification test on the actual recording data?
        '''
        # print(call_recording_media)
        # with open("zzzz.wav", "wb") as fp:
        #     fp.write(call_recording_media)

        # Create Transcription Request
        transcription_url = MANTECA_BASE_CALLBACK_URL + "/transcriptions"
        transcribe_recording_request = TranscribeRecording(callback_url=transcription_url)
        self.recordings_api_instance.transcribe_call_recording(BW_ACCOUNT_ID, call_id, recording_id, transcribe_recording_request)

        # Wait
        time.sleep(60)

        # Get the transcription
        transcription_list = self.recordings_api_instance.get_call_transcription(BW_ACCOUNT_ID, call_id, recording_id)
        assert len(transcription_list.transcripts) == 1
        transcription = transcription_list.transcripts[0]
        assert isinstance(transcription, Transcription)
        assert isinstance(transcription.text, str)
        assert isinstance(transcription.confidence, float)

        time.sleep(10)

        # Delete the transcription
        self.recordings_api_instance.delete_call_transcription(BW_ACCOUNT_ID, call_id, recording_id)
        with self.assertRaises(NotFoundException):
            self.recordings_api_instance.get_call_transcription(BW_ACCOUNT_ID, call_id, recording_id)

        # Delete Recording media
        delete_recording_response = self.recordings_api_instance.delete_recording_media(BW_ACCOUNT_ID, call_id, recording_id, _return_http_data_only=False)
        # Validate the 204 response
        assert delete_recording_response[1] == 204 # 

        # Delete Recording
        self.recordings_api_instance.delete_recording(BW_ACCOUNT_ID, call_id, recording_id)
        call_recordings = self.recordings_api_instance.list_call_recordings(BW_ACCOUNT_ID, create_call_response.call_id)
        assert len(call_recordings) == 0



if __name__ == '__main__':
    unittest.main()