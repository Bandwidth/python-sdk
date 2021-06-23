"""
api_tests.py

Integration tests for API requests

@copyright Bandwidth INC
"""
from bandwidth.bandwidth_client import BandwidthClient
from bandwidth.messaging.exceptions.messaging_exception import MessagingException
from bandwidth.voice.exceptions.api_error_response_exception import ApiErrorResponseException
from bandwidth.messaging.models.message_request import MessageRequest
from bandwidth.voice.models.api_create_call_request import ApiCreateCallRequest
from bandwidth.twofactorauth.models.two_factor_code_request_schema import TwoFactorCodeRequestSchema
from bandwidth.twofactorauth.models.two_factor_verify_request_schema import TwoFactorVerifyRequestSchema
from bandwidth.phonenumberlookup.models.order_request import OrderRequest

import unittest

import os

try:
    USERNAME = os.environ["USERNAME"]
    PASSWORD = os.environ["PASSWORD"]
    ACCOUNT_ID = os.environ["ACCOUNT_ID"]
    VOICE_APPLICATION_ID = os.environ["VOICE_APPLICATION_ID"]
    MESSAGING_APPLICATION_ID = os.environ["MESSAGING_APPLICATION_ID"]
    CALLBACK_URL = os.environ["CALLBACK_URL"]
    PHONE_NUMBER_OUTBOUND = os.environ["PHONE_NUMBER_OUTBOUND"]
    PHONE_NUMBER_INBOUND = os.environ["PHONE_NUMBER_INBOUND"]
    MFA_MESSAGING_APPLICATION_ID = os.environ["MFA_MESSAGING_APPLICATION_ID"]
    MFA_VOICE_APPLICATION_ID = os.environ["MFA_VOICE_APPLICATION_ID"]
    PHONE_NUMBER_MFA = os.environ["PHONE_NUMBER_MFA"]
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
            voice_basic_auth_user_name=USERNAME,
            voice_basic_auth_password=PASSWORD,
            messaging_basic_auth_user_name=USERNAME,
            messaging_basic_auth_password=PASSWORD,
            two_factor_auth_basic_auth_user_name=USERNAME,
            two_factor_auth_basic_auth_password=PASSWORD,
            phone_number_lookup_basic_auth_user_name=USERNAME,
            phone_number_lookup_basic_auth_password=PASSWORD,
        )
        self.voice_client = self.bandwidth_client.voice_client.client
        self.messaging_client = self.bandwidth_client.messaging_client.client
        self.auth_client = self.bandwidth_client.two_factor_auth_client.mfa
        self.tn_lookup_client = self.bandwidth_client.phone_number_lookup_client.client

    def test_create_message(self):
        body = MessageRequest()
        body.application_id = MESSAGING_APPLICATION_ID
        body.to = [PHONE_NUMBER_INBOUND]
        body.mfrom = PHONE_NUMBER_OUTBOUND
        body.text = "Python Monitoring"
        response = self.messaging_client.create_message(ACCOUNT_ID, body)
        self.assertTrue(len(response.body.id) > 0) #validate that _some_ id was returned

    def test_create_message_invalid_phone_number(self):
        body = MessageRequest()
        body.application_id = MESSAGING_APPLICATION_ID
        body.to = ["+1invalid"]
        body.mfrom = PHONE_NUMBER_OUTBOUND
        body.text = "Python Monitoring"
        try:
            self.messaging_client.create_message(ACCOUNT_ID, body)
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
        self.messaging_client.upload_media(ACCOUNT_ID, media_file_name, str(len(media_file)), body=media_file)

        #media download
        downloaded_media_file = self.messaging_client.get_media(ACCOUNT_ID, media_file_name).body

        #validate that the response is the same as the upload
        self.assertEqual(media_file, downloaded_media_file)

    def test_create_call_and_get_call_state(self):
        body = ApiCreateCallRequest()
        body.mfrom = PHONE_NUMBER_OUTBOUND
        body.to = PHONE_NUMBER_INBOUND
        body.application_id = VOICE_APPLICATION_ID
        body.answer_url = CALLBACK_URL
        response = self.voice_client.create_call(ACCOUNT_ID, body)
        self.assertTrue(len(response.body.call_id) > 1)

        #get phone call information
        import time
        time.sleep(1) #No guarantee that the info will be immediately available
        response = self.voice_client.get_call_state(ACCOUNT_ID, response.body.call_id)
        self.assertTrue(len(response.body.state) > 1)

    def test_create_call_invalid_phone_number(self):
        body = ApiCreateCallRequest()
        body.mfrom = PHONE_NUMBER_OUTBOUND
        body.to = "+1invalid"
        body.application_id = VOICE_APPLICATION_ID
        body.answer_url = CALLBACK_URL
        try:
            self.voice_client.create_call(ACCOUNT_ID, body)
            self.assertTrue(False)
        except ApiErrorResponseException as e:
            self.assertTrue(len(e.description) > 0)
        except:
            self.assertTrue(False);

    def test_mfa_messaging(self):
        body = TwoFactorCodeRequestSchema(
            mfrom = PHONE_NUMBER_MFA,
            to = PHONE_NUMBER_INBOUND,
            application_id = MFA_MESSAGING_APPLICATION_ID,
            scope = "scope",
            digits = 6,
            message = "Your temporary {NAME} {SCOPE} code is {CODE}"
        )
        response = self.auth_client.create_messaging_two_factor(ACCOUNT_ID, body)
        self.assertTrue(len(response.body.message_id) > 0)

    def test_mfa_voice(self):
        body = TwoFactorCodeRequestSchema(
            mfrom = PHONE_NUMBER_MFA,
            to = PHONE_NUMBER_INBOUND,
            application_id = MFA_VOICE_APPLICATION_ID,
            scope = "scope",
            digits = 6,
            message = "Your temporary {NAME} {SCOPE} code is {CODE}"
        )
        response = self.auth_client.create_voice_two_factor(ACCOUNT_ID, body)
        self.assertTrue(len(response.body.call_id) > 0)

    def test_mfa_verify(self):
        body = TwoFactorVerifyRequestSchema(
            to = PHONE_NUMBER_INBOUND,
            application_id = MFA_VOICE_APPLICATION_ID,
            scope = "scope",
            code = "123456",
            expiration_time_in_minutes = 3
        )
        response = self.auth_client.create_verify_two_factor(ACCOUNT_ID, body)
        self.assertTrue(isinstance(response.body.valid, bool))

    def test_tn_lookup(self):
        body = OrderRequest()
        body.tns = [PHONE_NUMBER_OUTBOUND]
        response = self.tn_lookup_client.create_lookup_request(ACCOUNT_ID, body)
        self.assertTrue(response.status_code == 202)

        # test get method with the returned request_id
        request_id = response.body.request_id
        get_response = self.tn_lookup_client.get_lookup_request_status(ACCOUNT_ID, request_id)
        self.assertTrue(get_response.status_code == 200)

if __name__ == '__main__':
    unittest.main()
