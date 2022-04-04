# bandwidth.CallsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_call**](CallsApi.md#create_call) | **POST** /api/v2/accounts/{accountId}/calls | Create Call
[**get_call**](CallsApi.md#get_call) | **GET** /api/v2/accounts/{accountId}/calls/{callId} | Get Call Information
[**modify_call**](CallsApi.md#modify_call) | **POST** /api/v2/accounts/{accountId}/calls/{callId} | Modify Call


# **create_call**
> CreateCallResponse create_call(account_id, create_call_request)

Create Call

Creates an outbound phone call.  Calls are created immediately unless your account has outbound call queueing enabled. When enabled, your outbound calls will be queued and initiated at a specific dequeueing rate, enabling your application to \"fire and forget\" when creating calls. Queued calls may not be modified until they are dequeued and placed, but may be removed from your queue on demand.  To enable call queueing on your account, contact our Account Management team.  <b>Please note: </b> Calls submitted to your queue will be placed aproximately in order, but exact ordering is not guaranteed.

### Example

* Basic Authentication (httpBasic):

```python
import time
import bandwidth
from bandwidth.api import calls_api
from bandwidth.model.api_error import ApiError
from bandwidth.model.create_call_response import CreateCallResponse
from bandwidth.model.create_call_request import CreateCallRequest
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
    api_instance = calls_api.CallsApi(api_client)
    account_id = "accountId_example" # str | 
    create_call_request = CreateCallRequest(
        _from="+15555555555",
        to="+15555555555, sip:john@doe.com",
        uui="eyJhbGciOiJIUzI1NiJ9.WyJoaSJd.-znkjYyCkgz4djmHUPSXl9YrJ6Nix_XvmlwKGFh5ERM;encoding=jwt,aGVsbG8gd29ybGQ=;encoding=base64",
        call_timeout=3.14,
        callback_timeout=3.14,
        answer_url="answer_url_example",
        answer_fallback_url="answer_fallback_url_example",
        username="username_example",
        password="password_example",
        fallback_username="fallback_username_example",
        fallback_password="fallback_password_example",
        answer_method="POST",
        answer_fallback_method="POST",
        disconnect_url="disconnect_url_example",
        disconnect_method="POST",
        tag="tag_example",
        application_id="application_id_example",
        machine_detection=MachineDetectionConfiguration(
            mode="async",
            detection_timeout=15,
            silence_timeout=10,
            speech_threshold=10,
            speech_end_threshold=5,
            delay_result=False,
            callback_url="callback_url_example",
            callback_method="POST",
            fallback_url="fallback_url_example",
            fallback_method="POST",
            username="username_example",
            password="password_example",
            fallback_username="fallback_username_example",
            fallback_password="fallback_password_example",
        ),
        priority=5,
    ) # CreateCallRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create Call
        api_response = api_instance.create_call(account_id, create_call_request)
        pprint(api_response)
    except bandwidth.ApiException as e:
        print("Exception when calling CallsApi->create_call: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  |
 **create_call_request** | [**CreateCallRequest**](CreateCallRequest.md)|  |

### Return type

[**CreateCallResponse**](CreateCallResponse.md)

### Authorization

[httpBasic](../README.md#httpBasic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Call successfully created |  * Location - The URL for further interactions with this call <br>  |
**400** | Something&#39;s not quite right... Your request is invalid. Please fix it before trying again. |  -  |
**401** | Your credentials are invalid. Please use your Bandwidth dashboard credentials to authenticate to the API. |  -  |
**403** | User unauthorized to perform this action. |  -  |
**404** | The resource specified cannot be found or does not belong to you. |  -  |
**415** | We don&#39;t support that media type. If a request body is required, please send it to us as &#x60;application/json&#x60;. |  -  |
**429** | You&#39;re sending requests to this endpoint too frequently. Please slow your request rate down and try again. |  * Retry-After - When you should try your request again <br>  |
**500** | Something unexpected happened. Please try again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_call**
> CallState get_call(account_id, call_id)

Get Call Information

Retrieve the current state of a specific call. This information is near-realtime, so it may take a few minutes for your call to be accessible using this endpoint.<br><br>**Note**: Call information is kept for 7 days after the calls are hung up. If you attempt to retrieve information for a call that is older than 7 days, you will get an HTTP 404 response.  The `disconnectCause` for a call can be: - `hangup`: one party hung up the call, a [`<Hangup>`](../../bxml/verbs/hangup.md) verb was executed, or there was no more BXML to execute; it indicates that the call ended normally. - `busy`: the callee was busy. - `timeout`: the call wasn't answered before the `callTimeout` was reached. - `cancel`: the call was cancelled by its originator while it was ringing. - `rejected`: the call was rejected by the callee. - `callback-error`: a BXML callback couldn't be delivered to your callback server. - `invalid-bxml`: invalid BXML was returned in response to a callback. - `application-error`: an unsupported action was tried on the call, e.g. trying to play a .ogg audio. - `account-limit`: the account rate limits were reached. - `node-capacity-exceeded`: the system maximum capacity was reached. - `error`: some error not described in any of the other causes happened on the call. - `unknown`: some unknown error happened on the call.  Note: this list is not exhaustive and other values can appear in the future.

### Example

* Basic Authentication (httpBasic):

```python
import time
import bandwidth
from bandwidth.api import calls_api
from bandwidth.model.api_error import ApiError
from bandwidth.model.call_state import CallState
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
    api_instance = calls_api.CallsApi(api_client)
    account_id = "accountId_example" # str | 
    call_id = "callId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get Call Information
        api_response = api_instance.get_call(account_id, call_id)
        pprint(api_response)
    except bandwidth.ApiException as e:
        print("Exception when calling CallsApi->get_call: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  |
 **call_id** | **str**|  |

### Return type

[**CallState**](CallState.md)

### Authorization

[httpBasic](../README.md#httpBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Call found |  -  |
**400** | Something&#39;s not quite right... Your request is invalid. Please fix it before trying again. |  -  |
**401** | Your credentials are invalid. Please use your Bandwidth dashboard credentials to authenticate to the API. |  -  |
**403** | User unauthorized to perform this action. |  -  |
**404** | The resource specified cannot be found or does not belong to you. |  -  |
**415** | We don&#39;t support that media type. If a request body is required, please send it to us as &#x60;application/json&#x60;. |  -  |
**429** | You&#39;re sending requests to this endpoint too frequently. Please slow your request rate down and try again. |  * Retry-After - When you should try your request again <br>  |
**500** | Something unexpected happened. Please try again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_call**
> modify_call(account_id, call_id, modify_call_request)

Modify Call

Interrupts and replaces an active call's BXML document. Two content types may be used: JSON, which allows hanging up the call or triggering a callback to fetch the new BXML; and XML, which allows sending the new BXML immediately.

### Example

* Basic Authentication (httpBasic):

```python
import time
import bandwidth
from bandwidth.api import calls_api
from bandwidth.model.api_error import ApiError
from bandwidth.model.modify_call_request import ModifyCallRequest
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
    api_instance = calls_api.CallsApi(api_client)
    account_id = "accountId_example" # str | 
    call_id = "callId_example" # str | 
    modify_call_request = ModifyCallRequest(
        state="active",
        redirect_url="redirect_url_example",
        redirect_fallback_url="redirect_fallback_url_example",
        redirect_method="POST",
        redirect_fallback_method="POST",
        username="username_example",
        password="password_example",
        fallback_username="fallback_username_example",
        fallback_password="fallback_password_example",
        tag="tag_example",
    ) # ModifyCallRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Modify Call
        api_instance.modify_call(account_id, call_id, modify_call_request)
    except bandwidth.ApiException as e:
        print("Exception when calling CallsApi->modify_call: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  |
 **call_id** | **str**|  |
 **modify_call_request** | [**ModifyCallRequest**](ModifyCallRequest.md)|  |

### Return type

void (empty response body)

### Authorization

[httpBasic](../README.md#httpBasic)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Call successfully modified |  -  |
**400** | Something&#39;s not quite right... Your request is invalid. Please fix it before trying again. |  -  |
**401** | Your credentials are invalid. Please use your Bandwidth dashboard credentials to authenticate to the API. |  -  |
**403** | User unauthorized to perform this action. |  -  |
**404** | The resource specified cannot be found or does not belong to you. |  -  |
**415** | We don&#39;t support that media type. If a request body is required, please send it to us as &#x60;application/json&#x60;. |  -  |
**429** | You&#39;re sending requests to this endpoint too frequently. Please slow your request rate down and try again. |  * Retry-After - When you should try your request again <br>  |
**500** | Something unexpected happened. Please try again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

