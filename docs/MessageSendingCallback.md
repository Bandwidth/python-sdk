# MessageSendingCallback

Message Sending Callback

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **datetime** |  | 
**type** | **str** |  | 
**to** | **str** |  | 
**description** | **str** |  | 
**message** | [**MessageSendingCallbackMessage**](MessageSendingCallbackMessage.md) |  | 

## Example

```python
from bandwidth.models.message_sending_callback import MessageSendingCallback

# TODO update the JSON string below
json = "{}"
# create an instance of MessageSendingCallback from a JSON string
message_sending_callback_instance = MessageSendingCallback.from_json(json)
# print the JSON string representation of the object
print MessageSendingCallback.to_json()

# convert the object into a dict
message_sending_callback_dict = message_sending_callback_instance.to_dict()
# create an instance of MessageSendingCallback from a dict
message_sending_callback_form_dict = message_sending_callback.from_dict(message_sending_callback_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


