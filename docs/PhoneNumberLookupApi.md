# bandwidth.PhoneNumberLookupApi

All URIs are relative to *https://messaging.bandwidth.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lookup_request**](PhoneNumberLookupApi.md#lookup_request) | **POST** /accounts/{accountId}/tnlookup | Create Request
[**lookup_request_status**](PhoneNumberLookupApi.md#lookup_request_status) | **GET** /accounts/{accountId}/tnlookup/{requestId} | Query Request Status


# **lookup_request**
> OrderResponse lookup_request(account_id, order_request)

Create Request

Create a TN Lookup Order.

### Example

* Basic Authentication (httpBasic):

```python
import time
import bandwidth
from bandwidth.api import phone_number_lookup_api
from bandwidth.model.order_response import OrderResponse
from bandwidth.model.order_request import OrderRequest
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
    api_instance = phone_number_lookup_api.PhoneNumberLookupApi(api_client)
    account_id = "9998887" # str | The ID of the Bandwidth account that the user belongs to.
    order_request = OrderRequest(
        tns=[
            "tns_example",
        ],
    ) # OrderRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create Request
        api_response = api_instance.lookup_request(account_id, order_request)
        pprint(api_response)
    except bandwidth.ApiException as e:
        print("Exception when calling PhoneNumberLookupApi->lookup_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The ID of the Bandwidth account that the user belongs to. |
 **order_request** | [**OrderRequest**](OrderRequest.md)|  |

### Return type

[**OrderResponse**](OrderResponse.md)

### Authorization

[httpBasic](../README.md#httpBasic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The request has been accepted for processing but not yet finished and in a terminal state (COMPLETE, PARTIAL_COMPLETE, or FAILED) |  -  |
**400** | Bad Request. Ensure that your request payload is properly formatted and that the telephone numbers used are valid. |  -  |
**401** | Unauthorized. Ensure that you are using the proper credentials for the environment you are accessing, your user has the proper role assigned to it, and that your Bandwidth account is enabled for TN Lookup access. |  -  |
**415** | Invalid content-type. Ensure that your content-type header is set to application/json. |  -  |
**429** | Too Many Requests. Reduce the amount of requests that you are sending in order to avoid receiving this status code. |  -  |
**5XX** | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lookup_request_status**
> OrderStatus lookup_request_status(account_id, request_id)

Query Request Status

Query an existing TN Lookup Order.

### Example

* Basic Authentication (httpBasic):

```python
import time
import bandwidth
from bandwidth.api import phone_number_lookup_api
from bandwidth.model.order_status import OrderStatus
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
    api_instance = phone_number_lookup_api.PhoneNumberLookupApi(api_client)
    account_id = "9998887" # str | The ID of the Bandwidth account that the user belongs to.
    request_id = "requestId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Query Request Status
        api_response = api_instance.lookup_request_status(account_id, request_id)
        pprint(api_response)
    except bandwidth.ApiException as e:
        print("Exception when calling PhoneNumberLookupApi->lookup_request_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The ID of the Bandwidth account that the user belongs to. |
 **request_id** | **str**|  |

### Return type

[**OrderStatus**](OrderStatus.md)

### Authorization

[httpBasic](../README.md#httpBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | If requestId exists, the result for that request is returned. See the Examples for details on the various responses that you can receive.  Generally, if you see a Response Code of 0 in a result for a TN, information will be available for it.  Any other Response Code will indicate no information was available for the TN. |  -  |
**400** | Bad Request. Ensure that you have set the requestId as a URL path parameter. |  -  |
**401** | Unauthorized. Ensure that you are using the proper credentials for the environment you are accessing, your user has the proper role assigned to it, and that your Bandwidth account is enabled for TN Lookup access. |  -  |
**404** | RequestId not found. Ensure that the requestId used in the URL path is valid and maps to a previous request that was submitted. |  -  |
**429** | Too Many Requests. Reduce the amount of requests that you are sending in order to avoid receiving this status code. |  -  |
**5XX** | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

