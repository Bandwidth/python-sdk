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

from bandwidth.models.message_failed_callback_message import MessageFailedCallbackMessage

class TestMessageFailedCallbackMessage(unittest.TestCase):
    """MessageFailedCallbackMessage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MessageFailedCallbackMessage:
        """Test MessageFailedCallbackMessage
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MessageFailedCallbackMessage`
        """
        model = MessageFailedCallbackMessage()
        if include_optional:
            return MessageFailedCallbackMessage(
                id = '1661365814859loidf7mcwd4qacn7',
                owner = '+15553332222',
                application_id = '93de2206-9669-4e07-948d-329f4b722ee2',
                time = '2016-09-14T18:20:16Z',
                segment_count = 1,
                direction = 'in',
                to = ["+15552223333"],
                var_from = '+15553332222',
                text = 'Hello world',
                tag = 'custom string',
                media = ["https://dev.bandwidth.com/images/bandwidth-logo.png","https://dev.bandwidth.com/images/github_logo.png"],
                priority = 'default'
            )
        else:
            return MessageFailedCallbackMessage(
                id = '1661365814859loidf7mcwd4qacn7',
                owner = '+15553332222',
                application_id = '93de2206-9669-4e07-948d-329f4b722ee2',
                time = '2016-09-14T18:20:16Z',
                segment_count = 1,
                direction = 'in',
                to = ["+15552223333"],
                var_from = '+15553332222',
                text = 'Hello world',
                tag = 'custom string',
                priority = 'default',
        )
        """

    def testMessageFailedCallbackMessage(self):
        """Test MessageFailedCallbackMessage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()