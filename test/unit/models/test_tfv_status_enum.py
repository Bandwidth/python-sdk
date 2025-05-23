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

from bandwidth.models.tfv_status_enum import TfvStatusEnum

class TestTfvStatusEnum(unittest.TestCase):
    """TfvStatusEnum unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTfvStatusEnum(self):
        """Test TfvStatusEnum"""
        verified = TfvStatusEnum('VERIFIED')
        unverified = TfvStatusEnum('UNVERIFIED')
        pending = TfvStatusEnum('PENDING')
        assert verified == 'VERIFIED'
        assert unverified == 'UNVERIFIED'
        assert pending == 'PENDING'

if __name__ == '__main__':
    unittest.main()
