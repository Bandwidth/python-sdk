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

from bandwidth.models.lookup_status import LookupStatus
from bandwidth.models.lookup_result import LookupResult

class TestLookupStatus(unittest.TestCase):
    """LookupStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LookupStatus:
        """Test LookupStatus
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        if include_optional:
            return LookupStatus(
                request_id = '004223a0-8b17-41b1-bf81-20732adf5590',
                status = 'COMPLETE',
                result = [
                    LookupResult(
                        response_code = 0, 
                        message = 'NOERROR', 
                        e_164_format = '+19195551234', 
                        formatted = '(919) 555-1234', 
                        country = 'US', 
                        line_type = 'Mobile', 
                        line_provider = 'Verizon Wireless', 
                        mobile_country_code = '310', 
                        mobile_network_code = '010', )
                    ],
                failed_telephone_numbers = ["+191955512345"]
            )
        else:
            return LookupStatus(
        )

    def testLookupStatus(self):
        """Test LookupStatus"""
        instance = self.make_instance(True)
        assert instance is not None
        assert isinstance(instance, LookupStatus)
        assert instance.request_id == '004223a0-8b17-41b1-bf81-20732adf5590'
        assert instance.status == 'COMPLETE'
        assert isinstance(instance.result, list)
        assert len(instance.result) == 1
        assert isinstance(instance.result[0], LookupResult)
        assert instance.result[0].response_code == 0
        assert instance.result[0].message == 'NOERROR'
        assert instance.result[0].e_164_format == '+19195551234'
        assert instance.result[0].formatted == '(919) 555-1234'
        assert instance.result[0].country == 'US'
        assert instance.result[0].line_type == 'Mobile'
        assert instance.result[0].line_provider == 'Verizon Wireless'
        assert instance.result[0].mobile_country_code == '310'
        assert instance.result[0].mobile_network_code == '010'
        assert instance.failed_telephone_numbers == ["+191955512345"]

if __name__ == '__main__':
    unittest.main()
