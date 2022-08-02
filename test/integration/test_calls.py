"""
Integration test for Bandwidth's Voice Voice Calls API
"""

import os
import time
import unittest
import datetime


import bandwidth
from bandwidth.api import calls_api
from bandwidth.model.create_call import CreateCall
from bandwidth.model.create_call_response import CreateCallResponse
from bandwidth.model.call_direction_enum import CallDirectionEnum
from bandwidth.model.callback_method_enum import CallbackMethodEnum
from bandwidth.model.machine_detection_configuration import MachineDetectionConfiguration
from bandwidth.model.machine_detection_mode_enum import MachineDetectionModeEnum
from bandwidth.model.call_state_enum import CallStateEnum
from bandwidth.model.redirect_method_enum import RedirectMethodEnum
from bandwidth.model.call_state import CallState
from bandwidth.model.update_call import UpdateCall
from bandwidth.exceptions import ApiException, UnauthorizedException, ForbiddenException, NotFoundException

try:
    BW_USERNAME = os.environ["BW_USERNAME"]
    BW_PASSWORD = os.environ["BW_PASSWORD"]
    BW_ACCOUNT_ID = os.environ["BW_ACCOUNT_ID"]
    BW_VOICE_APPLICATION_ID = os.environ["BW_VOICE_APPLICATION_ID"]
    BASE_CALLBACK_URL = os.environ["BASE_CALLBACK_URL"]
    BW_NUMBER = os.environ["BW_NUMBER"]
    USER_NUMBER = os.environ["USER_NUMBER"]
    FORBIDDEN_USERNAME = os.environ['BW_USERNAME_FORBIDDEN']
    FORBIDDEN_PASSWORD = os.environ['BW_PASSWORD_FORBIDDEN']
    MANTECA_ACTIVE_NUMBER = os.environ["MANTECA_ACTIVE_NUMBER"]
    MANTECA_IDLE_NUMBER = os.environ["MANTECA_IDLE_NUMBER"]
    MANTECA_BASE_URL = os.environ["MANTECA_BASE_URL"]
    MANTECA_STATUS_URL = MANTECA_BASE_URL + "tests/"
    MANTECA_APPLICATION_ID = os.environ["MANTECA_APPLICATION_ID"]

except KeyError as e:
    raise Exception("Environmental variables not found")

global testCallBody
testCallBody = CreateCall(to=USER_NUMBER, _from=BW_NUMBER, application_id=BW_VOICE_APPLICATION_ID, answer_url=BASE_CALLBACK_URL)

global testMantecaCallBody
testMantecaCallBody = CreateCall(to=MANTECA_IDLE_NUMBER, _from=MANTECA_ACTIVE_NUMBER, application_id=MANTECA_APPLICATION_ID, answer_url=MANTECA_BASE_URL + "/bxml/pause")

global updateStateCompleted
updateStateCompleted = UpdateCall(state=CallStateEnum("completed"))

global testCallId
testCallId = "Call-Id"

global testBxmlBody
testBxmlBody = '<?xml version="1.0" encoding="UTF-8"?><Bxml><SpeakSentence locale="en_US" gender="female" voice="susan">This is a test bxml response</SpeakSentence><Pause duration="3"/></Bxml>'


