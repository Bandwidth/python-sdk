# bandwidth.RecordingsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_call_transcription**](RecordingsApi.md#delete_call_transcription) | **DELETE** /api/v2/accounts/{accountId}/calls/{callId}/recordings/{recordingId}/transcription | Delete Transcription
[**delete_recording**](RecordingsApi.md#delete_recording) | **DELETE** /api/v2/accounts/{accountId}/calls/{callId}/recordings/{recordingId} | Delete Recording
[**delete_recording_media**](RecordingsApi.md#delete_recording_media) | **DELETE** /api/v2/accounts/{accountId}/calls/{callId}/recordings/{recordingId}/media | Delete Recording Media
[**download_call_recording**](RecordingsApi.md#download_call_recording) | **GET** /api/v2/accounts/{accountId}/calls/{callId}/recordings/{recordingId}/media | Download Recording
[**get_call_recording**](RecordingsApi.md#get_call_recording) | **GET** /api/v2/accounts/{accountId}/calls/{callId}/recordings/{recordingId} | Get Call Recording
[**get_call_recordings**](RecordingsApi.md#get_call_recordings) | **GET** /api/v2/accounts/{accountId}/calls/{callId}/recordings | Get Call Recordings
[**get_call_transcription**](RecordingsApi.md#get_call_transcription) | **GET** /api/v2/accounts/{accountId}/calls/{callId}/recordings/{recordingId}/transcription | Get Transcription
[**modify_call_recording_state**](RecordingsApi.md#modify_call_recording_state) | **PUT** /api/v2/accounts/{accountId}/calls/{callId}/recording | Update Recording
[**query_call_recordings**](RecordingsApi.md#query_call_recordings) | **GET** /api/v2/accounts/{accountId}/recordings | Get Call Recordings
[**transcribe_call_recording**](RecordingsApi.md#transcribe_call_recording) | **POST** /api/v2/accounts/{accountId}/calls/{callId}/recordings/{recordingId}/transcription | Create Transcription Request


# **delete_call_transcription**
> delete_call_transcription(account_id, call_id, recording_id)

Delete Transcription

Deletes the specified recording's transcription.  Note: After the deletion is requested and a `204` is returned, the transcription will not be accessible anymore. However, it is not deleted immediately. This deletion process, while transparent and irreversible, can take an additional 24 to 48 hours.

### Example

* Basic Authentication (httpBasic):

```python
import time
import bandwidth
from bandwidth.api import recordings_api
from bandwidth.model.api_error import ApiError
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

# Configure HTTP basic authorization: httpBasic
configuration = bandwidth.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with bandwidth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = recordings_api.RecordingsApi(api_client)
    account_id = "accountId_example" # str | 
    call_id = "callId_example" # str | 
    recording_id = "recordingId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete Transcription
        api_instance.delete_call_transcription(account_id, call_id, recording_id)
    except bandwidth.ApiException as e:
        print("Exception when calling RecordingsApi->delete_call_transcription: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  |
 **call_id** | **str**|  |
 **recording_id** | **str**|  |

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
**204** | The transcription was successfully deleted |  -  |
**400** | Something&#39;s not quite right... Your request is invalid. Please fix it before trying again. |  -  |
**401** | Your credentials are invalid. Please use your Bandwidth dashboard credentials to authenticate to the API. |  -  |
**403** | User unauthorized to perform this action. |  -  |
**404** | The resource specified cannot be found or does not belong to you. |  -  |
**415** | We don&#39;t support that media type. If a request body is required, please send it to us as &#x60;application/json&#x60;. |  -  |
**429** | You&#39;re sending requests to this endpoint too frequently. Please slow your request rate down and try again. |  * Retry-After - When you should try your request again <br>  |
**500** | Something unexpected happened. Please try again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_recording**
> delete_recording(account_id, call_id, recording_id)

Delete Recording

Delete the recording information, media and transcription.  Note: After the deletion is requested and a `204` is returned, neither the recording metadata nor the actual media nor its transcription will be accessible anymore. However, the media of the specified recording is not deleted immediately. This deletion process, while transparent and irreversible, can take an additional 24 to 48 hours.

### Example

* Basic Authentication (httpBasic):

```python
import time
import bandwidth
from bandwidth.api import recordings_api
from bandwidth.model.api_error import ApiError
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

# Configure HTTP basic authorization: httpBasic
configuration = bandwidth.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with bandwidth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = recordings_api.RecordingsApi(api_client)
    account_id = "accountId_example" # str | 
    call_id = "callId_example" # str | 
    recording_id = "recordingId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete Recording
        api_instance.delete_recording(account_id, call_id, recording_id)
    except bandwidth.ApiException as e:
        print("Exception when calling RecordingsApi->delete_recording: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  |
 **call_id** | **str**|  |
 **recording_id** | **str**|  |

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
**204** | The recording was successfully deleted |  -  |
**400** | Something&#39;s not quite right... Your request is invalid. Please fix it before trying again. |  -  |
**401** | Your credentials are invalid. Please use your Bandwidth dashboard credentials to authenticate to the API. |  -  |
**403** | User unauthorized to perform this action. |  -  |
**404** | The resource specified cannot be found or does not belong to you. |  -  |
**415** | We don&#39;t support that media type. If a request body is required, please send it to us as &#x60;application/json&#x60;. |  -  |
**429** | You&#39;re sending requests to this endpoint too frequently. Please slow your request rate down and try again. |  * Retry-After - When you should try your request again <br>  |
**500** | Something unexpected happened. Please try again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_recording_media**
> delete_recording_media(account_id, call_id, recording_id)

Delete Recording Media

Deletes the specified recording's media.

### Example

* Basic Authentication (httpBasic):

```python
import time
import bandwidth
from bandwidth.api import recordings_api
from bandwidth.model.api_error import ApiError
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

# Configure HTTP basic authorization: httpBasic
configuration = bandwidth.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with bandwidth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = recordings_api.RecordingsApi(api_client)
    account_id = "accountId_example" # str | 
    call_id = "callId_example" # str | 
    recording_id = "recordingId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete Recording Media
        api_instance.delete_recording_media(account_id, call_id, recording_id)
    except bandwidth.ApiException as e:
        print("Exception when calling RecordingsApi->delete_recording_media: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  |
 **call_id** | **str**|  |
 **recording_id** | **str**|  |

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
**204** | The recording media was successfully deleted |  -  |
**400** | Something&#39;s not quite right... Your request is invalid. Please fix it before trying again. |  -  |
**401** | Your credentials are invalid. Please use your Bandwidth dashboard credentials to authenticate to the API. |  -  |
**403** | User unauthorized to perform this action. |  -  |
**404** | The resource specified cannot be found or does not belong to you. |  -  |
**415** | We don&#39;t support that media type. If a request body is required, please send it to us as &#x60;application/json&#x60;. |  -  |
**429** | You&#39;re sending requests to this endpoint too frequently. Please slow your request rate down and try again. |  * Retry-After - When you should try your request again <br>  |
**500** | Something unexpected happened. Please try again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_call_recording**
> file_type download_call_recording(account_id, call_id, recording_id)

Download Recording

Downloads the specified recording.

### Example

* Basic Authentication (httpBasic):

```python
import time
import bandwidth
from bandwidth.api import recordings_api
from bandwidth.model.api_error import ApiError
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

# Configure HTTP basic authorization: httpBasic
configuration = bandwidth.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with bandwidth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = recordings_api.RecordingsApi(api_client)
    account_id = "accountId_example" # str | 
    call_id = "callId_example" # str | 
    recording_id = "recordingId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Download Recording
        api_response = api_instance.download_call_recording(account_id, call_id, recording_id)
        pprint(api_response)
    except bandwidth.ApiException as e:
        print("Exception when calling RecordingsApi->download_call_recording: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  |
 **call_id** | **str**|  |
 **recording_id** | **str**|  |

### Return type

**file_type**

### Authorization

[httpBasic](../README.md#httpBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: audio/vnd.wave, audio/mpeg, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Media found |  -  |
**400** | Something&#39;s not quite right... Your request is invalid. Please fix it before trying again. |  -  |
**401** | Your credentials are invalid. Please use your Bandwidth dashboard credentials to authenticate to the API. |  -  |
**403** | User unauthorized to perform this action. |  -  |
**404** | The resource specified cannot be found or does not belong to you. |  -  |
**415** | We don&#39;t support that media type. If a request body is required, please send it to us as &#x60;application/json&#x60;. |  -  |
**429** | You&#39;re sending requests to this endpoint too frequently. Please slow your request rate down and try again. |  * Retry-After - When you should try your request again <br>  |
**500** | Something unexpected happened. Please try again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_call_recording**
> CallRecordingMetadata get_call_recording(account_id, call_id, recording_id)

Get Call Recording

Returns metadata for the specified recording.

### Example

* Basic Authentication (httpBasic):

```python
import time
import bandwidth
from bandwidth.api import recordings_api
from bandwidth.model.api_error import ApiError
from bandwidth.model.call_recording_metadata import CallRecordingMetadata
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

# Configure HTTP basic authorization: httpBasic
configuration = bandwidth.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with bandwidth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = recordings_api.RecordingsApi(api_client)
    account_id = "accountId_example" # str | 
    call_id = "callId_example" # str | 
    recording_id = "recordingId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get Call Recording
        api_response = api_instance.get_call_recording(account_id, call_id, recording_id)
        pprint(api_response)
    except bandwidth.ApiException as e:
        print("Exception when calling RecordingsApi->get_call_recording: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  |
 **call_id** | **str**|  |
 **recording_id** | **str**|  |

### Return type

[**CallRecordingMetadata**](CallRecordingMetadata.md)

### Authorization

[httpBasic](../README.md#httpBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Recording found |  -  |
**400** | Something&#39;s not quite right... Your request is invalid. Please fix it before trying again. |  -  |
**401** | Your credentials are invalid. Please use your Bandwidth dashboard credentials to authenticate to the API. |  -  |
**403** | User unauthorized to perform this action. |  -  |
**404** | The resource specified cannot be found or does not belong to you. |  -  |
**415** | We don&#39;t support that media type. If a request body is required, please send it to us as &#x60;application/json&#x60;. |  -  |
**429** | You&#39;re sending requests to this endpoint too frequently. Please slow your request rate down and try again. |  * Retry-After - When you should try your request again <br>  |
**500** | Something unexpected happened. Please try again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_call_recordings**
> [CallRecordingMetadata] get_call_recordings(account_id, call_id)

Get Call Recordings

Returns a (potentially empty) list of metadata for the recordings that took place during the specified call.

### Example

* Basic Authentication (httpBasic):

```python
import time
import bandwidth
from bandwidth.api import recordings_api
from bandwidth.model.api_error import ApiError
from bandwidth.model.call_recording_metadata import CallRecordingMetadata
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

# Configure HTTP basic authorization: httpBasic
configuration = bandwidth.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with bandwidth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = recordings_api.RecordingsApi(api_client)
    account_id = "accountId_example" # str | 
    call_id = "callId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get Call Recordings
        api_response = api_instance.get_call_recordings(account_id, call_id)
        pprint(api_response)
    except bandwidth.ApiException as e:
        print("Exception when calling RecordingsApi->get_call_recordings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  |
 **call_id** | **str**|  |

### Return type

[**[CallRecordingMetadata]**](CallRecordingMetadata.md)

### Authorization

[httpBasic](../README.md#httpBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Recordings retrieved successfully |  -  |
**400** | Something&#39;s not quite right... Your request is invalid. Please fix it before trying again. |  -  |
**401** | Your credentials are invalid. Please use your Bandwidth dashboard credentials to authenticate to the API. |  -  |
**403** | User unauthorized to perform this action. |  -  |
**404** | The resource specified cannot be found or does not belong to you. |  -  |
**415** | We don&#39;t support that media type. If a request body is required, please send it to us as &#x60;application/json&#x60;. |  -  |
**429** | You&#39;re sending requests to this endpoint too frequently. Please slow your request rate down and try again. |  * Retry-After - When you should try your request again <br>  |
**500** | Something unexpected happened. Please try again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_call_transcription**
> TranscriptionResponse get_call_transcription(account_id, call_id, recording_id)

Get Transcription

Downloads the specified transcription.  If the transcribed recording was multi-channel, then there will be 2 transcripts. The caller/called party transcript will be the first item while [`<PlayAudio>`](/docs/voice/bxml/playAudio) and [`<SpeakSentence>`](/docs/voice/bxml/speakSentence) transcript will be the second item. During a [`<Transfer>`](/docs/voice/bxml/transfer) the A-leg transcript will be the first item while the B-leg transcript will be the second item.

### Example

* Basic Authentication (httpBasic):

```python
import time
import bandwidth
from bandwidth.api import recordings_api
from bandwidth.model.api_error import ApiError
from bandwidth.model.transcription_response import TranscriptionResponse
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

# Configure HTTP basic authorization: httpBasic
configuration = bandwidth.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with bandwidth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = recordings_api.RecordingsApi(api_client)
    account_id = "accountId_example" # str | 
    call_id = "callId_example" # str | 
    recording_id = "recordingId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get Transcription
        api_response = api_instance.get_call_transcription(account_id, call_id, recording_id)
        pprint(api_response)
    except bandwidth.ApiException as e:
        print("Exception when calling RecordingsApi->get_call_transcription: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  |
 **call_id** | **str**|  |
 **recording_id** | **str**|  |

### Return type

[**TranscriptionResponse**](TranscriptionResponse.md)

### Authorization

[httpBasic](../README.md#httpBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transcription found |  -  |
**400** | Something&#39;s not quite right... Your request is invalid. Please fix it before trying again. |  -  |
**401** | Your credentials are invalid. Please use your Bandwidth dashboard credentials to authenticate to the API. |  -  |
**403** | User unauthorized to perform this action. |  -  |
**404** | The resource specified cannot be found or does not belong to you. |  -  |
**415** | We don&#39;t support that media type. If a request body is required, please send it to us as &#x60;application/json&#x60;. |  -  |
**429** | You&#39;re sending requests to this endpoint too frequently. Please slow your request rate down and try again. |  * Retry-After - When you should try your request again <br>  |
**500** | Something unexpected happened. Please try again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_call_recording_state**
> modify_call_recording_state(account_id, call_id, modify_call_recording_request)

Update Recording

Pause or resume a recording on an active phone call

### Example

* Basic Authentication (httpBasic):

```python
import time
import bandwidth
from bandwidth.api import recordings_api
from bandwidth.model.api_error import ApiError
from bandwidth.model.modify_call_recording_request import ModifyCallRecordingRequest
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

# Configure HTTP basic authorization: httpBasic
configuration = bandwidth.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with bandwidth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = recordings_api.RecordingsApi(api_client)
    account_id = "accountId_example" # str | 
    call_id = "callId_example" # str | 
    modify_call_recording_request = ModifyCallRecordingRequest(
        state="paused",
    ) # ModifyCallRecordingRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Update Recording
        api_instance.modify_call_recording_state(account_id, call_id, modify_call_recording_request)
    except bandwidth.ApiException as e:
        print("Exception when calling RecordingsApi->modify_call_recording_state: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  |
 **call_id** | **str**|  |
 **modify_call_recording_request** | [**ModifyCallRecordingRequest**](ModifyCallRecordingRequest.md)|  |

### Return type

void (empty response body)

### Authorization

[httpBasic](../README.md#httpBasic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Recording state successfully modified |  -  |
**400** | Something&#39;s not quite right... Your request is invalid. Please fix it before trying again. |  -  |
**401** | Your credentials are invalid. Please use your Bandwidth dashboard credentials to authenticate to the API. |  -  |
**403** | User unauthorized to perform this action. |  -  |
**404** | The resource specified cannot be found or does not belong to you. |  -  |
**415** | We don&#39;t support that media type. If a request body is required, please send it to us as &#x60;application/json&#x60;. |  -  |
**429** | You&#39;re sending requests to this endpoint too frequently. Please slow your request rate down and try again. |  * Retry-After - When you should try your request again <br>  |
**500** | Something unexpected happened. Please try again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_call_recordings**
> [CallRecordingMetadata] query_call_recordings(account_id)

Get Call Recordings

Returns a list of metadata for the recordings associated with the specified account. The list can be filtered by the optional from, to, minStartTime, and maxStartTime arguments. The list is capped at 1000 entries and may be empty if no recordings match the specified criteria.

### Example

* Basic Authentication (httpBasic):

```python
import time
import bandwidth
from bandwidth.api import recordings_api
from bandwidth.model.api_error import ApiError
from bandwidth.model.call_recording_metadata import CallRecordingMetadata
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

# Configure HTTP basic authorization: httpBasic
configuration = bandwidth.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with bandwidth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = recordings_api.RecordingsApi(api_client)
    account_id = "accountId_example" # str | 
    _from = "from_example" # str | Filter results by the `from` field. (optional)
    to = "to_example" # str | Filter results by the `to` field. (optional)
    min_start_time = "minStartTime_example" # str | Filter results to recordings which have a `startTime` after or including `minStartTime` (in ISO8601 format). (optional)
    max_start_time = "maxStartTime_example" # str | Filter results to recordings which have a `startTime` before `maxStartTime` (in ISO8601 format). (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Call Recordings
        api_response = api_instance.query_call_recordings(account_id)
        pprint(api_response)
    except bandwidth.ApiException as e:
        print("Exception when calling RecordingsApi->query_call_recordings: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Call Recordings
        api_response = api_instance.query_call_recordings(account_id, _from=_from, to=to, min_start_time=min_start_time, max_start_time=max_start_time)
        pprint(api_response)
    except bandwidth.ApiException as e:
        print("Exception when calling RecordingsApi->query_call_recordings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  |
 **_from** | **str**| Filter results by the &#x60;from&#x60; field. | [optional]
 **to** | **str**| Filter results by the &#x60;to&#x60; field. | [optional]
 **min_start_time** | **str**| Filter results to recordings which have a &#x60;startTime&#x60; after or including &#x60;minStartTime&#x60; (in ISO8601 format). | [optional]
 **max_start_time** | **str**| Filter results to recordings which have a &#x60;startTime&#x60; before &#x60;maxStartTime&#x60; (in ISO8601 format). | [optional]

### Return type

[**[CallRecordingMetadata]**](CallRecordingMetadata.md)

### Authorization

[httpBasic](../README.md#httpBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Recordings retrieved successfully. |  -  |
**400** | Something&#39;s not quite right... Your request is invalid. Please fix it before trying again. |  -  |
**401** | Your credentials are invalid. Please use your Bandwidth dashboard credentials to authenticate to the API. |  -  |
**403** | User unauthorized to perform this action. |  -  |
**404** | The resource specified cannot be found or does not belong to you. |  -  |
**415** | We don&#39;t support that media type. If a request body is required, please send it to us as &#x60;application/json&#x60;. |  -  |
**429** | You&#39;re sending requests to this endpoint too frequently. Please slow your request rate down and try again. |  * Retry-After - When you should try your request again <br>  |
**500** | Something unexpected happened. Please try again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transcribe_call_recording**
> transcribe_call_recording(account_id, call_id, recording_id, transcribe_recording_request)

Create Transcription Request

Generate the transcription for a specific recording. Transcription can succeed only for recordings of length greater than 500 milliseconds and less than 4 hours.

### Example

* Basic Authentication (httpBasic):

```python
import time
import bandwidth
from bandwidth.api import recordings_api
from bandwidth.model.api_error import ApiError
from bandwidth.model.transcribe_recording_request import TranscribeRecordingRequest
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

# Configure HTTP basic authorization: httpBasic
configuration = bandwidth.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with bandwidth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = recordings_api.RecordingsApi(api_client)
    account_id = "accountId_example" # str | 
    call_id = "callId_example" # str | 
    recording_id = "recordingId_example" # str | 
    transcribe_recording_request = TranscribeRecordingRequest(
        callback_url="callback_url_example",
        callback_method="POST",
        username="username_example",
        password="password_example",
        tag="tag_example",
        callback_timeout=3.14,
    ) # TranscribeRecordingRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create Transcription Request
        api_instance.transcribe_call_recording(account_id, call_id, recording_id, transcribe_recording_request)
    except bandwidth.ApiException as e:
        print("Exception when calling RecordingsApi->transcribe_call_recording: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  |
 **call_id** | **str**|  |
 **recording_id** | **str**|  |
 **transcribe_recording_request** | [**TranscribeRecordingRequest**](TranscribeRecordingRequest.md)|  |

### Return type

void (empty response body)

### Authorization

[httpBasic](../README.md#httpBasic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Transcription successfully requested |  -  |
**400** | Something&#39;s not quite right... Your request is invalid. Please fix it before trying again. |  -  |
**401** | Your credentials are invalid. Please use your Bandwidth dashboard credentials to authenticate to the API. |  -  |
**403** | User unauthorized to perform this action. |  -  |
**404** | The resource specified cannot be found or does not belong to you. |  -  |
**410** | The media for this recording has been deleted, so we can&#39;t transcribe it |  -  |
**415** | We don&#39;t support that media type. If a request body is required, please send it to us as &#x60;application/json&#x60;. |  -  |
**429** | You&#39;re sending requests to this endpoint too frequently. Please slow your request rate down and try again. |  * Retry-After - When you should try your request again <br>  |
**500** | Something unexpected happened. Please try again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

