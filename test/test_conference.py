"""
    Bandwidth

    Bandwidth's Communication APIs  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: letstalk@bandwidth.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import bandwidth
from bandwidth.model.callback_method_enum import CallbackMethodEnum
from bandwidth.model.conference_member import ConferenceMember
globals()['CallbackMethodEnum'] = CallbackMethodEnum
globals()['ConferenceMember'] = ConferenceMember
from bandwidth.model.conference import Conference


class TestConference(unittest.TestCase):
    """Conference unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testConference(self):
        """Test Conference"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Conference()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
