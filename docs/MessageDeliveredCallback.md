# MessageDeliveredCallback

Message Delivered Callback

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **datetime** |  | 
**type** | **str** |  | 
**to** | **str** |  | 
**description** | **str** |  | 
**message** | [**MessageDeliveredCallbackMessage**](MessageDeliveredCallbackMessage.md) |  | 

## Example

```python
from bandwidth.models.message_delivered_callback import MessageDeliveredCallback

# TODO update the JSON string below
json = "{}"
# create an instance of MessageDeliveredCallback from a JSON string
message_delivered_callback_instance = MessageDeliveredCallback.from_json(json)
# print the JSON string representation of the object
print(MessageDeliveredCallback.to_json())

# convert the object into a dict
message_delivered_callback_dict = message_delivered_callback_instance.to_dict()
# create an instance of MessageDeliveredCallback from a dict
message_delivered_callback_from_dict = MessageDeliveredCallback.from_dict(message_delivered_callback_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


