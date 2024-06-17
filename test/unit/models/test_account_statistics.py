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

from bandwidth.models.account_statistics import AccountStatistics

class TestAccountStatistics(unittest.TestCase):
    """AccountStatistics unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccountStatistics:
        """Test AccountStatistics
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccountStatistics`
        """
        model = AccountStatistics()
        if include_optional:
            return AccountStatistics(
                current_call_queue_size = 0,
                max_call_queue_size = 900
            )
        else:
            return AccountStatistics(
        )
        """

    def testAccountStatistics(self):
        """Test AccountStatistics"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
