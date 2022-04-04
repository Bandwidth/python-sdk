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
from bandwidth.model.media import Media
from bandwidth.model.messaging_exception import MessagingException


class MediaApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.delete_media_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'httpBasic'
                ],
                'endpoint_path': '/users/{accountId}/media/{mediaId}',
                'operation_id': 'delete_media',
                'http_method': 'DELETE',
                'servers': [
                    {
                        'url': "https://messaging.bandwidth.com/api/v2",
                        'description': "No description provided",
                    },
                ]
            },
            params_map={
                'all': [
                    'account_id',
                    'media_id',
                ],
                'required': [
                    'account_id',
                    'media_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'media_id',
                ]
            },
            root_map={
                'validations': {
                    ('media_id',): {

                        'regex': {
                            'pattern': r'.+',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'account_id':
                        (str,),
                    'media_id':
                        (str,),
                },
                'attribute_map': {
                    'account_id': 'accountId',
                    'media_id': 'mediaId',
                },
                'location_map': {
                    'account_id': 'path',
                    'media_id': 'path',
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
        self.get_media_endpoint = _Endpoint(
            settings={
                'response_type': (file_type,),
                'auth': [
                    'httpBasic'
                ],
                'endpoint_path': '/users/{accountId}/media/{mediaId}',
                'operation_id': 'get_media',
                'http_method': 'GET',
                'servers': [
                    {
                        'url': "https://messaging.bandwidth.com/api/v2",
                        'description': "No description provided",
                    },
                ]
            },
            params_map={
                'all': [
                    'account_id',
                    'media_id',
                ],
                'required': [
                    'account_id',
                    'media_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'media_id',
                ]
            },
            root_map={
                'validations': {
                    ('media_id',): {

                        'regex': {
                            'pattern': r'.+',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'account_id':
                        (str,),
                    'media_id':
                        (str,),
                },
                'attribute_map': {
                    'account_id': 'accountId',
                    'media_id': 'mediaId',
                },
                'location_map': {
                    'account_id': 'path',
                    'media_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/octet-stream',
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.list_media_endpoint = _Endpoint(
            settings={
                'response_type': ([Media],),
                'auth': [
                    'httpBasic'
                ],
                'endpoint_path': '/users/{accountId}/media',
                'operation_id': 'list_media',
                'http_method': 'GET',
                'servers': [
                    {
                        'url': "https://messaging.bandwidth.com/api/v2",
                        'description': "No description provided",
                    },
                ]
            },
            params_map={
                'all': [
                    'account_id',
                    'continuation_token',
                ],
                'required': [
                    'account_id',
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
                    'continuation_token':
                        (str,),
                },
                'attribute_map': {
                    'account_id': 'accountId',
                    'continuation_token': 'Continuation-Token',
                },
                'location_map': {
                    'account_id': 'path',
                    'continuation_token': 'header',
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
        self.upload_media_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'httpBasic'
                ],
                'endpoint_path': '/users/{accountId}/media/{mediaId}',
                'operation_id': 'upload_media',
                'http_method': 'PUT',
                'servers': [
                    {
                        'url': "https://messaging.bandwidth.com/api/v2",
                        'description': "No description provided",
                    },
                ]
            },
            params_map={
                'all': [
                    'account_id',
                    'media_id',
                    'body',
                    'content_type',
                    'cache_control',
                ],
                'required': [
                    'account_id',
                    'media_id',
                    'body',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'media_id',
                ]
            },
            root_map={
                'validations': {
                    ('media_id',): {

                        'regex': {
                            'pattern': r'.+',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'account_id':
                        (str,),
                    'media_id':
                        (str,),
                    'body':
                        (file_type,),
                    'content_type':
                        (str,),
                    'cache_control':
                        (str,),
                },
                'attribute_map': {
                    'account_id': 'accountId',
                    'media_id': 'mediaId',
                    'content_type': 'Content-Type',
                    'cache_control': 'Cache-Control',
                },
                'location_map': {
                    'account_id': 'path',
                    'media_id': 'path',
                    'body': 'body',
                    'content_type': 'header',
                    'cache_control': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/octet-stream'
                ]
            },
            api_client=api_client
        )

    def delete_media(
        self,
        account_id,
        media_id,
        **kwargs
    ):
        """Delete Media  # noqa: E501

        Deletes a media file from Bandwidth API server. Make sure you don't have any application scripts still using the media before you delete. If you accidentally delete a media file, you can immediately upload a new file with the same name.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_media(account_id, media_id, async_req=True)
        >>> result = thread.get()

        Args:
            account_id (str): User's account ID
            media_id (str): The media ID to delete

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
        kwargs['account_id'] = \
            account_id
        kwargs['media_id'] = \
            media_id
        return self.delete_media_endpoint.call_with_http_info(**kwargs)

    def get_media(
        self,
        account_id,
        media_id,
        **kwargs
    ):
        """Get Media  # noqa: E501

        Downloads a media file you previously uploaded.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_media(account_id, media_id, async_req=True)
        >>> result = thread.get()

        Args:
            account_id (str): User's account ID
            media_id (str): Media ID to retrieve

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
            file_type
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
        kwargs['media_id'] = \
            media_id
        return self.get_media_endpoint.call_with_http_info(**kwargs)

    def list_media(
        self,
        account_id,
        **kwargs
    ):
        """List Media  # noqa: E501

        Gets a list of your media files. No query parameters are supported.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_media(account_id, async_req=True)
        >>> result = thread.get()

        Args:
            account_id (str): User's account ID

        Keyword Args:
            continuation_token (str): Continuation token used to retrieve subsequent media.. [optional]
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
            [Media]
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
        return self.list_media_endpoint.call_with_http_info(**kwargs)

    def upload_media(
        self,
        account_id,
        media_id,
        body,
        **kwargs
    ):
        """Upload Media  # noqa: E501

        Uploads a file the normal HTTP way. You may add headers to the request in order to provide some control to your media-file.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.upload_media(account_id, media_id, body, async_req=True)
        >>> result = thread.get()

        Args:
            account_id (str): User's account ID
            media_id (str): The user supplied custom media ID
            body (file_type):

        Keyword Args:
            content_type (str): The media type of the entity-body. [optional]
            cache_control (str): General-header field is used to specify directives that MUST be obeyed by all caching mechanisms along the request/response chain.. [optional]
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
        kwargs['account_id'] = \
            account_id
        kwargs['media_id'] = \
            media_id
        kwargs['body'] = \
            body
        return self.upload_media_endpoint.call_with_http_info(**kwargs)

