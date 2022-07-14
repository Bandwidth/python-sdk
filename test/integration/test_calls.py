"""
Integration test for Bandwidth's Voice Voice Calls API
"""

import os
import json
import time
import unittest

import bandwidth
from bandwidth.api import calls_api
from bandwidth.model.create_call import CreateCall
from bandwidth.model.create_call_response import CreateCallResponse
from bandwidth.model.call_callback import CallCallback
from bandwidth.model.call_direction_enum import CallDirectionEnum
from bandwidth.model.call_state_enum import CallStateEnum
from bandwidth.model.call_state import CallState
from bandwidth.model.update_call import UpdateCall
from bandwidth.model.voice_api_error import VoiceApiError
from bandwidth.exceptions import UnauthorizedException, ForbiddenException

try:
    BW_USERNAME = os.environ["BW_USERNAME"]
    BW_PASSWORD = os.environ["BW_PASSWORD"]
    BW_ACCOUNT_ID = os.environ["BW_ACCOUNT_ID"]
    BW_VOICE_APPLICATION_ID = os.environ["BW_VOICE_APPLICATION_ID"]
    BASE_CALLBACK_URL = os.environ["BASE_CALLBACK_URL"]
    BW_NUMBER = os.environ["BW_NUMBER"]
    USER_NUMBER = os.environ["USER_NUMBER"]

except KeyError as e:
    raise Exception("Environmental variables not found")

class CallsIntegration(unittest.TestCase):
    """Voice Calls API integration test"""


    def setUp(self):
        configuration = bandwidth.Configuration(
            username = BW_USERNAME,
            password = BW_PASSWORD,
        )
        api_client = bandwidth.ApiClient(configuration)
        self.api_instance = calls_api.CallsApi(api_client)
        self.account_id = BW_ACCOUNT_ID

    def tearDown(self):
        pass

    def testSuccessfulCalls(self):

        # Make a CreateCall body and assign the appropriate params
        answer_url = BASE_CALLBACK_URL
        call_body = CreateCall(to=USER_NUMBER, _from=BW_NUMBER, application_id=BW_VOICE_APPLICATION_ID, answer_url=answer_url)


        # Creating the call
        create_call_response: CreateCallResponse = self.api_instance.create_call(BW_ACCOUNT_ID, call_body)

        # Response Verification
        assert len(create_call_response.call_id) == 47    # assert request created and id matches expected length (47)
        assert create_call_response.account_id == BW_ACCOUNT_ID
        assert create_call_response.application_id == BW_VOICE_APPLICATION_ID
        assert create_call_response.to == USER_NUMBER
        assert create_call_response._from == BW_NUMBER
        assert create_call_response.call_url == "https://voice.bandwidth.com/api/v2/accounts/" + \
            BW_ACCOUNT_ID + "/calls/" + create_call_response.call_id

        call_id = create_call_response.call_id

      #  time.sleep(30)

        #GET call state information

      #  get_call_response: CallState(BW_ACCOUNT_ID, call_id)
        
        #Verification of Call State
       # assert len(get_call_response.call_id) == 47 # assert request created and id matches expected length (47)

        #GET call state information on bad callID to test error

        # Update Call with redirect

        #Update BXML directly

        # Test with wrong BXML

        #retry Create Call with using the wrong Voice Application ID

        #retry Create Call with the wrong Account ID


    """ def testUnauthorizedRequest(self):
        configuration = bandwidth.Configuration(
            username = 'bad_username',
            password = 'bad_password'
        )
        unauthorized_api_client = bandwidth.ApiClient(configuration)
        self.unauthorized_api_instance = calls_api.CallsApi(unauthorized_api_client)
        self.account_id = BW_ACCOUNT_ID
        answer_url = BASE_CALLBACK_URL
        call_body = CreateCall(to=USER_NUMBER, _from=BW_NUMBER, application_id=BW_VOICE_APPLICATION_ID, answer_url=answer_url)

        create_unauthorized_call_response: CreateCallResponse = self.unauthorized_api_instance.create_call(BW_ACCOUNT_ID, call_body)


        with self.assertRaises(UnauthorizedException) as context:
            unauthorized_api_instance.create_unauthorized_call_response(self.account_id, call_request)

        self.assertIs(type(context.exception), UnauthorizedException)
        self.assertIs(type(context.exception.status), int)
        self.assertEqual(context.exception.status, 401)
        self.assertIs(type(context.exception.body), str)

    def testForbiddenRequest(self):
        configuration = bandwidth.Configuration(
            username = os.environ['BW_USERNAME_FORBIDDEN'],
            password = os.environ['BW_PASSWORD_FORBIDDEN']
        )
        forbidden_api_client = bandwidth.ApiClient(configuration)
        forbidden_api_instance = phone_number_lookup_api.PhoneNumberLookupApi(forbidden_api_client)
        lookup_request = LookupRequest(
            tns=[
                os.environ['BW_NUMBER']
            ],
        ) """

"""         # This API throws a 401 when a user provides valid credentials with the `TN Lookup` role disabled
        # with self.assertRaises(ForbiddenException) as context:
        with self.assertRaises(UnauthorizedException) as context:
            forbidden_api_instance.create_lookup(self.account_id, lookup_request)

        # self.assertIs(type(context.exception), ForbiddenException)
        # self.assertEqual(context.exception.status, 403)
        self.assertIs(type(context.exception), UnauthorizedException)
        self.assertIs(type(context.exception.status), int)
        self.assertEqual(context.exception.status, 401)
        self.assertIs(type(context.exception.body), str) """


if __name__ == '__main__':
    unittest.main()