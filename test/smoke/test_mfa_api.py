"""
Integration test for Bandwidth's Multi-Factor Authentication API
"""

import os
import time
import unittest
import logging
from random import randint

import bandwidth
from bandwidth.api import mfa_api
from bandwidth.models.code_request import CodeRequest
from bandwidth.models.messaging_code_response import MessagingCodeResponse
from bandwidth.models.verify_code_request import VerifyCodeRequest
from bandwidth.models.verify_code_response import VerifyCodeResponse
from bandwidth.models.voice_code_response import VoiceCodeResponse
from bandwidth.exceptions import ApiException, BadRequestException, UnauthorizedException, ForbiddenException
from test.utils.env_variables import *

from hamcrest.core import *
from hamcrest.library import *

class TestMultiFactorAuthentication(unittest.TestCase):
    """Multi-Factor Authentication API integration Test
    """

    def setUp(self) -> None:
        configuration = bandwidth.Configuration(
            username=BW_USERNAME,
            password=BW_PASSWORD
        )
        api_client = bandwidth.ApiClient(configuration)
        self.api_instance = mfa_api.MFAApi(api_client)
        self.account_id = BW_ACCOUNT_ID
        self.messaging_code_request = CodeRequest(
            to=USER_NUMBER,
            var_from=BW_NUMBER,
            application_id=BW_MESSAGING_APPLICATION_ID,
            scope="scope",
            message="Your temporary {NAME} {SCOPE} code is {CODE}",
            digits=6,
        )
        self.voice_code_request = CodeRequest(
            to=USER_NUMBER,
            var_from=BW_NUMBER,
            application_id=BW_VOICE_APPLICATION_ID,
            scope="scope",
            message="Your temporary {NAME} {SCOPE} code is {CODE}",
            digits=6,
        )
        self.bad_code_request = CodeRequest(
            to=USER_NUMBER,
            var_from=BW_NUMBER,
            application_id='not_an_application_id',
            scope="scope",
            message="Your temporary {NAME} {SCOPE} code is {CODE}",
            digits=6,
        )

    def assertAuthException(self, context: Exception, expected_exception: Exception, expected_status_code: int) -> None:
        """Validates that an auth exception (401 or 403) is properly formatted
        Args:
            context (ApiException): Exception to validate
            expected_exception (ApiException): Expected exception type
            expected_status_code (int): Expected status code
        """
        self.assertIs(type(context.exception), expected_exception)
        self.assertIs(type(context.exception.status), int)
        self.assertEqual(context.exception.status, expected_status_code)
        self.assertIs(type(context.exception.body), str)

        # alternate option using hamcrest mathcers - reads like normal sentence, easy to read/speak & less brain overload
        assert_that(context.exception, is_(expected_exception))

        assert_that(context.exception, has_properties(
            'status', equal_to(expected_status_code),
            'body', not_none())
        )

    def testSuccessfulMfaGenerateMessagingCodeRequest(self) -> None:
        """Test a successful MFA messaging code request
        """
        api_response_with_http_info = self.api_instance.generate_messaging_code_with_http_info(
            self.account_id, self.messaging_code_request
        )
        self.assertEqual(api_response_with_http_info.status_code, 200)

        api_response: MessagingCodeResponse = self.api_instance.generate_messaging_code(
            self.account_id, self.messaging_code_request)
        self.assertIs(type(api_response.message_id), str)

    def testSuccessfulMfaGenerateVoiceCodeRequest(self) -> None:
        """Test a successful MFA voice code request
        """
        api_response_with_http_info = self.api_instance.generate_voice_code_with_http_info(
            self.account_id, self.voice_code_request
        )
        self.assertEqual(api_response_with_http_info.status_code, 200)

        api_response: VoiceCodeResponse = self.api_instance.generate_voice_code(
            self.account_id, self.voice_code_request)
        self.assertIs(type(api_response.call_id), str)

    # Will always have to test against False codes unless we incorporate the Manteca project into MFA
    def testSuccessfulMfaGVerifyCodeRequest(self) -> None:
        """Test a successful MFA verify code request
        """
        verify_code_request = VerifyCodeRequest(
            to="+1" + str(randint(1111111111, 9999999999)),
            scope="2FA",
            expiration_time_in_minutes=3.0,
            code="123456",
        )
        api_response_with_http_info = self.api_instance.verify_code_with_http_info(
            self.account_id, verify_code_request
        )
        self.assertEqual(api_response_with_http_info.status_code, 200)

        api_response: VerifyCodeResponse = self.api_instance.verify_code(
            self.account_id, verify_code_request)
        self.assertEqual(type(api_response), VerifyCodeResponse)
        self.assertEqual(type(api_response.valid), bool)
        self.assertIs(api_response.valid, False)

        # can be simplified
        assert_that(api_response, has_property('valid', False))

    def testBadRequest(self) -> None:
        """Validates a bad (400) request
        """
        with self.assertRaises(BadRequestException) as context:
            self.api_instance.generate_messaging_code(self.account_id, self.bad_code_request)

        self.assertAuthException(context, BadRequestException, 400)

    def testUnauthorizedRequest(self) -> None:
        """Validate an unauthorized (401) request
        """
        unauthorized_api_client = bandwidth.ApiClient()
        unauthorized_api_instance = mfa_api.MFAApi(unauthorized_api_client)

        with self.assertRaises(UnauthorizedException) as context:
            unauthorized_api_instance.generate_messaging_code(
                self.account_id, self.messaging_code_request
            )

        self.assertAuthException(context, UnauthorizedException, 401)

    def testForbiddenRequest(self) -> None:
        """Validate a forbidden (403) request
        """
        configuration = bandwidth.Configuration(
            username=FORBIDDEN_USERNAME,
            # password=FORBIDDEN_PASSWORD,
            password='bad_password'
        )
        forbidden_api_client = bandwidth.ApiClient(configuration)
        forbidden_api_instance = mfa_api.MFAApi(forbidden_api_client)

        with self.assertRaises(ForbiddenException) as context:
            forbidden_api_instance.generate_messaging_code(
                self.account_id, self.messaging_code_request
            )

        self.assertAuthException(context, ForbiddenException, 403)

    def testRateLimit(self) -> None:
        """Validate that the API returns a 429 error, and that the 429 clears after 30 seconds
        """
        verify_code_request = VerifyCodeRequest(
            to="+1" + str(randint(1111111111, 9999999999)),
            scope="2FA",
            expiration_time_in_minutes=3.0,
            code="123456",
        )
        call_count = 1
        while True:
            try:
                logging.debug('Testing rate limit, attempt #'+ str(call_count))
                self.api_instance.verify_code(
                    self.account_id, verify_code_request
                )
                call_count += 1
            except ApiException as e:
                if e.status == 429:
                    logging.debug('Got rate limit error')
                    time.sleep(35)
                    api_response_with_http_info = self.api_instance.verify_code_with_http_info(
                        self.account_id, verify_code_request
                    )
                    self.assertEqual(api_response_with_http_info.status_code, 200)
                    break
                else:
                    raise e
            except:
                logging.error("Unexpected error while testing rate limit!")
                raise Exception("Unexpected error while testing rate limit!")
