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

    
    def validateResult(self, result: LookupResult, e_164_format: str, line_provider: str):
        """Verify a successful phone number lookup LookupResult object

        Args:
            result (LookupResult): Result derived from LookupStatus result list
            e_164_format (str): Phone number in e164 format ex: +19195551234
            line_provider (str): Line service provider ex: Verizon
        """
        self.assertEqual(result.response_code, 0)
        self.assertIs(type(result.message), str)
        self.assertEqual(result.e_164_format, e_164_format)
        self.assertIs(type(result.formatted), str)
        self.assertTrue(result.country == "US" or result.country == "Canada")
        self.assertTrue(result.line_type == "Mobile" or result.line_type == "Fixed")
        self.assertIn(line_provider, result.line_provider)
        
        # if result has 1 of these attributes it should have the other
        if result.get('mobile_country_code') or result.get('mobile_network_code'):    
            self.assertIs(type(result.mobile_country_code), str)
            self.assertIs(type(result.mobile_network_code), str)
    

    def pollLookupStatus(self, request_id: str) -> LookupStatus:
        """Poll LookupRequest for 'COMPLETE' status

        Args:
            request_id (str): LookupResult.request_id value to query

        Raises:
            Exception: Tries 5 times and raises a general exception if the query takes more than 5 attempts to minimize run time.

        Returns:
            LookupStatus: LookupStatus in 'COMPLETE' state
        """
        get_lookup_status_response: LookupStatus = self.api_instance.get_lookup_status(self.account_id, request_id)
        get_lookup_status_response_attempts = 1
        while get_lookup_status_response.status != LookupStatusEnum('COMPLETE'): 
            # Raise an error if it takes more than 5 requests to get COMPLETE status
            if get_lookup_status_response_attempts == 5:
                raise Exception(f'Took too long to get phone number lookup \'COMPLETE\' status. Aborting test after {get_lookup_status_response_attempts} attempts.')
            time.sleep(2)

            get_lookup_status_response: LookupStatus = self.api_instance.get_lookup_status(self.account_id, request_id)
            get_lookup_status_response_attempts += 1
        
        return get_lookup_status_response
    
    
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

        # Create the lookup request and validate the response
        create_lookup_response: CreateLookupResponse = self.api_instance.create_lookup(self.account_id, lookup_request, _return_http_data_only=False)
        self.assertEqual(create_lookup_response[1], 202)
        self.assertIs(type(create_lookup_response[0].status), LookupStatusEnum)
        self.assertEqual(create_lookup_response[0].status, LookupStatusEnum("IN_PROGRESS"))
        self.assertIs(type(create_lookup_response[0].request_id), str)
        self.assertRegex(create_lookup_response[0].request_id, r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')
        
        # Check the status code for the GET LookupStatus response
        get_lookup_status_response: LookupStatus = self.api_instance.get_lookup_status(self.account_id, create_lookup_response[0].request_id, _return_http_data_only=False)
        self.assertEqual(get_lookup_status_response[1], 200)

        # make the request again without _return_http_data_only=False to just get the LookupStatus model
        get_lookup_status_response: LookupStatus = self.pollLookupStatus(create_lookup_response[0].request_id)

        self.assertEqual(get_lookup_status_response.request_id, create_lookup_response[0].request_id)
        self.assertIs(type(get_lookup_status_response), LookupStatus)
        
        # Assert that each result is of type LookupResult
        for i in range(len(get_lookup_status_response.result)):
            self.assertIs(type(get_lookup_status_response.result[i]), LookupResult)

        # Check the information for a Bandwidth TN
        bw_lookup_result: LookupResult = get_lookup_status_response.result[0]
        self.validateResult(bw_lookup_result, os.environ['BW_NUMBER'], "Bandwidth")

        # Check the information for a Verizon TN
        vzw_lookup_result = get_lookup_status_response.result[1]
        self.validateResult(vzw_lookup_result, os.environ['VZW_NUMBER'], "Verizon")

        # Check the information for an AT&T TN
        att_lookup_result = get_lookup_status_response.result[2]
        self.validateResult(att_lookup_result, os.environ['ATT_NUMBER'], "AT&T")

        # Check the information for a T-Mobile TN
        t_mobile_lookup_result = get_lookup_status_response.result[3]
        self.validateResult(t_mobile_lookup_result, os.environ['T_MOBILE_NUMBER'], "T-Mobile")

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
