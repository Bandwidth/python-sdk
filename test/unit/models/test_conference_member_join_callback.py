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
from datetime import datetime

from bandwidth.models.conference_member_join_callback import ConferenceMemberJoinCallback

class TestConferenceMemberJoinCallback(unittest.TestCase):
    """ConferenceMemberJoinCallback unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConferenceMemberJoinCallback:
        """Test ConferenceMemberJoinCallback
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        if include_optional:
            return ConferenceMemberJoinCallback(
                event_type = 'bridgeComplete',
                event_time = '2022-06-17T22:19:40.375Z',
                conference_id = 'conf-fe23a767-a75a5b77-20c5-4cca-b581-cbbf0776eca9',
                name = 'my-conference-name',
                var_from = '+15555555555',
                to = '+15555555555',
                call_id = 'c-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85',
                tag = 'exampleTag'
            )
        else:
            return ConferenceMemberJoinCallback(
        )

    def testConferenceMemberJoinCallback(self):
        """Test ConferenceMemberJoinCallback"""
        instance = self.make_instance(True)
        assert instance is not None
        assert isinstance(instance, ConferenceMemberJoinCallback)
        assert instance.event_type == 'bridgeComplete'
        assert isinstance(instance.event_time, datetime)
        assert instance.conference_id == 'conf-fe23a767-a75a5b77-20c5-4cca-b581-cbbf0776eca9'
        assert instance.name == 'my-conference-name'
        assert instance.var_from == '+15555555555'
        assert instance.to == '+15555555555'
        assert instance.call_id == 'c-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85'
        assert instance.tag == 'exampleTag'

if __name__ == '__main__':
    unittest.main()
