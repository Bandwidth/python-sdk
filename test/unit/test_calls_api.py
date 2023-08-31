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

import bandwidth
from bandwidth.api.calls_api import CallsApi  # noqa: E501
from bandwidth.rest import ApiException


class TestCallsApi(unittest.TestCase):
    """CallsApi unit test stubs"""

    def setUp(self):
        self.api = bandwidth.api.calls_api.CallsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_call(self):
        """Test case for create_call

        Create Call  # noqa: E501
        """
        pass

    def test_get_call_state(self):
        """Test case for get_call_state

        Get Call State Information  # noqa: E501
        """
        pass

    def test_update_call(self):
        """Test case for update_call

        Update Call  # noqa: E501
        """
        pass

    def test_update_call_bxml(self):
        """Test case for update_call_bxml

        Update Call BXML  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
