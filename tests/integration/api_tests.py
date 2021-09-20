"""
api_tests.py

Integration tests for API requests

@copyright Bandwidth INC
"""
from bandwidth.bandwidth_client import BandwidthClient
from bandwidth.messaging.exceptions.messaging_exception import MessagingException
from bandwidth.exceptions.api_exception import APIException
from bandwidth.messaging.models.message_request import MessageRequest
from bandwidth.voice.models.create_call_request import CreateCallRequest
from bandwidth.voice.models.machine_detection_request import MachineDetectionRequest
from bandwidth.multifactorauth.models.two_factor_code_request_schema import TwoFactorCodeRequestSchema
from bandwidth.multifactorauth.models.two_factor_verify_request_schema import TwoFactorVerifyRequestSchema
from bandwidth.phonenumberlookup.models.order_request import OrderRequest
from bandwidth.configuration import Environment

import unittest

import os
import sys

try:
    BW_USERNAME = os.environ["BW_USERNAME"]
    BW_PASSWORD = os.environ["BW_PASSWORD"]
    BW_ACCOUNT_ID = os.environ["BW_ACCOUNT_ID"]
    BW_VOICE_APPLICATION_ID = os.environ["BW_VOICE_APPLICATION_ID"]
    BW_MESSAGING_APPLICATION_ID = os.environ["BW_MESSAGING_APPLICATION_ID"]
    BASE_CALLBACK_URL = os.environ["BASE_CALLBACK_URL"]
    BW_NUMBER = os.environ["BW_NUMBER"]
    USER_NUMBER = os.environ["USER_NUMBER"]
except:
    raise Exception("Environmental variables not found")


