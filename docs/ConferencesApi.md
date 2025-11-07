# bandwidth.ConferencesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_conference_recording**](ConferencesApi.md#download_conference_recording) | **GET** /accounts/{accountId}/conferences/{conferenceId}/recordings/{recordingId}/media | Download Conference Recording
[**get_conference**](ConferencesApi.md#get_conference) | **GET** /accounts/{accountId}/conferences/{conferenceId} | Get Conference Information
[**get_conference_member**](ConferencesApi.md#get_conference_member) | **GET** /accounts/{accountId}/conferences/{conferenceId}/members/{memberId} | Get Conference Member
[**get_conference_recording**](ConferencesApi.md#get_conference_recording) | **GET** /accounts/{accountId}/conferences/{conferenceId}/recordings/{recordingId} | Get Conference Recording Information
[**list_conference_recordings**](ConferencesApi.md#list_conference_recordings) | **GET** /accounts/{accountId}/conferences/{conferenceId}/recordings | Get Conference Recordings
[**list_conferences**](ConferencesApi.md#list_conferences) | **GET** /accounts/{accountId}/conferences | Get Conferences
[**update_conference**](ConferencesApi.md#update_conference) | **POST** /accounts/{accountId}/conferences/{conferenceId} | Update Conference
[**update_conference_bxml**](ConferencesApi.md#update_conference_bxml) | **PUT** /accounts/{accountId}/conferences/{conferenceId}/bxml | Update Conference BXML
[**update_conference_member**](ConferencesApi.md#update_conference_member) | **PUT** /accounts/{accountId}/conferences/{conferenceId}/members/{memberId} | Update Conference Member


# **download_conference_recording**
> bytearray download_conference_recording(account_id, conference_id, recording_id)

Download Conference Recording

Downloads the specified recording file.

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
    api_instance = bandwidth.ConferencesApi(api_client)
    account_id = '9900000' # str | Your Bandwidth Account ID.
    conference_id = 'conf-fe23a767-a75a5b77-20c5-4cca-b581-cbbf0776eca9' # str | Programmable Voice API Conference ID.
    recording_id = 'r-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85' # str | Programmable Voice API Recording ID.

    try:
        # Download Conference Recording
        api_response = api_instance.download_conference_recording(account_id, conference_id, recording_id)
        print("The response of ConferencesApi->download_conference_recording:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConferencesApi->download_conference_recording: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Your Bandwidth Account ID. | 
 **conference_id** | **str**| Programmable Voice API Conference ID. | 
 **recording_id** | **str**| Programmable Voice API Recording ID. | 

### Return type

**bytearray**

### Authorization

[Basic](../README.md#Basic)

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

# **get_conference**
> Conference get_conference(account_id, conference_id)

Get Conference Information

Returns information about the specified conference.

### Example

* Basic Authentication (Basic):

```python
import bandwidth
from bandwidth.models.conference import Conference
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
    api_instance = bandwidth.ConferencesApi(api_client)
    account_id = '9900000' # str | Your Bandwidth Account ID.
    conference_id = 'conf-fe23a767-a75a5b77-20c5-4cca-b581-cbbf0776eca9' # str | Programmable Voice API Conference ID.

    try:
        # Get Conference Information
        api_response = api_instance.get_conference(account_id, conference_id)
        print("The response of ConferencesApi->get_conference:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConferencesApi->get_conference: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Your Bandwidth Account ID. | 
 **conference_id** | **str**| Programmable Voice API Conference ID. | 

### Return type

[**Conference**](Conference.md)

### Authorization

[Basic](../README.md#Basic)

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

# **get_conference_member**
> ConferenceMember get_conference_member(account_id, conference_id, member_id)

Get Conference Member

Returns information about the specified conference member.

### Example

* Basic Authentication (Basic):

```python
import bandwidth
from bandwidth.models.conference_member import ConferenceMember
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
    api_instance = bandwidth.ConferencesApi(api_client)
    account_id = '9900000' # str | Your Bandwidth Account ID.
    conference_id = 'conf-fe23a767-a75a5b77-20c5-4cca-b581-cbbf0776eca9' # str | Programmable Voice API Conference ID.
    member_id = 'c-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85' # str | Programmable Voice API Conference Member ID.

    try:
        # Get Conference Member
        api_response = api_instance.get_conference_member(account_id, conference_id, member_id)
        print("The response of ConferencesApi->get_conference_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConferencesApi->get_conference_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Your Bandwidth Account ID. | 
 **conference_id** | **str**| Programmable Voice API Conference ID. | 
 **member_id** | **str**| Programmable Voice API Conference Member ID. | 

### Return type

[**ConferenceMember**](ConferenceMember.md)

### Authorization

[Basic](../README.md#Basic)

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

# **get_conference_recording**
> ConferenceRecordingMetadata get_conference_recording(account_id, conference_id, recording_id)

Get Conference Recording Information

Returns metadata for the specified recording.

### Example

* Basic Authentication (Basic):

```python
import bandwidth
from bandwidth.models.conference_recording_metadata import ConferenceRecordingMetadata
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
    api_instance = bandwidth.ConferencesApi(api_client)
    account_id = '9900000' # str | Your Bandwidth Account ID.
    conference_id = 'conf-fe23a767-a75a5b77-20c5-4cca-b581-cbbf0776eca9' # str | Programmable Voice API Conference ID.
    recording_id = 'r-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85' # str | Programmable Voice API Recording ID.

    try:
        # Get Conference Recording Information
        api_response = api_instance.get_conference_recording(account_id, conference_id, recording_id)
        print("The response of ConferencesApi->get_conference_recording:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConferencesApi->get_conference_recording: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Your Bandwidth Account ID. | 
 **conference_id** | **str**| Programmable Voice API Conference ID. | 
 **recording_id** | **str**| Programmable Voice API Recording ID. | 

### Return type

[**ConferenceRecordingMetadata**](ConferenceRecordingMetadata.md)

### Authorization

[Basic](../README.md#Basic)

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

# **list_conference_recordings**
> List[ConferenceRecordingMetadata] list_conference_recordings(account_id, conference_id)

Get Conference Recordings

Returns a (potentially empty) list of metadata for the recordings that took place during the specified conference.

### Example

* Basic Authentication (Basic):

```python
import bandwidth
from bandwidth.models.conference_recording_metadata import ConferenceRecordingMetadata
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
    api_instance = bandwidth.ConferencesApi(api_client)
    account_id = '9900000' # str | Your Bandwidth Account ID.
    conference_id = 'conf-fe23a767-a75a5b77-20c5-4cca-b581-cbbf0776eca9' # str | Programmable Voice API Conference ID.

    try:
        # Get Conference Recordings
        api_response = api_instance.list_conference_recordings(account_id, conference_id)
        print("The response of ConferencesApi->list_conference_recordings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConferencesApi->list_conference_recordings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Your Bandwidth Account ID. | 
 **conference_id** | **str**| Programmable Voice API Conference ID. | 

### Return type

[**List[ConferenceRecordingMetadata]**](ConferenceRecordingMetadata.md)

### Authorization

[Basic](../README.md#Basic)

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

# **list_conferences**
> List[Conference] list_conferences(account_id, name=name, min_created_time=min_created_time, max_created_time=max_created_time, page_size=page_size, page_token=page_token)

Get Conferences

Returns a max of 1000 conferences, sorted by `createdTime` from oldest to newest.

**NOTE:** If the number of conferences in the account is bigger than `pageSize`, a `Link` header (with format `<{url}>; rel="next"`) will be returned in the response. The url can be used to retrieve the next page of conference records.

### Example

* Basic Authentication (Basic):

```python
import bandwidth
from bandwidth.models.conference import Conference
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
    api_instance = bandwidth.ConferencesApi(api_client)
    account_id = '9900000' # str | Your Bandwidth Account ID.
    name = 'my-custom-name' # str | Filter results by the `name` field. (optional)
    min_created_time = '2022-06-21T19:13:21Z' # str | Filter results to conferences which have a `createdTime` after or at `minCreatedTime` (in ISO8601 format). (optional)
    max_created_time = '2022-06-21T19:13:21Z' # str | Filter results to conferences which have a `createdTime` before or at `maxCreatedTime` (in ISO8601 format). (optional)
    page_size = 1000 # int | Specifies the max number of conferences that will be returned. (optional) (default to 1000)
    page_token = 'eyJwYWdlVG9rZW4iOiJ0b2tlbiJ9' # str | Not intended for explicit use. To use pagination, follow the links in the `Link` header of the response, as indicated in the endpoint description. (optional)

    try:
        # Get Conferences
        api_response = api_instance.list_conferences(account_id, name=name, min_created_time=min_created_time, max_created_time=max_created_time, page_size=page_size, page_token=page_token)
        print("The response of ConferencesApi->list_conferences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConferencesApi->list_conferences: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Your Bandwidth Account ID. | 
 **name** | **str**| Filter results by the &#x60;name&#x60; field. | [optional] 
 **min_created_time** | **str**| Filter results to conferences which have a &#x60;createdTime&#x60; after or at &#x60;minCreatedTime&#x60; (in ISO8601 format). | [optional] 
 **max_created_time** | **str**| Filter results to conferences which have a &#x60;createdTime&#x60; before or at &#x60;maxCreatedTime&#x60; (in ISO8601 format). | [optional] 
 **page_size** | **int**| Specifies the max number of conferences that will be returned. | [optional] [default to 1000]
 **page_token** | **str**| Not intended for explicit use. To use pagination, follow the links in the &#x60;Link&#x60; header of the response, as indicated in the endpoint description. | [optional] 

### Return type

[**List[Conference]**](Conference.md)

### Authorization

[Basic](../README.md#Basic)

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

# **update_conference**
> update_conference(account_id, conference_id, update_conference)

Update Conference

Update the conference state.

### Example

* Basic Authentication (Basic):

```python
import bandwidth
from bandwidth.models.update_conference import UpdateConference
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
    api_instance = bandwidth.ConferencesApi(api_client)
    account_id = '9900000' # str | Your Bandwidth Account ID.
    conference_id = 'conf-fe23a767-a75a5b77-20c5-4cca-b581-cbbf0776eca9' # str | Programmable Voice API Conference ID.
    update_conference = bandwidth.UpdateConference() # UpdateConference | 

    try:
        # Update Conference
        api_instance.update_conference(account_id, conference_id, update_conference)
    except Exception as e:
        print("Exception when calling ConferencesApi->update_conference: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Your Bandwidth Account ID. | 
 **conference_id** | **str**| Programmable Voice API Conference ID. | 
 **update_conference** | [**UpdateConference**](UpdateConference.md)|  | 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Conference was successfully modified. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**415** | Unsupported Media Type |  -  |
**429** | Too Many Requests |  * Retry-After - When you should try your request again. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_conference_bxml**
> update_conference_bxml(account_id, conference_id, body)

Update Conference BXML

Update the conference BXML document.

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
    api_instance = bandwidth.ConferencesApi(api_client)
    account_id = '9900000' # str | Your Bandwidth Account ID.
    conference_id = 'conf-fe23a767-a75a5b77-20c5-4cca-b581-cbbf0776eca9' # str | Programmable Voice API Conference ID.
    body = <?xml version="1.0" encoding="UTF-8"?>
<Bxml>
    <StopRecording/>
</Bxml> # str | 

    try:
        # Update Conference BXML
        api_instance.update_conference_bxml(account_id, conference_id, body)
    except Exception as e:
        print("Exception when calling ConferencesApi->update_conference_bxml: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Your Bandwidth Account ID. | 
 **conference_id** | **str**| Programmable Voice API Conference ID. | 
 **body** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/xml
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Conference successfully modified. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**415** | Unsupported Media Type |  -  |
**429** | Too Many Requests |  * Retry-After - When you should try your request again. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_conference_member**
> update_conference_member(account_id, conference_id, member_id, update_conference_member)

Update Conference Member

Updates settings for a particular conference member.

### Example

* Basic Authentication (Basic):

```python
import bandwidth
from bandwidth.models.update_conference_member import UpdateConferenceMember
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
    api_instance = bandwidth.ConferencesApi(api_client)
    account_id = '9900000' # str | Your Bandwidth Account ID.
    conference_id = 'conf-fe23a767-a75a5b77-20c5-4cca-b581-cbbf0776eca9' # str | Programmable Voice API Conference ID.
    member_id = 'c-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85' # str | Programmable Voice API Conference Member ID.
    update_conference_member = bandwidth.UpdateConferenceMember() # UpdateConferenceMember | 

    try:
        # Update Conference Member
        api_instance.update_conference_member(account_id, conference_id, member_id, update_conference_member)
    except Exception as e:
        print("Exception when calling ConferencesApi->update_conference_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Your Bandwidth Account ID. | 
 **conference_id** | **str**| Programmable Voice API Conference ID. | 
 **member_id** | **str**| Programmable Voice API Conference Member ID. | 
 **update_conference_member** | [**UpdateConferenceMember**](UpdateConferenceMember.md)|  | 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Conference member was successfully modified. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**415** | Unsupported Media Type |  -  |
**429** | Too Many Requests |  * Retry-After - When you should try your request again. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

