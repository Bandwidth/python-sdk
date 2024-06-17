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

from bandwidth.models.call_state_enum import CallStateEnum

class TestCallStateEnum(unittest.TestCase):
    """CallStateEnum unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCallStateEnum(self):
        """Test CallStateEnum"""
        active = CallStateEnum('active')
        completed = CallStateEnum('completed')
        assert active == 'active'
        assert completed == 'completed'

if __name__ == '__main__':
    unittest.main()
