# bandwidth.TranscriptionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_real_time_transcription**](TranscriptionsApi.md#delete_real_time_transcription) | **DELETE** /accounts/{accountId}/calls/{callId}/transcriptions/{transcriptionId} | Delete Real-time Transcription
[**get_real_time_transcription**](TranscriptionsApi.md#get_real_time_transcription) | **GET** /accounts/{accountId}/calls/{callId}/transcriptions/{transcriptionId} | Get Real-time Transcription
[**list_real_time_transcriptions**](TranscriptionsApi.md#list_real_time_transcriptions) | **GET** /accounts/{accountId}/calls/{callId}/transcriptions | List Real-time Transcriptions


# **delete_real_time_transcription**
> delete_real_time_transcription(account_id, call_id, transcription_id)

Delete Real-time Transcription

Delete the specified transcription that was created on this call via [startTranscription](/docs/voice/bxml/startTranscription).

Note: After the deletion is requested and a `200` is returned, the transcription will not be accessible anymore. However, it is not deleted immediately. This deletion process, while transparent and irreversible, can take an additional 24 to 48 hours.

### Example

* Basic Authentication (Basic):
* OAuth Authentication (OAuth2):

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

# Configure your client ID and secret for OAuth
configuration = bandwidth.Configuration(
    client_id = os.environ["CLIENT_ID"],
    client_secret = os.environ["CLIENT_SECRET"]
)

# Enter a context with an instance of the API client
with bandwidth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bandwidth.TranscriptionsApi(api_client)
    account_id = '9900000' # str | Your Bandwidth Account ID.
    call_id = 'c-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85' # str | Programmable Voice API Call ID.
    transcription_id = 't-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85' # str | Programmable Voice API Transcription ID.

    try:
        # Delete Real-time Transcription
        api_instance.delete_real_time_transcription(account_id, call_id, transcription_id)
    except Exception as e:
        print("Exception when calling TranscriptionsApi->delete_real_time_transcription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Your Bandwidth Account ID. | 
 **call_id** | **str**| Programmable Voice API Call ID. | 
 **transcription_id** | **str**| Programmable Voice API Transcription ID. | 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No Content |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**415** | Unsupported Media Type |  -  |
**429** | Too Many Requests |  * Retry-After - When you should try your request again. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_real_time_transcription**
> CallTranscriptionResponse get_real_time_transcription(account_id, call_id, transcription_id)

Get Real-time Transcription

Retrieve the specified transcription that was created on this call via [startTranscription](/docs/voice/bxml/startTranscription).

### Example

* Basic Authentication (Basic):
* OAuth Authentication (OAuth2):

```python
import bandwidth
from bandwidth.models.call_transcription_response import CallTranscriptionResponse
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

# Configure your client ID and secret for OAuth
configuration = bandwidth.Configuration(
    client_id = os.environ["CLIENT_ID"],
    client_secret = os.environ["CLIENT_SECRET"]
)

# Enter a context with an instance of the API client
with bandwidth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bandwidth.TranscriptionsApi(api_client)
    account_id = '9900000' # str | Your Bandwidth Account ID.
    call_id = 'c-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85' # str | Programmable Voice API Call ID.
    transcription_id = 't-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85' # str | Programmable Voice API Transcription ID.

    try:
        # Get Real-time Transcription
        api_response = api_instance.get_real_time_transcription(account_id, call_id, transcription_id)
        print("The response of TranscriptionsApi->get_real_time_transcription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranscriptionsApi->get_real_time_transcription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Your Bandwidth Account ID. | 
 **call_id** | **str**| Programmable Voice API Call ID. | 
 **transcription_id** | **str**| Programmable Voice API Transcription ID. | 

### Return type

[**CallTranscriptionResponse**](CallTranscriptionResponse.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**415** | Unsupported Media Type |  -  |
**429** | Too Many Requests |  * Retry-After - When you should try your request again. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_real_time_transcriptions**
> List[CallTranscriptionMetadata] list_real_time_transcriptions(account_id, call_id)

List Real-time Transcriptions

List the transcriptions created on this call via [startTranscription](/docs/voice/bxml/startTranscription).

### Example

* Basic Authentication (Basic):
* OAuth Authentication (OAuth2):

```python
import bandwidth
from bandwidth.models.call_transcription_metadata import CallTranscriptionMetadata
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

# Configure your client ID and secret for OAuth
configuration = bandwidth.Configuration(
    client_id = os.environ["CLIENT_ID"],
    client_secret = os.environ["CLIENT_SECRET"]
)

# Enter a context with an instance of the API client
with bandwidth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bandwidth.TranscriptionsApi(api_client)
    account_id = '9900000' # str | Your Bandwidth Account ID.
    call_id = 'c-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85' # str | Programmable Voice API Call ID.

    try:
        # List Real-time Transcriptions
        api_response = api_instance.list_real_time_transcriptions(account_id, call_id)
        print("The response of TranscriptionsApi->list_real_time_transcriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranscriptionsApi->list_real_time_transcriptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Your Bandwidth Account ID. | 
 **call_id** | **str**| Programmable Voice API Call ID. | 

### Return type

[**List[CallTranscriptionMetadata]**](CallTranscriptionMetadata.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**415** | Unsupported Media Type |  -  |
**429** | Too Many Requests |  * Retry-After - When you should try your request again. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

