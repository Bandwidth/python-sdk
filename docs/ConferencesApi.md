# bandwidth.ConferencesApi

All URIs are relative to *https://messaging.bandwidth.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_conference_recording**](ConferencesApi.md#download_conference_recording) | **GET** /api/v2/accounts/{accountId}/conferences/{conferenceId}/recordings/{recordingId}/media | Download Conference Recording
[**get_conference**](ConferencesApi.md#get_conference) | **GET** /api/v2/accounts/{accountId}/conferences/{conferenceId} | Get Conference Information
[**get_conference_member**](ConferencesApi.md#get_conference_member) | **GET** /api/v2/accounts/{accountId}/conferences/{conferenceId}/members/{memberId} | Get Conference Member
[**get_conference_recording**](ConferencesApi.md#get_conference_recording) | **GET** /api/v2/accounts/{accountId}/conferences/{conferenceId}/recordings/{recordingId} | Get Conference Recording Information
[**get_conference_recordings**](ConferencesApi.md#get_conference_recordings) | **GET** /api/v2/accounts/{accountId}/conferences/{conferenceId}/recordings | Get Conference Recordings
[**get_conferences**](ConferencesApi.md#get_conferences) | **GET** /api/v2/accounts/{accountId}/conferences | Get Conferences
[**modify_conference**](ConferencesApi.md#modify_conference) | **POST** /api/v2/accounts/{accountId}/conferences/{conferenceId} | Update Conference
[**modify_conference_member**](ConferencesApi.md#modify_conference_member) | **PUT** /api/v2/accounts/{accountId}/conferences/{conferenceId}/members/{memberId} | Update Conference Member


# **download_conference_recording**
> file_type download_conference_recording(account_id, conference_id, recording_id)

Download Conference Recording

Downloads the specified recording file.

### Example

* Basic Authentication (httpBasic):

```python
import time
import bandwidth
from bandwidth.api import conferences_api
from bandwidth.model.api_error import ApiError
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
    api_instance = conferences_api.ConferencesApi(api_client)
    account_id = "accountId_example" # str | 
    conference_id = "conferenceId_example" # str | 
    recording_id = "recordingId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Download Conference Recording
        api_response = api_instance.download_conference_recording(account_id, conference_id, recording_id)
        pprint(api_response)
    except bandwidth.ApiException as e:
        print("Exception when calling ConferencesApi->download_conference_recording: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  |
 **conference_id** | **str**|  |
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

# **get_conference**
> ConferenceState get_conference(account_id, conference_id)

Get Conference Information

Returns information about the specified conference.

### Example

* Basic Authentication (httpBasic):

```python
import time
import bandwidth
from bandwidth.api import conferences_api
from bandwidth.model.api_error import ApiError
from bandwidth.model.conference_state import ConferenceState
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
    api_instance = conferences_api.ConferencesApi(api_client)
    account_id = "accountId_example" # str | 
    conference_id = "conferenceId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get Conference Information
        api_response = api_instance.get_conference(account_id, conference_id)
        pprint(api_response)
    except bandwidth.ApiException as e:
        print("Exception when calling ConferencesApi->get_conference: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  |
 **conference_id** | **str**|  |

### Return type

[**ConferenceState**](ConferenceState.md)

### Authorization

[httpBasic](../README.md#httpBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Conference found |  -  |
**400** | Something&#39;s not quite right... Your request is invalid. Please fix it before trying again. |  -  |
**401** | Your credentials are invalid. Please use your Bandwidth dashboard credentials to authenticate to the API. |  -  |
**403** | User unauthorized to perform this action. |  -  |
**404** | The resource specified cannot be found or does not belong to you. |  -  |
**415** | We don&#39;t support that media type. If a request body is required, please send it to us as &#x60;application/json&#x60;. |  -  |
**429** | You&#39;re sending requests to this endpoint too frequently. Please slow your request rate down and try again. |  * Retry-After - When you should try your request again <br>  |
**500** | Something unexpected happened. Please try again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_conference_member**
> ConferenceMemberState get_conference_member(account_id, conference_id, member_id)

Get Conference Member

Returns information about the specified conference member.

### Example

* Basic Authentication (httpBasic):

```python
import time
import bandwidth
from bandwidth.api import conferences_api
from bandwidth.model.api_error import ApiError
from bandwidth.model.conference_member_state import ConferenceMemberState
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
    api_instance = conferences_api.ConferencesApi(api_client)
    account_id = "accountId_example" # str | 
    conference_id = "conferenceId_example" # str | 
    member_id = "memberId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get Conference Member
        api_response = api_instance.get_conference_member(account_id, conference_id, member_id)
        pprint(api_response)
    except bandwidth.ApiException as e:
        print("Exception when calling ConferencesApi->get_conference_member: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  |
 **conference_id** | **str**|  |
 **member_id** | **str**|  |

### Return type

[**ConferenceMemberState**](ConferenceMemberState.md)

### Authorization

[httpBasic](../README.md#httpBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Conference member found |  -  |
**400** | Something&#39;s not quite right... Your request is invalid. Please fix it before trying again. |  -  |
**401** | Your credentials are invalid. Please use your Bandwidth dashboard credentials to authenticate to the API. |  -  |
**403** | User unauthorized to perform this action. |  -  |
**404** | The resource specified cannot be found or does not belong to you. |  -  |
**415** | We don&#39;t support that media type. If a request body is required, please send it to us as &#x60;application/json&#x60;. |  -  |
**429** | You&#39;re sending requests to this endpoint too frequently. Please slow your request rate down and try again. |  * Retry-After - When you should try your request again <br>  |
**500** | Something unexpected happened. Please try again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_conference_recording**
> CallRecordingMetadata get_conference_recording(account_id, conference_id, recording_id)

Get Conference Recording Information

Returns metadata for the specified recording.

### Example

* Basic Authentication (httpBasic):

```python
import time
import bandwidth
from bandwidth.api import conferences_api
from bandwidth.model.api_error import ApiError
from bandwidth.model.call_recording_metadata import CallRecordingMetadata
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
    api_instance = conferences_api.ConferencesApi(api_client)
    account_id = "accountId_example" # str | 
    conference_id = "conferenceId_example" # str | 
    recording_id = "recordingId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get Conference Recording Information
        api_response = api_instance.get_conference_recording(account_id, conference_id, recording_id)
        pprint(api_response)
    except bandwidth.ApiException as e:
        print("Exception when calling ConferencesApi->get_conference_recording: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  |
 **conference_id** | **str**|  |
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

# **get_conference_recordings**
> [ConferenceRecordingMetadata] get_conference_recordings(account_id, conference_id)

Get Conference Recordings

Returns a (potentially empty) list of metadata for the recordings that took place during the specified conference.

### Example

* Basic Authentication (httpBasic):

```python
import time
import bandwidth
from bandwidth.api import conferences_api
from bandwidth.model.api_error import ApiError
from bandwidth.model.conference_recording_metadata import ConferenceRecordingMetadata
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
    api_instance = conferences_api.ConferencesApi(api_client)
    account_id = "accountId_example" # str | 
    conference_id = "conferenceId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get Conference Recordings
        api_response = api_instance.get_conference_recordings(account_id, conference_id)
        pprint(api_response)
    except bandwidth.ApiException as e:
        print("Exception when calling ConferencesApi->get_conference_recordings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  |
 **conference_id** | **str**|  |

### Return type

[**[ConferenceRecordingMetadata]**](ConferenceRecordingMetadata.md)

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

# **get_conferences**
> [ConferenceState] get_conferences(account_id)

Get Conferences

Returns a max of 1000 conferences, sorted by `createdTime` from oldest to newest.  **NOTE:** If the number of conferences in the account is bigger than `pageSize`, a `Link` header (with format `<{url}>; rel=\"next\"`) will be returned in the response. The url can be used to retrieve the next page of conference records.

### Example

* Basic Authentication (httpBasic):

```python
import time
import bandwidth
from bandwidth.api import conferences_api
from bandwidth.model.api_error import ApiError
from bandwidth.model.conference_state import ConferenceState
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
    api_instance = conferences_api.ConferencesApi(api_client)
    account_id = "accountId_example" # str | 
    name = "name_example" # str | Filter results by the `name` field. (optional)
    min_created_time = "minCreatedTime_example" # str | Filter results to conferences which have a `createdTime` after or at `minCreatedTime` (in ISO8601 format). (optional)
    max_created_time = "maxCreatedTime_example" # str | Filter results to conferences which have a `createdTime` before or at `maxCreatedTime` (in ISO8601 format). (optional)
    page_size = 1000 # int | Specifies the max number of conferences that will be returned. Range: integer values between 1 - 1000. Default value is 1000. (optional) if omitted the server will use the default value of 1000
    page_token = "pageToken_example" # str | Not intended for explicit use. To use pagination, follow the links in the `Link` header of the response, as indicated in the endpoint description. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Conferences
        api_response = api_instance.get_conferences(account_id)
        pprint(api_response)
    except bandwidth.ApiException as e:
        print("Exception when calling ConferencesApi->get_conferences: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Conferences
        api_response = api_instance.get_conferences(account_id, name=name, min_created_time=min_created_time, max_created_time=max_created_time, page_size=page_size, page_token=page_token)
        pprint(api_response)
    except bandwidth.ApiException as e:
        print("Exception when calling ConferencesApi->get_conferences: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  |
 **name** | **str**| Filter results by the &#x60;name&#x60; field. | [optional]
 **min_created_time** | **str**| Filter results to conferences which have a &#x60;createdTime&#x60; after or at &#x60;minCreatedTime&#x60; (in ISO8601 format). | [optional]
 **max_created_time** | **str**| Filter results to conferences which have a &#x60;createdTime&#x60; before or at &#x60;maxCreatedTime&#x60; (in ISO8601 format). | [optional]
 **page_size** | **int**| Specifies the max number of conferences that will be returned. Range: integer values between 1 - 1000. Default value is 1000. | [optional] if omitted the server will use the default value of 1000
 **page_token** | **str**| Not intended for explicit use. To use pagination, follow the links in the &#x60;Link&#x60; header of the response, as indicated in the endpoint description. | [optional]

### Return type

[**[ConferenceState]**](ConferenceState.md)

### Authorization

[httpBasic](../README.md#httpBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Conferences retrieved successfully |  -  |
**400** | Something&#39;s not quite right... Your request is invalid. Please fix it before trying again. |  -  |
**401** | Your credentials are invalid. Please use your Bandwidth dashboard credentials to authenticate to the API. |  -  |
**403** | User unauthorized to perform this action. |  -  |
**404** | The resource specified cannot be found or does not belong to you. |  -  |
**415** | We don&#39;t support that media type. If a request body is required, please send it to us as &#x60;application/json&#x60;. |  -  |
**429** | You&#39;re sending requests to this endpoint too frequently. Please slow your request rate down and try again. |  * Retry-After - When you should try your request again <br>  |
**500** | Something unexpected happened. Please try again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_conference**
> modify_conference(account_id, conference_id, modify_conference_request)

Update Conference

Modify the conference state.

### Example

* Basic Authentication (httpBasic):

```python
import time
import bandwidth
from bandwidth.api import conferences_api
from bandwidth.model.modify_conference_request import ModifyConferenceRequest
from bandwidth.model.api_error import ApiError
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
    api_instance = conferences_api.ConferencesApi(api_client)
    account_id = "accountId_example" # str | 
    conference_id = "conferenceId_example" # str | 
    modify_conference_request = ModifyConferenceRequest(
        status="active",
        redirect_url="redirect_url_example",
        redirect_fallback_url="redirect_fallback_url_example",
        redirect_method="POST",
        redirect_fallback_method="POST",
        username="username_example",
        password="password_example",
        fallback_username="fallback_username_example",
        fallback_password="fallback_password_example",
    ) # ModifyConferenceRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Update Conference
        api_instance.modify_conference(account_id, conference_id, modify_conference_request)
    except bandwidth.ApiException as e:
        print("Exception when calling ConferencesApi->modify_conference: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  |
 **conference_id** | **str**|  |
 **modify_conference_request** | [**ModifyConferenceRequest**](ModifyConferenceRequest.md)|  |

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
**204** | Conference successfully modified |  -  |
**400** | Something&#39;s not quite right... Your request is invalid. Please fix it before trying again. |  -  |
**401** | Your credentials are invalid. Please use your Bandwidth dashboard credentials to authenticate to the API. |  -  |
**403** | User unauthorized to perform this action. |  -  |
**404** | The resource specified cannot be found or does not belong to you. |  -  |
**415** | We don&#39;t support that media type. If a request body is required, please send it to us as &#x60;application/json&#x60;. |  -  |
**429** | You&#39;re sending requests to this endpoint too frequently. Please slow your request rate down and try again. |  * Retry-After - When you should try your request again <br>  |
**500** | Something unexpected happened. Please try again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_conference_member**
> modify_conference_member(account_id, conference_id, member_id, conference_member_state)

Update Conference Member

Updates settings for a particular conference member.

### Example

* Basic Authentication (httpBasic):

```python
import time
import bandwidth
from bandwidth.api import conferences_api
from bandwidth.model.api_error import ApiError
from bandwidth.model.conference_member_state import ConferenceMemberState
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
    api_instance = conferences_api.ConferencesApi(api_client)
    account_id = "accountId_example" # str | 
    conference_id = "conferenceId_example" # str | 
    member_id = "memberId_example" # str | 
    conference_member_state = ConferenceMemberState(
        call_id="call_id_example",
        conference_id="conference_id_example",
        member_url="member_url_example",
        mute=True,
        hold=True,
        call_ids_to_coach=[
            "call_ids_to_coach_example",
        ],
    ) # ConferenceMemberState | 

    # example passing only required values which don't have defaults set
    try:
        # Update Conference Member
        api_instance.modify_conference_member(account_id, conference_id, member_id, conference_member_state)
    except bandwidth.ApiException as e:
        print("Exception when calling ConferencesApi->modify_conference_member: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  |
 **conference_id** | **str**|  |
 **member_id** | **str**|  |
 **conference_member_state** | [**ConferenceMemberState**](ConferenceMemberState.md)|  |

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
**204** | Conference member successfully modified |  -  |
**400** | Something&#39;s not quite right... Your request is invalid. Please fix it before trying again. |  -  |
**401** | Your credentials are invalid. Please use your Bandwidth dashboard credentials to authenticate to the API. |  -  |
**403** | User unauthorized to perform this action. |  -  |
**404** | The resource specified cannot be found or does not belong to you. |  -  |
**415** | We don&#39;t support that media type. If a request body is required, please send it to us as &#x60;application/json&#x60;. |  -  |
**429** | You&#39;re sending requests to this endpoint too frequently. Please slow your request rate down and try again. |  * Retry-After - When you should try your request again <br>  |
**500** | Something unexpected happened. Please try again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

