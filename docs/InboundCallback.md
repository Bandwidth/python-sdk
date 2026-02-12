# InboundCallback

Represents an inbound callback.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **datetime** |  | 
**type** | [**InboundCallbackTypeEnum**](InboundCallbackTypeEnum.md) |  | 
**to** | **str** | The destination phone number the message was sent to. For inbound callbacks, this is the Bandwidth number or alphanumeric identifier that received the message.  | 
**description** | **str** | A detailed description of the event described by the callback. | 
**message** | [**InboundCallbackMessage**](InboundCallbackMessage.md) |  | 
**carrier_name** | **str** | The name of the Authorized Message Provider (AMP) that handled this message. In the US, this is the carrier that the message was sent to. This field is present only when this account feature has been enabled. | [optional] 

## Example

```python
from bandwidth.models.inbound_callback import InboundCallback

# TODO update the JSON string below
json = "{}"
# create an instance of InboundCallback from a JSON string
inbound_callback_instance = InboundCallback.from_json(json)
# print the JSON string representation of the object
print(InboundCallback.to_json())

# convert the object into a dict
inbound_callback_dict = inbound_callback_instance.to_dict()
# create an instance of InboundCallback from a dict
inbound_callback_from_dict = InboundCallback.from_dict(inbound_callback_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


