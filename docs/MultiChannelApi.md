# bandwidth.MultiChannelApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_multi_channel_message**](MultiChannelApi.md#create_multi_channel_message) | **POST** /users/{accountId}/messages/multiChannel | Create Multi-Channel Message


# **create_multi_channel_message**
> CreateMultiChannelMessageResponse create_multi_channel_message(account_id, multi_channel_message_request)

Create Multi-Channel Message

Endpoint for sending Multi-Channel messages.

### Example

* Basic Authentication (Basic):
* OAuth Authentication (OAuth2):

```python
import bandwidth
from bandwidth.models.create_multi_channel_message_response import CreateMultiChannelMessageResponse
from bandwidth.models.multi_channel_message_request import MultiChannelMessageRequest
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
    api_instance = bandwidth.MultiChannelApi(api_client)
    account_id = '9900000' # str | Your Bandwidth Account ID.
    multi_channel_message_request = bandwidth.MultiChannelMessageRequest() # MultiChannelMessageRequest | 

    try:
        # Create Multi-Channel Message
        api_response = api_instance.create_multi_channel_message(account_id, multi_channel_message_request)
        print("The response of MultiChannelApi->create_multi_channel_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MultiChannelApi->create_multi_channel_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Your Bandwidth Account ID. | 
 **multi_channel_message_request** | [**MultiChannelMessageRequest**](MultiChannelMessageRequest.md)|  | 

### Return type

[**CreateMultiChannelMessageResponse**](CreateMultiChannelMessageResponse.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2)

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
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**406** | Not Acceptable |  -  |
**415** | Unsupported Media Type |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

