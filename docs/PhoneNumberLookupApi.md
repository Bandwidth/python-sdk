# bandwidth.PhoneNumberLookupApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_lookup**](PhoneNumberLookupApi.md#create_lookup) | **POST** /accounts/{accountId}/tnlookup | Create Lookup
[**get_lookup_status**](PhoneNumberLookupApi.md#get_lookup_status) | **GET** /accounts/{accountId}/tnlookup/{requestId} | Get Lookup Request Status


# **create_lookup**
> CreateLookupResponse create_lookup(account_id, lookup_request)

Create Lookup

Create a Phone Number Lookup Request.

### Example

* Basic Authentication (Basic):

```python
import bandwidth
from bandwidth.models.create_lookup_response import CreateLookupResponse
from bandwidth.models.lookup_request import LookupRequest
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
    account_id = '9900000' # str | Your Bandwidth Account ID.
    lookup_request = bandwidth.LookupRequest() # LookupRequest | Phone number lookup request.

    try:
        # Create Lookup
        api_response = api_instance.create_lookup(account_id, lookup_request)
        print("The response of PhoneNumberLookupApi->create_lookup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhoneNumberLookupApi->create_lookup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Your Bandwidth Account ID. | 
 **lookup_request** | [**LookupRequest**](LookupRequest.md)| Phone number lookup request. | 

### Return type

[**CreateLookupResponse**](CreateLookupResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**415** | Unsupported Media Type |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lookup_status**
> LookupStatus get_lookup_status(account_id, request_id)

Get Lookup Request Status

Get an existing Phone Number Lookup Request.

### Example

* Basic Authentication (Basic):

```python
import bandwidth
from bandwidth.models.lookup_status import LookupStatus
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
    account_id = '9900000' # str | Your Bandwidth Account ID.
    request_id = '004223a0-8b17-41b1-bf81-20732adf5590' # str | The phone number lookup request ID from Bandwidth.

    try:
        # Get Lookup Request Status
        api_response = api_instance.get_lookup_status(account_id, request_id)
        print("The response of PhoneNumberLookupApi->get_lookup_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhoneNumberLookupApi->get_lookup_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Your Bandwidth Account ID. | 
 **request_id** | **str**| The phone number lookup request ID from Bandwidth. | 

### Return type

[**LookupStatus**](LookupStatus.md)

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
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

