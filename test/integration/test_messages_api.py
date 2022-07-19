"""
    Bandwidth


    Bandwidth's Communication APIs  # noqa: E501


    The version of the OpenAPI document: 1.0.0
    Contact: letstalk@bandwidth.com
    Generated by: https://openapi-generator.tech
"""

from array import array
import os
import json
import unittest
from datetime import datetime

import bandwidth
from bandwidth.api import messages_api
from bandwidth.exceptions import ApiException, UnauthorizedException
from bandwidth.model.list_message_direction_enum import ListMessageDirectionEnum
from bandwidth.model.list_message_item import ListMessageItem
from bandwidth.model.message_request import MessageRequest
from bandwidth.model.message_status_enum import MessageStatusEnum
from bandwidth.model.message_type_enum import MessageTypeEnum
from bandwidth.model.messages_list import MessagesList
from bandwidth.model.priority_enum import PriorityEnum
from bandwidth.model.message import Message
from bandwidth.model.messaging_request_error import MessagingRequestError
from bandwidth.model.create_message_request_error import CreateMessageRequestError
from bandwidth.model.field_error import FieldError


class TestMessagesApi(unittest.TestCase):
    """MessagesApi unit test stubs"""

    def setUp(self):
        configuration = bandwidth.Configuration(
            username = os.environ.get('BW_USERNAME'),
            password = os.environ.get('BW_PASSWORD')
        )
        api_client = bandwidth.ApiClient(configuration)
        self.api_instance = messages_api.MessagesApi(api_client)
        self.account_id = os.environ.get('BW_ACCOUNT_ID')


    def test_create_message(self):
        message_request = MessageRequest(
            application_id=os.environ.get('BW_MESSAGING_APPLICATION_ID'),
            to=[os.environ.get('USER_NUMBER')],
            _from=os.environ.get('BW_NUMBER'),
            text="python integration",
            media=["https://dev.bandwidth.com/images/bandwidth-logo.png","https://dev.bandwidth.com/images/github_logo.png"],
            tag="python integration tag",
            priority=PriorityEnum("default"),
        )
        
        try:
            api_response: Message = self.api_instance.create_message(self.account_id, message_request)
        except bandwidth.ApiException as e:
            print("Exception when calling MessagesApi->create_message: %s\n" % e)
            
        self.assertIsInstance(api_response, Message)
        self.assertEqual(api_response.application_id,message_request.application_id)
        self.assertEqual(api_response.to, message_request.to)
        self.assertEqual(api_response._from, message_request._from)
        self.assertEqual(api_response.owner, message_request._from)
        self.assertEqual(api_response.text, message_request.text)
        self.assertEqual(api_response.media, message_request.media)
        self.assertEqual(api_response.tag, message_request.tag)
        self.assertEqual(api_response.priority, message_request.priority)
        self.assertEqual(api_response.segment_count, 1)
        self.assertTrue(datetime.fromisoformat(api_response.time[:-1]))


    def test_create_message_bad_request(self):
        message_request = MessageRequest(
            application_id=os.environ.get('BW_MESSAGING_APPLICATION_ID'),
            to=['+invalid'],
            _from='+invalid',
            text='',
        )
        
        with self.assertRaises(ApiException) as context:
            self.api_instance.create_message(self.account_id, message_request)
            
        self.assertEqual(context.exception.status, 400)

        e = CreateMessageRequestError(field_errors=(json.loads(context.exception.body))['fieldErrors'], **json.loads(context.exception.body))
        self.assertIsInstance(e, CreateMessageRequestError)
        self.assertEqual(e.type, 'request-validation')
        self.assertIsInstance(e.description, str)
        self.assertIsInstance(e.field_errors, list)

        error = e.field_errors[0]
        self.assertIsInstance(error, FieldError)
        self.assertIsInstance(error.fieldName, str)
        self.assertIsInstance(error.description, str)
    

    def test_create_message_unauthorized(self):
        api_client = bandwidth.ApiClient()
        api_instance = messages_api.MessagesApi(api_client)
        message_request = MessageRequest(
            application_id=os.environ.get('BW_MESSAGING_APPLICATION_ID'),
            to=['+invalid'],
            _from='+invalid',
            text='',
        )
        
        with self.assertRaises(UnauthorizedException) as context:
            api_instance.create_message(self.account_id, message_request)
             
        self.assertEqual(context.exception.status, 401)

        e = MessagingRequestError(**json.loads(context.exception.body))
        self.assertIsInstance(e, MessagingRequestError)
        self.assertEqual(e.type, 'unauthorized')
        self.assertEqual(e.description, 'Authentication Failed')


    def test_list_messages(self):
        message_direction = ListMessageDirectionEnum("OUTBOUND")
        
        try:
            api_response = self.api_instance.list_messages(self.account_id, message_direction=message_direction)
        except bandwidth.ApiException as e:
            print("Exception when calling MessagesApi->list_messages: %s\n" % e)

        self.assertIsInstance(api_response, MessagesList)
        self.assertGreater(api_response.total_count, 0)
        self.assertTrue(api_response.messages[0], ListMessageItem)
        
        message = api_response.messages[0]
        self.assertEqual(message.account_id, os.environ.get('BW_ACCOUNT_ID'))
        self.assertTrue(message.carrier_name)
        self.assertRegex(message.destination_tn, '^\\+[1-9]\\d{1,14}$')
        self.assertFalse(message.error_code)
        self.assertIsInstance(message.message_direction, ListMessageDirectionEnum)
        self.assertTrue(message.message_id)
        self.assertIsInstance(message.message_status, MessageStatusEnum)
        self.assertIsInstance(message.message_type, MessageTypeEnum)
        self.assertTrue(datetime.fromisoformat(message.receive_time[:-1]))
        self.assertTrue(message.segment_count)
        self.assertRegex(message.source_tn, '^\\+[1-9]\\d{1,14}$')

    
    def test_list_messages_bad_request(self):
        
        with self.assertRaises(ApiException) as context:
            self.api_instance.list_messages(self.account_id)
        
        self.assertEqual(context.exception.status, 400)

        e = MessagingRequestError(**json.loads(context.exception.body))
        self.assertIsInstance(e, MessagingRequestError)
        self.assertEqual(e.type, 'bad-request')
        self.assertIsInstance(e.description, str)

    
    def test_list_messages_unauthorized(self):
        api_client = bandwidth.ApiClient()
        api_instance = messages_api.MessagesApi(api_client)
        
        with self.assertRaises(UnauthorizedException) as context:
            api_instance.list_messages(self.account_id)
             
        self.assertEqual(context.exception.status, 401)

        e = MessagingRequestError(**json.loads(context.exception.body))
        self.assertIsInstance(e, MessagingRequestError)
        self.assertEqual(e.type, 'unauthorized')
        self.assertEqual(e.description, 'Your request could not be authenticated')
        

if __name__ == '__main__':
    unittest.main()
