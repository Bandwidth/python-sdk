# MultiChannelCallbackData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **datetime** | The time of the callback event. | [optional] 
**type** | [**MultiChannelStatusEnum**](MultiChannelStatusEnum.md) |  | [optional] 
**to** | **str** | The phone number the message should be sent to in E164 format. | [optional] 
**description** | **str** |  | [optional] 
**message** | [**MultiChannelMessageCallbackData**](MultiChannelMessageCallbackData.md) |  | [optional] 

## Example

```python
from bandwidth.models.multi_channel_callback_data import MultiChannelCallbackData

# TODO update the JSON string below
json = "{}"
# create an instance of MultiChannelCallbackData from a JSON string
multi_channel_callback_data_instance = MultiChannelCallbackData.from_json(json)
# print the JSON string representation of the object
print(MultiChannelCallbackData.to_json())

# convert the object into a dict
multi_channel_callback_data_dict = multi_channel_callback_data_instance.to_dict()
# create an instance of MultiChannelCallbackData from a dict
multi_channel_callback_data_from_dict = MultiChannelCallbackData.from_dict(multi_channel_callback_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