class MonitorTest(unittest.TestCase):
    """
    Class that holds basic monitoring tests for the Python SDK. Makes requests to cover JSON call and response,
    error handling, and binary string uploads and downloads
    """
    def setUp(self):
        """
        Creates the client object
        """
        self.bandwidth_client = BandwidthClient(
            voice_basic_auth_user_name=BW_USERNAME,
            voice_basic_auth_password=BW_PASSWORD,
            messaging_basic_auth_user_name=BW_USERNAME,
            messaging_basic_auth_password=BW_PASSWORD,
            multi_factor_auth_basic_auth_user_name=BW_USERNAME,
            multi_factor_auth_basic_auth_password=BW_PASSWORD,
            phone_number_lookup_basic_auth_user_name=BW_USERNAME,
            phone_number_lookup_basic_auth_password=BW_PASSWORD,
        )
        self.voice_client = self.bandwidth_client.voice_client.client
        self.messaging_client = self.bandwidth_client.messaging_client.client
        self.auth_client = self.bandwidth_client.multi_factor_auth_client.mfa
        self.tn_lookup_client = self.bandwidth_client.phone_number_lookup_client.client

        self.bandwidth_client_with_environment = BandwidthClient(
            voice_basic_auth_user_name=BW_USERNAME,
            voice_basic_auth_password=BW_PASSWORD,
            messaging_basic_auth_user_name=BW_USERNAME,
            messaging_basic_auth_password=BW_PASSWORD,
            multi_factor_auth_basic_auth_user_name=BW_USERNAME,
            multi_factor_auth_basic_auth_password=BW_PASSWORD,
            phone_number_lookup_basic_auth_user_name=BW_USERNAME,
            phone_number_lookup_basic_auth_password=BW_PASSWORD,
            environment=Environment.CUSTOM,
            base_url="https://test.com"
        )


    def test_create_message(self):
        body = MessageRequest()
        body.application_id = BW_MESSAGING_APPLICATION_ID
        body.to = [USER_NUMBER]
        body.mfrom = BW_NUMBER
        body.text = "Python Monitoring"
        response = self.messaging_client.create_message("BW_ACCOUNT_ID", body)
        self.assertTrue(len(response.body.id) > 0) #validate that _some_ id was returned


    def test_create_message_invalid_phone_number(self):
        body = MessageRequest()
        body.application_id = BW_MESSAGING_APPLICATION_ID
        body.to = ["+1invalid"]
        body.mfrom = BW_NUMBER
        body.text = "Python Monitoring"
        try:
            self.messaging_client.create_message(BW_ACCOUNT_ID, body)
            self.assertTrue(False)
        except MessagingException as e:
            self.assertTrue(len(e.description) > 0)
        except:
            self.assertTrue(False)


    def test_upload_download_media(self):
        #define constants for upload media and download media
        media_file_name = 'python_monitoring' #future update to add special symbols
        media_file = b'12345'

        #media upload
        self.messaging_client.upload_media(BW_ACCOUNT_ID, media_file_name, media_file)

        #media download
        downloaded_media_file = self.messaging_client.get_media(BW_ACCOUNT_ID, media_file_name).body

        #validate that the response is the same as the upload
        self.assertEqual(media_file, downloaded_media_file)


    def test_create_call_and_get_call(self):
        body = CreateCallRequest()
        body.mfrom = BW_NUMBER
        body.to = USER_NUMBER
        body.application_id = BW_VOICE_APPLICATION_ID
        body.answer_url = BASE_CALLBACK_URL
        response = self.voice_client.create_call(BW_ACCOUNT_ID, body)
        self.assertTrue(len(response.body.call_id) > 1)

        #get phone call information
        response = self.voice_client.get_call(BW_ACCOUNT_ID, response.body.call_id)
        self.assertTrue(len(response.body.state) > 1)


    def test_create_call_invalid_phone_number(self):
        body = CreateCallRequest()
        body.mfrom = BW_NUMBER
        body.to = "+1invalid"
        body.application_id = BW_VOICE_APPLICATION_ID
        body.answer_url = BASE_CALLBACK_URL
        try:
            self.voice_client.create_call(BW_ACCOUNT_ID, body)
        except APIException as e:
            self.assertTrue(len(e.description) > 0)
        except:
            self.assertTrue(False);


    def create_call_amd_and_get_call(self):
        machine_detection_parameters = MachineDetectionRequest()
        machine_detection_parameters.mode = "async"
        machine_detection_parameters.callback_url = BASE_CALLBACK_URL
        machine_detection_parameters.callback_method = "POST"
        machine_detection_parameters.detection_timeout = 5.0
        machine_detection_parameters.silence_timeout = 5.0
        machine_detection_parameters.speech_threshold = 5.0
        machine_detection_parameters.speech_end_threshold = 5.0
        machine_detection_parameters.delay_result = True

        body = CreateCallRequest()
        body.mfrom = BW_NUMBER
        body.to = USER_NUMBER
        body.application_id = BW_VOICE_APPLICATION_ID
        body.answer_url = BASE_CALLBACK_URL
        body.machine_detection = machine_detection_parameters
        create_response = self.voice_client.create_call(BW_ACCOUNT_ID, body)
        self.assertTrue(len(create_response.body.call_id) > 1)

        #get phone call information
        get_response = self.voice_client.get_call(BW_ACCOUNT_ID, create_response.body.call_id)
        self.assertTrue(len(get_response.body.state) > 1)
        self.assertEqual(get_response.body.callId, create_response.body.call_id)
        self.assertIs(get_response.body.call_id, str)
        self.assertIs(get_response.body.application_id, str)
        self.assertIs(get_response.body.account_id, str)
        self.assertIs(get_response.body.to, str)
        self.assertIs(get_response.body.mfrom, str)
        self.assertIs(get_response.body.direction, str)
        self.assertIs(get_response.body.state, str)
        self.assertIs(get_response.body.start_time, str)
        self.assertIs(get_response.body.last_update, str)

        if get_response.body.disconnect_cause:
            self.assertIs(get_response.body.disconnect_cause, str)
        if get_response.body.error_message:
            self.assertIs(get_response.body.error_message, str)
        if get_response.body.error_id:
            self.assertIs(get_response.body.error_id, str)


    def test_mfa_messaging(self):
        body = TwoFactorCodeRequestSchema(
            mfrom = BW_NUMBER,
            to = USER_NUMBER,
            application_id = BW_MESSAGING_APPLICATION_ID,
            scope = "scope",
            digits = 6,
            message = "Your temporary {NAME} {SCOPE} code is {CODE}"
        )
        response = self.auth_client.create_messaging_two_factor(BW_ACCOUNT_ID, body)
        self.assertTrue(len(response.body.message_id) > 0)


    def test_mfa_voice(self):
        body = TwoFactorCodeRequestSchema(
            mfrom = BW_NUMBER,
            to = USER_NUMBER,
            application_id = BW_VOICE_APPLICATION_ID,
            scope = "scope",
            digits = 6,
            message = "Your temporary {NAME} {SCOPE} code is {CODE}"
        )
        response = self.auth_client.create_voice_two_factor(BW_ACCOUNT_ID, body)
        self.assertTrue(len(response.body.call_id) > 0)


    def test_mfa_verify(self):
        body = TwoFactorVerifyRequestSchema(
            to = USER_NUMBER,
            application_id = BW_VOICE_APPLICATION_ID,
            scope = "scope",
            code = "123456",
            expiration_time_in_minutes = 3
        )
        response = self.auth_client.create_verify_two_factor(BW_ACCOUNT_ID, body)
        self.assertTrue(isinstance(response.body.valid, bool))


    def test_tn_lookup(self):
        body = OrderRequest()
        body.tns = [BW_NUMBER]
        response = self.tn_lookup_client.create_lookup_request(BW_ACCOUNT_ID, body)
        self.assertTrue(response.status_code == 202)

        # test get method with the returned request_id
        request_id = response.body.request_id
        get_response = self.tn_lookup_client.get_lookup_request_status(BW_ACCOUNT_ID, request_id)
        self.assertTrue(get_response.status_code == 200)


if __name__ == '__main__':
    unittest.main()

