"""
Integration test for Bandwidth's Phone Number Lookup API
"""

import os
import json
import time
import unittest

import bandwidth
from bandwidth.api import phone_number_lookup_api
from bandwidth.model.lookup_request import LookupRequest
from bandwidth.model.create_lookup_response import CreateLookupResponse
from bandwidth.model.lookup_status import LookupStatus
from bandwidth.model.lookup_result import LookupResult
from bandwidth.model.lookup_status_enum import LookupStatusEnum
from bandwidth.model.tn_lookup_request_error import TnLookupRequestError
from bandwidth.exceptions import UnauthorizedException, ForbiddenException


class TestPhoneNumberLookupIntegration(unittest.TestCase):
    """Phone Number Lookup API integration test"""

    
    def setUp(self):
        configuration = bandwidth.Configuration(
            username = os.environ['BW_USERNAME'],
            password = os.environ['BW_PASSWORD']
        )
        api_client = bandwidth.ApiClient(configuration)
        self.api_instance = phone_number_lookup_api.PhoneNumberLookupApi(api_client)
        self.account_id = os.environ['BW_ACCOUNT_ID']

    
    def testSuccessfulPhoneNumberLookup(self):
        """Test Phone Number Lookup API"""
        lookup_request = LookupRequest(
            tns=[
                os.environ['BW_NUMBER'],
                os.environ['VZW_NUMBER'],
                os.environ['ATT_NUMBER'],
                os.environ['T_MOBILE_NUMBER'],
                # os.environ['BW_INVALID_TN_LOOKUP_NUMBER']
            ],
        ) 

        create_lookup_response: CreateLookupResponse = self.api_instance.create_lookup(self.account_id, lookup_request, _return_http_data_only=False)
        self.assertEqual(create_lookup_response[1], 202)
        self.assertIs(type(create_lookup_response[0].status), LookupStatusEnum)
        self.assertEqual(create_lookup_response[0].status, LookupStatusEnum("IN_PROGRESS"))
        self.assertIs(type(create_lookup_response[0].request_id), str)
        self.assertRegex(create_lookup_response[0].request_id, r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')
        
        get_lookup_status_response: LookupStatus = self.api_instance.get_lookup_status(self.account_id, create_lookup_response[0].request_id, _return_http_data_only=False)
        self.assertEqual(get_lookup_status_response[1], 200)

        # make the request again without _return_http_data_only=False to just get the LookupStatus model
        get_lookup_status_response: LookupStatus = self.api_instance.get_lookup_status(self.account_id, create_lookup_response[0].request_id)
        get_lookup_status_response_attempts = 1
        while get_lookup_status_response.status != LookupStatusEnum('COMPLETE'): 
            # Raise an error if it takes more than 5 requests to get COMPLETE status
            if get_lookup_status_response_attempts == 5:
                raise Exception(f'Took too long to get phone number lookup \'COMPLETE\' status. Aborting test after {get_lookup_status_response_attempts} attempts.')
            time.sleep(2)

            get_lookup_status_response: LookupStatus = self.api_instance.get_lookup_status(self.account_id, create_lookup_response[0].request_id)
            get_lookup_status_response_attempts += 1

        self.assertEqual(get_lookup_status_response.request_id, create_lookup_response[0].request_id)
        self.assertIs(type(get_lookup_status_response), LookupStatus)
        
        # Assert that each result is of type LookupResult
        for i in range(len(get_lookup_status_response.result)):
            self.assertIs(type(get_lookup_status_response.result[i]), LookupResult)

        # Check the information for a Bandwidth TN
        bw_lookup_result: LookupResult = get_lookup_status_response.result[0]
        self.assertEqual(bw_lookup_result.response_code, 0)
        self.assertIs(type(bw_lookup_result.message), str)
        self.assertEqual(bw_lookup_result.e_164_format, os.environ['BW_NUMBER'])
        self.assertIs(type(bw_lookup_result.formatted), str)
        self.assertTrue(bw_lookup_result.country == "US" or bw_lookup_result.country == "Canada")
        self.assertTrue(bw_lookup_result.line_type == "Mobile" or bw_lookup_result.line_type == "Fixed")
        self.assertIn("Bandwidth", bw_lookup_result.line_provider)

        # Check the information for a Verizon TN
        vzw_lookup_result = get_lookup_status_response.result[1]
        self.assertEqual(vzw_lookup_result.response_code, 0)
        self.assertIs(type(vzw_lookup_result.message), str)
        self.assertEqual(vzw_lookup_result.e_164_format, os.environ['VZW_NUMBER'])
        self.assertIs(type(vzw_lookup_result.formatted), str)
        self.assertTrue(vzw_lookup_result.country == "US" or vzw_lookup_result.country == "Canada")
        self.assertTrue(vzw_lookup_result.line_type == "Mobile" or vzw_lookup_result.line_type == "Fixed")
        self.assertIn("Verizon", vzw_lookup_result.line_provider)
        self.assertIs(type(vzw_lookup_result.mobile_country_code), str)
        self.assertIs(type(vzw_lookup_result.mobile_network_code), str)

        # Check the information for an AT&T TN
        att_lookup_result = get_lookup_status_response.result[2]
        self.assertEqual(att_lookup_result.response_code, 0)
        self.assertIs(type(att_lookup_result.message), str)
        self.assertEqual(att_lookup_result.e_164_format, os.environ['VZW_NUMBER'])
        self.assertIs(type(att_lookup_result.formatted), str)
        self.assertTrue(att_lookup_result.country == "US" or att_lookup_result.country == "Canada")
        self.assertTrue(att_lookup_result.line_type == "Mobile" or att_lookup_result.line_type == "Fixed")
        self.assertIn("AT&T", att_lookup_result.line_provider)
        self.assertIs(type(att_lookup_result.mobile_country_code), str)
        self.assertIs(type(att_lookup_result.mobile_network_code), str)

        # Check the information for a T-Mobile TN
        t_mobile_lookup_result = get_lookup_status_response.result[3]
        self.assertEqual(t_mobile_lookup_result.response_code, 0)
        self.assertIs(type(t_mobile_lookup_result.message), str)
        self.assertEqual(t_mobile_lookup_result.e_164_format, os.environ['VZW_NUMBER'])
        self.assertIs(type(t_mobile_lookup_result.formatted), str)
        self.assertTrue(t_mobile_lookup_result.country == "US" or t_mobile_lookup_result.country == "Canada")
        self.assertTrue(t_mobile_lookup_result.line_type == "Mobile" or t_mobile_lookup_result.line_type == "Fixed")
        self.assertIn("T-Mobile", t_mobile_lookup_result.line_provider)
        self.assertIs(type(t_mobile_lookup_result.mobile_country_code), str)
        self.assertIs(type(t_mobile_lookup_result.mobile_network_code), str)

        # The only way to get a failed number is if the api call to the downstream service fails - so there is no way to force this in our testing currently
        # check the failed_telephone_number list 
        # self.assertIs(type(get_lookup_status_response.failed_telephone_numbers), list)
        # self.assertIn(os.environ['BW_INVALID_TN_LOOKUP_NUMBER'], get_lookup_status_response.failed_telephone_numbers)

    
    def testFailedPhoneNumberLookup(self):
        """Test Phone Number Lookup API with bad data to force an error"""
        with self.assertRaises(bandwidth.ApiException) as context:
            lookup_request = LookupRequest(
                tns=[
                    'not a number',
                ],
            )
            self.api_instance.create_lookup(self.account_id, lookup_request)
        
        self.assertIs(type(context.exception.status), int)
        self.assertIs(type(context.exception.body), str)

        # initialize TnLookupRequestError model 
        error = TnLookupRequestError(message=(json.loads(context.exception.body))['message'])
        self.assertIs(type(error), TnLookupRequestError)

    
    def testDuplicatePhoneNumberLookup(self):
        with self.assertRaises(bandwidth.ApiException) as context:
            lookup_request = LookupRequest(
                tns=[
                    os.environ['BW_NUMBER'],
                    os.environ['BW_NUMBER']
                ],
            )
            self.api_instance.create_lookup(self.account_id, lookup_request)
    

    def testUnauthorizedRequest(self):
        configuration = bandwidth.Configuration(
            username = 'bad_username',
            password = 'bad_password'
        )
        unauthorized_api_client = bandwidth.ApiClient(configuration)
        unauthorized_api_instance = phone_number_lookup_api.PhoneNumberLookupApi(unauthorized_api_client)
        lookup_request = LookupRequest(
            tns=[
                os.environ['BW_NUMBER']
            ],
        )

        with self.assertRaises(UnauthorizedException) as context:
            unauthorized_api_instance.create_lookup(self.account_id, lookup_request)
        
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
        )

        # This API throws a 401 when a user provides valid credentials with the `TN Lookup` role disabled
        # with self.assertRaises(ForbiddenException) as context:
        with self.assertRaises(UnauthorizedException) as context:
            forbidden_api_instance.create_lookup(self.account_id, lookup_request)
        
        # self.assertIs(type(context.exception), ForbiddenException)
        # self.assertEqual(context.exception.status, 403)
        self.assertIs(type(context.exception), UnauthorizedException)
        self.assertIs(type(context.exception.status), int)
        self.assertEqual(context.exception.status, 401)
        self.assertIs(type(context.exception.body), str)


if __name__ == '__main__':
    unittest.main()
