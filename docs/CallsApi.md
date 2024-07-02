# bandwidth.CallsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_call**](CallsApi.md#create_call) | **POST** /accounts/{accountId}/calls | Create Call
[**get_call_state**](CallsApi.md#get_call_state) | **GET** /accounts/{accountId}/calls/{callId} | Get Call State Information
[**list_calls**](CallsApi.md#list_calls) | **GET** /accounts/{accountId}/calls | Get Calls
[**update_call**](CallsApi.md#update_call) | **POST** /accounts/{accountId}/calls/{callId} | Update Call
[**update_call_bxml**](CallsApi.md#update_call_bxml) | **PUT** /accounts/{accountId}/calls/{callId}/bxml | Update Call BXML


# **create_call**
> CreateCallResponse create_call(account_id, create_call)

Create Call

Creates an outbound phone call.  All calls are initially queued. Your outbound calls will initiated at a specific dequeueing rate, enabling your application to \"fire and forget\" when creating calls. Queued calls may not be modified until they are dequeued and placed, but may be removed from your queue on demand.  <b>Please note:</b> Calls submitted to your queue will be placed approximately in order, but exact ordering is not guaranteed.

### Example

* Basic Authentication (Basic):

```python
import bandwidth
from bandwidth.models.create_call import CreateCall
from bandwidth.models.create_call_response import CreateCallResponse
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
    api_instance = bandwidth.CallsApi(api_client)
    account_id = '9900000' # str | Your Bandwidth Account ID.
    create_call = bandwidth.CreateCall() # CreateCall | JSON object containing information to create an outbound call

    try:
        # Create Call
        api_response = api_instance.create_call(account_id, create_call)
        print("The response of CallsApi->create_call:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CallsApi->create_call: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Your Bandwidth Account ID. | 
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
**429** | Too Many Requests |  * Retry-After - When you should try your request again. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_call_state**
> CallState get_call_state(account_id, call_id)

Get Call State Information

Retrieve the current state of a specific call. This information is near-realtime, so it may take a few minutes for your call to be accessible using this endpoint.  **Note**: Call information is kept for 7 days after the calls are hung up. If you attempt to retrieve information for a call that is older than 7 days, you will get an HTTP 404 response.

### Example

* Basic Authentication (Basic):

```python
import bandwidth
from bandwidth.models.call_state import CallState
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
    api_instance = bandwidth.CallsApi(api_client)
    account_id = '9900000' # str | Your Bandwidth Account ID.
    call_id = 'c-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85' # str | Programmable Voice API Call ID.

    try:
        # Get Call State Information
        api_response = api_instance.get_call_state(account_id, call_id)
        print("The response of CallsApi->get_call_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CallsApi->get_call_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Your Bandwidth Account ID. | 
 **call_id** | **str**| Programmable Voice API Call ID. | 

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
**429** | Too Many Requests |  * Retry-After - When you should try your request again. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_calls**
> List[CallState] list_calls(account_id, to=to, var_from=var_from, min_start_time=min_start_time, max_start_time=max_start_time, disconnect_cause=disconnect_cause, page_size=page_size, page_token=page_token)

Get Calls

Returns a max of 10000 calls, sorted by `createdTime` from oldest to newest.  **NOTE:** If the number of calls in the account is bigger than `pageSize`, a `Link` header (with format `<{url}>; rel=\"next\"`) will be returned in the response. The url can be used to retrieve the next page of call records. Also, call information is kept for 7 days after the calls are hung up. If you attempt to retrieve information for a call that is older than 7 days, you will get an empty array [] in response.

### Example

* Basic Authentication (Basic):

```python
import bandwidth
from bandwidth.models.call_state import CallState
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
    api_instance = bandwidth.CallsApi(api_client)
    account_id = '9900000' # str | Your Bandwidth Account ID.
    to = '%2b19195551234' # str | Filter results by the `to` field. (optional)
    var_from = '%2b19195554321' # str | Filter results by the `from` field. (optional)
    min_start_time = '2022-06-21T19:13:21Z' # str | Filter results to calls which have a `startTime` after or including `minStartTime` (in ISO8601 format). (optional)
    max_start_time = '2022-06-21T19:13:21Z' # str | Filter results to calls which have a `startTime` before or including `maxStartTime` (in ISO8601 format). (optional)
    disconnect_cause = 'hangup' # str | Filter results to calls with specified call Disconnect Cause. (optional)
    page_size = 1000 # int | Specifies the max number of calls that will be returned. (optional) (default to 1000)
    page_token = 'page_token_example' # str | Not intended for explicit use. To use pagination, follow the links in the `Link` header of the response, as indicated in the endpoint description. (optional)

    try:
        # Get Calls
        api_response = api_instance.list_calls(account_id, to=to, var_from=var_from, min_start_time=min_start_time, max_start_time=max_start_time, disconnect_cause=disconnect_cause, page_size=page_size, page_token=page_token)
        print("The response of CallsApi->list_calls:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CallsApi->list_calls: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Your Bandwidth Account ID. | 
 **to** | **str**| Filter results by the &#x60;to&#x60; field. | [optional] 
 **var_from** | **str**| Filter results by the &#x60;from&#x60; field. | [optional] 
 **min_start_time** | **str**| Filter results to calls which have a &#x60;startTime&#x60; after or including &#x60;minStartTime&#x60; (in ISO8601 format). | [optional] 
 **max_start_time** | **str**| Filter results to calls which have a &#x60;startTime&#x60; before or including &#x60;maxStartTime&#x60; (in ISO8601 format). | [optional] 
 **disconnect_cause** | **str**| Filter results to calls with specified call Disconnect Cause. | [optional] 
 **page_size** | **int**| Specifies the max number of calls that will be returned. | [optional] [default to 1000]
 **page_token** | **str**| Not intended for explicit use. To use pagination, follow the links in the &#x60;Link&#x60; header of the response, as indicated in the endpoint description. | [optional] 

### Return type

[**List[CallState]**](CallState.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Calls retrieved successfully |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**415** | Unsupported Media Type |  -  |
**429** | Too Many Requests |  * Retry-After - When you should try your request again. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_call**
> update_call(account_id, call_id, update_call)

Update Call

Interrupts and redirects a call to a different URL that should return a BXML document.

### Example

* Basic Authentication (Basic):

```python
import bandwidth
from bandwidth.models.update_call import UpdateCall
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
    api_instance = bandwidth.CallsApi(api_client)
    account_id = '9900000' # str | Your Bandwidth Account ID.
    call_id = 'c-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85' # str | Programmable Voice API Call ID.
    update_call = bandwidth.UpdateCall() # UpdateCall | JSON object containing information to redirect an existing call to a new BXML document

    try:
        # Update Call
        api_instance.update_call(account_id, call_id, update_call)
    except Exception as e:
        print("Exception when calling CallsApi->update_call: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Your Bandwidth Account ID. | 
 **call_id** | **str**| Programmable Voice API Call ID. | 
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
**200** | Call was successfully modified. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**409** | Conflict |  -  |
**415** | Unsupported Media Type |  -  |
**429** | Too Many Requests |  * Retry-After - When you should try your request again. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_call_bxml**
> update_call_bxml(account_id, call_id, body)

Update Call BXML

Interrupts and replaces an active call's BXML document.

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
    api_instance = bandwidth.CallsApi(api_client)
    account_id = '9900000' # str | Your Bandwidth Account ID.
    call_id = 'c-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85' # str | Programmable Voice API Call ID.
    body = <?xml version=\"1.0\" encoding=\"UTF-8\"?>
<Bxml>
  <SpeakSentence>This is a test sentence.</SpeakSentence>
</Bxml> # str | 

    try:
        # Update Call BXML
        api_instance.update_call_bxml(account_id, call_id, body)
    except Exception as e:
        print("Exception when calling CallsApi->update_call_bxml: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Your Bandwidth Account ID. | 
 **call_id** | **str**| Programmable Voice API Call ID. | 
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
**204** | Call BXML was successfully replaced. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**409** | Conflict |  -  |
**415** | Unsupported Media Type |  -  |
**429** | Too Many Requests |  * Retry-After - When you should try your request again. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

