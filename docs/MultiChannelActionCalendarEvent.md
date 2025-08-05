# MultiChannelActionCalendarEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**RbmActionTypeEnum**](RbmActionTypeEnum.md) |  | 
**text** | **str** | Displayed text for user to click | 
**postback_data** | **bytearray** | Base64 payload the customer receives when the reply is clicked. | 
**title** | **str** | The title of the event. | 
**start_time** | **datetime** | The start time of the event. | 
**end_time** | **datetime** | The end time of the event. | 
**description** | **str** | The description of the event. | [optional] 

## Example

```python
from bandwidth.models.multi_channel_action_calendar_event import MultiChannelActionCalendarEvent

# TODO update the JSON string below
json = "{}"
# create an instance of MultiChannelActionCalendarEvent from a JSON string
multi_channel_action_calendar_event_instance = MultiChannelActionCalendarEvent.from_json(json)
# print the JSON string representation of the object
print(MultiChannelActionCalendarEvent.to_json())

# convert the object into a dict
multi_channel_action_calendar_event_dict = multi_channel_action_calendar_event_instance.to_dict()
# create an instance of MultiChannelActionCalendarEvent from a dict
multi_channel_action_calendar_event_from_dict = MultiChannelActionCalendarEvent.from_dict(multi_channel_action_calendar_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


