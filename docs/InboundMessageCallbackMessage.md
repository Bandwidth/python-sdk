# InboundMessageCallbackMessage

Inbound Message Callback Message Schema

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
**media** | **List[str]** |  | [optional] 
**priority** | [**PriorityEnum**](PriorityEnum.md) |  | [optional] 

## Example

```python
from bandwidth.models.inbound_message_callback_message import InboundMessageCallbackMessage

# TODO update the JSON string below
json = "{}"
# create an instance of InboundMessageCallbackMessage from a JSON string
inbound_message_callback_message_instance = InboundMessageCallbackMessage.from_json(json)
# print the JSON string representation of the object
print(InboundMessageCallbackMessage.to_json())

# convert the object into a dict
inbound_message_callback_message_dict = inbound_message_callback_message_instance.to_dict()
# create an instance of InboundMessageCallbackMessage from a dict
inbound_message_callback_message_form_dict = inbound_message_callback_message.from_dict(inbound_message_callback_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


