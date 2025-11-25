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
import bandwidth
from bandwidth.models.message import Message
from bandwidth.models.message_request import MessageRequest
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
    api_instance = bandwidth.MessagesApi(api_client)
    account_id = '9900000' # str | Your Bandwidth Account ID.
    message_request = bandwidth.MessageRequest() # MessageRequest | 

    try:
        # Create Message
        api_response = api_instance.create_message(account_id, message_request)
        print("The response of MessagesApi->create_message:\n")
        pprint(api_response)
    except Exception as e:
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
**405** | Method Not Allowed |  -  |
**406** | Not Acceptable |  -  |
**415** | Unsupported Media Type |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_messages**
> MessagesList list_messages(account_id, message_id=message_id, source_tn=source_tn, destination_tn=destination_tn, message_status=message_status, message_direction=message_direction, carrier_name=carrier_name, message_type=message_type, error_code=error_code, from_date_time=from_date_time, to_date_time=to_date_time, campaign_id=campaign_id, from_bw_latency=from_bw_latency, bw_queued=bw_queued, product=product, location=location, carrier_queued=carrier_queued, from_carrier_latency=from_carrier_latency, calling_number_country_a3=calling_number_country_a3, called_number_country_a3=called_number_country_a3, from_segment_count=from_segment_count, to_segment_count=to_segment_count, from_message_size=from_message_size, to_message_size=to_message_size, sort=sort, page_token=page_token, limit=limit, limit_total_count=limit_total_count)

List Messages

Returns a list of messages based on query parameters.

### Example

* Basic Authentication (Basic):

