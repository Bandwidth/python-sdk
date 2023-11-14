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

from pydantic import Field, StrictStr

from bandwidth.models.create_lookup_response import CreateLookupResponse
from bandwidth.models.lookup_request import LookupRequest
from bandwidth.models.lookup_status import LookupStatus

from bandwidth.api_client import ApiClient
from bandwidth.api_response import ApiResponse
from bandwidth.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class PhoneNumberLookupApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def create_lookup(self, account_id : Annotated[StrictStr, Field(..., description="Your Bandwidth Account ID.")], lookup_request : Annotated[LookupRequest, Field(..., description="Phone number lookup request.")], **kwargs) -> CreateLookupResponse:  # noqa: E501
        """Create Lookup  # noqa: E501

        Create a Phone Number Lookup Request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_lookup(account_id, lookup_request, async_req=True)
        >>> result = thread.get()

        :param account_id: Your Bandwidth Account ID. (required)
        :type account_id: str
        :param lookup_request: Phone number lookup request. (required)
        :type lookup_request: LookupRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CreateLookupResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the create_lookup_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.create_lookup_with_http_info(account_id, lookup_request, **kwargs)  # noqa: E501

    @validate_arguments
    def create_lookup_with_http_info(self, account_id : Annotated[StrictStr, Field(..., description="Your Bandwidth Account ID.")], lookup_request : Annotated[LookupRequest, Field(..., description="Phone number lookup request.")], **kwargs) -> ApiResponse:  # noqa: E501
        """Create Lookup  # noqa: E501

        Create a Phone Number Lookup Request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_lookup_with_http_info(account_id, lookup_request, async_req=True)
        >>> result = thread.get()

        :param account_id: Your Bandwidth Account ID. (required)
        :type account_id: str
        :param lookup_request: Phone number lookup request. (required)
        :type lookup_request: LookupRequest
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
        :rtype: tuple(CreateLookupResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _hosts = [
            'https://numbers.bandwidth.com/api/v1'
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
            'lookup_request'
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
                    " to method create_lookup" % _key
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
        if _params['lookup_request'] is not None:
            _body_params = _params['lookup_request']

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
            '202': "CreateLookupResponse",
            '400': "TnLookupRequestError",
            '401': "TnLookupRequestError",
            '403': "TnLookupRequestError",
            '415': "TnLookupRequestError",
            '429': "TnLookupRequestError",
            '500': "TnLookupRequestError",
        }

        return self.api_client.call_api(
            '/accounts/{accountId}/tnlookup', 'POST',
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
    def get_lookup_status(self, account_id : Annotated[StrictStr, Field(..., description="Your Bandwidth Account ID.")], request_id : Annotated[StrictStr, Field(..., description="The phone number lookup request ID from Bandwidth.")], **kwargs) -> LookupStatus:  # noqa: E501
        """Get Lookup Request Status  # noqa: E501

        Get an existing Phone Number Lookup Request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_lookup_status(account_id, request_id, async_req=True)
        >>> result = thread.get()

        :param account_id: Your Bandwidth Account ID. (required)
        :type account_id: str
        :param request_id: The phone number lookup request ID from Bandwidth. (required)
        :type request_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: LookupStatus
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_lookup_status_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_lookup_status_with_http_info(account_id, request_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_lookup_status_with_http_info(self, account_id : Annotated[StrictStr, Field(..., description="Your Bandwidth Account ID.")], request_id : Annotated[StrictStr, Field(..., description="The phone number lookup request ID from Bandwidth.")], **kwargs) -> ApiResponse:  # noqa: E501
        """Get Lookup Request Status  # noqa: E501

        Get an existing Phone Number Lookup Request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_lookup_status_with_http_info(account_id, request_id, async_req=True)
        >>> result = thread.get()

        :param account_id: Your Bandwidth Account ID. (required)
        :type account_id: str
        :param request_id: The phone number lookup request ID from Bandwidth. (required)
        :type request_id: str
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
        :rtype: tuple(LookupStatus, status_code(int), headers(HTTPHeaderDict))
        """

        _hosts = [
            'https://numbers.bandwidth.com/api/v1'
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
            'request_id'
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
                    " to method get_lookup_status" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['account_id']:
            _path_params['accountId'] = _params['account_id']

        if _params['request_id']:
            _path_params['requestId'] = _params['request_id']


        # process the query parameters
        _query_params = []
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
            '200': "LookupStatus",
            '400': "TnLookupRequestError",
            '401': "TnLookupRequestError",
            '403': "TnLookupRequestError",
            '404': None,
            '429': "TnLookupRequestError",
            '500': "TnLookupRequestError",
        }

        return self.api_client.call_api(
            '/accounts/{accountId}/tnlookup/{requestId}', 'GET',
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