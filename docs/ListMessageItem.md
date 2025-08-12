# ListMessageItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** | The message id | [optional] 
**account_id** | **str** | The account id associated with this message. | [optional] 
**source_tn** | **str** | The source phone number of the message. | [optional] 
**destination_tn** | **str** | The recipient phone number of the message. | [optional] 
**message_status** | [**MessageStatusEnum**](MessageStatusEnum.md) |  | [optional] 
**message_direction** | [**ListMessageDirectionEnum**](ListMessageDirectionEnum.md) |  | [optional] 
**message_type** | [**MessageTypeEnum**](MessageTypeEnum.md) |  | [optional] 
**segment_count** | **int** | The number of segments the user&#39;s message is broken into before sending over carrier networks. | [optional] 
**error_code** | **int** | The numeric error code of the message. | [optional] 
**receive_time** | **datetime** | The ISO 8601 datetime of the message. | [optional] 
**carrier_name** | **str** | The name of the carrier. Not currently supported for MMS coming soon. | [optional] 
**message_size** | **int** | The size of the message including message content and headers. | [optional] 
**message_length** | **int** | The length of the message content. | [optional] 
**attachment_count** | **int** | The number of attachments the message has. | [optional] 
**recipient_count** | **int** | The number of recipients the message has. | [optional] 
**campaign_class** | **str** | The campaign class of the message if it has one. | [optional] 
**campaign_id** | **str** | The campaign ID of the message if it has one. | [optional] 
**bw_latency** | **int** | The Bandwidth latency of the message in seconds. Only available for accounts with the Advanced Quality Metrics feature enabled. | [optional] 
**calling_number_country_a3** | **str** | The A3 country code of the calling number. | [optional] 
**called_number_country_a3** | **str** | The A3 country code of the called number. | [optional] 
**product** | **str** | The messaging product associated with the message. | [optional] 
**location** | **str** | The location ID associated with this message. | [optional] 

## Example

```python
from bandwidth.models.list_message_item import ListMessageItem

# TODO update the JSON string below
json = "{}"
# create an instance of ListMessageItem from a JSON string
list_message_item_instance = ListMessageItem.from_json(json)
# print the JSON string representation of the object
print(ListMessageItem.to_json())

# convert the object into a dict
list_message_item_dict = list_message_item_instance.to_dict()
# create an instance of ListMessageItem from a dict
list_message_item_from_dict = ListMessageItem.from_dict(list_message_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


