# bandwidth.RecordingsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_recording**](RecordingsApi.md#delete_recording) | **DELETE** /accounts/{accountId}/calls/{callId}/recordings/{recordingId} | Delete Recording
[**delete_recording_media**](RecordingsApi.md#delete_recording_media) | **DELETE** /accounts/{accountId}/calls/{callId}/recordings/{recordingId}/media | Delete Recording Media
[**delete_recording_transcription**](RecordingsApi.md#delete_recording_transcription) | **DELETE** /accounts/{accountId}/calls/{callId}/recordings/{recordingId}/transcription | Delete Transcription
[**download_call_recording**](RecordingsApi.md#download_call_recording) | **GET** /accounts/{accountId}/calls/{callId}/recordings/{recordingId}/media | Download Recording
[**get_call_recording**](RecordingsApi.md#get_call_recording) | **GET** /accounts/{accountId}/calls/{callId}/recordings/{recordingId} | Get Call Recording
[**get_recording_transcription**](RecordingsApi.md#get_recording_transcription) | **GET** /accounts/{accountId}/calls/{callId}/recordings/{recordingId}/transcription | Get Transcription
[**list_account_call_recordings**](RecordingsApi.md#list_account_call_recordings) | **GET** /accounts/{accountId}/recordings | Get Call Recordings
[**list_call_recordings**](RecordingsApi.md#list_call_recordings) | **GET** /accounts/{accountId}/calls/{callId}/recordings | List Call Recordings
[**transcribe_call_recording**](RecordingsApi.md#transcribe_call_recording) | **POST** /accounts/{accountId}/calls/{callId}/recordings/{recordingId}/transcription | Create Transcription Request
[**update_call_recording_state**](RecordingsApi.md#update_call_recording_state) | **PUT** /accounts/{accountId}/calls/{callId}/recording | Update Recording


# **delete_recording**
> delete_recording(account_id, call_id, recording_id)

Delete Recording

Delete the recording information, media and transcription.  Note: After the deletion is requested and a `204` is returned, neither the recording metadata nor the actual media nor its transcription will be accessible anymore. However, the media of the specified recording is not deleted immediately. This deletion process, while transparent and irreversible, can take an additional 24 to 48 hours.

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bandwidth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bandwidth.RecordingsApi(api_client)
    account_id = '9900000' # str | Your Bandwidth Account ID.
    call_id = 'c-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85' # str | Programmable Voice API Call ID.
    recording_id = 'r-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85' # str | Programmable Voice API Recording ID.

    try:
        # Delete Recording
        api_instance.delete_recording(account_id, call_id, recording_id)
    except Exception as e:
        print("Exception when calling RecordingsApi->delete_recording: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Your Bandwidth Account ID. | 
 **call_id** | **str**| Programmable Voice API Call ID. | 
 **recording_id** | **str**| Programmable Voice API Recording ID. | 

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
**204** | Recording was deleted. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**415** | Unsupported Media Type |  -  |
**429** | Too Many Requests |  * Retry-After - When you should try your request again. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_recording_media**
> delete_recording_media(account_id, call_id, recording_id)

Delete Recording Media

Deletes the specified recording's media.

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bandwidth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bandwidth.RecordingsApi(api_client)
    account_id = '9900000' # str | Your Bandwidth Account ID.
    call_id = 'c-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85' # str | Programmable Voice API Call ID.
    recording_id = 'r-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85' # str | Programmable Voice API Recording ID.

    try:
        # Delete Recording Media
        api_instance.delete_recording_media(account_id, call_id, recording_id)
    except Exception as e:
        print("Exception when calling RecordingsApi->delete_recording_media: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Your Bandwidth Account ID. | 
 **call_id** | **str**| Programmable Voice API Call ID. | 
 **recording_id** | **str**| Programmable Voice API Recording ID. | 

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
**204** | The recording media was successfully deleted. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**415** | Unsupported Media Type |  -  |
**429** | Too Many Requests |  * Retry-After - When you should try your request again. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_recording_transcription**
> delete_recording_transcription(account_id, call_id, recording_id)

Delete Transcription

Deletes the specified recording's transcription.  Note: After the deletion is requested and a `204` is returned, the transcription will not be accessible anymore. However, it is not deleted immediately. This deletion process, while transparent and irreversible, can take an additional 24 to 48 hours.

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bandwidth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bandwidth.RecordingsApi(api_client)
    account_id = '9900000' # str | Your Bandwidth Account ID.
    call_id = 'c-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85' # str | Programmable Voice API Call ID.
    recording_id = 'r-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85' # str | Programmable Voice API Recording ID.

    try:
        # Delete Transcription
        api_instance.delete_recording_transcription(account_id, call_id, recording_id)
    except Exception as e:
        print("Exception when calling RecordingsApi->delete_recording_transcription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Your Bandwidth Account ID. | 
 **call_id** | **str**| Programmable Voice API Call ID. | 
 **recording_id** | **str**| Programmable Voice API Recording ID. | 

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
**204** | The transcription was successfully deleted. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**415** | Unsupported Media Type |  -  |
**429** | Too Many Requests |  * Retry-After - When you should try your request again. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_call_recording**
> bytearray download_call_recording(account_id, call_id, recording_id)

Download Recording

Downloads the specified recording.

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bandwidth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bandwidth.RecordingsApi(api_client)
    account_id = '9900000' # str | Your Bandwidth Account ID.
    call_id = 'c-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85' # str | Programmable Voice API Call ID.
    recording_id = 'r-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85' # str | Programmable Voice API Recording ID.

    try:
        # Download Recording
        api_response = api_instance.download_call_recording(account_id, call_id, recording_id)
        print("The response of RecordingsApi->download_call_recording:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordingsApi->download_call_recording: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Your Bandwidth Account ID. | 
 **call_id** | **str**| Programmable Voice API Call ID. | 
 **recording_id** | **str**| Programmable Voice API Recording ID. | 

### Return type

**bytearray**

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: audio/vnd.wave, audio/mpeg, application/json

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

# **get_call_recording**
> CallRecordingMetadata get_call_recording(account_id, call_id, recording_id)

Get Call Recording

Returns metadata for the specified recording.

### Example

* Basic Authentication (Basic):
* OAuth Authentication (OAuth2):

```python
import bandwidth
from bandwidth.models.call_recording_metadata import CallRecordingMetadata
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bandwidth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bandwidth.RecordingsApi(api_client)
    account_id = '9900000' # str | Your Bandwidth Account ID.
    call_id = 'c-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85' # str | Programmable Voice API Call ID.
    recording_id = 'r-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85' # str | Programmable Voice API Recording ID.

    try:
        # Get Call Recording
        api_response = api_instance.get_call_recording(account_id, call_id, recording_id)
        print("The response of RecordingsApi->get_call_recording:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordingsApi->get_call_recording: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Your Bandwidth Account ID. | 
 **call_id** | **str**| Programmable Voice API Call ID. | 
 **recording_id** | **str**| Programmable Voice API Recording ID. | 

### Return type

[**CallRecordingMetadata**](CallRecordingMetadata.md)

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

# **get_recording_transcription**
> RecordingTranscriptions get_recording_transcription(account_id, call_id, recording_id)

Get Transcription

Downloads the specified transcription. If the recording was multi-channel, then there will be 2 transcripts. The caller/called party transcript will be the first item while [`<PlayAudio>`](/docs/voice/bxml/playAudio) and [`<SpeakSentence>`](/docs/voice/bxml/speakSentence) transcript will be the second item. During a [`<Transfer>`](/docs/voice/bxml/transfer) the A-leg transcript will be the first item while the B-leg transcript will be the second item.

### Example

* Basic Authentication (Basic):
* OAuth Authentication (OAuth2):

```python
import bandwidth
from bandwidth.models.recording_transcriptions import RecordingTranscriptions
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bandwidth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bandwidth.RecordingsApi(api_client)
    account_id = '9900000' # str | Your Bandwidth Account ID.
    call_id = 'c-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85' # str | Programmable Voice API Call ID.
    recording_id = 'r-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85' # str | Programmable Voice API Recording ID.

    try:
        # Get Transcription
        api_response = api_instance.get_recording_transcription(account_id, call_id, recording_id)
        print("The response of RecordingsApi->get_recording_transcription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordingsApi->get_recording_transcription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Your Bandwidth Account ID. | 
 **call_id** | **str**| Programmable Voice API Call ID. | 
 **recording_id** | **str**| Programmable Voice API Recording ID. | 

### Return type

[**RecordingTranscriptions**](RecordingTranscriptions.md)

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

# **list_account_call_recordings**
> List[CallRecordingMetadata] list_account_call_recordings(account_id, to=to, var_from=var_from, min_start_time=min_start_time, max_start_time=max_start_time)

Get Call Recordings

Returns a list of metadata for the recordings associated with the specified account. The list can be filtered by the optional from, to, minStartTime, and maxStartTime arguments. The list is capped at 1000 entries and may be empty if no recordings match the specified criteria.

### Example

* Basic Authentication (Basic):
* OAuth Authentication (OAuth2):

```python
import bandwidth
from bandwidth.models.call_recording_metadata import CallRecordingMetadata
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bandwidth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bandwidth.RecordingsApi(api_client)
    account_id = '9900000' # str | Your Bandwidth Account ID.
    to = '%2b19195551234' # str | Filter results by the `to` field. (optional)
    var_from = '%2b19195554321' # str | Filter results by the `from` field. (optional)
    min_start_time = '2022-06-21T19:13:21Z' # str | Filter results to recordings which have a `startTime` after or including `minStartTime` (in ISO8601 format). (optional)
    max_start_time = '2022-06-21T19:13:21Z' # str | Filter results to recordings which have a `startTime` before `maxStartTime` (in ISO8601 format). (optional)

    try:
        # Get Call Recordings
        api_response = api_instance.list_account_call_recordings(account_id, to=to, var_from=var_from, min_start_time=min_start_time, max_start_time=max_start_time)
        print("The response of RecordingsApi->list_account_call_recordings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordingsApi->list_account_call_recordings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Your Bandwidth Account ID. | 
 **to** | **str**| Filter results by the &#x60;to&#x60; field. | [optional] 
 **var_from** | **str**| Filter results by the &#x60;from&#x60; field. | [optional] 
 **min_start_time** | **str**| Filter results to recordings which have a &#x60;startTime&#x60; after or including &#x60;minStartTime&#x60; (in ISO8601 format). | [optional] 
 **max_start_time** | **str**| Filter results to recordings which have a &#x60;startTime&#x60; before &#x60;maxStartTime&#x60; (in ISO8601 format). | [optional] 

### Return type

[**List[CallRecordingMetadata]**](CallRecordingMetadata.md)

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

# **list_call_recordings**
> List[CallRecordingMetadata] list_call_recordings(account_id, call_id)

List Call Recordings

Returns a (potentially empty) list of metadata for the recordings that took place during the specified call.

### Example

* Basic Authentication (Basic):
* OAuth Authentication (OAuth2):

```python
import bandwidth
from bandwidth.models.call_recording_metadata import CallRecordingMetadata
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bandwidth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bandwidth.RecordingsApi(api_client)
    account_id = '9900000' # str | Your Bandwidth Account ID.
    call_id = 'c-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85' # str | Programmable Voice API Call ID.

    try:
        # List Call Recordings
        api_response = api_instance.list_call_recordings(account_id, call_id)
        print("The response of RecordingsApi->list_call_recordings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordingsApi->list_call_recordings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Your Bandwidth Account ID. | 
 **call_id** | **str**| Programmable Voice API Call ID. | 

### Return type

[**List[CallRecordingMetadata]**](CallRecordingMetadata.md)

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

# **transcribe_call_recording**
> transcribe_call_recording(account_id, call_id, recording_id, transcribe_recording)

Create Transcription Request

Generate the transcription for a specific recording. Transcription can succeed only for recordings of length greater than 500 milliseconds and less than 4 hours.

### Example

* Basic Authentication (Basic):
* OAuth Authentication (OAuth2):

```python
import bandwidth
from bandwidth.models.transcribe_recording import TranscribeRecording
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bandwidth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bandwidth.RecordingsApi(api_client)
    account_id = '9900000' # str | Your Bandwidth Account ID.
    call_id = 'c-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85' # str | Programmable Voice API Call ID.
    recording_id = 'r-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85' # str | Programmable Voice API Recording ID.
    transcribe_recording = bandwidth.TranscribeRecording() # TranscribeRecording | 

    try:
        # Create Transcription Request
        api_instance.transcribe_call_recording(account_id, call_id, recording_id, transcribe_recording)
    except Exception as e:
        print("Exception when calling RecordingsApi->transcribe_call_recording: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Your Bandwidth Account ID. | 
 **call_id** | **str**| Programmable Voice API Call ID. | 
 **recording_id** | **str**| Programmable Voice API Recording ID. | 
 **transcribe_recording** | [**TranscribeRecording**](TranscribeRecording.md)|  | 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Transcription was successfully requested. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**415** | Unsupported Media Type |  -  |
**429** | Too Many Requests |  * Retry-After - When you should try your request again. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_call_recording_state**
> update_call_recording_state(account_id, call_id, update_call_recording)

Update Recording

Pause or resume a recording on an active phone call.

### Example

* Basic Authentication (Basic):
* OAuth Authentication (OAuth2):

```python
import bandwidth
from bandwidth.models.update_call_recording import UpdateCallRecording
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bandwidth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bandwidth.RecordingsApi(api_client)
    account_id = '9900000' # str | Your Bandwidth Account ID.
    call_id = 'c-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85' # str | Programmable Voice API Call ID.
    update_call_recording = bandwidth.UpdateCallRecording() # UpdateCallRecording | 

    try:
        # Update Recording
        api_instance.update_call_recording_state(account_id, call_id, update_call_recording)
    except Exception as e:
        print("Exception when calling RecordingsApi->update_call_recording_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Your Bandwidth Account ID. | 
 **call_id** | **str**| Programmable Voice API Call ID. | 
 **update_call_recording** | [**UpdateCallRecording**](UpdateCallRecording.md)|  | 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
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

