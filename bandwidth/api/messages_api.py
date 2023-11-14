# coding: utf-8

"""
    Bandwidth

    Bandwidth's Communication APIs

    The version of the OpenAPI document: 1.0.0
    Contact: letstalk@bandwidth.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import Field, StrictBool, StrictInt, StrictStr

from typing import Optional

from bandwidth.models.list_message_direction_enum import ListMessageDirectionEnum
from bandwidth.models.message import Message
from bandwidth.models.message_request import MessageRequest
from bandwidth.models.message_status_enum import MessageStatusEnum
from bandwidth.models.message_type_enum import MessageTypeEnum
from bandwidth.models.messages_list import MessagesList

from bandwidth.api_client import ApiClient
from bandwidth.api_response import ApiResponse
from bandwidth.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class MessagesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def create_message(self, account_id : Annotated[StrictStr, Field(..., description="Your Bandwidth Account ID.")], message_request : MessageRequest, **kwargs) -> Message:  # noqa: E501
        """Create Message  # noqa: E501

        Endpoint for sending text messages and picture messages using V2 messaging.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_message(account_id, message_request, async_req=True)
        >>> result = thread.get()

        :param account_id: Your Bandwidth Account ID. (required)
        :type account_id: str
        :param message_request: (required)
        :type message_request: MessageRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Message
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the create_message_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.create_message_with_http_info(account_id, message_request, **kwargs)  # noqa: E501

    @validate_arguments
    def create_message_with_http_info(self, account_id : Annotated[StrictStr, Field(..., description="Your Bandwidth Account ID.")], message_request : MessageRequest, **kwargs) -> ApiResponse:  # noqa: E501
        """Create Message  # noqa: E501

        Endpoint for sending text messages and picture messages using V2 messaging.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_message_with_http_info(account_id, message_request, async_req=True)
        >>> result = thread.get()

        :param account_id: Your Bandwidth Account ID. (required)
        :type account_id: str
        :param message_request: (required)
        :type message_request: MessageRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Message, status_code(int), headers(HTTPHeaderDict))
        """

        _hosts = [
            'https://messaging.bandwidth.com/api/v2'
        ]
        _host = _hosts[0]
        if kwargs.get('_host_index'):
            _host_index = int(kwargs.get('_host_index'))
            if _host_index < 0 or _host_index >= len(_hosts):
                raise ApiValueError(
                    "Invalid host index. Must be 0 <= index < %s"
                    % len(_host)
                )
            _host = _hosts[_host_index]
        _params = locals()

        _all_params = [
            'account_id',
            'message_request'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params and _key != "_host_index":
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_message" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['account_id']:
            _path_params['accountId'] = _params['account_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['message_request'] is not None:
            _body_params = _params['message_request']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['Basic']  # noqa: E501

        _response_types_map = {
            '202': "Message",
            '400': "CreateMessageRequestError",
            '401': "MessagingRequestError",
            '403': "MessagingRequestError",
            '404': "MessagingRequestError",
            '406': "MessagingRequestError",
            '415': "MessagingRequestError",
            '429': "MessagingRequestError",
            '500': "MessagingRequestError",
        }

        return self.api_client.call_api(
            '/users/{accountId}/messages', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            _host=_host,
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def list_messages(self, account_id : Annotated[StrictStr, Field(..., description="Your Bandwidth Account ID.")], message_id : Annotated[Optional[StrictStr], Field(description="The ID of the message to search for. Special characters need to be encoded using URL encoding. Message IDs could come in different formats, e.g., 9e0df4ca-b18d-40d7-a59f-82fcdf5ae8e6 and 1589228074636lm4k2je7j7jklbn2 are valid message ID formats. Note that you must include at least one query parameter.")] = None, source_tn : Annotated[Optional[StrictStr], Field(description="The phone number that sent the message. Accepted values are: a single full phone number a comma separated list of full phone numbers (maximum of 10) or a single partial phone number (minimum of 5 characters e.g. '%2B1919').")] = None, destination_tn : Annotated[Optional[StrictStr], Field(description="The phone number that received the message. Accepted values are: a single full phone number a comma separated list of full phone numbers (maximum of 10) or a single partial phone number (minimum of 5 characters e.g. '%2B1919').")] = None, message_status : Annotated[Optional[MessageStatusEnum], Field(description="The status of the message. One of RECEIVED QUEUED SENDING SENT FAILED DELIVERED ACCEPTED UNDELIVERED.")] = None, message_direction : Annotated[Optional[ListMessageDirectionEnum], Field(description="The direction of the message. One of INBOUND OUTBOUND.")] = None, carrier_name : Annotated[Optional[StrictStr], Field(description="The name of the carrier used for this message. Possible values include but are not limited to Verizon and TMobile. Special characters need to be encoded using URL encoding (i.e. AT&T should be passed as AT%26T).")] = None, message_type : Annotated[Optional[MessageTypeEnum], Field(description="The type of message. Either sms or mms.")] = None, error_code : Annotated[Optional[StrictInt], Field(description="The error code of the message.")] = None, from_date_time : Annotated[Optional[StrictStr], Field(description="The start of the date range to search in ISO 8601 format. Uses the message receive time. The date range to search in is currently 14 days.")] = None, to_date_time : Annotated[Optional[StrictStr], Field(description="The end of the date range to search in ISO 8601 format. Uses the message receive time. The date range to search in is currently 14 days.")] = None, campaign_id : Annotated[Optional[StrictStr], Field(description="The campaign ID of the message.")] = None, sort : Annotated[Optional[StrictStr], Field(description="The field and direction to sort by combined with a colon. Direction is either asc or desc.")] = None, page_token : Annotated[Optional[StrictStr], Field(description="A base64 encoded value used for pagination of results.")] = None, limit : Annotated[Optional[StrictInt], Field(description="The maximum records requested in search result. Default 100. The sum of limit and after cannot be more than 10000.")] = None, limit_total_count : Annotated[Optional[StrictBool], Field(description="When set to true, the response's totalCount field will have a maximum value of 10,000. When set to false, or excluded, this will give an accurate totalCount of all messages that match the provided filters. If you are experiencing latency, try using this parameter to limit your results.")] = None, **kwargs) -> MessagesList:  # noqa: E501
        """List Messages  # noqa: E501

        Returns a list of messages based on query parameters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_messages(account_id, message_id, source_tn, destination_tn, message_status, message_direction, carrier_name, message_type, error_code, from_date_time, to_date_time, campaign_id, sort, page_token, limit, limit_total_count, async_req=True)
        >>> result = thread.get()

        :param account_id: Your Bandwidth Account ID. (required)
        :type account_id: str
        :param message_id: The ID of the message to search for. Special characters need to be encoded using URL encoding. Message IDs could come in different formats, e.g., 9e0df4ca-b18d-40d7-a59f-82fcdf5ae8e6 and 1589228074636lm4k2je7j7jklbn2 are valid message ID formats. Note that you must include at least one query parameter.
        :type message_id: str
        :param source_tn: The phone number that sent the message. Accepted values are: a single full phone number a comma separated list of full phone numbers (maximum of 10) or a single partial phone number (minimum of 5 characters e.g. '%2B1919').
        :type source_tn: str
        :param destination_tn: The phone number that received the message. Accepted values are: a single full phone number a comma separated list of full phone numbers (maximum of 10) or a single partial phone number (minimum of 5 characters e.g. '%2B1919').
        :type destination_tn: str
        :param message_status: The status of the message. One of RECEIVED QUEUED SENDING SENT FAILED DELIVERED ACCEPTED UNDELIVERED.
        :type message_status: MessageStatusEnum
        :param message_direction: The direction of the message. One of INBOUND OUTBOUND.
        :type message_direction: ListMessageDirectionEnum
        :param carrier_name: The name of the carrier used for this message. Possible values include but are not limited to Verizon and TMobile. Special characters need to be encoded using URL encoding (i.e. AT&T should be passed as AT%26T).
        :type carrier_name: str
        :param message_type: The type of message. Either sms or mms.
        :type message_type: MessageTypeEnum
        :param error_code: The error code of the message.
        :type error_code: int
        :param from_date_time: The start of the date range to search in ISO 8601 format. Uses the message receive time. The date range to search in is currently 14 days.
        :type from_date_time: str
        :param to_date_time: The end of the date range to search in ISO 8601 format. Uses the message receive time. The date range to search in is currently 14 days.
        :type to_date_time: str
        :param campaign_id: The campaign ID of the message.
        :type campaign_id: str
        :param sort: The field and direction to sort by combined with a colon. Direction is either asc or desc.
        :type sort: str
        :param page_token: A base64 encoded value used for pagination of results.
        :type page_token: str
        :param limit: The maximum records requested in search result. Default 100. The sum of limit and after cannot be more than 10000.
        :type limit: int
        :param limit_total_count: When set to true, the response's totalCount field will have a maximum value of 10,000. When set to false, or excluded, this will give an accurate totalCount of all messages that match the provided filters. If you are experiencing latency, try using this parameter to limit your results.
        :type limit_total_count: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: MessagesList
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the list_messages_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.list_messages_with_http_info(account_id, message_id, source_tn, destination_tn, message_status, message_direction, carrier_name, message_type, error_code, from_date_time, to_date_time, campaign_id, sort, page_token, limit, limit_total_count, **kwargs)  # noqa: E501

    @validate_arguments
    def list_messages_with_http_info(self, account_id : Annotated[StrictStr, Field(..., description="Your Bandwidth Account ID.")], message_id : Annotated[Optional[StrictStr], Field(description="The ID of the message to search for. Special characters need to be encoded using URL encoding. Message IDs could come in different formats, e.g., 9e0df4ca-b18d-40d7-a59f-82fcdf5ae8e6 and 1589228074636lm4k2je7j7jklbn2 are valid message ID formats. Note that you must include at least one query parameter.")] = None, source_tn : Annotated[Optional[StrictStr], Field(description="The phone number that sent the message. Accepted values are: a single full phone number a comma separated list of full phone numbers (maximum of 10) or a single partial phone number (minimum of 5 characters e.g. '%2B1919').")] = None, destination_tn : Annotated[Optional[StrictStr], Field(description="The phone number that received the message. Accepted values are: a single full phone number a comma separated list of full phone numbers (maximum of 10) or a single partial phone number (minimum of 5 characters e.g. '%2B1919').")] = None, message_status : Annotated[Optional[MessageStatusEnum], Field(description="The status of the message. One of RECEIVED QUEUED SENDING SENT FAILED DELIVERED ACCEPTED UNDELIVERED.")] = None, message_direction : Annotated[Optional[ListMessageDirectionEnum], Field(description="The direction of the message. One of INBOUND OUTBOUND.")] = None, carrier_name : Annotated[Optional[StrictStr], Field(description="The name of the carrier used for this message. Possible values include but are not limited to Verizon and TMobile. Special characters need to be encoded using URL encoding (i.e. AT&T should be passed as AT%26T).")] = None, message_type : Annotated[Optional[MessageTypeEnum], Field(description="The type of message. Either sms or mms.")] = None, error_code : Annotated[Optional[StrictInt], Field(description="The error code of the message.")] = None, from_date_time : Annotated[Optional[StrictStr], Field(description="The start of the date range to search in ISO 8601 format. Uses the message receive time. The date range to search in is currently 14 days.")] = None, to_date_time : Annotated[Optional[StrictStr], Field(description="The end of the date range to search in ISO 8601 format. Uses the message receive time. The date range to search in is currently 14 days.")] = None, campaign_id : Annotated[Optional[StrictStr], Field(description="The campaign ID of the message.")] = None, sort : Annotated[Optional[StrictStr], Field(description="The field and direction to sort by combined with a colon. Direction is either asc or desc.")] = None, page_token : Annotated[Optional[StrictStr], Field(description="A base64 encoded value used for pagination of results.")] = None, limit : Annotated[Optional[StrictInt], Field(description="The maximum records requested in search result. Default 100. The sum of limit and after cannot be more than 10000.")] = None, limit_total_count : Annotated[Optional[StrictBool], Field(description="When set to true, the response's totalCount field will have a maximum value of 10,000. When set to false, or excluded, this will give an accurate totalCount of all messages that match the provided filters. If you are experiencing latency, try using this parameter to limit your results.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """List Messages  # noqa: E501

        Returns a list of messages based on query parameters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_messages_with_http_info(account_id, message_id, source_tn, destination_tn, message_status, message_direction, carrier_name, message_type, error_code, from_date_time, to_date_time, campaign_id, sort, page_token, limit, limit_total_count, async_req=True)
        >>> result = thread.get()

        :param account_id: Your Bandwidth Account ID. (required)
        :type account_id: str
        :param message_id: The ID of the message to search for. Special characters need to be encoded using URL encoding. Message IDs could come in different formats, e.g., 9e0df4ca-b18d-40d7-a59f-82fcdf5ae8e6 and 1589228074636lm4k2je7j7jklbn2 are valid message ID formats. Note that you must include at least one query parameter.
        :type message_id: str
        :param source_tn: The phone number that sent the message. Accepted values are: a single full phone number a comma separated list of full phone numbers (maximum of 10) or a single partial phone number (minimum of 5 characters e.g. '%2B1919').
        :type source_tn: str
        :param destination_tn: The phone number that received the message. Accepted values are: a single full phone number a comma separated list of full phone numbers (maximum of 10) or a single partial phone number (minimum of 5 characters e.g. '%2B1919').
        :type destination_tn: str
        :param message_status: The status of the message. One of RECEIVED QUEUED SENDING SENT FAILED DELIVERED ACCEPTED UNDELIVERED.
        :type message_status: MessageStatusEnum
        :param message_direction: The direction of the message. One of INBOUND OUTBOUND.
        :type message_direction: ListMessageDirectionEnum
        :param carrier_name: The name of the carrier used for this message. Possible values include but are not limited to Verizon and TMobile. Special characters need to be encoded using URL encoding (i.e. AT&T should be passed as AT%26T).
        :type carrier_name: str
        :param message_type: The type of message. Either sms or mms.
        :type message_type: MessageTypeEnum
        :param error_code: The error code of the message.
        :type error_code: int
        :param from_date_time: The start of the date range to search in ISO 8601 format. Uses the message receive time. The date range to search in is currently 14 days.
        :type from_date_time: str
        :param to_date_time: The end of the date range to search in ISO 8601 format. Uses the message receive time. The date range to search in is currently 14 days.
        :type to_date_time: str
        :param campaign_id: The campaign ID of the message.
        :type campaign_id: str
        :param sort: The field and direction to sort by combined with a colon. Direction is either asc or desc.
        :type sort: str
        :param page_token: A base64 encoded value used for pagination of results.
        :type page_token: str
        :param limit: The maximum records requested in search result. Default 100. The sum of limit and after cannot be more than 10000.
        :type limit: int
        :param limit_total_count: When set to true, the response's totalCount field will have a maximum value of 10,000. When set to false, or excluded, this will give an accurate totalCount of all messages that match the provided filters. If you are experiencing latency, try using this parameter to limit your results.
        :type limit_total_count: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(MessagesList, status_code(int), headers(HTTPHeaderDict))
        """

        _hosts = [
            'https://messaging.bandwidth.com/api/v2'
        ]
        _host = _hosts[0]
        if kwargs.get('_host_index'):
            _host_index = int(kwargs.get('_host_index'))
            if _host_index < 0 or _host_index >= len(_hosts):
                raise ApiValueError(
                    "Invalid host index. Must be 0 <= index < %s"
                    % len(_host)
                )
            _host = _hosts[_host_index]
        _params = locals()

        _all_params = [
            'account_id',
            'message_id',
            'source_tn',
            'destination_tn',
            'message_status',
            'message_direction',
            'carrier_name',
            'message_type',
            'error_code',
            'from_date_time',
            'to_date_time',
            'campaign_id',
            'sort',
            'page_token',
            'limit',
            'limit_total_count'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params and _key != "_host_index":
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_messages" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['account_id']:
            _path_params['accountId'] = _params['account_id']


        # process the query parameters
        _query_params = []
        if _params.get('message_id') is not None:  # noqa: E501
            _query_params.append(('messageId', _params['message_id']))

        if _params.get('source_tn') is not None:  # noqa: E501
            _query_params.append(('sourceTn', _params['source_tn']))

        if _params.get('destination_tn') is not None:  # noqa: E501
            _query_params.append(('destinationTn', _params['destination_tn']))

        if _params.get('message_status') is not None:  # noqa: E501
            _query_params.append(('messageStatus', _params['message_status'].value))

        if _params.get('message_direction') is not None:  # noqa: E501
            _query_params.append(('messageDirection', _params['message_direction'].value))

        if _params.get('carrier_name') is not None:  # noqa: E501
            _query_params.append(('carrierName', _params['carrier_name']))

        if _params.get('message_type') is not None:  # noqa: E501
            _query_params.append(('messageType', _params['message_type'].value))

        if _params.get('error_code') is not None:  # noqa: E501
            _query_params.append(('errorCode', _params['error_code']))

        if _params.get('from_date_time') is not None:  # noqa: E501
            _query_params.append(('fromDateTime', _params['from_date_time']))

        if _params.get('to_date_time') is not None:  # noqa: E501
            _query_params.append(('toDateTime', _params['to_date_time']))

        if _params.get('campaign_id') is not None:  # noqa: E501
            _query_params.append(('campaignId', _params['campaign_id']))

        if _params.get('sort') is not None:  # noqa: E501
            _query_params.append(('sort', _params['sort']))

        if _params.get('page_token') is not None:  # noqa: E501
            _query_params.append(('pageToken', _params['page_token']))

        if _params.get('limit') is not None:  # noqa: E501
            _query_params.append(('limit', _params['limit']))

        if _params.get('limit_total_count') is not None:  # noqa: E501
            _query_params.append(('limitTotalCount', _params['limit_total_count']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['Basic']  # noqa: E501

        _response_types_map = {
            '200': "MessagesList",
            '400': "MessagingRequestError",
            '401': "MessagingRequestError",
            '403': "MessagingRequestError",
            '404': "MessagingRequestError",
            '415': "MessagingRequestError",
            '429': "MessagingRequestError",
            '500': "MessagingRequestError",
        }

        return self.api_client.call_api(
            '/users/{accountId}/messages', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            _host=_host,
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))