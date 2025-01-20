# MessageCallback

Message Callback Schema

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **datetime** |  | 
**type** | [**CallbackTypeEnum**](CallbackTypeEnum.md) |  | 
**to** | **str** |  | 
**description** | **str** | A detailed description of the event described by the callback. | 
**message** | [**MessageCallbackMessage**](MessageCallbackMessage.md) |  | 
**error_code** | **int** | Optional error code, applicable only when type is &#x60;message-failed&#x60;. | [optional] 

## Example

```python
from bandwidth.models.message_callback import MessageCallback

# TODO update the JSON string below
json = "{}"
# create an instance of MessageCallback from a JSON string
message_callback_instance = MessageCallback.from_json(json)
# print the JSON string representation of the object
print(MessageCallback.to_json())

# convert the object into a dict
message_callback_dict = message_callback_instance.to_dict()
# create an instance of MessageCallback from a dict
message_callback_from_dict = MessageCallback.from_dict(message_callback_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


