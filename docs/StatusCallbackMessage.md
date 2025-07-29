# StatusCallbackMessage

Message payload schema within a callback

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier of the message. | 
**owner** | **str** | The Bandwidth phone number or alphanumeric identifier associated with the message. | 
**application_id** | **str** | The ID of the Application your from number or senderId is associated with in the Bandwidth Phone Number Dashboard. | 
**time** | **datetime** |  | 
**segment_count** | **int** | The number of segments the user&#39;s message is broken into before sending over carrier networks. | 
**direction** | [**MessageDirectionEnum**](MessageDirectionEnum.md) |  | 
**to** | **List[str]** | The phone number recipients of the message. | 
**var_from** | **str** | The Bandwidth phone number or alphanumeric identifier the message was sent from. | 
**text** | **str** |  | [optional] 
**tag** | **str** | A custom string that will be included in callback events of the message. Max 1024 characters. | [optional] 
**media** | **List[str]** | Optional media, not applicable for sms | [optional] 
**priority** | [**PriorityEnum**](PriorityEnum.md) |  | [optional] 
**channel** | [**MultiChannelMessageChannelEnum**](MultiChannelMessageChannelEnum.md) |  | [optional] 

## Example

```python
from bandwidth.models.status_callback_message import StatusCallbackMessage

# TODO update the JSON string below
json = "{}"
# create an instance of StatusCallbackMessage from a JSON string
status_callback_message_instance = StatusCallbackMessage.from_json(json)
# print the JSON string representation of the object
print(StatusCallbackMessage.to_json())

# convert the object into a dict
status_callback_message_dict = status_callback_message_instance.to_dict()
# create an instance of StatusCallbackMessage from a dict
status_callback_message_from_dict = StatusCallbackMessage.from_dict(status_callback_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


