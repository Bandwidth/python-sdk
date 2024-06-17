"""
Integration test for Bandwidth's Messaging API
"""

import os
import json
import unittest
from datetime import datetime

import bandwidth
from hamcrest import *

from bandwidth import ApiResponse
from bandwidth.api import messages_api
from bandwidth.models.list_message_direction_enum import ListMessageDirectionEnum
from bandwidth.models.list_message_item import ListMessageItem
from bandwidth.models.message_request import MessageRequest
from bandwidth.models.message_status_enum import MessageStatusEnum
from bandwidth.models.message_type_enum import MessageTypeEnum
from bandwidth.models.messages_list import MessagesList
from bandwidth.models.priority_enum import PriorityEnum
from bandwidth.models.message import Message
from bandwidth.exceptions import ApiException, UnauthorizedException
from test.utils.env_variables import *


class TestMessagesApi(unittest.TestCase):
    """MessagesApi unit test stubs"""

    def setUp(self):
        # API Client
        configuration = bandwidth.Configuration(
            username=BW_USERNAME,
            password=BW_PASSWORD
        )
        api_client = bandwidth.ApiClient(configuration)
        self.api_instance = messages_api.MessagesApi(api_client)
        self.account_id = BW_ACCOUNT_ID

        # Unauthorized API Client
        self.unauthorized_api_client = bandwidth.ApiClient()
        self.unauthorized_api_instance = messages_api.MessagesApi(self.unauthorized_api_client)

        # Message Properties
        self.application_id = BW_MESSAGING_APPLICATION_ID
        self.to_number = [USER_NUMBER]
        self.from_number = BW_NUMBER
        self.text = 'python integration'
        self.media = ['https://cdn2.thecatapi.com/images/MTY3ODIyMQ.jpg']
        self.tag = 'python integration tag'
        self.priority = PriorityEnum("default")

        # Message Request
        self.message_request = MessageRequest(
            application_id=self.application_id,
            to=self.to_number,
            var_from=self.from_number,
            text=self.text,
            media=self.media,
            tag=self.tag,
            priority=self.priority,
        )

        # Invalid Message Request
        self.invalid_message_request = MessageRequest(
            application_id=self.application_id,
            to=['+invalid'],
            var_from='+invalid',
            text='',
        )

    def test_create_message(self):
        response: ApiResponse = self.api_instance.create_message_with_http_info(
            self.account_id,
            self.message_request,
        )

        assert_that(response.status_code, equal_to(202))

        api_response = response.data
        assert_that(api_response, instance_of(Message))
        assert_that(api_response, has_properties(
            'application_id', self.application_id,
            'to', self.to_number,
            'var_from', self.from_number,
            'owner', self.from_number,
            'text', self.text,
            'media', self.media,
            'tag', self.tag,
            'priority', instance_of(PriorityEnum),
            'priority', self.priority,
            'segment_count', 1,
        )
                    )
        assert_that(api_response.time, instance_of(datetime))

    def test_create_message_bad_request(self):
        assert_that(calling(self.api_instance.create_message).with_args(
            self.account_id, self.invalid_message_request)), raises(ApiException)

    def test_create_message_unauthorized(self):
        assert_that(calling(self.unauthorized_api_instance.create_message).with_args(
            self.account_id, self.invalid_message_request)), raises(UnauthorizedException)

    @unittest.skip('The SDK catches incorrect content-type before making the request and attempts to create an ApiException,\
                    but the creation of the exception fails since there is no response body. This should probably create some\
                    kind of Client Exception instead, since this is not an actual API Exception.')
    def test_create_message_invalid_media(self):
        assert_that(calling(self.api_instance.create_message).with_args(
            self.account_id, self.message_request, _content_type='application/xml')), raises(ApiException)

    def test_list_messages(self):
        message_direction = ListMessageDirectionEnum("OUTBOUND")

        response = self.api_instance.list_messages_with_http_info(self.account_id, message_direction=message_direction)

        assert_that(response.status_code, equal_to(200))

        api_response = response.data
        assert_that(api_response, instance_of(MessagesList))
        assert_that(api_response, has_properties(
            'total_count', greater_than(0),
            'messages', instance_of(list)
        ))

        assert_that(api_response.messages[0], instance_of(ListMessageItem))

        message = api_response.messages[0]
        assert_that(message, has_properties(
            'account_id', self.account_id,
            'destination_tn', matches_regexp('^\\+[1-9]\\d{1,14}$'),
            'message_direction', ListMessageDirectionEnum("OUTBOUND"),
            'message_id', matches_regexp('^.+$'),
            'message_status', instance_of(MessageStatusEnum),
            'message_type', instance_of(MessageTypeEnum),
            'segment_count', greater_than(0),
            'source_tn', matches_regexp('^\\+[1-9]\\d{1,14}$')
        ))
        assert_that(message.receive_time, instance_of(datetime))

    def test_list_messages_bad_request(self):
        assert_that(calling(self.api_instance.list_messages).with_args(
            self.account_id), raises(ApiException))

    def test_list_messages_unauthorized(self):
        assert_that(calling(self.unauthorized_api_instance.list_messages).with_args(
            self.account_id), raises(UnauthorizedException))


if __name__ == '__main__':
    unittest.main()
