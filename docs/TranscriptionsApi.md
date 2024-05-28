# bandwidth.TranscriptionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_real_time_transcription**](TranscriptionsApi.md#delete_real_time_transcription) | **DELETE** /accounts/{accountId}/calls/{callId}/transcriptions/{transcriptionId} | Delete a specific transcription
[**get_real_time_transcription**](TranscriptionsApi.md#get_real_time_transcription) | **GET** /accounts/{accountId}/calls/{callId}/transcriptions/{transcriptionId} | Retrieve a specific transcription
[**list_real_time_transcriptions**](TranscriptionsApi.md#list_real_time_transcriptions) | **GET** /accounts/{accountId}/calls/{callId}/transcriptions | Enumerate transcriptions made with StartTranscription


# **delete_real_time_transcription**
> delete_real_time_transcription(account_id, call_id, transcription_id)

Delete a specific transcription

Delete the specified transcription that was created on this call via [startTranscription](/docs/voice/bxml/startTranscription).  Note: After the deletion is requested and a `204` is returned, the transcription will not be accessible anymore. However, it is not deleted immediately. This deletion process, while transparent and irreversible, can take an additional 24 to 48 hours.

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
    api_instance = bandwidth.TranscriptionsApi(api_client)
    account_id = '9900000' # str | Your Bandwidth Account ID.
    call_id = 'c-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85' # str | Programmable Voice API Call ID.
    transcription_id = 't-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85' # str | Programmable Voice API Transcription ID.

    try:
        # Delete a specific transcription
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

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Transcription data was deleted. |  -  |
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

Retrieve a specific transcription

Retrieve the specified transcription that was created on this call via [startTranscription](/docs/voice/bxml/startTranscription).

### Example

* Basic Authentication (Basic):

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

# Enter a context with an instance of the API client
with bandwidth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bandwidth.TranscriptionsApi(api_client)
    account_id = '9900000' # str | Your Bandwidth Account ID.
    call_id = 'c-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85' # str | Programmable Voice API Call ID.
    transcription_id = 't-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85' # str | Programmable Voice API Transcription ID.

    try:
        # Retrieve a specific transcription
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

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transcription found. |  -  |
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

Enumerate transcriptions made with StartTranscription

Enumerates the transcriptions created on this call via [startTranscription](/docs/voice/bxml/startTranscription).

### Example

* Basic Authentication (Basic):

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

# Enter a context with an instance of the API client
with bandwidth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bandwidth.TranscriptionsApi(api_client)
    account_id = '9900000' # str | Your Bandwidth Account ID.
    call_id = 'c-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85' # str | Programmable Voice API Call ID.

    try:
        # Enumerate transcriptions made with StartTranscription
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

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transcription found. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**415** | Unsupported Media Type |  -  |
**429** | Too Many Requests |  * Retry-After - When you should try your request again. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

