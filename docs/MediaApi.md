# bandwidth.MediaApi

All URIs are relative to *https://messaging.bandwidth.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_media**](MediaApi.md#delete_media) | **DELETE** /users/{accountId}/media/{mediaId} | Delete Media
[**get_media**](MediaApi.md#get_media) | **GET** /users/{accountId}/media/{mediaId} | Get Media
[**list_media**](MediaApi.md#list_media) | **GET** /users/{accountId}/media | List Media
[**upload_media**](MediaApi.md#upload_media) | **PUT** /users/{accountId}/media/{mediaId} | Upload Media


# **delete_media**
> delete_media(account_id, media_id)

Delete Media

Deletes a media file from Bandwidth API server. Make sure you don't have any application scripts still using the media before you delete. If you accidentally delete a media file, you can immediately upload a new file with the same name.

### Example

* Basic Authentication (httpBasic):

```python
import time
import bandwidth
from bandwidth.api import media_api
from bandwidth.model.messaging_exception import MessagingException
from pprint import pprint
# Defining the host is optional and defaults to https://messaging.bandwidth.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = bandwidth.Configuration(
    host = "https://messaging.bandwidth.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: httpBasic
configuration = bandwidth.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with bandwidth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = media_api.MediaApi(api_client)
    account_id = "900000" # str | User's account ID
    media_id = "tjdla-4562ld" # str | The media ID to delete

    # example passing only required values which don't have defaults set
    try:
        # Delete Media
        api_instance.delete_media(account_id, media_id)
    except bandwidth.ApiException as e:
        print("Exception when calling MediaApi->delete_media: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| User&#39;s account ID |
 **media_id** | **str**| The media ID to delete |

### Return type

void (empty response body)

### Authorization

[httpBasic](../README.md#httpBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | successful operation |  -  |
**400** | 400 Request is malformed or invalid |  -  |
**401** | 401 The specified user does not have access to the account |  -  |
**403** | 403 The user does not have access to this API |  -  |
**404** | 404 Path not found |  -  |
**415** | 415 The content-type of the request is incorrect |  -  |
**429** | 429 The rate limit has been reached |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_media**
> file_type get_media(account_id, media_id)

Get Media

Downloads a media file you previously uploaded.

### Example

* Basic Authentication (httpBasic):

```python
import time
import bandwidth
from bandwidth.api import media_api
from bandwidth.model.messaging_exception import MessagingException
from pprint import pprint
# Defining the host is optional and defaults to https://messaging.bandwidth.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = bandwidth.Configuration(
    host = "https://messaging.bandwidth.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: httpBasic
configuration = bandwidth.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with bandwidth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = media_api.MediaApi(api_client)
    account_id = "900000" # str | User's account ID
    media_id = "0a610655-ba58" # str | Media ID to retrieve

    # example passing only required values which don't have defaults set
    try:
        # Get Media
        api_response = api_instance.get_media(account_id, media_id)
        pprint(api_response)
    except bandwidth.ApiException as e:
        print("Exception when calling MediaApi->get_media: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| User&#39;s account ID |
 **media_id** | **str**| Media ID to retrieve |

### Return type

**file_type**

### Authorization

[httpBasic](../README.md#httpBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | 400 Request is malformed or invalid |  -  |
**401** | 401 The specified user does not have access to the account |  -  |
**403** | 403 The user does not have access to this API |  -  |
**404** | 404 Path not found |  -  |
**415** | 415 The content-type of the request is incorrect |  -  |
**429** | 429 The rate limit has been reached |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_media**
> [Media] list_media(account_id)

List Media

Gets a list of your media files. No query parameters are supported.

### Example

* Basic Authentication (httpBasic):

```python
import time
import bandwidth
from bandwidth.api import media_api
from bandwidth.model.messaging_exception import MessagingException
from bandwidth.model.media import Media
from pprint import pprint
# Defining the host is optional and defaults to https://messaging.bandwidth.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = bandwidth.Configuration(
    host = "https://messaging.bandwidth.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: httpBasic
configuration = bandwidth.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with bandwidth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = media_api.MediaApi(api_client)
    account_id = "900000" # str | User's account ID
    continuation_token = "12345" # str | Continuation token used to retrieve subsequent media. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Media
        api_response = api_instance.list_media(account_id)
        pprint(api_response)
    except bandwidth.ApiException as e:
        print("Exception when calling MediaApi->list_media: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Media
        api_response = api_instance.list_media(account_id, continuation_token=continuation_token)
        pprint(api_response)
    except bandwidth.ApiException as e:
        print("Exception when calling MediaApi->list_media: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| User&#39;s account ID |
 **continuation_token** | **str**| Continuation token used to retrieve subsequent media. | [optional]

### Return type

[**[Media]**](Media.md)

### Authorization

[httpBasic](../README.md#httpBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  * Continuation-Token - Continuation token used to retrieve subsequent media. <br>  |
**400** | 400 Request is malformed or invalid |  -  |
**401** | 401 The specified user does not have access to the account |  -  |
**403** | 403 The user does not have access to this API |  -  |
**404** | 404 Path not found |  -  |
**415** | 415 The content-type of the request is incorrect |  -  |
**429** | 429 The rate limit has been reached |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_media**
> upload_media(account_id, media_id, body)

Upload Media

Uploads a file the normal HTTP way. You may add headers to the request in order to provide some control to your media-file.

### Example

* Basic Authentication (httpBasic):

```python
import time
import bandwidth
from bandwidth.api import media_api
from bandwidth.model.messaging_exception import MessagingException
from pprint import pprint
# Defining the host is optional and defaults to https://messaging.bandwidth.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = bandwidth.Configuration(
    host = "https://messaging.bandwidth.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: httpBasic
configuration = bandwidth.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with bandwidth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = media_api.MediaApi(api_client)
    account_id = "900000" # str | User's account ID
    media_id = "my-media-id" # str | The user supplied custom media ID
    body = open('/path/to/file', 'rb') # file_type | 
    content_type = "audio/wav" # str | The media type of the entity-body (optional)
    cache_control = "no-cache" # str | General-header field is used to specify directives that MUST be obeyed by all caching mechanisms along the request/response chain. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Upload Media
        api_instance.upload_media(account_id, media_id, body)
    except bandwidth.ApiException as e:
        print("Exception when calling MediaApi->upload_media: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Upload Media
        api_instance.upload_media(account_id, media_id, body, content_type=content_type, cache_control=cache_control)
    except bandwidth.ApiException as e:
        print("Exception when calling MediaApi->upload_media: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| User&#39;s account ID |
 **media_id** | **str**| The user supplied custom media ID |
 **body** | **file_type**|  |
 **content_type** | **str**| The media type of the entity-body | [optional]
 **cache_control** | **str**| General-header field is used to specify directives that MUST be obeyed by all caching mechanisms along the request/response chain. | [optional]

### Return type

void (empty response body)

### Authorization

[httpBasic](../README.md#httpBasic)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | successful operation |  -  |
**400** | 400 Request is malformed or invalid |  -  |
**401** | 401 The specified user does not have access to the account |  -  |
**403** | 403 The user does not have access to this API |  -  |
**404** | 404 Path not found |  -  |
**415** | 415 The content-type of the request is incorrect |  -  |
**429** | 429 The rate limit has been reached |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

