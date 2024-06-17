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

from bandwidth.models.message_failed_callback import MessageFailedCallback
from bandwidth.models.message_failed_callback_message import MessageFailedCallbackMessage

class TestMessageFailedCallback(unittest.TestCase):
    """MessageFailedCallback unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MessageFailedCallback:
        """Test MessageFailedCallback
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        if include_optional:
            return MessageFailedCallback(
                time = '2016-09-14T18:20:16Z',
                type = 'message-failed',
                to = '+15552223333',
                description = 'rejected-unallocated-from-number',
                message = MessageFailedCallbackMessage(
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
                    priority = 'default', ),
                error_code = 9902
            )
        else:
            return MessageFailedCallback(
                time = '2016-09-14T18:20:16Z',
                type = 'message-failed',
                to = '+15552223333',
                description = 'rejected-unallocated-from-number',
                message = MessageFailedCallbackMessage(
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
                    priority = 'default', ),
                error_code = 9902,
        )

    def testMessageFailedCallback(self):
        """Test MessageFailedCallback"""
        instance = self.make_instance(True)
        assert instance is not None
        assert isinstance(instance, MessageFailedCallback)
        assert isinstance(instance.time, datetime)
        assert instance.type == 'message-failed'
        assert instance.to == '+15552223333'
        assert instance.description == 'rejected-unallocated-from-number'
        assert isinstance(instance.message, MessageFailedCallbackMessage)
        assert instance.message.id == '1661365814859loidf7mcwd4qacn7'
        assert instance.message.owner == '+15553332222'
        assert instance.message.application_id == '93de2206-9669-4e07-948d-329f4b722ee2'
        assert isinstance(instance.message.time, datetime)
        assert instance.message.segment_count == 1
        assert instance.message.direction == 'in'
        assert instance.message.to == ["+15552223333"]
        assert instance.message.var_from == '+15553332222'
        assert instance.message.text == 'Hello world'
        assert instance.message.tag == 'custom string'
        assert instance.message.media == ["https://dev.bandwidth.com/images/bandwidth-logo.png","https://dev.bandwidth.com/images/github_logo.png"]
        assert instance.message.priority == 'default'
        assert instance.error_code == 9902

if __name__ == '__main__':
    unittest.main()
