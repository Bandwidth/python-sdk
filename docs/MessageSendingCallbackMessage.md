# MessageSendingCallbackMessage

Message Sending Callback Message Schema

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**owner** | **str** |  | 
**application_id** | **str** |  | 
**time** | **datetime** |  | 
**segment_count** | **int** |  | 
**direction** | [**MessageDirectionEnum**](MessageDirectionEnum.md) |  | 
**to** | **List[str]** |  | 
**var_from** | **str** |  | 
**text** | **str** |  | 
**tag** | **str** |  | [optional] 
**media** | **List[str]** |  | 
**priority** | [**PriorityEnum**](PriorityEnum.md) |  | 

## Example

```python
from bandwidth.models.message_sending_callback_message import MessageSendingCallbackMessage

# TODO update the JSON string below
json = "{}"
# create an instance of MessageSendingCallbackMessage from a JSON string
message_sending_callback_message_instance = MessageSendingCallbackMessage.from_json(json)
# print the JSON string representation of the object
print(MessageSendingCallbackMessage.to_json())

# convert the object into a dict
message_sending_callback_message_dict = message_sending_callback_message_instance.to_dict()
# create an instance of MessageSendingCallbackMessage from a dict
message_sending_callback_message_from_dict = MessageSendingCallbackMessage.from_dict(message_sending_callback_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


