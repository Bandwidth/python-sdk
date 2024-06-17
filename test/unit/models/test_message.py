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

from bandwidth.models.message import Message

class TestMessage(unittest.TestCase):
    """Message unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Message:
        """Test Message
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Message`
        """
        model = Message()
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
        """

    def testMessage(self):
        """Test Message"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
