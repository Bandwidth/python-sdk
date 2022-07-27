"""
    Bandwidth


    Bandwidth's Communication APIs  # noqa: E501


    The version of the OpenAPI document: 1.0.0
    Contact: letstalk@bandwidth.com
    Generated by: https://openapi-generator.tech
"""

import os
import json
import unittest
from datetime import datetime

import bandwidth
from bandwidth.api import messages_api
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
from bandwidth.exceptions import ApiException, UnauthorizedException


class TestMessagesApi(unittest.TestCase):
    """MessagesApi unit test stubs"""

    def setUp(self):
        # API Client
        configuration = bandwidth.Configuration(
            username = os.environ.get('BW_USERNAME'),
            password = os.environ.get('BW_PASSWORD')
        )
        api_client = bandwidth.ApiClient(configuration)
        self.api_instance = messages_api.MessagesApi(api_client)
        self.account_id = os.environ.get('BW_ACCOUNT_ID')

        # Unauthorized API Client
        self.unauthorized_api_client = bandwidth.ApiClient()
        self.unauthorized_api_instance = messages_api.MessagesApi(self.unauthorized_api_client)

        # Message Properties
        self.application_id = os.environ.get('BW_MESSAGING_APPLICATION_ID')
        self.to_number = [os.environ.get('USER_NUMBER')]
        self.from_number = os.environ.get('BW_NUMBER')
        self.text = 'python integration'
        self.media = ['https://cdn2.thecatapi.com/images/MTY3ODIyMQ.jpg']
        self.tag = 'python integration tag'
        self.priority = PriorityEnum("default")

        # Message Request
        self.message_request = MessageRequest(
            application_id=self.application_id,
            to=self.to_number,
            _from=self.from_number,
            text=self.text,
            media=self.media,
            tag=self.tag,
            priority=self.priority,
        )
        
        # Invalid Message Request
        self.invalid_message_request = MessageRequest(
            application_id=self.application_id,
            to=['+invalid'],
            _from='+invalid',
            text='',
        )


    def test_create_message(self):
        response: Message = self.api_instance.create_message(self.account_id, self.message_request, _return_http_data_only=False)

        self.assertEqual(response[1], 202)

        api_response = response[0]
        self.assertIsInstance(api_response, Message)
        self.assertEqual(api_response.application_id,self.application_id)
        self.assertEqual(api_response.to, self.to_number)
        self.assertEqual(api_response._from, self.from_number)
        self.assertEqual(api_response.owner, self.from_number)
        self.assertEqual(api_response.text, self.text)
        self.assertEqual(api_response.media, self.media)
        self.assertEqual(api_response.tag, self.tag)
        self.assertIsInstance(api_response.priority, PriorityEnum)
        self.assertEqual(api_response.priority, self.priority)
        self.assertEqual(api_response.segment_count, 1)
        self.assertTrue(datetime.fromisoformat(api_response.time[:-1]))


    def test_create_message_bad_request(self):
        with self.assertRaises(ApiException) as context:
            self.api_instance.create_message(self.account_id, self.invalid_message_request)
            
        self.assertEqual(context.exception.status, 400)

        e = json.loads(context.exception.body)
        self.assertEqual(e['type'], 'request-validation')
        self.assertIsInstance(e['description'], str)
        self.assertIsInstance(e['fieldErrors'], list)

        field_error = e['fieldErrors'][0]
        self.assertEqual(field_error['fieldName'], 'to')
        self.assertEqual(field_error['description'], "'+invalid' must be replaced with a valid E164 formatted telephone number")
    

    def test_create_message_unauthorized(self):
        with self.assertRaises(UnauthorizedException) as context:
            self.unauthorized_api_instance.create_message(self.account_id, self.invalid_message_request)
             
        self.assertEqual(context.exception.status, 401)

        e = json.loads(context.exception.body)
        self.assertEqual(e['type'], 'unauthorized')
        self.assertEqual(e['description'], 'Authentication Failed')

    
    @unittest.skip('The SDK catches incorrect content-type before making the request and attempts to create an ApiException,\
                    but the creation of the exception fails since there is no response body. This should probably create some\
                    kind of Client Exception instead, since this is not an actual API Exception.')
    def test_create_message_invalid_media(self):
        with self.assertRaises(ApiException) as context:
            self.api_instance.create_message(self.account_id, self.message_request, _content_type='application/xml')


    def test_list_messages(self):
        message_direction = ListMessageDirectionEnum("OUTBOUND")
        
        response = self.api_instance.list_messages(self.account_id, message_direction=message_direction, _return_http_data_only=False)

        self.assertEqual(response[1], 200)

        api_response = response[0]
        self.assertIsInstance(api_response, MessagesList)
        self.assertGreater(api_response.total_count, 0)
        self.assertTrue(api_response.messages[0], ListMessageItem)
        
        message = api_response.messages[0]
        self.assertEqual(message.account_id, self.account_id)
        self.assertRegex(message.destination_tn, '^\\+[1-9]\\d{1,14}$')
        self.assertEqual(message.message_direction, ListMessageDirectionEnum("OUTBOUND"))
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

        e = json.loads(context.exception.body)
        self.assertEqual(e['type'], 'bad-request')
        self.assertIsInstance(e['description'], str)

    
    def test_list_messages_unauthorized(self):
        
        with self.assertRaises(UnauthorizedException) as context:
            self.unauthorized_api_instance.list_messages(self.account_id)
             
        self.assertEqual(context.exception.status, 401)

        e = json.loads(context.exception.body)
        self.assertEqual(e['type'], 'unauthorized')
        self.assertEqual(e['description'], 'Your request could not be authenticated')
        

if __name__ == '__main__':
    unittest.main()
