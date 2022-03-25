"""
    Messaging

    Test Bandwidth's HTTP Messaging platform ## Base Path <code>https://messaging.bandwidth.com/api/v2</code>  # noqa: E501

    The version of the OpenAPI document: 4.2.8
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
from bandwidth.model.error_with_request import ErrorWithRequest
from bandwidth.model.forbidden_request import ForbiddenRequest
from bandwidth.model.two_factor_code_request_schema import TwoFactorCodeRequestSchema
from bandwidth.model.two_factor_messaging_response import TwoFactorMessagingResponse
from bandwidth.model.two_factor_verify_code_response import TwoFactorVerifyCodeResponse
from bandwidth.model.two_factor_verify_request_schema import TwoFactorVerifyRequestSchema
from bandwidth.model.two_factor_voice_response import TwoFactorVoiceResponse
from bandwidth.model.unauthorized_request import UnauthorizedRequest


class MFAApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.messaging_two_factor_endpoint = _Endpoint(
            settings={
                'response_type': (TwoFactorMessagingResponse,),
                'auth': [
                    'httpBasic'
                ],
                'endpoint_path': '/accounts/{accountId}/code/messaging',
                'operation_id': 'messaging_two_factor',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'account_id',
                    'two_factor_code_request_schema',
                ],
                'required': [
                    'account_id',
                    'two_factor_code_request_schema',
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
                    'two_factor_code_request_schema':
                        (TwoFactorCodeRequestSchema,),
                },
                'attribute_map': {
                    'account_id': 'accountId',
                },
                'location_map': {
                    'account_id': 'path',
                    'two_factor_code_request_schema': 'body',
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
        self.verify_two_factor_endpoint = _Endpoint(
            settings={
                'response_type': (TwoFactorVerifyCodeResponse,),
                'auth': [
                    'httpBasic'
                ],
                'endpoint_path': '/accounts/{accountId}/code/verify',
                'operation_id': 'verify_two_factor',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'account_id',
                    'two_factor_verify_request_schema',
                ],
                'required': [
                    'account_id',
                    'two_factor_verify_request_schema',
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
                    'two_factor_verify_request_schema':
                        (TwoFactorVerifyRequestSchema,),
                },
                'attribute_map': {
                    'account_id': 'accountId',
                },
                'location_map': {
                    'account_id': 'path',
                    'two_factor_verify_request_schema': 'body',
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
        self.voice_two_factor_endpoint = _Endpoint(
            settings={
                'response_type': (TwoFactorVoiceResponse,),
                'auth': [
                    'httpBasic'
                ],
                'endpoint_path': '/accounts/{accountId}/code/voice',
                'operation_id': 'voice_two_factor',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'account_id',
                    'two_factor_code_request_schema',
                ],
                'required': [
                    'account_id',
                    'two_factor_code_request_schema',
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
                    'two_factor_code_request_schema':
                        (TwoFactorCodeRequestSchema,),
                },
                'attribute_map': {
                    'account_id': 'accountId',
                },
                'location_map': {
                    'account_id': 'path',
                    'two_factor_code_request_schema': 'body',
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

    def messaging_two_factor(
        self,
        account_id,
        two_factor_code_request_schema,
        **kwargs
    ):
        """Messaging Authentication  # noqa: E501

        Multi-Factor authentication with Bandwidth Messaging services. Allows a user to send an MFA code via a text message (SMS).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.messaging_two_factor(account_id, two_factor_code_request_schema, async_req=True)
        >>> result = thread.get()

        Args:
            account_id (str): Bandwidth Account ID with Messaging service enabled
            two_factor_code_request_schema (TwoFactorCodeRequestSchema):

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
            async_req (bool): execute request asynchronously

        Returns:
            TwoFactorMessagingResponse
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
        kwargs['account_id'] = \
            account_id
        kwargs['two_factor_code_request_schema'] = \
            two_factor_code_request_schema
        return self.messaging_two_factor_endpoint.call_with_http_info(**kwargs)

    def verify_two_factor(
        self,
        account_id,
        two_factor_verify_request_schema,
        **kwargs
    ):
        """Verify Authentication Code  # noqa: E501

        Allows a user to verify an MFA code.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.verify_two_factor(account_id, two_factor_verify_request_schema, async_req=True)
        >>> result = thread.get()

        Args:
            account_id (str): Bandwidth Account ID with Two-Factor enabled
            two_factor_verify_request_schema (TwoFactorVerifyRequestSchema):

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
            async_req (bool): execute request asynchronously

        Returns:
            TwoFactorVerifyCodeResponse
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
        kwargs['account_id'] = \
            account_id
        kwargs['two_factor_verify_request_schema'] = \
            two_factor_verify_request_schema
        return self.verify_two_factor_endpoint.call_with_http_info(**kwargs)

    def voice_two_factor(
        self,
        account_id,
        two_factor_code_request_schema,
        **kwargs
    ):
        """Voice Authentication  # noqa: E501

        Multi-Factor authentication with Bandwidth Voice services. Allows for a user to send an MFA code via a phone call.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.voice_two_factor(account_id, two_factor_code_request_schema, async_req=True)
        >>> result = thread.get()

        Args:
            account_id (str): Bandwidth Account ID with Voice service enabled
            two_factor_code_request_schema (TwoFactorCodeRequestSchema):

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
            async_req (bool): execute request asynchronously

        Returns:
            TwoFactorVoiceResponse
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
        kwargs['account_id'] = \
            account_id
        kwargs['two_factor_code_request_schema'] = \
            two_factor_code_request_schema
        return self.voice_two_factor_endpoint.call_with_http_info(**kwargs)

