# bandwidth.MediaApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_media**](MediaApi.md#delete_media) | **DELETE** /users/{accountId}/media/{mediaId} | Delete Media
[**get_media**](MediaApi.md#get_media) | **GET** /users/{accountId}/media/{mediaId} | Get Media
[**list_media**](MediaApi.md#list_media) | **GET** /users/{accountId}/media | List Media
[**upload_media**](MediaApi.md#upload_media) | **PUT** /users/{accountId}/media/{mediaId} | Upload Media


# **delete_media**
> delete_media(account_id, media_id)

Delete Media

Deletes a media file from Bandwidth API server. Make sure you don't have any application scripts still using the media before you delete.  If you accidentally delete a media file you can immediately upload a new file with the same name.

### Example

* Basic Authentication (Basic):

```python
import bandwidth
from bandwidth.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bandwidth.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = bandwidth.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with bandwidth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bandwidth.MediaApi(api_client)
    account_id = '9900000' # str | Your Bandwidth Account ID.
    media_id = '14762070468292kw2fuqty55yp2b2/0/bw.png' # str | Media ID to retrieve.

    try:
        # Delete Media
        api_instance.delete_media(account_id, media_id)
    except Exception as e:
        print("Exception when calling MediaApi->delete_media: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Your Bandwidth Account ID. | 
 **media_id** | **str**| Media ID to retrieve. | 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**406** | Not Acceptable |  -  |
**415** | Unsupported Media Type |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_media**
> bytearray get_media(account_id, media_id)

Get Media

Downloads a media file you previously uploaded.

### Example

* Basic Authentication (Basic):

```python
import bandwidth
from bandwidth.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bandwidth.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = bandwidth.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with bandwidth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bandwidth.MediaApi(api_client)
    account_id = '9900000' # str | Your Bandwidth Account ID.
    media_id = '14762070468292kw2fuqty55yp2b2/0/bw.png' # str | Media ID to retrieve.

    try:
        # Get Media
        api_response = api_instance.get_media(account_id, media_id)
        print("The response of MediaApi->get_media:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaApi->get_media: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Your Bandwidth Account ID. | 
 **media_id** | **str**| Media ID to retrieve. | 

### Return type

**bytearray**

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**406** | Not Acceptable |  -  |
**415** | Unsupported Media Type |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_media**
> List[Media] list_media(account_id, continuation_token=continuation_token)

List Media

Gets a list of your media files. No query parameters are supported.

### Example

* Basic Authentication (Basic):

```python
import bandwidth
from bandwidth.models.media import Media
from bandwidth.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bandwidth.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = bandwidth.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with bandwidth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bandwidth.MediaApi(api_client)
    account_id = '9900000' # str | Your Bandwidth Account ID.
    continuation_token = '1XEi2tsFtLo1JbtLwETnM1ZJ+PqAa8w6ENvC5QKvwyrCDYII663Gy5M4s40owR1tjkuWUif6qbWvFtQJR5/ipqbUnfAqL254LKNlPy6tATCzioKSuHuOqgzloDkSwRtX0LtcL2otHS69hK343m+SjdL+vlj71tT39' # str | Continuation token used to retrieve subsequent media. (optional)

    try:
        # List Media
        api_response = api_instance.list_media(account_id, continuation_token=continuation_token)
        print("The response of MediaApi->list_media:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaApi->list_media: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Your Bandwidth Account ID. | 
 **continuation_token** | **str**| Continuation token used to retrieve subsequent media. | [optional] 

### Return type

[**List[Media]**](Media.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Continuation-Token - Continuation token used to retrieve subsequent media. <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**406** | Not Acceptable |  -  |
**415** | Unsupported Media Type |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_media**
> upload_media(account_id, media_id, body, content_type=content_type, cache_control=cache_control)

Upload Media

Upload a file. You may add headers to the request in order to provide some control to your media file.  If a file is uploaded with the same name as a file that already exists under this account, the previous file will be overwritten.  A list of supported media types can be found [here](https://support.bandwidth.com/hc/en-us/articles/360014128994-What-MMS-file-types-are-supported-).

### Example

* Basic Authentication (Basic):

```python
import bandwidth
from bandwidth.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bandwidth.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = bandwidth.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with bandwidth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bandwidth.MediaApi(api_client)
    account_id = '9900000' # str | Your Bandwidth Account ID.
    media_id = '14762070468292kw2fuqty55yp2b2/0/bw.png' # str | Media ID to retrieve.
    body = None # bytearray | 
    content_type = 'audio/wav' # str | The media type of the entity-body. (optional)
    cache_control = 'no-cache' # str | General-header field is used to specify directives that MUST be obeyed by all caching mechanisms along the request/response chain.  (optional)

    try:
        # Upload Media
        api_instance.upload_media(account_id, media_id, body, content_type=content_type, cache_control=cache_control)
    except Exception as e:
        print("Exception when calling MediaApi->upload_media: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Your Bandwidth Account ID. | 
 **media_id** | **str**| Media ID to retrieve. | 
 **body** | **bytearray**|  | 
 **content_type** | **str**| The media type of the entity-body. | [optional] 
 **cache_control** | **str**| General-header field is used to specify directives that MUST be obeyed by all caching mechanisms along the request/response chain.  | [optional] 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json, application/ogg, application/pdf, application/rtf, application/zip, application/x-tar, application/xml, application/gzip, application/x-bzip2, application/x-gzip, application/smil, application/javascript, audio/mp4, audio/mpeg, audio/ogg, audio/flac, audio/webm, audio/wav, audio/amr, audio/3gpp, image/bmp, image/gif, image/heic, image/heif, image/jpeg, image/pjpeg, image/png, image/svg+xml, image/tiff, image/webp, image/x-icon, text/css, text/csv, text/calendar, text/html, text/plain, text/javascript, text/vcard, text/vnd.wap.wml, text/xml, video/avi, video/mp4, video/mpeg, video/ogg, video/quicktime, video/webm, video/x-ms-wmv, video/x-flv
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**406** | Not Acceptable |  -  |
**415** | Unsupported Media Type |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

