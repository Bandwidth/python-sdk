# bandwidth.MessagesApi

All URIs are relative to *https://messaging.bandwidth.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_message**](MessagesApi.md#create_message) | **POST** /users/{accountId}/messages | Create Message
[**get_messages**](MessagesApi.md#get_messages) | **GET** /users/{accountId}/messages | Get Messages


# **create_message**
> BandwidthMessage create_message(account_id, message_request)

Create Message

Endpoint for sending text messages and picture messages using V2 messaging.

### Example

* Basic Authentication (httpBasic):

```python
import time
import bandwidth
from bandwidth.api import messages_api
from bandwidth.model.messaging_exception import MessagingException
from bandwidth.model.message_request import MessageRequest
from bandwidth.model.bandwidth_message import BandwidthMessage
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
    api_instance = messages_api.MessagesApi(api_client)
    account_id = "900000" # str | User's account ID
    message_request = MessageRequest(
        application_id="93de2206-9669-4e07-948d-329f4b722ee2",
        to=["+15554443333","+15552223333"],
        _from="+15551113333",
        text="Hello world",
        media=["https://dev.bandwidth.com/images/bandwidth-logo.png","https://dev.bandwidth.com/images/github_logo.png"],
        tag="custom string",
        priority="default",
    ) # MessageRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create Message
        api_response = api_instance.create_message(account_id, message_request)
        pprint(api_response)
    except bandwidth.ApiException as e:
        print("Exception when calling MessagesApi->create_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| User&#39;s account ID |
 **message_request** | [**MessageRequest**](MessageRequest.md)|  |

### Return type

[**BandwidthMessage**](BandwidthMessage.md)

### Authorization

[httpBasic](../README.md#httpBasic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | successful operation |  -  |
**400** | 400 Request is malformed or invalid |  -  |
**401** | 401 The specified user does not have access to the account |  -  |
**403** | 403 The user does not have access to this API |  -  |
**404** | 404 Path not found |  -  |
**415** | 415 The content-type of the request is incorrect |  -  |
**429** | 429 The rate limit has been reached |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_messages**
> BandwidthMessagesList get_messages(account_id)

Get Messages

Gets a list of messages based on query parameters.

### Example

* Basic Authentication (httpBasic):

```python
import time
import bandwidth
from bandwidth.api import messages_api
from bandwidth.model.messaging_exception import MessagingException
from bandwidth.model.bandwidth_messages_list import BandwidthMessagesList
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
    api_instance = messages_api.MessagesApi(api_client)
    account_id = "900000" # str | User's account ID
    message_id = "9e0df4ca-b18d-40d7-a59f-82fcdf5ae8e6" # str | The ID of the message to search for. Special characters need to be encoded using URL encoding (optional)
    source_tn = "%2B15554443333" # str | The phone number that sent the message. Accepted values are: a single full phone number, a comma separated list of full phone numbers (maximum of 10), or a single partial phone number (minimum of 5 characters, e.g. '%2B1919') (optional)
    destination_tn = "%2B15554443333" # str | The phone number that received the message. Accepted values are: a single full phone number, a comma separated list of full phone numbers (maximum of 10), or a single partial phone number (minimum of 5 characters, e.g. '%2B1919') (optional)
    message_status = "RECEIVED" # str | The status of the message. One of RECEIVED, QUEUED, SENDING, SENT, FAILED, DELIVERED, ACCEPTED, UNDELIVERED (optional)
    message_direction = "OUTBOUND" # str | The direction of the message. One of INBOUND, OUTBOUND (optional)
    carrier_name = "Verizon" # str | The name of the carrier used for this message. Possible values include, but are not limited to, Verizon and TMobile. Special characters need to be encoded using URL encoding (i.e. AT&T should be passed as AT%26T) (optional)
    message_type = "mms" # str | The type of the message. One of mms, sms (optional)
    error_code = 9902 # int | The error code of the message (optional)
    from_date_time = "2016-09-14T18:20:16.000Z" # str | The start of the date range to search in ISO 8601 format. Uses the message receive time. The date range to search in is currently 14 days. (optional)
    to_date_time = "2016-09-14T18:20:16.000Z" # str | The end of the date range to search in ISO 8601 format. Uses the message receive time. The date range to search in is currently 14 days. (optional)
    sort = "sourceTn:desc" # str | The field and direction to sort by, combined with a colon. Direction is one of asc, desc (optional)
    page_token = "gdEewhcJLQRB5" # str | A base64 encoded value used for pagination of results (optional)
    limit = 50 # int | The maximum records requested in search result. Default 100. The sum of limit and after cannot be more than 10000 (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Messages
        api_response = api_instance.get_messages(account_id)
        pprint(api_response)
    except bandwidth.ApiException as e:
        print("Exception when calling MessagesApi->get_messages: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Messages
        api_response = api_instance.get_messages(account_id, message_id=message_id, source_tn=source_tn, destination_tn=destination_tn, message_status=message_status, message_direction=message_direction, carrier_name=carrier_name, message_type=message_type, error_code=error_code, from_date_time=from_date_time, to_date_time=to_date_time, sort=sort, page_token=page_token, limit=limit)
        pprint(api_response)
    except bandwidth.ApiException as e:
        print("Exception when calling MessagesApi->get_messages: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| User&#39;s account ID |
 **message_id** | **str**| The ID of the message to search for. Special characters need to be encoded using URL encoding | [optional]
 **source_tn** | **str**| The phone number that sent the message. Accepted values are: a single full phone number, a comma separated list of full phone numbers (maximum of 10), or a single partial phone number (minimum of 5 characters, e.g. &#39;%2B1919&#39;) | [optional]
 **destination_tn** | **str**| The phone number that received the message. Accepted values are: a single full phone number, a comma separated list of full phone numbers (maximum of 10), or a single partial phone number (minimum of 5 characters, e.g. &#39;%2B1919&#39;) | [optional]
 **message_status** | **str**| The status of the message. One of RECEIVED, QUEUED, SENDING, SENT, FAILED, DELIVERED, ACCEPTED, UNDELIVERED | [optional]
 **message_direction** | **str**| The direction of the message. One of INBOUND, OUTBOUND | [optional]
 **carrier_name** | **str**| The name of the carrier used for this message. Possible values include, but are not limited to, Verizon and TMobile. Special characters need to be encoded using URL encoding (i.e. AT&amp;T should be passed as AT%26T) | [optional]
 **message_type** | **str**| The type of the message. One of mms, sms | [optional]
 **error_code** | **int**| The error code of the message | [optional]
 **from_date_time** | **str**| The start of the date range to search in ISO 8601 format. Uses the message receive time. The date range to search in is currently 14 days. | [optional]
 **to_date_time** | **str**| The end of the date range to search in ISO 8601 format. Uses the message receive time. The date range to search in is currently 14 days. | [optional]
 **sort** | **str**| The field and direction to sort by, combined with a colon. Direction is one of asc, desc | [optional]
 **page_token** | **str**| A base64 encoded value used for pagination of results | [optional]
 **limit** | **int**| The maximum records requested in search result. Default 100. The sum of limit and after cannot be more than 10000 | [optional]

### Return type

[**BandwidthMessagesList**](BandwidthMessagesList.md)

### Authorization

[httpBasic](../README.md#httpBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | 400 Request is malformed or invalid |  -  |
**401** | 401 The specified user does not have access to the account |  -  |
**403** | 403 The user does not have access to this API |  -  |
**404** | 404 Path not found |  -  |
**415** | 415 The content-type of the request is incorrect |  -  |
**429** | 429 The rate limit has been reached |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