class CallsIntegration(unittest.TestCase):
    """Voice Calls API integration test"""

    global callIdArray
    callIdArray = []

    def setUp(self):
        configuration = bandwidth.Configuration(
            username = BW_USERNAME,
            password = BW_PASSWORD,
        )
        api_client = bandwidth.ApiClient(configuration)
        self.api_instance = calls_api.CallsApi(api_client)

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


    def tearDown(self):
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
                get_call_response: CallState = self.api_instance.get_call_state(BW_ACCOUNT_ID, callId, _return_http_data_only=False)
                if get_call_response[0].state == 'active':
                    self.api_instance.update_call(BW_ACCOUNT_ID, callId, body, _return_http_data_only=False)
                elif get_call_response[0].state == 'complete':
                    callIdArray.remove(callId)
            callIdArray.clear()
        pass                

    def assertApiException(self, context: ApiException, expectedException: ApiException, expected_status_code: int):
        """Validates that common API exceptions, (401, 403, and 404) are properly formatted
        Args:
            context (ApiException): Exception to validate
            expectedException (ApiException): Expected exception type
            expected_status_code (int): Expected status code
        """
        self.assertIs(type(context.exception.status), int)
        self.assertEqual(context.exception.status, expected_status_code)
        self.assertIs(type(context.exception.body), str)

    def test_create_call(self):
        """
            Validate a Create Call request with all optional parameters
        """
        time.sleep(3)        
        call_body = CreateCall(
            to=USER_NUMBER, 
            _from=BW_NUMBER, 
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

        create_call_response: CreateCallResponse = self.api_instance.create_call(BW_ACCOUNT_ID, call_body, _return_http_data_only=False)

        #Adding the call to the callIdArray
        callIdArray.append(create_call_response[0].call_id)

        self.assertEqual(create_call_response[1], 201)
        self.assertIs(type(create_call_response[0].call_id), str)
        self.assertEqual(create_call_response[0].account_id, BW_ACCOUNT_ID)
        self.assertEqual(create_call_response[0].application_id, BW_VOICE_APPLICATION_ID)
        self.assertEqual(create_call_response[0].to, USER_NUMBER)
        self.assertEqual(create_call_response[0]._from, BW_NUMBER)
        self.assertEqual(create_call_response[0].call_url, ("https://voice.bandwidth.com/api/v2/accounts/" + \
            BW_ACCOUNT_ID + "/calls/" + create_call_response[0].call_id))    

    def test_create_call_bad_request(self):
        """Validate a bad (400) request
        """
        call_body = CreateCall(to="invalidNumberFormat", _from=BW_NUMBER, application_id=BW_VOICE_APPLICATION_ID, answer_url=BASE_CALLBACK_URL)
        
        with self.assertRaises(ApiException) as context:
            self.api_instance.create_call(BW_ACCOUNT_ID, call_body, _return_http_data_only=False)
            
        self.assertEqual(context.exception.status, 400)

    def test_create_call_unauthorized(self) -> None:
        """Validate an unauthorized (401) request
        """
        with self.assertRaises(UnauthorizedException) as context:
            self.unauthorized_api_instance.create_call(BW_ACCOUNT_ID, testCallBody, _return_http_data_only=False)

        self.assertApiException(context, UnauthorizedException, 401)

    def test_create_call_forbidden(self) -> None:
        """Validate a forbidden (403) request
        """
        with self.assertRaises(ForbiddenException) as context:
            self.forbidden_api_instance.create_call(BW_ACCOUNT_ID, testCallBody, _return_http_data_only=False)

        self.assertApiException(context, ForbiddenException, 403)


    def test_get_call_state(self):
        """Validate an Get Call State Request
        """
        create_call_response: CreateCallResponse = self.api_instance.create_call(BW_ACCOUNT_ID, testCallBody, _return_http_data_only=False)
        call_id = create_call_response[0].call_id

        #Adding the call to the callIdArray
        callIdArray.append(create_call_response[0].call_id)

        time.sleep(3)

        get_call_response: CallState = self.api_instance.get_call_state(BW_ACCOUNT_ID, call_id, _return_http_data_only=False)
        
        self.assertEqual(get_call_response[1], 200)
        self.assertEqual(get_call_response[0].call_id, call_id)
        self.assertIs(type(get_call_response[0].state), str)
        self.assertEqual(get_call_response[0].direction, CallDirectionEnum("outbound"))
        self.assertIs(type(get_call_response[0].enqueued_time), datetime.datetime)
        self.assertIs(type(get_call_response[0].last_update), datetime.datetime)
        self.assertIs(type(get_call_response[0].start_time), datetime.datetime)

    def test_get_call_state_unauthorized(self) -> None:
        """Validate an unauthorized (401) request
        """
        with self.assertRaises(UnauthorizedException) as context:
            self.unauthorized_api_instance.get_call_state(BW_ACCOUNT_ID, testCallId, _return_http_data_only=False)

        self.assertApiException(context, UnauthorizedException, 401)

    def test_get_call_state_forbidden(self) -> None:
        """Validate a forbidden (403) request
        """
        with self.assertRaises(ForbiddenException) as context:
            self.forbidden_api_instance.get_call_state(BW_ACCOUNT_ID, testCallId, _return_http_data_only=False)

        self.assertApiException(context, ForbiddenException, 403)  

    def test_get_call_state_not_found(self):
        """Validate an invalid Get Call State Request due to a bad callID
        """
        with self.assertRaises(NotFoundException) as context:
            self.api_instance.get_call_state(BW_ACCOUNT_ID, testCallId, _return_http_data_only=False)
        
        self.assertApiException(context, NotFoundException, 404)

    def test_update_call(self):
        """Validate an UpdateCall Request
        """
        time.sleep(3)            
        create_call_response: CreateCallResponse = self.api_instance.create_call(BW_ACCOUNT_ID, testMantecaCallBody, _return_http_data_only=False)
        call_id = create_call_response[0].call_id

        #Adding the call to the callIdArray
        callIdArray.append(create_call_response[0].call_id)

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

        time.sleep(3)
        update_call_response: UpdateCall = self.api_instance.update_call(BW_ACCOUNT_ID, call_id, updateCallBody, _return_http_data_only=False)
        self.assertEqual(update_call_response[1], 200)

        time.sleep(3)
        # hanging-up the call
        update_call_response: UpdateCall = self.api_instance.update_call(BW_ACCOUNT_ID, call_id, updateStateCompleted, _return_http_data_only=False)
        self.assertEqual(update_call_response[1], 200)
    
    def test_update_call_bad_request(self):
        """Validate a bad (400) update call request
        """
        create_call_response: CreateCallResponse = self.api_instance.create_call(BW_ACCOUNT_ID, testMantecaCallBody, _return_http_data_only=False)
        call_id = create_call_response[0].call_id

        #Adding the call to the callIdArray
        callIdArray.append(create_call_response[0].call_id)

        time.sleep(3)        

        with self.assertRaises(ApiException) as context:
            badRequestBody = UpdateCall(states="badRequest")
            self.api_instance.update_call(BW_ACCOUNT_ID, call_id, badRequestBody, _return_http_data_only=False)
            
        self.assertEqual(context.exception.status, 400)
                
        # hanging-up the call
        time.sleep(3)
        update_call_response: UpdateCall = self.api_instance.update_call(BW_ACCOUNT_ID, call_id, updateStateCompleted, _return_http_data_only=False)
        self.assertEqual(update_call_response[1], 200)           

    def test_update_call_unauthorized(self):
        """Validate an unauthorized (401) update call request
        """
        with self.assertRaises(UnauthorizedException) as context:
            self.unauthorized_api_instance.update_call(BW_ACCOUNT_ID, testCallId, updateStateCompleted, _return_http_data_only=False)

        self.assertApiException(context, UnauthorizedException, 401)

    def test_update_call_forbidden(self):
        """Validate a forbidden (403) update call request
        """
        create_call_response: CreateCallResponse = self.api_instance.create_call(BW_ACCOUNT_ID, testMantecaCallBody, _return_http_data_only=False)
        call_id = create_call_response[0].call_id

        #Adding the call to the callIdArray
        callIdArray.append(create_call_response[0].call_id)

        time.sleep(2)        

        with self.assertRaises(ForbiddenException) as context:
            self.forbidden_api_instance.update_call(BW_ACCOUNT_ID, call_id, updateStateCompleted, _return_http_data_only=False)

        self.assertApiException(context, ForbiddenException, 403)

        time.sleep(12)
        # hanging-up the call
        update_call_response: UpdateCall = self.api_instance.update_call(BW_ACCOUNT_ID, call_id, updateStateCompleted, _return_http_data_only=False)
        self.assertEqual(update_call_response[1], 200)       

    def test_update_call_not_found(self):
        """Validate a not found update call request
        """
        with self.assertRaises(NotFoundException) as context:
            self.api_instance.update_call(BW_ACCOUNT_ID, testCallId, updateStateCompleted, _return_http_data_only=False)
        
        self.assertApiException(context, NotFoundException, 404)

    def test_update_call_bxml(self):
        """Validate an UpdateCallBxml Request
        """
        create_call_response: CreateCallResponse = self.api_instance.create_call(BW_ACCOUNT_ID, testMantecaCallBody, _return_http_data_only=False)
        call_id = create_call_response[0].call_id

        #Adding the call to the callIdArray
        callIdArray.append(create_call_response[0].call_id)

        time.sleep(5)
        update_call_bxml_response: UpdateCall = self.api_instance.update_call_bxml(BW_ACCOUNT_ID, call_id, testBxmlBody, _return_http_data_only=False)
        self.assertEqual(update_call_bxml_response[1], 204)
        
        time.sleep(5)  
        # hanging-up the call
        update_call_response: UpdateCall = self.api_instance.update_call(BW_ACCOUNT_ID, call_id, updateStateCompleted, _return_http_data_only=False)
        self.assertEqual(update_call_response[1], 200)

    def test_update_call_bxml_bad_request(self):    
        """Validate a bad (400) update call bxml request
        """
        create_call_response: CreateCallResponse = self.api_instance.create_call(BW_ACCOUNT_ID, testMantecaCallBody, _return_http_data_only=False)
        call_id = create_call_response[0].call_id

        #Adding the call to the callIdArray
        callIdArray.append(create_call_response[0].call_id)

        time.sleep(3)        

        invalidBxmlBody = "invalidBXML"

        with self.assertRaises(ApiException) as context:
            self.api_instance.update_call_bxml(BW_ACCOUNT_ID, call_id, invalidBxmlBody, _return_http_data_only=False)
            
        self.assertEqual(context.exception.status, 400)

        time.sleep(2)  
        # hanging-up the call
        update_call_response: UpdateCall = self.api_instance.update_call(BW_ACCOUNT_ID, call_id, updateStateCompleted, _return_http_data_only=False)
        self.assertEqual(update_call_response[1], 200)


    def test_update_call_bxml_unauthorized(self):
        """Validate an unauthorized (401) update call bxml request
        """

        with self.assertRaises(UnauthorizedException) as context:
            self.unauthorized_api_instance.update_call_bxml(BW_ACCOUNT_ID, testCallId, testBxmlBody, _return_http_data_only=False)

        self.assertApiException(context, UnauthorizedException, 401)

    def test_update_call_bxml_forbidden(self):
        """Validate a forbidden (403) update call bxml request
        """
        create_call_response: CreateCallResponse = self.api_instance.create_call(BW_ACCOUNT_ID, testMantecaCallBody, _return_http_data_only=False)
        call_id = create_call_response[0].call_id

        #Adding the call to the callIdArray
        callIdArray.append(create_call_response[0].call_id)

        time.sleep(2)        
        with self.assertRaises(ForbiddenException) as context:
            self.forbidden_api_instance.update_call_bxml(BW_ACCOUNT_ID, call_id, testBxmlBody, _return_http_data_only=False)

        self.assertApiException(context, ForbiddenException, 403)

    def test_update_call_bxml_not_found(self):
        """
            Validate a not found update call bxml request
        """
        with self.assertRaises(NotFoundException) as context:
            self.api_instance.update_call_bxml(BW_ACCOUNT_ID, testCallId, testBxmlBody, _return_http_data_only=False)
        
        self.assertApiException(context, NotFoundException, 404)               

if __name__ == '__main__':
    unittest.main()