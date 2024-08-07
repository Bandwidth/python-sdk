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

from bandwidth.models.call_direction_enum import CallDirectionEnum

class TestCallDirectionEnum(unittest.TestCase):
    """CallDirectionEnum unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCallDirectionEnum(self):
        """Test CallDirectionEnum"""
        inbound = CallDirectionEnum('inbound')
        outbound = CallDirectionEnum('outbound')
        assert inbound == 'inbound'
        assert outbound == 'outbound'


if __name__ == '__main__':
    unittest.main()
