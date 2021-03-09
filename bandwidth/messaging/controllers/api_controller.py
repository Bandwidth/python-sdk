# -*- coding: utf-8 -*-

"""
bandwidth

This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from bandwidth.api_helper import APIHelper
from bandwidth.configuration import Server
from bandwidth.http.api_response import ApiResponse
from bandwidth.utilities.file_wrapper import FileWrapper
from bandwidth.messaging.controllers.base_controller import BaseController
from bandwidth.http.auth.messaging_basic_auth import MessagingBasicAuth
from bandwidth.messaging.models.media import Media
from bandwidth.messaging.models.bandwidth_messages_list import BandwidthMessagesList
from bandwidth.messaging.models.bandwidth_message import BandwidthMessage
from bandwidth.messaging.exceptions.messaging_exception import MessagingException


class APIController(BaseController):

    """A Controller to access Endpoints in the bandwidth API."""

    def __init__(self, config, call_back=None):
        super(APIController, self).__init__(config, call_back)

    def list_media(self,
                   user_id,
                   continuation_token=None):
        """Does a GET request to /users/{userId}/media.

        listMedia

        Args:
            user_id (string): User's account ID
            continuation_token (string, optional): Continuation token used to
                retrieve subsequent media.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers.
                successful operation

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/users/{userId}/media'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'userId': {'value': user_id, 'encode': False}
        })
        _query_builder = self.config.get_base_uri(Server.MESSAGINGDEFAULT)
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'Continuation-Token': continuation_token
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        MessagingBasicAuth.apply(self.config, _request)
        _response = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _response.status_code == 400:
            raise MessagingException('400 Request is malformed or invalid', _response)
        elif _response.status_code == 401:
            raise MessagingException('401 The specified user does not have access to the account', _response)
        elif _response.status_code == 403:
            raise MessagingException('403 The user does not have access to this API', _response)
        elif _response.status_code == 404:
            raise MessagingException('404 Path not found', _response)
        elif _response.status_code == 415:
            raise MessagingException('415 The content-type of the request is incorrect', _response)
        elif _response.status_code == 429:
            raise MessagingException('429 The rate limit has been reached', _response)
        self.validate_response(_response)

        decoded = APIHelper.json_deserialize(_response.text, Media.from_dictionary)
        _result = ApiResponse(_response, body=decoded)
        return _result

    def get_media(self,
                  user_id,
                  media_id):
        """Does a GET request to /users/{userId}/media/{mediaId}.

        getMedia

        Args:
            user_id (string): User's account ID
            media_id (string): Media ID to retrieve

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers.
                successful operation

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/users/{userId}/media/{mediaId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'userId': {'value': user_id, 'encode': False},
            'mediaId': {'value': media_id, 'encode': False}
        })
        _query_builder = self.config.get_base_uri(Server.MESSAGINGDEFAULT)
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url)
        MessagingBasicAuth.apply(self.config, _request)
        _response = self.execute_request(_request, binary=True)

        # Endpoint and global error handling using HTTP status codes.
        if _response.status_code == 400:
            raise MessagingException('400 Request is malformed or invalid', _response)
        elif _response.status_code == 401:
            raise MessagingException('401 The specified user does not have access to the account', _response)
        elif _response.status_code == 403:
            raise MessagingException('403 The user does not have access to this API', _response)
        elif _response.status_code == 404:
            raise MessagingException('404 Path not found', _response)
        elif _response.status_code == 415:
            raise MessagingException('415 The content-type of the request is incorrect', _response)
        elif _response.status_code == 429:
            raise MessagingException('429 The rate limit has been reached', _response)
        self.validate_response(_response)

        decoded = _response.text
        _result = ApiResponse(_response, body=decoded)
        return _result

    def upload_media(self,
                     user_id,
                     media_id,
                     content_length,
                     body,
                     content_type='application/octet-stream',
                     cache_control=None):
        """Does a PUT request to /users/{userId}/media/{mediaId}.

        uploadMedia

        Args:
            user_id (string): User's account ID
            media_id (string): The user supplied custom media ID
            content_length (long|int): The size of the entity-body
            body (typing.BinaryIO): TODO: type description here.
            content_type (string, optional): The media type of the
                entity-body
            cache_control (string, optional): General-header field is used to
                specify directives that MUST be obeyed by all caching
                mechanisms along the request/response chain.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/users/{userId}/media/{mediaId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'userId': {'value': user_id, 'encode': False},
            'mediaId': {'value': media_id, 'encode': False}
        })
        _query_builder = self.config.get_base_uri(Server.MESSAGINGDEFAULT)
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        if isinstance(body, FileWrapper):
            body_wrapper = body.file_stream
            body_content_type = body.content_type
        else:
            body_wrapper = body
            body_content_type = content_type

        # Prepare headers
        _headers = {
            'content-type': body_content_type,
            'Content-Length': content_length,
            'Cache-Control': cache_control
        }

        # Prepare and execute request
        _request = self.config.http_client.put(_query_url, headers=_headers, parameters=body_wrapper)
        MessagingBasicAuth.apply(self.config, _request)
        _response = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _response.status_code == 400:
            raise MessagingException('400 Request is malformed or invalid', _response)
        elif _response.status_code == 401:
            raise MessagingException('401 The specified user does not have access to the account', _response)
        elif _response.status_code == 403:
            raise MessagingException('403 The user does not have access to this API', _response)
        elif _response.status_code == 404:
            raise MessagingException('404 Path not found', _response)
        elif _response.status_code == 415:
            raise MessagingException('415 The content-type of the request is incorrect', _response)
        elif _response.status_code == 429:
            raise MessagingException('429 The rate limit has been reached', _response)
        self.validate_response(_response)

        # Return appropriate type
        return ApiResponse(_response)

    def delete_media(self,
                     user_id,
                     media_id):
        """Does a DELETE request to /users/{userId}/media/{mediaId}.

        deleteMedia

        Args:
            user_id (string): User's account ID
            media_id (string): The media ID to delete

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/users/{userId}/media/{mediaId}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'userId': {'value': user_id, 'encode': False},
            'mediaId': {'value': media_id, 'encode': False}
        })
        _query_builder = self.config.get_base_uri(Server.MESSAGINGDEFAULT)
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        _request = self.config.http_client.delete(_query_url)
        MessagingBasicAuth.apply(self.config, _request)
        _response = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _response.status_code == 400:
            raise MessagingException('400 Request is malformed or invalid', _response)
        elif _response.status_code == 401:
            raise MessagingException('401 The specified user does not have access to the account', _response)
        elif _response.status_code == 403:
            raise MessagingException('403 The user does not have access to this API', _response)
        elif _response.status_code == 404:
            raise MessagingException('404 Path not found', _response)
        elif _response.status_code == 415:
            raise MessagingException('415 The content-type of the request is incorrect', _response)
        elif _response.status_code == 429:
            raise MessagingException('429 The rate limit has been reached', _response)
        self.validate_response(_response)

        # Return appropriate type
        return ApiResponse(_response)

    def get_messages(self,
                     user_id,
                     message_id=None,
                     source_tn=None,
                     destination_tn=None,
                     message_status=None,
                     error_code=None,
                     from_date_time=None,
                     to_date_time=None,
                     page_token=None,
                     limit=None):
        """Does a GET request to /users/{userId}/messages.

        getMessages

        Args:
            user_id (string): User's account ID
            message_id (string, optional): The ID of the message to search
                for. Special characters need to be encoded using URL encoding
            source_tn (string, optional): The phone number that sent the
                message
            destination_tn (string, optional): The phone number that received
                the message
            message_status (string, optional): The status of the message. One
                of RECEIVED, QUEUED, SENDING, SENT, FAILED, DELIVERED,
                DLR_EXPIRED
            error_code (int, optional): The error code of the message
            from_date_time (string, optional): The start of the date range to
                search in ISO 8601 format. Uses the message receive time. The
                date range to search in is currently 14 days.
            to_date_time (string, optional): The end of the date range to
                search in ISO 8601 format. Uses the message receive time. The
                date range to search in is currently 14 days.
            page_token (string, optional): A base64 encoded value used for
                pagination of results
            limit (int, optional): The maximum records requested in search
                result. Default 100. The sum of limit and after cannot be more
                than 10000

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers.
                successful operation

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/users/{userId}/messages'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'userId': {'value': user_id, 'encode': False}
        })
        _query_builder = self.config.get_base_uri(Server.MESSAGINGDEFAULT)
        _query_builder += _url_path
        _query_parameters = {
            'messageId': message_id,
            'sourceTn': source_tn,
            'destinationTn': destination_tn,
            'messageStatus': message_status,
            'errorCode': error_code,
            'fromDateTime': from_date_time,
            'toDateTime': to_date_time,
            'pageToken': page_token,
            'limit': limit
        }
        _query_builder = APIHelper.append_url_with_query_parameters(
            _query_builder,
            _query_parameters
        )
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        MessagingBasicAuth.apply(self.config, _request)
        _response = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _response.status_code == 400:
            raise MessagingException('400 Request is malformed or invalid', _response)
        elif _response.status_code == 401:
            raise MessagingException('401 The specified user does not have access to the account', _response)
        elif _response.status_code == 403:
            raise MessagingException('403 The user does not have access to this API', _response)
        elif _response.status_code == 404:
            raise MessagingException('404 Path not found', _response)
        elif _response.status_code == 415:
            raise MessagingException('415 The content-type of the request is incorrect', _response)
        elif _response.status_code == 429:
            raise MessagingException('429 The rate limit has been reached', _response)
        self.validate_response(_response)

        decoded = APIHelper.json_deserialize(_response.text, BandwidthMessagesList.from_dictionary)
        _result = ApiResponse(_response, body=decoded)
        return _result

    def create_message(self,
                       user_id,
                       body):
        """Does a POST request to /users/{userId}/messages.

        createMessage

        Args:
            user_id (string): User's account ID
            body (MessageRequest): TODO: type description here.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers.
                successful operation

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/users/{userId}/messages'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'userId': {'value': user_id, 'encode': False}
        })
        _query_builder = self.config.get_base_uri(Server.MESSAGINGDEFAULT)
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        MessagingBasicAuth.apply(self.config, _request)
        _response = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _response.status_code == 400:
            raise MessagingException('400 Request is malformed or invalid', _response)
        elif _response.status_code == 401:
            raise MessagingException('401 The specified user does not have access to the account', _response)
        elif _response.status_code == 403:
            raise MessagingException('403 The user does not have access to this API', _response)
        elif _response.status_code == 404:
            raise MessagingException('404 Path not found', _response)
        elif _response.status_code == 415:
            raise MessagingException('415 The content-type of the request is incorrect', _response)
        elif _response.status_code == 429:
            raise MessagingException('429 The rate limit has been reached', _response)
        self.validate_response(_response)

        decoded = APIHelper.json_deserialize(_response.text, BandwidthMessage.from_dictionary)
        _result = ApiResponse(_response, body=decoded)
        return _result
