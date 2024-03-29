# coding: utf-8

"""
    Bandwidth

    Bandwidth's Communication APIs

    The version of the OpenAPI document: 1.0.0
    Contact: letstalk@bandwidth.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

import bandwidth
from bandwidth.models.lookup_status import LookupStatus  # noqa: E501
from bandwidth.rest import ApiException

class TestLookupStatus(unittest.TestCase):
    """LookupStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test LookupStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LookupStatus`
        """
        model = bandwidth.models.lookup_status.LookupStatus()  # noqa: E501
        if include_optional :
            return LookupStatus(
                request_id = '004223a0-8b17-41b1-bf81-20732adf5590', 
                status = 'COMPLETE', 
                result = [
                    bandwidth.models.lookup_result.lookupResult(
                        response_code = 0, 
                        message = 'NOERROR', 
                        e/164_format = '+19195551234', 
                        formatted = '(919) 555-1234', 
                        country = 'US', 
                        line_type = 'Mobile', 
                        line_provider = 'Verizon Wireless', 
                        mobile_country_code = '310', 
                        mobile_network_code = '010', )
                    ], 
                failed_telephone_numbers = ["+191955512345"]
            )
        else :
            return LookupStatus(
        )
        """

    def testLookupStatus(self):
        """Test LookupStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
