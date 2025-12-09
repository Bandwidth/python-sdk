# MultiChannelAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**RbmActionTypeEnum**](RbmActionTypeEnum.md) |  | 
**text** | **str** | Displayed text for user to click | 
**postback_data** | **bytearray** | Base64 payload the customer receives when the reply is clicked. | 
**phone_number** | **str** | The phone number to dial. Must be E164 format. | 
**latitude** | **float** | The latitude of the location. | 
**longitude** | **float** | The longitude of the location. | 
**label** | **str** | The label of the location. | [optional] 
**title** | **str** | The title of the event. | 
**start_time** | **datetime** | The start time of the event. | 
**end_time** | **datetime** | The end time of the event. | 
**description** | **str** | The description of the event. | [optional] 
**url** | **str** | The URL to open in browser. | 
**application** | [**RbmOpenUrlEnum**](RbmOpenUrlEnum.md) |  | [optional] 
**webview_view_mode** | [**RbmVebViewEnum**](RbmVebViewEnum.md) |  | [optional] 

## Example

```python
from bandwidth.models.multi_channel_action import MultiChannelAction

# TODO update the JSON string below
json = "{}"
# create an instance of MultiChannelAction from a JSON string
multi_channel_action_instance = MultiChannelAction.from_json(json)
# print the JSON string representation of the object
print(MultiChannelAction.to_json())

# convert the object into a dict
multi_channel_action_dict = multi_channel_action_instance.to_dict()
# create an instance of MultiChannelAction from a dict
multi_channel_action_from_dict = MultiChannelAction.from_dict(multi_channel_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


