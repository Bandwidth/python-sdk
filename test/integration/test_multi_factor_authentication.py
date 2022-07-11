"""
Integration test for Bandwidth's Multi-Factor Authentication API
"""

import os
import json
import time
import unittest

import bandwidth
from bandwidth.api import mfa_api
from bandwidth.model.code_request import CodeRequest
from bandwidth.model.messaging_code_response import MessagingCodeResponse
from bandwidth.model.verify_code_request import VerifyCodeRequest
from bandwidth.model.verify_code_response import VerifyCodeResponse
from bandwidth.model.mfa_request_error import MfaRequestError
from bandwidth.model.mfa_unauthorized_request_error import MfaUnauthorizedRequestError
from bandwidth.model.mfa_forbidden_request_error import MfaForbiddenRequestError
from bandwidth.model.voice_code_response import VoiceCodeResponse
from bandwidth.exceptions import ApiException, UnauthorizedException, ForbiddenException


class TestMultiFactorAuthentication(unittest.TestCase):
    """Multi-Factor Authentication API integration test
    """

    def setUp(self):
        configuration = bandwidth.Configuration(
            username=os.environ['BW_USERNAME'],
            password=os.environ['BW_PASSWORD']
        )
        api_client = bandwidth.ApiClient(configuration)
        self.api_instance = mfa_api.MFAApi(api_client)
        self.account_id = os.environ['BW_ACCOUNT_ID']

        self.messaging_code_request = CodeRequest(
            to=os.environ['USER_NUMBER'],
            _from=os.environ['BW_NUMBER'],
            application_id=os.environ['BW_MESSAGING_APPLICATION_ID'],
            scope="scope",
            message="Your temporary {NAME} {SCOPE} code is {CODE}",
            digits=6,
        )

        self.voice_code_request = CodeRequest(
            to=os.environ['USER_NUMBER'],
            _from=os.environ['BW_NUMBER'],
            application_id=os.environ['BW_VOICE_APPLICATION_ID'],
            scope="scope",
            message="Your temporary {NAME} {SCOPE} code is {CODE}",
            digits=6,
        )

        self.bad_code_request = CodeRequest(
            to=os.environ['USER_NUMBER'],
            _from=os.environ['BW_NUMBER'],
            application_id='not_an_application_id',
            scope="scope",
            message="Your temporary {NAME} {SCOPE} code is {CODE}",
            digits=6,
        )

    def validateAuthException(self, context: ApiException, expectedException: ApiException, expected_status_code: int):
        """Validates that an auth exception (401 or 403) is properly formatted
        Args:
            context (ApiException): Exception to validate
            expectedException (ApiException): Expected exception type
            expected_status_code (int): Expected status code
        """
        self.assertIs(type(context.exception), expectedException)
        self.assertIs(type(context.exception.status), int)
        self.assertEqual(context.exception.status, expected_status_code)
        self.assertIs(type(context.exception.body), str)

    def testSuccessfulMfaGenerateMessagingCodeRequest(self):
        """Test a successful MFA messaging code request 
        """
        api_response_with_http_info = self.api_instance.generate_messaging_code(
            self.account_id, self.messaging_code_request, _return_http_data_only=False)
        self.assertEqual(api_response_with_http_info[1], 200)

        api_response: MessagingCodeResponse = self.api_instance.generate_messaging_code(
            self.account_id, self.messaging_code_request)
        self.assertIs(type(api_response.message_id), str)

    def testSuccessfulMfaGenerateVoiceCodeRequest(self):
        """Test a successful MFA voice code request
        """
        api_response_with_http_info = self.api_instance.generate_voice_code(
            self.account_id, self.voice_code_request, _return_http_data_only=False)
        self.assertEqual(api_response_with_http_info[1], 200)

        api_response: VoiceCodeResponse = self.api_instance.generate_voice_code(
            self.account_id, self.voice_code_request)
        self.assertIs(type(api_response.call_id), str)

    # Will always have to test against False codes unless we incorporate the Manteca project into MFA
    def testSuccessfulMfaGVerifyCodeRequest(self):
        """Test a successful MFA verify code request
        """
        verify_code_request = VerifyCodeRequest(
            to=os.environ['USER_NUMBER'],
            scope="2FA",
            expiration_time_in_minutes=3.0,
            code="123456",
        )
        api_response_with_http_info = self.api_instance.verify_code(
            self.account_id, verify_code_request, _return_http_data_only=False)
        self.assertEqual(api_response_with_http_info[1], 200)

        api_response: VerifyCodeResponse = self.api_instance.verify_code(
            self.account_id, verify_code_request)
        self.assertEqual(type(api_response), VerifyCodeResponse)
        self.assertEqual(type(api_response.valid), bool)
        self.assertIs(api_response.valid, False)

    def testBadRequest(self):
        """Validates a bad (400) request
        """
        with self.assertRaises(ApiException) as context:
            self.api_instance.generate_messaging_code(self.account_id, self.bad_code_request)

        self.validateAuthException(context, ApiException, 400)

    @unittest.skip('Skip while we determine how to force this API to return a 401')
    def testUnauthorizedRequest(self):
        """Validate an unauthorized (401) request
        """
        configuration = bandwidth.Configuration(
            username='bad_username',
            password='bad_password'
        )
        unauthorized_api_client = bandwidth.ApiClient(configuration)
        unauthorized_api_instance = mfa_api.MFAApi(unauthorized_api_client)

        with self.assertRaises(UnauthorizedException) as context:
            unauthorized_api_instance.generate_messaging_code(
                self.account_id, self.messaging_code_request)

        self.validateAuthException(context, UnauthorizedException, 401)

    def testForbiddenRequest(self):
        """Validate a forbidden (403) request
        """
        configuration = bandwidth.Configuration(
            username=os.environ['BW_USERNAME_FORBIDDEN'],
            # password=os.environ['BW_PASSWORD_FORBIDDEN'],
            password='bad_password'
        )
        forbidden_api_client = bandwidth.ApiClient(configuration)
        forbidden_api_instance = mfa_api.MFAApi(forbidden_api_client)

        with self.assertRaises(ForbiddenException) as context:
            forbidden_api_instance.generate_messaging_code(
                self.account_id, self.messaging_code_request)

        self.validateAuthException(context, ForbiddenException, 403)
