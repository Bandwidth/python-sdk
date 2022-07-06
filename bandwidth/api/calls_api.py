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
from bandwidth.model.call_state import CallState
from bandwidth.model.create_call import CreateCall
from bandwidth.model.create_call_response import CreateCallResponse
from bandwidth.model.update_call import UpdateCall
from bandwidth.model.voice_api_error import VoiceApiError


class CallsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_call_endpoint = _Endpoint(
            settings={
                'response_type': (CreateCallResponse,),
                'auth': [
                    'Basic'
                ],
                'endpoint_path': '/accounts/{accountId}/calls',
                'operation_id': 'create_call',
                'http_method': 'POST',
                'servers': [
                    {
                        'url': "https://voice.bandwidth.com/api/v2",
                        'description': "Production",
                    },
                ]
            },
            params_map={
                'all': [
                    'account_id',
                    'create_call',
                ],
                'required': [
                    'account_id',
                    'create_call',
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
                    'create_call':
                        (CreateCall,),
                },
                'attribute_map': {
                    'account_id': 'accountId',
                },
                'location_map': {
                    'account_id': 'path',
                    'create_call': 'body',
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
        self.get_call_state_endpoint = _Endpoint(
            settings={
                'response_type': (CallState,),
                'auth': [
                    'Basic'
                ],
                'endpoint_path': '/accounts/{accountId}/calls/{callId}',
                'operation_id': 'get_call_state',
                'http_method': 'GET',
                'servers': [
                    {
                        'url': "https://voice.bandwidth.com/api/v2",
                        'description': "Production",
                    },
                ]
            },
            params_map={
                'all': [
                    'account_id',
                    'call_id',
                ],
                'required': [
                    'account_id',
                    'call_id',
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
                    'call_id':
                        (str,),
                },
                'attribute_map': {
                    'account_id': 'accountId',
                    'call_id': 'callId',
                },
                'location_map': {
                    'account_id': 'path',
                    'call_id': 'path',
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
        self.update_call_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'Basic'
                ],
                'endpoint_path': '/accounts/{accountId}/calls/{callId}',
                'operation_id': 'update_call',
                'http_method': 'POST',
                'servers': [
                    {
                        'url': "https://voice.bandwidth.com/api/v2",
                        'description': "Production",
                    },
                ]
            },
            params_map={
                'all': [
                    'account_id',
                    'call_id',
                    'update_call',
                ],
                'required': [
                    'account_id',
                    'call_id',
                    'update_call',
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
                    'call_id':
                        (str,),
                    'update_call':
                        (UpdateCall,),
                },
                'attribute_map': {
                    'account_id': 'accountId',
                    'call_id': 'callId',
                },
                'location_map': {
                    'account_id': 'path',
                    'call_id': 'path',
                    'update_call': 'body',
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
        self.update_call_bxml_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'Basic'
                ],
                'endpoint_path': '/accounts/{accountId}/calls/{callId}/bxml',
                'operation_id': 'update_call_bxml',
                'http_method': 'PUT',
                'servers': [
                    {
                        'url': "https://voice.bandwidth.com/api/v2",
                        'description': "Production",
                    },
                ]
            },
            params_map={
                'all': [
                    'account_id',
                    'call_id',
                    'body',
                ],
                'required': [
                    'account_id',
                    'call_id',
                    'body',
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
                    'call_id':
                        (str,),
                    'body':
                        (str,),
                },
                'attribute_map': {
                    'account_id': 'accountId',
                    'call_id': 'callId',
                },
                'location_map': {
                    'account_id': 'path',
                    'call_id': 'path',
                    'body': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/xml'
                ]
            },
            api_client=api_client
        )

    def create_call(
        self,
        account_id,
        create_call,
        **kwargs
    ):
        """Create Call  # noqa: E501

        Creates an outbound phone call.  All calls are initially queued. Your outbound calls will initiated at a specific dequeueing rate, enabling your application to \"fire and forget\" when creating calls. Queued calls may not be modified until they are dequeued and placed, but may be removed from your queue on demand.  <b>Please note:</b> Calls submitted to your queue will be placed approximately in order, but exact ordering is not guaranteed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_call(account_id, create_call, async_req=True)
        >>> result = thread.get()

        Args:
            account_id (str): Your Bandwidth Account ID
            create_call (CreateCall): JSON object containing information to create an outbound call

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
            CreateCallResponse
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
        kwargs['create_call'] = \
            create_call
        return self.create_call_endpoint.call_with_http_info(**kwargs)

    def get_call_state(
        self,
        account_id,
        call_id,
        **kwargs
    ):
        """Get Call State Information  # noqa: E501

        Retrieve the current state of a specific call. This information is near-realtime, so it may take a few minutes for your call to be accessible using this endpoint.  **Note**: Call information is kept for 7 days after the calls are hung up. If you attempt to retrieve information for a call that is older than 7 days, you will get an HTTP 404 response.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_call_state(account_id, call_id, async_req=True)
        >>> result = thread.get()

        Args:
            account_id (str): Your Bandwidth Account ID
            call_id (str): Programmable Voice API Call ID

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
            CallState
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
        kwargs['call_id'] = \
            call_id
        return self.get_call_state_endpoint.call_with_http_info(**kwargs)

    def update_call(
        self,
        account_id,
        call_id,
        update_call,
        **kwargs
    ):
        """Update Call  # noqa: E501

        Interrupts and redirects a call to a different URL that should return a BXML document.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_call(account_id, call_id, update_call, async_req=True)
        >>> result = thread.get()

        Args:
            account_id (str): Your Bandwidth Account ID
            call_id (str): Programmable Voice API Call ID
            update_call (UpdateCall): JSON object containing information to redirect an existing call to a new BXML document

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
            None
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
        kwargs['call_id'] = \
            call_id
        kwargs['update_call'] = \
            update_call
        return self.update_call_endpoint.call_with_http_info(**kwargs)

    def update_call_bxml(
        self,
        account_id,
        call_id,
        body,
        **kwargs
    ):
        """Update Call BXML  # noqa: E501

        Interrupts and replaces an active call's BXML document.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_call_bxml(account_id, call_id, body, async_req=True)
        >>> result = thread.get()

        Args:
            account_id (str): Your Bandwidth Account ID
            call_id (str): Programmable Voice API Call ID
            body (str):

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
            None
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
        kwargs['call_id'] = \
            call_id
        kwargs['body'] = \
            body
        return self.update_call_bxml_endpoint.call_with_http_info(**kwargs)

