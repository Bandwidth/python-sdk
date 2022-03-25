# bandwidth.StatisticsApi

All URIs are relative to *https://messaging.bandwidth.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_statistics**](StatisticsApi.md#get_statistics) | **GET** /api/v2/accounts/{accountId}/statistics | Get Account Statistics


# **get_statistics**
> AccountStatistics get_statistics(account_id)

Get Account Statistics

Returns details about the current state of the account.

### Example

* Basic Authentication (httpBasic):

```python
import time
import bandwidth
from bandwidth.api import statistics_api
from bandwidth.model.account_statistics import AccountStatistics
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
    api_instance = statistics_api.StatisticsApi(api_client)
    account_id = "accountId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get Account Statistics
        api_response = api_instance.get_statistics(account_id)
        pprint(api_response)
    except bandwidth.ApiException as e:
        print("Exception when calling StatisticsApi->get_statistics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  |

### Return type

[**AccountStatistics**](AccountStatistics.md)

### Authorization

[httpBasic](../README.md#httpBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statistics found |  -  |
**400** | Something&#39;s not quite right... Your request is invalid. Please fix it before trying again. |  -  |
**401** | Your credentials are invalid. Please use your Bandwidth dashboard credentials to authenticate to the API. |  -  |
**403** | User unauthorized to perform this action. |  -  |
**404** | The resource specified cannot be found or does not belong to you. |  -  |
**429** | You&#39;re sending requests to this endpoint too frequently. Please slow your request rate down and try again. |  * Retry-After - When you should try your request again <br>  |
**500** | Something unexpected happened. Please try again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

