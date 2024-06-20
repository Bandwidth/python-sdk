"""
Integration test for Bandwidth's Voice Calls API
"""
from bandwidth import ApiResponse
from test.utils.env_variables import *
from test.utils.call_cleanup import callCleanup
import time
import unittest
import datetime

from hamcrest import assert_that, has_properties, not_none, instance_of

import bandwidth
from bandwidth.api import calls_api
from bandwidth.models.create_call import CreateCall
from bandwidth.models.create_call_response import CreateCallResponse
from bandwidth.models.call_direction_enum import CallDirectionEnum
from bandwidth.models.callback_method_enum import CallbackMethodEnum
from bandwidth.models.machine_detection_configuration import MachineDetectionConfiguration
from bandwidth.models.machine_detection_mode_enum import MachineDetectionModeEnum
from bandwidth.models.call_state_enum import CallStateEnum
from bandwidth.models.redirect_method_enum import RedirectMethodEnum
from bandwidth.models.call_state import CallState
from bandwidth.models.update_call import UpdateCall
from bandwidth.exceptions import ApiException, UnauthorizedException, ForbiddenException, NotFoundException


class CallsIntegration(unittest.TestCase):
    """Voice Calls API integration test"""

    def setUp(self):
        configuration = bandwidth.Configuration(
            username=BW_USERNAME,
            password=BW_PASSWORD,
        )
        api_client = bandwidth.ApiClient(configuration)
        self.calls_api_instance = calls_api.CallsApi(api_client)

        # Unauthorized API Client

        unauthorizedConfiguration = bandwidth.Configuration(
             username='bad_username',
             password='bad_password'
        )
        unauthorized_api_client = bandwidth.ApiClient(unauthorizedConfiguration)
        self.unauthorized_api_instance = calls_api.CallsApi(unauthorized_api_client)

        # Forbidden API Client

        forbiddenConfiguration = bandwidth.Configuration(
            username=FORBIDDEN_USERNAME,
            password=FORBIDDEN_PASSWORD
        )
        forbidden_api_client = bandwidth.ApiClient(forbiddenConfiguration)
        self.forbidden_api_instance = calls_api.CallsApi(forbidden_api_client)
        self.account_id = BW_ACCOUNT_ID
        self.createCallBody = CreateCall(
            to=USER_NUMBER,
            var_from=BW_NUMBER,
            privacy=True,
            display_name="Anonymous",
            application_id=BW_VOICE_APPLICATION_ID,
            answer_url=BASE_CALLBACK_URL,
            answer_method=CallbackMethodEnum("POST"),
            username="mySecretUsername",
            password="mySecretPassword1!",
            answer_fallback_url="https://www.myFallbackServer.com/webhooks/answer",
            answer_fallback_method=CallbackMethodEnum("POST"),
            fallback_username="mySecretUsername",
            fallback_password="mySecretPassword1!",
            disconnect_url="https://myServer.com/bandwidth/webhooks/disconnectUrl",
            disconnect_method=CallbackMethodEnum("POST"),
            call_timeout=30.0,
            callback_timeout=15.0,
            machine_detection=MachineDetectionConfiguration(
                mode=MachineDetectionModeEnum("async"),
                detection_timeout=15.0,
                silence_timeout=10.0,
                speech_threshold=10.0,
                speech_end_threshold=5.0,
                machine_speech_end_threshold=5.0,
                delay_result=False,
                callback_url="https://myServer.com/bandwidth/webhooks/machineDetectionComplete",
                callback_method=CallbackMethodEnum("POST"),
                username="mySecretUsername",
                password="mySecretPassword1!",
                fallback_url="https://myFallbackServer.com/bandwidth/webhooks/machineDetectionComplete",
                fallback_method=CallbackMethodEnum("POST"),
                fallback_username="mySecretUsername",
                fallback_password="mySecretPassword1!",
            ),
            priority=5,
            tag="tag_example",
        )
        self.testCallBody = CreateCall(to=USER_NUMBER, var_from=BW_NUMBER, application_id=BW_VOICE_APPLICATION_ID, answer_url=BASE_CALLBACK_URL)
        self.testMantecaCallBody = CreateCall(to=MANTECA_IDLE_NUMBER, var_from=MANTECA_ACTIVE_NUMBER, application_id=MANTECA_APPLICATION_ID, answer_url=MANTECA_BASE_URL + "/bxml/pause")
        self.updateStateCompleted = UpdateCall(state=CallStateEnum("completed"))
        self.testCallId = "Call-Id"
        self.testBxmlBody = '<?xml version="1.0" encoding="UTF-8"?><Bxml><SpeakSentence locale="en_US" gender="female" voice="susan">This is a test bxml response</SpeakSentence><Pause duration="3"/></Bxml>'
        self.callIdArray = []
        self.TEST_SLEEP = 5
        self.TEST_SLEEP_LONG = 15

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

    def test_create_call(self):
        """
            Validate a Create Call request with all optional parameters
        """
        time.sleep(self.TEST_SLEEP)
        create_call_response: ApiResponse = self.calls_api_instance.create_call_with_http_info(
            BW_ACCOUNT_ID,
            self.createCallBody
        )

        #Adding the call to the self.callIdArray
        self.callIdArray.append(create_call_response.data.call_id)

        assert_that(create_call_response.status_code, 201)
        assert_that(create_call_response.data, has_properties(
            'call_id', instance_of(str),
            'account_id', BW_ACCOUNT_ID,
            'application_id', BW_VOICE_APPLICATION_ID,
            'to', USER_NUMBER,
            'var_from', BW_NUMBER
        ))

    def test_create_call_bad_request(self):
        """Validate a bad (400) request
        """
        call_body = CreateCall(to="invalidNumberFormat", var_from=BW_NUMBER, application_id=BW_VOICE_APPLICATION_ID, answer_url=BASE_CALLBACK_URL)

        with self.assertRaises(ApiException) as context:
            self.calls_api_instance.create_call_with_http_info(BW_ACCOUNT_ID, call_body)

        assert_that(context.exception.status, 400)

    def test_create_call_unauthorized(self) -> None:
        """Validate an unauthorized (401) request
        """
        with self.assertRaises(UnauthorizedException) as context:
            self.unauthorized_api_instance.create_call(BW_ACCOUNT_ID, self.testCallBody)

        self.assertApiException(context, UnauthorizedException, 401)

    def test_create_call_forbidden(self) -> None:
        """Validate a forbidden (403) request
        """
        with self.assertRaises(ForbiddenException) as context:
            self.forbidden_api_instance.create_call(BW_ACCOUNT_ID, self.testCallBody)

        self.assertApiException(context, ForbiddenException, 403)


    def test_get_call_state(self):
        """Validate an Get Call State Request
        """
        create_call_response: CreateCallResponse = self.calls_api_instance.create_call(BW_ACCOUNT_ID, self.testCallBody)
        call_id = create_call_response.call_id

        #Adding the call to the self.callIdArray
        self.callIdArray.append(call_id)

        time.sleep(self.TEST_SLEEP)

        get_call_response: ApiResponse = self.calls_api_instance.get_call_state_with_http_info(BW_ACCOUNT_ID, call_id)

        assert_that(get_call_response.status_code, 200)
        assert_that(get_call_response.data, has_properties(
            "call_id", call_id,
            "state", instance_of(str),
            "direction", CallDirectionEnum("outbound"),
            "enqueued_time", instance_of(datetime.datetime),
            "last_update", instance_of(datetime.datetime),
            "start_time", instance_of(datetime.datetime)
        ))

    def test_get_call_state_unauthorized(self) -> None:
        """Validate an unauthorized (401) request
        """
        with self.assertRaises(UnauthorizedException) as context:
            self.unauthorized_api_instance.get_call_state(BW_ACCOUNT_ID, self.testCallId)

        self.assertApiException(context, UnauthorizedException, 401)

    def test_get_call_state_forbidden(self) -> None:
        """Validate a forbidden (403) request
        """
        with self.assertRaises(ForbiddenException) as context:
            self.forbidden_api_instance.get_call_state(BW_ACCOUNT_ID, self.testCallId)

        self.assertApiException(context, ForbiddenException, 403)

    def test_get_call_state_not_found(self):
        """Validate an invalid Get Call State Request due to a bad callID
        """
        with self.assertRaises(NotFoundException) as context:
            self.calls_api_instance.get_call_state(BW_ACCOUNT_ID, self.testCallId)

        self.assertApiException(context, NotFoundException, 404)

    def test_update_call(self):
        """Validate an UpdateCall Request
        """
        time.sleep(self.TEST_SLEEP)
        create_call_response: CreateCallResponse = self.calls_api_instance.create_call(BW_ACCOUNT_ID, self.testMantecaCallBody)
        call_id = create_call_response.call_id

        #Adding the call to the self.callIdArray
        self.callIdArray.append(call_id)

        updateCallBody = UpdateCall(
            state=CallStateEnum("active"),
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

        time.sleep(self.TEST_SLEEP)
        update_call_response: ApiResponse = self.calls_api_instance.update_call_with_http_info(BW_ACCOUNT_ID, call_id, updateCallBody)
        assert_that(update_call_response.status_code, 200)

        time.sleep(self.TEST_SLEEP)
        # hanging-up the call
        update_call_response: ApiResponse = self.calls_api_instance.update_call_with_http_info(BW_ACCOUNT_ID, call_id, self.updateStateCompleted)
        assert_that(update_call_response.status_code, 200)

    def test_update_call_bad_request(self):
        """Validate a bad (400) update call request
        """
        create_call_response: CreateCallResponse = self.calls_api_instance.create_call(BW_ACCOUNT_ID, self.testMantecaCallBody)
        call_id = create_call_response.call_id

        #Adding the call to the self.callIdArray
        self.callIdArray.append(call_id)

        time.sleep(self.TEST_SLEEP)

        with self.assertRaises(ApiException) as context:
            badRequestBody = UpdateCall(states="badRequest")
            self.calls_api_instance.update_call(BW_ACCOUNT_ID, call_id, badRequestBody)

        assert_that(context.exception.status, 400)

        # hanging-up the call
        time.sleep(self.TEST_SLEEP)
        update_call_response: ApiResponse = self.calls_api_instance.update_call_with_http_info(BW_ACCOUNT_ID, call_id, self.updateStateCompleted)
        assert_that(update_call_response.status_code, 200)

    def test_update_call_unauthorized(self):
        """Validate an unauthorized (401) update call request
        """
        with self.assertRaises(UnauthorizedException) as context:
            self.unauthorized_api_instance.update_call(BW_ACCOUNT_ID, self.testCallId, self.updateStateCompleted)

        self.assertApiException(context, UnauthorizedException, 401)

    def test_update_call_forbidden(self):
        """Validate a forbidden (403) update call request
        """
        create_call_response: CreateCallResponse = self.calls_api_instance.create_call(BW_ACCOUNT_ID, self.testMantecaCallBody)
        call_id = create_call_response.call_id

        #Adding the call to the self.callIdArray
        self.callIdArray.append(call_id)

        time.sleep(self.TEST_SLEEP)

        with self.assertRaises(ForbiddenException) as context:
            self.forbidden_api_instance.update_call(BW_ACCOUNT_ID, call_id, self.updateStateCompleted)

        self.assertApiException(context, ForbiddenException, 403)

        time.sleep(self.TEST_SLEEP_LONG)
        # hanging-up the call
        update_call_response: ApiResponse = self.calls_api_instance.update_call_with_http_info(BW_ACCOUNT_ID, call_id, self.updateStateCompleted)
        assert_that(update_call_response.status_code, 200)

    def test_update_call_not_found(self):
        """Validate a not found update call request
        """
        with self.assertRaises(NotFoundException) as context:
            self.calls_api_instance.update_call(BW_ACCOUNT_ID, self.testCallId, self.updateStateCompleted)

        self.assertApiException(context, NotFoundException, 404)

    def test_update_call_bxml(self):
        """Validate an UpdateCallBxml Request
        """
        create_call_response: CreateCallResponse = self.calls_api_instance.create_call(BW_ACCOUNT_ID, self.testMantecaCallBody)
        call_id = create_call_response.call_id

        #Adding the call to the self.callIdArray
        self.callIdArray.append(create_call_response.call_id)

        time.sleep(self.TEST_SLEEP)
        update_call_bxml_response: ApiResponse = self.calls_api_instance.update_call_bxml_with_http_info(BW_ACCOUNT_ID, call_id, self.testBxmlBody)
        assert_that(update_call_bxml_response.status_code, 204)

        time.sleep(self.TEST_SLEEP)
        # hanging-up the call
        update_call_response: ApiResponse = self.calls_api_instance.update_call_with_http_info(BW_ACCOUNT_ID, call_id, self.updateStateCompleted)
        assert_that(update_call_response.status_code, 200)

    def test_update_call_bxml_bad_request(self):
        """Validate a bad (400) update call bxml request
        """
        create_call_response: CreateCallResponse = self.calls_api_instance.create_call(BW_ACCOUNT_ID, self.testMantecaCallBody)
        call_id = create_call_response.call_id

        #Adding the call to the self.callIdArray
        self.callIdArray.append(call_id)

        time.sleep(self.TEST_SLEEP)

        invalidBxmlBody = "invalidBXML"

        with self.assertRaises(ApiException) as context:
            self.calls_api_instance.update_call_bxml_with_http_info(BW_ACCOUNT_ID, call_id, invalidBxmlBody)

        assert_that(context.exception.status, 400)

        time.sleep(self.TEST_SLEEP)
        # hanging-up the call
        update_call_response: ApiResponse = self.calls_api_instance.update_call_with_http_info(BW_ACCOUNT_ID, call_id, self.updateStateCompleted)
        assert_that(update_call_response.status_code, 200)


    def test_update_call_bxml_unauthorized(self):
        """Validate an unauthorized (401) update call bxml request
        """

        with self.assertRaises(UnauthorizedException) as context:
            self.unauthorized_api_instance.update_call_bxml(BW_ACCOUNT_ID, self.testCallId, self.testBxmlBody)

        self.assertApiException(context, UnauthorizedException, 401)

    def test_update_call_bxml_forbidden(self):
        """Validate a forbidden (403) update call bxml request
        """
        create_call_response: CreateCallResponse = self.calls_api_instance.create_call(BW_ACCOUNT_ID, self.testMantecaCallBody)
        call_id = create_call_response.call_id

        #Adding the call to the self.callIdArray
        self.callIdArray.append(call_id)

        time.sleep(self.TEST_SLEEP)
        with self.assertRaises(ForbiddenException) as context:
            self.forbidden_api_instance.update_call_bxml(BW_ACCOUNT_ID, call_id, self.testBxmlBody)

        self.assertApiException(context, ForbiddenException, 403)

    def test_update_call_bxml_not_found(self):
        """
            Validate a not found update call bxml request
        """
        with self.assertRaises(NotFoundException) as context:
            self.calls_api_instance.update_call_bxml(BW_ACCOUNT_ID, self.testCallId, self.testBxmlBody)

        self.assertApiException(context, NotFoundException, 404)

if __name__ == '__main__':
    unittest.main()
