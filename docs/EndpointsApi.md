# bandwidth.EndpointsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_endpoint**](EndpointsApi.md#create_endpoint) | **POST** /accounts/{accountId}/endpoints | Create Endpoint
[**delete_endpoint**](EndpointsApi.md#delete_endpoint) | **DELETE** /accounts/{accountId}/endpoints/{endpointId} | Delete Endpoint
[**get_endpoint**](EndpointsApi.md#get_endpoint) | **GET** /accounts/{accountId}/endpoints/{endpointId} | Get Endpoint
[**list_endpoints**](EndpointsApi.md#list_endpoints) | **GET** /accounts/{accountId}/endpoints | List Endpoints
[**update_endpoint_bxml**](EndpointsApi.md#update_endpoint_bxml) | **PUT** /accounts/{accountId}/endpoints/{endpointId}/bxml | Update Endpoint BXML


# **create_endpoint**
> CreateEndpointResponse create_endpoint(account_id, body)

Create Endpoint

Creates a new Endpoint for the specified account.

### Example

* Basic Authentication (Basic):
* OAuth Authentication (OAuth2):

```python
import bandwidth
from bandwidth.models.create_endpoint_response import CreateEndpointResponse
from bandwidth.models.create_web_rtc_connection_request import CreateWebRtcConnectionRequest
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
    api_instance = bandwidth.EndpointsApi(api_client)
    account_id = '9900000' # str | Your Bandwidth Account ID.
    body = bandwidth.CreateWebRtcConnectionRequest() # CreateWebRtcConnectionRequest | 

    try:
        # Create Endpoint
        api_response = api_instance.create_endpoint(account_id, body)
        print("The response of EndpointsApi->create_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->create_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Your Bandwidth Account ID. | 
 **body** | **CreateWebRtcConnectionRequest**|  | 

### Return type

[**CreateEndpointResponse**](CreateEndpointResponse.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**415** | Unsupported Media Type |  -  |
**429** | Too Many Requests |  -  |
**500** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_endpoint**
> delete_endpoint(account_id, endpoint_id)

Delete Endpoint

Deletes the specified endpoint. If the endpoint is actively streaming media, the media stream will be terminated.

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
    api_instance = bandwidth.EndpointsApi(api_client)
    account_id = '9900000' # str | Your Bandwidth Account ID.
    endpoint_id = 'e-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85' # str | BRTC Endpoint ID.

    try:
        # Delete Endpoint
        api_instance.delete_endpoint(account_id, endpoint_id)
    except Exception as e:
        print("Exception when calling EndpointsApi->delete_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Your Bandwidth Account ID. | 
 **endpoint_id** | **str**| BRTC Endpoint ID. | 

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
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**415** | Unsupported Media Type |  -  |
**429** | Too Many Requests |  -  |
**500** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_endpoint**
> EndpointResponse get_endpoint(account_id, endpoint_id)

Get Endpoint

Returns information about the specified endpoint.

### Example

* Basic Authentication (Basic):
* OAuth Authentication (OAuth2):

```python
import bandwidth
from bandwidth.models.endpoint_response import EndpointResponse
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
    api_instance = bandwidth.EndpointsApi(api_client)
    account_id = '9900000' # str | Your Bandwidth Account ID.
    endpoint_id = 'e-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85' # str | BRTC Endpoint ID.

    try:
        # Get Endpoint
        api_response = api_instance.get_endpoint(account_id, endpoint_id)
        print("The response of EndpointsApi->get_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->get_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Your Bandwidth Account ID. | 
 **endpoint_id** | **str**| BRTC Endpoint ID. | 

### Return type

[**EndpointResponse**](EndpointResponse.md)

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
**429** | Too Many Requests |  -  |
**500** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_endpoints**
> ListEndpointsResponse list_endpoints(account_id, type=type, status=status, after_cursor=after_cursor, limit=limit)

List Endpoints

Returns a list of endpoints associated with the specified account.

### Example

* Basic Authentication (Basic):
* OAuth Authentication (OAuth2):

```python
import bandwidth
from bandwidth.models.endpoint_status_enum import EndpointStatusEnum
from bandwidth.models.endpoint_type_enum import EndpointTypeEnum
from bandwidth.models.list_endpoints_response import ListEndpointsResponse
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
    api_instance = bandwidth.EndpointsApi(api_client)
    account_id = '9900000' # str | Your Bandwidth Account ID.
    type = bandwidth.EndpointTypeEnum() # EndpointTypeEnum | The type of endpoint. (optional)
    status = bandwidth.EndpointStatusEnum() # EndpointStatusEnum | The status of the endpoint. (optional)
    after_cursor = 'TWF5IHRoZSBmb3JjZSBiZSB3aXRoIHlvdQ==' # str | The cursor to use for pagination. This is the value of the `next` link in the previous response. (optional)
    limit = 100 # int | The maximum number of endpoints to return in the response. (optional) (default to 100)

    try:
        # List Endpoints
        api_response = api_instance.list_endpoints(account_id, type=type, status=status, after_cursor=after_cursor, limit=limit)
        print("The response of EndpointsApi->list_endpoints:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->list_endpoints: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Your Bandwidth Account ID. | 
 **type** | [**EndpointTypeEnum**](.md)| The type of endpoint. | [optional] 
 **status** | [**EndpointStatusEnum**](.md)| The status of the endpoint. | [optional] 
 **after_cursor** | **str**| The cursor to use for pagination. This is the value of the &#x60;next&#x60; link in the previous response. | [optional] 
 **limit** | **int**| The maximum number of endpoints to return in the response. | [optional] [default to 100]

### Return type

[**ListEndpointsResponse**](ListEndpointsResponse.md)

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
**429** | Too Many Requests |  -  |
**500** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_endpoint_bxml**
> update_endpoint_bxml(account_id, endpoint_id, body)

Update Endpoint BXML

Updates the BXML for the specified endpoint.

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
    api_instance = bandwidth.EndpointsApi(api_client)
    account_id = '9900000' # str | Your Bandwidth Account ID.
    endpoint_id = 'e-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85' # str | BRTC Endpoint ID.
    body = 'body_example' # str | 

    try:
        # Update Endpoint BXML
        api_instance.update_endpoint_bxml(account_id, endpoint_id, body)
    except Exception as e:
        print("Exception when calling EndpointsApi->update_endpoint_bxml: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Your Bandwidth Account ID. | 
 **endpoint_id** | **str**| BRTC Endpoint ID. | 
 **body** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/xml
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**415** | Unsupported Media Type |  -  |
**429** | Too Many Requests |  -  |
**500** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

