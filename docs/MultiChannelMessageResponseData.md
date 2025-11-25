# MultiChannelMessageResponseData

The data returned in a multichannel message response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the message. | 
**time** | **datetime** | The time the message was received by the Bandwidth API. | 
**direction** | [**MessageDirectionEnum**](MessageDirectionEnum.md) |  | 
**to** | **List[str]** | The destination phone number(s) of the message, in E164 format. | 
**channel_list** | [**List[MultiChannelChannelListResponseObject]**](MultiChannelChannelListResponseObject.md) | A list of message bodies. The messages will be attempted in the order they are listed. Once a message sends successfully, the others will be ignored. | 
**tag** | **str** | A custom string that will be included in callback events of the message. Max 1024 characters. | [optional] 
**priority** | [**PriorityEnum**](PriorityEnum.md) |  | [optional] 
**expiration** | **datetime** | A string with the date/time value that the message will automatically expire by. This must be a valid RFC-3339 value, e.g., 2021-03-14T01:59:26Z or 2021-03-13T20:59:26-05:00. Must be a date-time in the future. | [optional] 

## Example

```python
from bandwidth.models.multi_channel_message_response_data import MultiChannelMessageResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of MultiChannelMessageResponseData from a JSON string
multi_channel_message_response_data_instance = MultiChannelMessageResponseData.from_json(json)
# print the JSON string representation of the object
print(MultiChannelMessageResponseData.to_json())

# convert the object into a dict
multi_channel_message_response_data_dict = multi_channel_message_response_data_instance.to_dict()
# create an instance of MultiChannelMessageResponseData from a dict
multi_channel_message_response_data_from_dict = MultiChannelMessageResponseData.from_dict(multi_channel_message_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


