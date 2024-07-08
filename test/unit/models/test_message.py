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

from bandwidth.models.message import Message

class TestMessage(unittest.TestCase):
    """Message unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Message:
        """Test Message
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        if include_optional:
            return Message(
                id = '1589228074636lm4k2je7j7jklbn2',
                owner = '+15554443333',
                application_id = '93de2206-9669-4e07-948d-329f4b722ee2',
                time = '2022-09-14T18:20:16Z',
                segment_count = 2,
                direction = 'in',
                to = ["+15552223333"],
                var_from = '+15553332222',
                media = ["https://dev.bandwidth.com/images/bandwidth-logo.png"],
                text = 'Hello world',
                tag = 'custom tag',
                priority = 'default',
                expiration = '2021-02-01T11:29:18-05:00'
            )
        else:
            return Message(
        )

    def testMessage(self):
        """Test Message"""
        instance = self.make_instance(True)
        assert instance is not None
        assert isinstance(instance, Message)
        assert instance.id == '1589228074636lm4k2je7j7jklbn2'
        assert instance.owner == '+15554443333'
        assert instance.application_id == '93de2206-9669-4e07-948d-329f4b722ee2'
        assert isinstance(instance.time, datetime)
        assert instance.segment_count == 2
        assert instance.direction == 'in'
        assert instance.to == ["+15552223333"]
        assert instance.var_from == '+15553332222'
        assert instance.media == ["https://dev.bandwidth.com/images/bandwidth-logo.png"]
        assert instance.text == 'Hello world'
        assert instance.tag == 'custom tag'
        assert instance.priority == 'default'
        assert isinstance(instance.expiration, datetime)

if __name__ == '__main__':
    unittest.main()
