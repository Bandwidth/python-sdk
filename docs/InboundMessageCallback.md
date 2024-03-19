# InboundMessageCallback

Inbound Message Callback

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **datetime** |  | 
**type** | **str** |  | 
**to** | **str** |  | 
**description** | **str** |  | 
**message** | [**InboundMessageCallbackMessage**](InboundMessageCallbackMessage.md) |  | 

## Example

```python
from bandwidth.models.inbound_message_callback import InboundMessageCallback

# TODO update the JSON string below
json = "{}"
# create an instance of InboundMessageCallback from a JSON string
inbound_message_callback_instance = InboundMessageCallback.from_json(json)
# print the JSON string representation of the object
print(InboundMessageCallback.to_json())

# convert the object into a dict
inbound_message_callback_dict = inbound_message_callback_instance.to_dict()
# create an instance of InboundMessageCallback from a dict
inbound_message_callback_form_dict = inbound_message_callback.from_dict(inbound_message_callback_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


