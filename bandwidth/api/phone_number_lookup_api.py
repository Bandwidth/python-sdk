"""
    Bandwidth

    Bandwidth's Communication APIs  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: letstalk@bandwidth.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from bandwidth.api_client import ApiClient, Endpoint as _Endpoint
from bandwidth.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from bandwidth.model.create_lookup_response import CreateLookupResponse
from bandwidth.model.lookup_request import LookupRequest
from bandwidth.model.lookup_status import LookupStatus
from bandwidth.model.tn_lookup_request_error import TnLookupRequestError


class PhoneNumberLookupApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_lookup_endpoint = _Endpoint(
            settings={
                'response_type': (CreateLookupResponse,),
                'auth': [
                    'Basic'
                ],
                'endpoint_path': '/accounts/{accountId}/tnlookup',
                'operation_id': 'create_lookup',
                'http_method': 'POST',
                'servers': [
                    {
                        'url': "https://numbers.bandwidth.com/api/v1",
                        'description': "Production",
                    },
                ]
            },
            params_map={
                'all': [
                    'account_id',
                    'lookup_request',
                ],
                'required': [
                    'account_id',
                    'lookup_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'account_id':
                        (str,),
                    'lookup_request':
                        (LookupRequest,),
                },
                'attribute_map': {
                    'account_id': 'accountId',
                },
                'location_map': {
                    'account_id': 'path',
                    'lookup_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.get_lookup_status_endpoint = _Endpoint(
            settings={
                'response_type': (LookupStatus,),
                'auth': [
                    'Basic'
                ],
                'endpoint_path': '/accounts/{accountId}/tnlookup/{requestId}',
                'operation_id': 'get_lookup_status',
                'http_method': 'GET',
                'servers': [
                    {
                        'url': "https://numbers.bandwidth.com/api/v1",
                        'description': "Production",
                    },
                ]
            },
            params_map={
                'all': [
                    'account_id',
                    'request_id',
                ],
                'required': [
                    'account_id',
                    'request_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'account_id':
                        (str,),
                    'request_id':
                        (str,),
                },
                'attribute_map': {
                    'account_id': 'accountId',
                    'request_id': 'requestId',
                },
                'location_map': {
                    'account_id': 'path',
                    'request_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def create_lookup(
        self,
        account_id,
        lookup_request,
        **kwargs
    ):
        """Create Lookup  # noqa: E501

        Create a Phone Number Lookup Request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_lookup(account_id, lookup_request, async_req=True)
        >>> result = thread.get()

        Args:
            account_id (str): The ID of the Bandwidth account that the user belongs to.
            lookup_request (LookupRequest): Phone number lookup request.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            CreateLookupResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['account_id'] = \
            account_id
        kwargs['lookup_request'] = \
            lookup_request
        return self.create_lookup_endpoint.call_with_http_info(**kwargs)

    def get_lookup_status(
        self,
        account_id,
        request_id,
        **kwargs
    ):
        """Get Lookup Request Status  # noqa: E501

        Get an existing Phone Number Lookup Request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_lookup_status(account_id, request_id, async_req=True)
        >>> result = thread.get()

        Args:
            account_id (str): The ID of the Bandwidth account that the user belongs to.
            request_id (str): The phone number lookup request ID from Bandwidth.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            LookupStatus
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['account_id'] = \
            account_id
        kwargs['request_id'] = \
            request_id
        return self.get_lookup_status_endpoint.call_with_http_info(**kwargs)

