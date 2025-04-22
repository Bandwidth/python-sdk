# MultiChannelMessageCallbackData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** | The ID of the message. | [optional] 
**status** | [**MultiChannelStatusEnum**](MultiChannelStatusEnum.md) |  | [optional] 
**direction** | [**MultiChannelMessageDirectionEnum**](MultiChannelMessageDirectionEnum.md) |  | [optional] 
**var_from** | **str** | The sender ID of the message. This could be an alphanumeric sender ID. | [optional] 
**to** | **str** | The phone number the message should be sent to in E164 format. | [optional] 
**application_id** | **str** | The ID of the Application your from number or senderId is associated with in the Bandwidth Phone Number Dashboard. | [optional] 
**channel** | [**MultiChannelMessageChannelEnum**](MultiChannelMessageChannelEnum.md) |  | [optional] 
**tag** | **str** | A custom string that will be included in callback events of the message. Max 1024 characters. | [optional] 

## Example

```python
from bandwidth.models.multi_channel_message_callback_data import MultiChannelMessageCallbackData

# TODO update the JSON string below
json = "{}"
# create an instance of MultiChannelMessageCallbackData from a JSON string
multi_channel_message_callback_data_instance = MultiChannelMessageCallbackData.from_json(json)
# print the JSON string representation of the object
print(MultiChannelMessageCallbackData.to_json())

# convert the object into a dict
multi_channel_message_callback_data_dict = multi_channel_message_callback_data_instance.to_dict()
# create an instance of MultiChannelMessageCallbackData from a dict
multi_channel_message_callback_data_from_dict = MultiChannelMessageCallbackData.from_dict(multi_channel_message_callback_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