```python
import bandwidth
from bandwidth.models.list_message_direction_enum import ListMessageDirectionEnum
from bandwidth.models.message_status_enum import MessageStatusEnum
from bandwidth.models.message_type_enum import MessageTypeEnum
from bandwidth.models.messages_list import MessagesList
from bandwidth.models.product_type_enum import ProductTypeEnum
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
    api_instance = bandwidth.MessagesApi(api_client)
    account_id = '9900000' # str | Your Bandwidth Account ID.
    message_id = '9e0df4ca-b18d-40d7-a59f-82fcdf5ae8e6' # str | The ID of the message to search for. Special characters need to be encoded using URL encoding. Message IDs could come in different formats, e.g., 9e0df4ca-b18d-40d7-a59f-82fcdf5ae8e6 and 1589228074636lm4k2je7j7jklbn2 are valid message ID formats. Note that you must include at least one query parameter. (optional)
    source_tn = '%2B15554443333' # str | The phone number that sent the message. Accepted values are: a single full phone number a comma separated list of full phone numbers (maximum of 10) or a single partial phone number (minimum of 5 characters e.g. '%2B1919'). (optional)
    destination_tn = '%2B15554443333' # str | The phone number that received the message. Accepted values are: a single full phone number a comma separated list of full phone numbers (maximum of 10) or a single partial phone number (minimum of 5 characters e.g. '%2B1919'). (optional)
    message_status = bandwidth.MessageStatusEnum() # MessageStatusEnum | The status of the message. One of RECEIVED QUEUED SENDING SENT FAILED DELIVERED ACCEPTED UNDELIVERED. (optional)
    message_direction = bandwidth.ListMessageDirectionEnum() # ListMessageDirectionEnum | The direction of the message. One of INBOUND OUTBOUND. (optional)
    carrier_name = 'Verizon' # str | The name of the carrier used for this message. Possible values include but are not limited to Verizon and TMobile. Special characters need to be encoded using URL encoding (i.e. AT&T should be passed as AT%26T). (optional)
    message_type = bandwidth.MessageTypeEnum() # MessageTypeEnum | The type of message. Either sms or mms. (optional)
    error_code = 9902 # int | The error code of the message. (optional)
    from_date_time = '2022-09-14T18:20:16.000Z' # str | The start of the date range to search in ISO 8601 format. Uses the message receive time. The date range to search in is currently 14 days. (optional)
    to_date_time = '2022-09-14T18:20:16.000Z' # str | The end of the date range to search in ISO 8601 format. Uses the message receive time. The date range to search in is currently 14 days. (optional)
    campaign_id = 'CJEUMDK' # str | The campaign ID of the message. (optional)
    from_bw_latency = 5 # int | The minimum Bandwidth latency of the message in seconds. Only available for accounts with the Advanced Quality Metrics feature enabled. (optional)
    bw_queued = true # bool | A boolean value indicating whether the message is queued in the Bandwidth network. (optional)
    product = bandwidth.ProductTypeEnum() # ProductTypeEnum | Messaging product associated with the message. (optional)
    location = '123ABC' # str | Location Id associated with the message. (optional)
    carrier_queued = true # bool | A boolean value indicating whether the message is queued in the carrier network. Only available for OUTBOUND messages from accounts with the Advanced Quality Metrics feature enabled. (optional)
    from_carrier_latency = 50 # int | The minimum carrier latency of the message in seconds. Only available for OUTBOUND messages from accounts with the Advanced Quality Metrics feature enabled. (optional)
    calling_number_country_a3 = 'USA' # str | Calling number country in A3 format. (optional)
    called_number_country_a3 = 'USA' # str | Called number country in A3 format. (optional)
    from_segment_count = 1 # int | Segment count (start range). (optional)
    to_segment_count = 3 # int | Segment count (end range). (optional)
    from_message_size = 100 # int | Message size (start range). (optional)
    to_message_size = 120 # int | Message size (end range). (optional)
    sort = 'sourceTn:desc' # str | The field and direction to sort by combined with a colon. Direction is either asc or desc. (optional)
    page_token = 'gdEewhcJLQRB5' # str | A base64 encoded value used for pagination of results. (optional)
    limit = 50 # int | The maximum records requested in search result. Default 100. The sum of limit and after cannot be more than 10000. (optional)
    limit_total_count = true # bool | When set to true, the response's totalCount field will have a maximum value of 10,000. When set to false, or excluded, this will give an accurate totalCount of all messages that match the provided filters. If you are experiencing latency, try using this parameter to limit your results. (optional)

    try:
        # List Messages
        api_response = api_instance.list_messages(account_id, message_id=message_id, source_tn=source_tn, destination_tn=destination_tn, message_status=message_status, message_direction=message_direction, carrier_name=carrier_name, message_type=message_type, error_code=error_code, from_date_time=from_date_time, to_date_time=to_date_time, campaign_id=campaign_id, from_bw_latency=from_bw_latency, bw_queued=bw_queued, product=product, location=location, carrier_queued=carrier_queued, from_carrier_latency=from_carrier_latency, calling_number_country_a3=calling_number_country_a3, called_number_country_a3=called_number_country_a3, from_segment_count=from_segment_count, to_segment_count=to_segment_count, from_message_size=from_message_size, to_message_size=to_message_size, sort=sort, page_token=page_token, limit=limit, limit_total_count=limit_total_count)
        print("The response of MessagesApi->list_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->list_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Your Bandwidth Account ID. | 
 **message_id** | **str**| The ID of the message to search for. Special characters need to be encoded using URL encoding. Message IDs could come in different formats, e.g., 9e0df4ca-b18d-40d7-a59f-82fcdf5ae8e6 and 1589228074636lm4k2je7j7jklbn2 are valid message ID formats. Note that you must include at least one query parameter. | [optional] 
 **source_tn** | **str**| The phone number that sent the message. Accepted values are: a single full phone number a comma separated list of full phone numbers (maximum of 10) or a single partial phone number (minimum of 5 characters e.g. &#39;%2B1919&#39;). | [optional] 
 **destination_tn** | **str**| The phone number that received the message. Accepted values are: a single full phone number a comma separated list of full phone numbers (maximum of 10) or a single partial phone number (minimum of 5 characters e.g. &#39;%2B1919&#39;). | [optional] 
 **message_status** | [**MessageStatusEnum**](.md)| The status of the message. One of RECEIVED QUEUED SENDING SENT FAILED DELIVERED ACCEPTED UNDELIVERED. | [optional] 
 **message_direction** | [**ListMessageDirectionEnum**](.md)| The direction of the message. One of INBOUND OUTBOUND. | [optional] 
 **carrier_name** | **str**| The name of the carrier used for this message. Possible values include but are not limited to Verizon and TMobile. Special characters need to be encoded using URL encoding (i.e. AT&amp;T should be passed as AT%26T). | [optional] 
 **message_type** | [**MessageTypeEnum**](.md)| The type of message. Either sms or mms. | [optional] 
 **error_code** | **int**| The error code of the message. | [optional] 
 **from_date_time** | **str**| The start of the date range to search in ISO 8601 format. Uses the message receive time. The date range to search in is currently 14 days. | [optional] 
 **to_date_time** | **str**| The end of the date range to search in ISO 8601 format. Uses the message receive time. The date range to search in is currently 14 days. | [optional] 
 **campaign_id** | **str**| The campaign ID of the message. | [optional] 
 **from_bw_latency** | **int**| The minimum Bandwidth latency of the message in seconds. Only available for accounts with the Advanced Quality Metrics feature enabled. | [optional] 
 **bw_queued** | **bool**| A boolean value indicating whether the message is queued in the Bandwidth network. | [optional] 
 **product** | [**ProductTypeEnum**](.md)| Messaging product associated with the message. | [optional] 
 **location** | **str**| Location Id associated with the message. | [optional] 
 **carrier_queued** | **bool**| A boolean value indicating whether the message is queued in the carrier network. Only available for OUTBOUND messages from accounts with the Advanced Quality Metrics feature enabled. | [optional] 
 **from_carrier_latency** | **int**| The minimum carrier latency of the message in seconds. Only available for OUTBOUND messages from accounts with the Advanced Quality Metrics feature enabled. | [optional] 
 **calling_number_country_a3** | **str**| Calling number country in A3 format. | [optional] 
 **called_number_country_a3** | **str**| Called number country in A3 format. | [optional] 
 **from_segment_count** | **int**| Segment count (start range). | [optional] 
 **to_segment_count** | **int**| Segment count (end range). | [optional] 
 **from_message_size** | **int**| Message size (start range). | [optional] 
 **to_message_size** | **int**| Message size (end range). | [optional] 
 **sort** | **str**| The field and direction to sort by combined with a colon. Direction is either asc or desc. | [optional] 
 **page_token** | **str**| A base64 encoded value used for pagination of results. | [optional] 
 **limit** | **int**| The maximum records requested in search result. Default 100. The sum of limit and after cannot be more than 10000. | [optional] 
 **limit_total_count** | **bool**| When set to true, the response&#39;s totalCount field will have a maximum value of 10,000. When set to false, or excluded, this will give an accurate totalCount of all messages that match the provided filters. If you are experiencing latency, try using this parameter to limit your results. | [optional] 

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

