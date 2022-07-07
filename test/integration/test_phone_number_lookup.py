"""
Integration test for Bandwidth's Phone Number Lookup API
"""

import os
import json
import unittest

import bandwidth
from bandwidth.api import phone_number_lookup_api
from bandwidth.model.lookup_request import LookupRequest
from bandwidth.model.create_lookup_response import CreateLookupResponse
from bandwidth.model.lookup_status import LookupStatus
from bandwidth.model.lookup_result import LookupResult
from bandwidth.model.lookup_status_enum import LookupStatusEnum
from bandwidth.model.tn_lookup_request_error import TnLookupRequestError


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

    
    def tearDown(self):
        pass

    
    def testSuccessfulPhoneNumberLookup(self):
        """Test Phone Number Lookup API"""
        lookup_request = LookupRequest(
            tns=[
                os.environ['BW_NUMBER'],
            ],
        ) 

        create_lookup_response: CreateLookupResponse = self.api_instance.create_lookup(self.account_id, lookup_request, _return_http_data_only=False)
        self.assertEqual(create_lookup_response[1], 202)
        self.assertIs(type(create_lookup_response[0].status), LookupStatusEnum)
        self.assertIs(type(create_lookup_response[0].request_id), str)
        
        get_lookup_status_response: LookupStatus = self.api_instance.get_lookup_status(self.account_id, create_lookup_response[0].request_id, _return_http_data_only=False)
        self.assertEqual(get_lookup_status_response[1], 200)
        self.assertEqual(get_lookup_status_response[0].request_id, create_lookup_response[0].request_id)
        self.assertIs(type(get_lookup_status_response[0]), LookupStatus)
        self.assertIs(type(get_lookup_status_response[0].result[0]), LookupResult)
    
    def testFailedPhoneNumberLookup(self):
        """Test Phone Number Lookup API with bad data to force an error"""
        with self.assertRaises(bandwidth.ApiException) as context:
            lookup_request = LookupRequest(
                tns=[
                    'not a number',
                ],
            )
            create_lookup_response: CreateLookupResponse = self.api_instance.create_lookup(self.account_id, lookup_request)
        
        self.assertIs(type(context.exception.status), int)
        self.assertIs(type(context.exception.body), str)

        # initialize TnLookupRequestError model 
        error = TnLookupRequestError(message=(json.loads(context.exception.body))['message'])
        self.assertIs(type(error), TnLookupRequestError)


if __name__ == '__main__':
    unittest.main()
