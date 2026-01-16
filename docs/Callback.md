# Callback

Callbacks are divided into two types based on direction of the related message: - `statusCallback` indicates status of an outbound MT SMS, MMS, or RBM message. - `inboundCallback` indicates an inbound MO message or a multichannel message client's response to a suggestion or location request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **datetime** |  | 
**event_time** | **datetime** | Represents the time at which the message was read, for &#x60;message-read&#x60; callbacks. | [optional] 
**type** | [**InboundCallbackTypeEnum**](InboundCallbackTypeEnum.md) |  | 
**to** | **str** | The destination phone number the message was sent to. For inbound callbacks, this is the Bandwidth number or alphanumeric identifier that received the message.  | 
**description** | **str** | A detailed description of the event described by the callback. | 
**message** | [**InboundCallbackMessage**](InboundCallbackMessage.md) |  | 
**error_code** | **int** | Optional error code, applicable only when type is &#x60;message-failed&#x60;. | [optional] 
**carrier_name** | **str** | The name of the Authorized Message Provider (AMP) that handled this message. In the US, this is the carrier that the message was sent to. This field is present only when this account feature has been enabled. | [optional] 

## Example

```python
from bandwidth.models.callback import Callback

# TODO update the JSON string below
json = "{}"
# create an instance of Callback from a JSON string
callback_instance = Callback.from_json(json)
# print the JSON string representation of the object
print(Callback.to_json())

# convert the object into a dict
callback_dict = callback_instance.to_dict()
# create an instance of Callback from a dict
callback_from_dict = Callback.from_dict(callback_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


