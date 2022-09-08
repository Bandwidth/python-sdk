# bandwidth.MessagesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_message**](MessagesApi.md#create_message) | **POST** /users/{accountId}/messages | Create Message
[**list_messages**](MessagesApi.md#list_messages) | **GET** /users/{accountId}/messages | List Messages


# **create_message**
> Message create_message(account_id, message_request)

Create Message

Endpoint for sending text messages and picture messages using V2 messaging.

### Example

* Basic Authentication (Basic):

```python
import time
import bandwidth
from bandwidth.api import messages_api
from bandwidth.model.messaging_request_error import MessagingRequestError
from bandwidth.model.create_message_request_error import CreateMessageRequestError
from bandwidth.model.message_request import MessageRequest
from bandwidth.model.message import Message
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
    api_instance = messages_api.MessagesApi(api_client)
    account_id = "9900000" # str | Your Bandwidth Account ID.
    message_request = MessageRequest(
        application_id="93de2206-9669-4e07-948d-329f4b722ee2",
        to=["+15554443333","+15552223333"],
        _from="+15551113333",
        text="Hello world",
        media=["https://dev.bandwidth.com/images/bandwidth-logo.png","https://dev.bandwidth.com/images/github_logo.png"],
        tag="custom string",
        priority=PriorityEnum("default"),
        expiration="2021-02-01T11:29:18-05:00",
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
 **account_id** | **str**| Your Bandwidth Account ID. |
 **message_request** | [**MessageRequest**](MessageRequest.md)|  |

### Return type

[**Message**](Message.md)

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
**404** | Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_messages**
> MessagesList list_messages(account_id)

List Messages

Returns a list of messages based on query parameters.

### Example

* Basic Authentication (Basic):

```python
import time
import bandwidth
from bandwidth.api import messages_api
from bandwidth.model.message_status_enum import MessageStatusEnum
from bandwidth.model.messaging_request_error import MessagingRequestError
from bandwidth.model.list_message_direction_enum import ListMessageDirectionEnum
from bandwidth.model.messages_list import MessagesList
from bandwidth.model.message_type_enum import MessageTypeEnum
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
    api_instance = messages_api.MessagesApi(api_client)
    account_id = "9900000" # str | Your Bandwidth Account ID.
    message_id = "9e0df4ca-b18d-40d7-a59f-82fcdf5ae8e6" # str | The ID of the message to search for. Special characters need to be encoded using URL encoding. Message IDs could come in different formats, e.g., 9e0df4ca-b18d-40d7-a59f-82fcdf5ae8e6 and 1589228074636lm4k2je7j7jklbn2 are valid message ID formats. Note that you must include at least one query parameter. (optional)
    source_tn = "%2B15554443333" # str | The phone number that sent the message. Accepted values are: a single full phone number a comma separated list of full phone numbers (maximum of 10) or a single partial phone number (minimum of 5 characters e.g. '%2B1919'). (optional)
    destination_tn = "%2B15554443333" # str | The phone number that received the message. Accepted values are: a single full phone number a comma separated list of full phone numbers (maximum of 10) or a single partial phone number (minimum of 5 characters e.g. '%2B1919'). (optional)
    message_status = MessageStatusEnum("RECEIVED") # MessageStatusEnum | The status of the message. One of RECEIVED QUEUED SENDING SENT FAILED DELIVERED ACCEPTED UNDELIVERED. (optional)
    message_direction = ListMessageDirectionEnum("INBOUND") # ListMessageDirectionEnum | The direction of the message. One of INBOUND OUTBOUND. (optional)
    carrier_name = "Verizon" # str | The name of the carrier used for this message. Possible values include but are not limited to Verizon and TMobile. Special characters need to be encoded using URL encoding (i.e. AT&T should be passed as AT%26T). (optional)
    message_type = MessageTypeEnum("sms") # MessageTypeEnum | The type of message. Either sms or mms. (optional)
    error_code = 9902 # int | The error code of the message. (optional)
    from_date_time = "2022-09-14T18:20:16.000Z" # str | The start of the date range to search in ISO 8601 format. Uses the message receive time. The date range to search in is currently 14 days. (optional)
    to_date_time = "2022-09-14T18:20:16.000Z" # str | The end of the date range to search in ISO 8601 format. Uses the message receive time. The date range to search in is currently 14 days. (optional)
    sort = "sourceTn:desc" # str | The field and direction to sort by combined with a colon. Direction is either asc or desc. (optional)
    page_token = "gdEewhcJLQRB5" # str | A base64 encoded value used for pagination of results. (optional)
    limit = 50 # int | The maximum records requested in search result. Default 100. The sum of limit and after cannot be more than 10000. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Messages
        api_response = api_instance.list_messages(account_id)
        pprint(api_response)
    except bandwidth.ApiException as e:
        print("Exception when calling MessagesApi->list_messages: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Messages
        api_response = api_instance.list_messages(account_id, message_id=message_id, source_tn=source_tn, destination_tn=destination_tn, message_status=message_status, message_direction=message_direction, carrier_name=carrier_name, message_type=message_type, error_code=error_code, from_date_time=from_date_time, to_date_time=to_date_time, sort=sort, page_token=page_token, limit=limit)
        pprint(api_response)
    except bandwidth.ApiException as e:
        print("Exception when calling MessagesApi->list_messages: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Your Bandwidth Account ID. |
 **message_id** | **str**| The ID of the message to search for. Special characters need to be encoded using URL encoding. Message IDs could come in different formats, e.g., 9e0df4ca-b18d-40d7-a59f-82fcdf5ae8e6 and 1589228074636lm4k2je7j7jklbn2 are valid message ID formats. Note that you must include at least one query parameter. | [optional]
 **source_tn** | **str**| The phone number that sent the message. Accepted values are: a single full phone number a comma separated list of full phone numbers (maximum of 10) or a single partial phone number (minimum of 5 characters e.g. &#39;%2B1919&#39;). | [optional]
 **destination_tn** | **str**| The phone number that received the message. Accepted values are: a single full phone number a comma separated list of full phone numbers (maximum of 10) or a single partial phone number (minimum of 5 characters e.g. &#39;%2B1919&#39;). | [optional]
 **message_status** | **MessageStatusEnum**| The status of the message. One of RECEIVED QUEUED SENDING SENT FAILED DELIVERED ACCEPTED UNDELIVERED. | [optional]
 **message_direction** | **ListMessageDirectionEnum**| The direction of the message. One of INBOUND OUTBOUND. | [optional]
 **carrier_name** | **str**| The name of the carrier used for this message. Possible values include but are not limited to Verizon and TMobile. Special characters need to be encoded using URL encoding (i.e. AT&amp;T should be passed as AT%26T). | [optional]
 **message_type** | **MessageTypeEnum**| The type of message. Either sms or mms. | [optional]
 **error_code** | **int**| The error code of the message. | [optional]
 **from_date_time** | **str**| The start of the date range to search in ISO 8601 format. Uses the message receive time. The date range to search in is currently 14 days. | [optional]
 **to_date_time** | **str**| The end of the date range to search in ISO 8601 format. Uses the message receive time. The date range to search in is currently 14 days. | [optional]
 **sort** | **str**| The field and direction to sort by combined with a colon. Direction is either asc or desc. | [optional]
 **page_token** | **str**| A base64 encoded value used for pagination of results. | [optional]
 **limit** | **int**| The maximum records requested in search result. Default 100. The sum of limit and after cannot be more than 10000. | [optional]

### Return type

[**MessagesList**](MessagesList.md)

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
**415** | Unsupported Media Type |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

