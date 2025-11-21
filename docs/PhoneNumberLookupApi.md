# bandwidth.PhoneNumberLookupApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_async_bulk_lookup**](PhoneNumberLookupApi.md#create_async_bulk_lookup) | **POST** /accounts/{accountId}/phoneNumberLookup/bulk | Create Asynchronous Bulk Number Lookup
[**create_sync_lookup**](PhoneNumberLookupApi.md#create_sync_lookup) | **POST** /accounts/{accountId}/phoneNumberLookup | Create Synchronous Number Lookup
[**get_async_bulk_lookup**](PhoneNumberLookupApi.md#get_async_bulk_lookup) | **GET** /accounts/{accountId}/phoneNumberLookup/bulk/{requestId} | Get Asynchronous Bulk Number Lookup


# **create_async_bulk_lookup**
> CreateAsyncBulkLookupResponse create_async_bulk_lookup(account_id, async_lookup_request)

Create Asynchronous Bulk Number Lookup

Creates an asynchronous bulk phone number lookup request. Maximum of 15,000 telephone numbers per request. Use the [Get Asynchronous Bulk Number Lookup](#tag/Phone-Number-Lookup/operation/getAsyncBulkLookup) endpoint to check the status of the request and view the results.

### Example

* Basic Authentication (Basic):
* OAuth Authentication (OAuth2):

```python
import bandwidth
from bandwidth.models.async_lookup_request import AsyncLookupRequest
from bandwidth.models.create_async_bulk_lookup_response import CreateAsyncBulkLookupResponse
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
    api_instance = bandwidth.PhoneNumberLookupApi(api_client)
    account_id = '9900000' # str | 
    async_lookup_request = bandwidth.AsyncLookupRequest() # AsyncLookupRequest | Asynchronous bulk phone number lookup request.

    try:
        # Create Asynchronous Bulk Number Lookup
        api_response = api_instance.create_async_bulk_lookup(account_id, async_lookup_request)
        print("The response of PhoneNumberLookupApi->create_async_bulk_lookup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhoneNumberLookupApi->create_async_bulk_lookup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **async_lookup_request** | [**AsyncLookupRequest**](AsyncLookupRequest.md)| Asynchronous bulk phone number lookup request. | 

### Return type

[**CreateAsyncBulkLookupResponse**](CreateAsyncBulkLookupResponse.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**0** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_sync_lookup**
> CreateSyncLookupResponse create_sync_lookup(account_id, sync_lookup_request)

Create Synchronous Number Lookup

Creates a synchronous phone number lookup request. Maximum of 100 telephone numbers per request.

### Example

* Basic Authentication (Basic):
* OAuth Authentication (OAuth2):

```python
import bandwidth
from bandwidth.models.create_sync_lookup_response import CreateSyncLookupResponse
from bandwidth.models.sync_lookup_request import SyncLookupRequest
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
    api_instance = bandwidth.PhoneNumberLookupApi(api_client)
    account_id = '9900000' # str | 
    sync_lookup_request = bandwidth.SyncLookupRequest() # SyncLookupRequest | Synchronous phone number lookup request.

    try:
        # Create Synchronous Number Lookup
        api_response = api_instance.create_sync_lookup(account_id, sync_lookup_request)
        print("The response of PhoneNumberLookupApi->create_sync_lookup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhoneNumberLookupApi->create_sync_lookup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **sync_lookup_request** | [**SyncLookupRequest**](SyncLookupRequest.md)| Synchronous phone number lookup request. | 

### Return type

[**CreateSyncLookupResponse**](CreateSyncLookupResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_async_bulk_lookup**
> GetAsyncBulkLookupResponse get_async_bulk_lookup(account_id, request_id)

Get Asynchronous Bulk Number Lookup

Get an existing [Asynchronous Bulk Number Lookup](#tag/Phone-Number-Lookup/operation/createAsyncBulkLookup). Use this endpoint to check the status of the request and view the results.

### Example

* Basic Authentication (Basic):

```python
import bandwidth
from bandwidth.models.get_async_bulk_lookup_response import GetAsyncBulkLookupResponse
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
    api_instance = bandwidth.PhoneNumberLookupApi(api_client)
    account_id = '9900000' # str | 
    request_id = '004223a0-8b17-41b1-bf81-20732adf5590' # str | 

    try:
        # Get Asynchronous Bulk Number Lookup
        api_response = api_instance.get_async_bulk_lookup(account_id, request_id)
        print("The response of PhoneNumberLookupApi->get_async_bulk_lookup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhoneNumberLookupApi->get_async_bulk_lookup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **request_id** | **str**|  | 

### Return type

[**GetAsyncBulkLookupResponse**](GetAsyncBulkLookupResponse.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

