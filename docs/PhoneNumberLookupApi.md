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
import time
import bandwidth
from bandwidth.api import phone_number_lookup_api
from bandwidth.model.create_lookup_response import CreateLookupResponse
from bandwidth.model.lookup_request import LookupRequest
from bandwidth.model.tn_lookup_request_error import TnLookupRequestError
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
    api_instance = phone_number_lookup_api.PhoneNumberLookupApi(api_client)
    account_id = "9900000" # str | The ID of the Bandwidth account that the user belongs to.
    lookup_request = LookupRequest(
        tns=[
            "tns_example",
        ],
    ) # LookupRequest | Phone number lookup request.

    # example passing only required values which don't have defaults set
    try:
        # Create Lookup
        api_response = api_instance.create_lookup(account_id, lookup_request)
        pprint(api_response)
    except bandwidth.ApiException as e:
        print("Exception when calling PhoneNumberLookupApi->create_lookup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The ID of the Bandwidth account that the user belongs to. |
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
import time
import bandwidth
from bandwidth.api import phone_number_lookup_api
from bandwidth.model.lookup_status import LookupStatus
from bandwidth.model.tn_lookup_request_error import TnLookupRequestError
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
    api_instance = phone_number_lookup_api.PhoneNumberLookupApi(api_client)
    account_id = "9900000" # str | The ID of the Bandwidth account that the user belongs to.
    request_id = "004223a0-8b17-41b1-bf81-20732adf5590" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get Lookup Request Status
        api_response = api_instance.get_lookup_status(account_id, request_id)
        pprint(api_response)
    except bandwidth.ApiException as e:
        print("Exception when calling PhoneNumberLookupApi->get_lookup_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The ID of the Bandwidth account that the user belongs to. |
 **request_id** | **str**|  |

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

