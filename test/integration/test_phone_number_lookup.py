"""
Integration test for Bandwidth's Phone Number Lookup API
"""

import os
import unittest

import bandwidth
from bandwidth.api import phone_number_lookup_api
from bandwidth.model.lookup_request import LookupRequest
from bandwidth.model.create_lookup_response import CreateLookupResponse
from bandwidth.model.lookup_status import LookupStatus
from bandwidth.model.lookup_status_enum import LookupStatusEnum
from bandwidth.model.tn_lookup_request_error import TnLookupRequestError


class TestPhoneNumberLookupIntegration(unittest.TestCase):
    """Phone Number Lookup API integration test"""

    
    def setUp(self):
        configuration = bandwidth.Configuration(
            username = os.environ['BW_USERNAME'],
            password = os.environ['BW_PASSWORD']
        )
        self.account_id = os.environ['BW_ACCOUNT_ID']
        self.api_client = bandwidth.ApiClient(configuration)

    
    def tearDown(self):
        pass

    
    def testSuccessfulPhoneNumberLookup(self):
        """Test Phone Number Lookup API"""
        api_instance = phone_number_lookup_api.PhoneNumberLookupApi(self.api_client)
        lookup_request = LookupRequest(
            tns=[
                os.environ['BW_NUMBER'],
            ],
        ) 

        create_lookup_response: CreateLookupResponse = api_instance.create_lookup(self.account_id, lookup_request, _return_http_data_only=False)
        self.assertEqual(202, create_lookup_response[1])
        self.assertIs(LookupStatusEnum, type(create_lookup_response[0].status))
        get_lookup_status_response: LookupStatus = api_instance.get_lookup_status(self.account_id, create_lookup_response[0].request_id)
    
    
    def testFailedPhoneNumberLookup(self):
        pass


if __name__ == '__main__':
    unittest.main()
