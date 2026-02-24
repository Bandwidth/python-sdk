# StatusCallback

Represents a status callback for an outbound MT SMS or MMS or RBM message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **datetime** |  | 
**event_time** | **datetime** | Represents the time at which the message was read, for &#x60;message-read&#x60; callbacks. | [optional] 
**type** | [**StatusCallbackTypeEnum**](StatusCallbackTypeEnum.md) |  | 
**to** | **str** | The destination phone number the message was sent to. For status callbacks, this the the Bandwidth user&#39;s client phone number. | 
**description** | **str** | A detailed description of the event described by the callback. | 
**message** | [**StatusCallbackMessage**](StatusCallbackMessage.md) |  | 
**error_code** | **int** | Optional error code, applicable only when type is &#x60;message-failed&#x60;. | [optional] 
**carrier_name** | **str** | The name of the Authorized Message Provider (AMP) that handled this message. In the US, this is the carrier that the message was sent to. This field is present only when this account feature has been enabled. | [optional] 

## Example

```python
from bandwidth.models.status_callback import StatusCallback

# TODO update the JSON string below
json = "{}"
# create an instance of StatusCallback from a JSON string
status_callback_instance = StatusCallback.from_json(json)
# print the JSON string representation of the object
print(StatusCallback.to_json())

# convert the object into a dict
status_callback_dict = status_callback_instance.to_dict()
# create an instance of StatusCallback from a dict
status_callback_from_dict = StatusCallback.from_dict(status_callback_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


