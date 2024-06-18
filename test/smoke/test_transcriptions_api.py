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
from bandwidth.models import CreateCall
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

    def test_create_call(self) -> None:

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
        print(response.response.data)
        print(MANTECA_BASE_URL + '/tests')

        # Get the test id from the response
        test_id = response.response.data.decode("utf-8")
        answer_url = MANTECA_BASE_URL + '/bxml/idle'
        print(answer_url)
        print(test_id)

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


        time.sleep(3)
        print("Call ID: " + self.call_id)
        start_transcription_bxml = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><Response><StartTranscription name=\"#{$manteca_call_id}\" tracks=\"inbound\"></StartTranscription><Pause duration=\"6\"/></Response>"
        start_response = self.calls_api_instance.update_call_bxml_with_http_info(
            BW_ACCOUNT_ID, self.call_id, start_transcription_bxml)
        assert_that(start_response.status_code, equal_to(204))

        # stop_transcription_bxml = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><Response><StopTranscription name=\"#{$manteca_call_id}\"></StopTranscription></Response>"
        # stop_response = self.calls_api_instance.update_call_bxml_with_http_info(
        #     BW_ACCOUNT_ID, self.call_id, stop_transcription_bxml)
        # assert_that(response.stop_response, equal_to(204))

        # end_response = self.calls_api_instance.update_call_with_http_info(
        #     BW_ACCOUNT_ID, self.call_id, {"state": "completed"})
        # assert_that(end_response.status_code, equal_to(200))


    def test_delete_real_time_transcription(self) -> None:
        """Test case for delete_real_time_transcription

        Delete a specific transcription
        """
        pass

    def test_get_real_time_transcription(self) -> None:
        """Test case for get_real_time_transcription

        Retrieve a specific transcription
        """
        pass

    def test_list_real_time_transcriptions(self) -> None:
        """Test case for list_real_time_transcriptions

        Enumerate transcriptions made with StartTranscription
        """
        pass


if __name__ == '__main__':
    unittest.main()
