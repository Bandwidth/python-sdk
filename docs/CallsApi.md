# bandwidth.CallsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_call**](CallsApi.md#create_call) | **POST** /accounts/{accountId}/calls | Create Call
[**get_call_state**](CallsApi.md#get_call_state) | **GET** /accounts/{accountId}/calls/{callId} | Get Call State Information
[**update_call**](CallsApi.md#update_call) | **POST** /accounts/{accountId}/calls/{callId} | Update Call
[**update_call_bxml**](CallsApi.md#update_call_bxml) | **PUT** /accounts/{accountId}/calls/{callId}/bxml | Update Call BXML


# **create_call**
> CreateCallResponse create_call(account_id, create_call)

Create Call

Creates an outbound phone call.  All calls are initially queued. Your outbound calls will initiated at a specific dequeueing rate, enabling your application to \"fire and forget\" when creating calls. Queued calls may not be modified until they are dequeued and placed, but may be removed from your queue on demand.  <b>Please note:</b> Calls submitted to your queue will be placed approximately in order, but exact ordering is not guaranteed.

### Example

* Basic Authentication (Basic):

```python
import time
import bandwidth
from bandwidth.api import calls_api
from bandwidth.model.create_call import CreateCall
from bandwidth.model.create_call_response import CreateCallResponse
from bandwidth.model.voice_api_error import VoiceApiError
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with bandwidth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = calls_api.CallsApi(api_client)
    account_id = "9900000" # str | Your Bandwidth Account ID
    create_call = CreateCall(
        to="+19195551234",
        _from="+19195554321",
        uui="eyJhbGciOiJIUzI1NiJ9.WyJoaSJd.-znkjYyCkgz4djmHUPSXl9YrJ6Nix_XvmlwKGFh5ERM;encoding=jwt,aGVsbG8gd29ybGQ=;encoding=base64",
        application_id="1234-qwer-5679-tyui",
        answer_url="https://www.myCallbackServer.com/webhooks/answer",
        answer_method=CallbackMethodEnum("POST"),
        username="mySecretUsername",
        password="mySecretPassword1!",
        answer_fallback_url="https://www.myFallbackServer.com/webhooks/answer",
        answer_fallback_method=CallbackMethodEnum("POST"),
        fallback_username="mySecretUsername",
        fallback_password="mySecretPassword1!",
        disconnect_url="disconnect_url_example",
        disconnect_method=CallbackMethodEnum("POST"),
        call_timeout=30,
        callback_timeout=15,
        machine_detection=MachineDetectionConfiguration(
            mode=MachineDetectionModeEnum("async"),
            detection_timeout=15,
            silence_timeout=10,
            speech_threshold=10,
            speech_end_threshold=5,
            machine_speech_end_threshold=5,
            delay_result=False,
            callback_url="https://myServer.com/bandwidth/webhooks/machineDetectionComplete",
            callback_method=CallbackMethodEnum("POST"),
            username="mySecretUsername",
            password="mySecretPassword1!",
            fallback_url="https://myFallbackServer.com/bandwidth/webhooks/machineDetectionComplete",
            fallback_method=CallbackMethodEnum("POST"),
            fallback_username="mySecretUsername",
            fallback_password="mySecretPassword1!",
        ),
        priority=5,
        tag="tag_example",
    ) # CreateCall | JSON object containing information to create an outbound call

    # example passing only required values which don't have defaults set
    try:
        # Create Call
        api_response = api_instance.create_call(account_id, create_call)
        pprint(api_response)
    except bandwidth.ApiException as e:
        print("Exception when calling CallsApi->create_call: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Your Bandwidth Account ID |
 **create_call** | [**CreateCall**](CreateCall.md)| JSON object containing information to create an outbound call |

### Return type

[**CreateCallResponse**](CreateCallResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Call Successfully Created |  * Location - The URL for further interactions with this call <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**415** | Unsupported Media Type |  -  |
**429** | Too Many Requests |  * Retry-After - When you should try your request again <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_call_state**
> CallState get_call_state(account_id, call_id)

Get Call State Information

Retrieve the current state of a specific call. This information is near-realtime, so it may take a few minutes for your call to be accessible using this endpoint.  **Note**: Call information is kept for 7 days after the calls are hung up. If you attempt to retrieve information for a call that is older than 7 days, you will get an HTTP 404 response.

### Example

* Basic Authentication (Basic):

```python
import time
import bandwidth
from bandwidth.api import calls_api
from bandwidth.model.call_state import CallState
from bandwidth.model.voice_api_error import VoiceApiError
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with bandwidth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = calls_api.CallsApi(api_client)
    account_id = "9900000" # str | Your Bandwidth Account ID
    call_id = "c-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85" # str | Programmable Voice API Call ID

    # example passing only required values which don't have defaults set
    try:
        # Get Call State Information
        api_response = api_instance.get_call_state(account_id, call_id)
        pprint(api_response)
    except bandwidth.ApiException as e:
        print("Exception when calling CallsApi->get_call_state: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Your Bandwidth Account ID |
 **call_id** | **str**| Programmable Voice API Call ID |

### Return type

[**CallState**](CallState.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Call found |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**415** | Unsupported Media Type |  -  |
**429** | Too Many Requests |  * Retry-After - When you should try your request again <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_call**
> update_call(account_id, call_id, update_call)

Update Call

Interrupts and redirects a call to a different URL that should return a BXML document.

### Example

* Basic Authentication (Basic):

```python
import time
import bandwidth
from bandwidth.api import calls_api
from bandwidth.model.update_call import UpdateCall
from bandwidth.model.voice_api_error import VoiceApiError
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with bandwidth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = calls_api.CallsApi(api_client)
    account_id = "9900000" # str | Your Bandwidth Account ID
    call_id = "c-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85" # str | Programmable Voice API Call ID
    update_call = UpdateCall(
        state=CallStateEnum("active"),
        redirect_url="https://myServer.com/bandwidth/webhooks/redirect",
        redirect_method=RedirectMethodEnum("POST"),
        username="mySecretUsername",
        password="mySecretPassword1!",
        redirect_fallback_url="https://myFallbackServer.com/bandwidth/webhooks/redirect",
        redirect_fallback_method=RedirectMethodEnum("POST"),
        fallback_username="mySecretUsername",
        fallback_password="mySecretPassword1!",
        tag="My Custom Tag",
    ) # UpdateCall | JSON object containing information to redirect an existing call to a new BXML document

    # example passing only required values which don't have defaults set
    try:
        # Update Call
        api_instance.update_call(account_id, call_id, update_call)
    except bandwidth.ApiException as e:
        print("Exception when calling CallsApi->update_call: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Your Bandwidth Account ID |
 **call_id** | **str**| Programmable Voice API Call ID |
 **update_call** | [**UpdateCall**](UpdateCall.md)| JSON object containing information to redirect an existing call to a new BXML document |

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
**200** | Call Successfully Modified |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**415** | Unsupported Media Type |  -  |
**429** | Too Many Requests |  * Retry-After - When you should try your request again <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_call_bxml**
> update_call_bxml(account_id, call_id, body)

Update Call BXML

Interrupts and replaces an active call's BXML document.

### Example

* Basic Authentication (Basic):

```python
import time
import bandwidth
from bandwidth.api import calls_api
from bandwidth.model.voice_api_error import VoiceApiError
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with bandwidth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = calls_api.CallsApi(api_client)
    account_id = "9900000" # str | Your Bandwidth Account ID
    call_id = "c-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85" # str | Programmable Voice API Call ID
    body = '''<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<Bxml>
  <SpeakSentence>This is a test sentence.</SpeakSentence>
</Bxml>''' # str | 

    # example passing only required values which don't have defaults set
    try:
        # Update Call BXML
        api_instance.update_call_bxml(account_id, call_id, body)
    except bandwidth.ApiException as e:
        print("Exception when calling CallsApi->update_call_bxml: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Your Bandwidth Account ID |
 **call_id** | **str**| Programmable Voice API Call ID |
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
**204** | Call BXML Successfully Replaced |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**415** | Unsupported Media Type |  -  |
**429** | Too Many Requests |  * Retry-After - When you should try your request again <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

