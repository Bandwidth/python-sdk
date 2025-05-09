"""
Integration test for Bandwidth's Voice Transcriptions API
"""
import unittest
import time

from hamcrest import *
from bandwidth import ApiClient, Configuration
from bandwidth.rest import RESTClientObject, RESTResponse
from bandwidth.api.transcriptions_api import TranscriptionsApi
from bandwidth.api.calls_api import CallsApi
from bandwidth.models import CreateCall, CallTranscriptionMetadata, CallTranscriptionResponse, CallTranscription
from test.utils.env_variables import *


class TestTranscriptionsApi(unittest.TestCase):
    """TranscriptionsApi integration Test"""

    def setUp(self) -> None:
        configuration = Configuration(
            username=BW_USERNAME,
            password=BW_PASSWORD
        )
        api_client = ApiClient(configuration)

        self.calls_api_instance = CallsApi(api_client)
        self.transcriptions_api_instance = TranscriptionsApi(api_client)

        # Rest client for interacting with Manteca
        self.rest_client = RESTClientObject(Configuration.get_default_copy())

        # Call ID Array
        self.callIdArray = []
        self.SLEEP_TIME_SEC = 3

        # Transcription ID
        self.transcription_id: str

    def create_call_transcription(self) -> None:

        # Initialize the call with Manteca
        response = self.rest_client.request(
            method='POST',
            url=MANTECA_BASE_URL + '/tests',
            body={
                'os': OPERATING_SYSTEM,
                'language': 'python' + PYTHON_VERSION,
                'type': 'CALL'
            },
            headers={
                'Content-Type': 'application/json'
            }
        )

        # Get the test id from the response
        test_id = response.response.data.decode("utf-8")
        answer_url = MANTECA_BASE_URL + '/bxml/idle'

        # Make a CreateCall body and assign the appropriate params
        call_body = CreateCall(to=MANTECA_IDLE_NUMBER, var_from=MANTECA_ACTIVE_NUMBER,
                               application_id=MANTECA_APPLICATION_ID, answer_url=answer_url, tag=test_id)

        # Make the call
        create_call_response: CreateCallResponse = self.calls_api_instance.create_call(
            BW_ACCOUNT_ID, call_body)
        # assert_that(create_call_response.status_code, equal_to(201))

        # Get the call id from the response
        self.call_id = create_call_response.call_id

        # Adding the call to the callIdArray
        self.callIdArray.append(create_call_response.call_id)


        time.sleep(self.SLEEP_TIME_SEC)
        start_transcription_bxml = '<?xml version="1.0" encoding="UTF-8"?><Response><StartTranscription name="' + self.call_id + '" tracks="inbound"></StartTranscription><Pause duration="6"/></Response>'
        start_response = self.calls_api_instance.update_call_bxml_with_http_info(
            BW_ACCOUNT_ID, self.call_id, start_transcription_bxml)
        assert_that(start_response.status_code, equal_to(204))

        stop_transcription_bxml = '<?xml version="1.0" encoding="UTF-8"?><Response><StopTranscription name="' + self.call_id + '"></StopTranscription></Response>'
        stop_response = self.calls_api_instance.update_call_bxml_with_http_info(
            BW_ACCOUNT_ID, self.call_id, stop_transcription_bxml)
        assert_that(stop_response.status_code, equal_to(204))
        time.sleep(self.SLEEP_TIME_SEC)

        end_response = self.calls_api_instance.update_call_with_http_info(
            BW_ACCOUNT_ID, self.call_id, {"state": "completed"})
        assert_that(end_response.status_code, equal_to(200))

    def list_real_time_transcriptions(self) -> None:
        """Test case for list_real_time_transcriptions

        Enumerate transcriptions made with StartTranscription
        """
        time.sleep(self.SLEEP_TIME_SEC * 20)
        response = self.transcriptions_api_instance.list_real_time_transcriptions_with_http_info(
            BW_ACCOUNT_ID, self.call_id)

        assert_that(response.status_code, equal_to(200))
        assert_that(response.data, instance_of(list))
        assert_that(response.data[0], instance_of(CallTranscriptionMetadata))
        assert_that(response.data[0].transcription_id, instance_of(str))
        assert_that(response.data[0].transcription_url, instance_of(str))
        assert_that(response.data[0].transcription_name, instance_of(str))

        self.transcription_id = response.data[0].transcription_id

    def get_real_time_transcription(self) -> None:
        """Test case for get_real_time_transcription

        Retrieve a specific transcription
        """
        response = self.transcriptions_api_instance.get_real_time_transcription_with_http_info(
            BW_ACCOUNT_ID, self.call_id, self.transcription_id)

        assert_that(response.status_code, equal_to(200))
        assert_that(response.data, instance_of(CallTranscriptionResponse))
        assert_that(response.data.account_id, equal_to(BW_ACCOUNT_ID))
        assert_that(response.data.call_id, equal_to(self.call_id))
        assert_that(response.data.transcription_id, equal_to(self.transcription_id))
        assert_that(response.data.tracks, instance_of(list))
        assert_that(response.data.tracks[0], instance_of(CallTranscription))
        assert_that(response.data.tracks[0].track, equal_to('inbound'))
        assert_that(response.data.tracks[0].confidence, instance_of(float))

    def delete_real_time_transcription(self) -> None:
        """Test case for delete_real_time_transcription

        Delete a specific transcription
        """
        response = self.transcriptions_api_instance.delete_real_time_transcription_with_http_info(
            BW_ACCOUNT_ID, self.call_id, self.transcription_id)

        assert_that(response.status_code, equal_to(200))

    def _steps(self):
        call_order = [
            'create_call_transcription',
            'list_real_time_transcriptions',
            'get_real_time_transcription',
            'delete_real_time_transcription'
        ]
        for name in call_order:
            yield name, getattr(self, name)

    @unittest.skip("PV Issues")
    def test_steps(self) -> None:
        """Test each function from _steps.call_order in specified order
        """

        for name, step in self._steps():
            step()

if __name__ == '__main__':
    unittest.main()
