# MessageDeliveredCallbackMessage

Message Delivered Callback Message Schema

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
**tag** | **str** |  | 
**media** | **List[str]** |  | [optional] 
**priority** | [**PriorityEnum**](PriorityEnum.md) |  | [optional] 

## Example

```python
from bandwidth.models.message_delivered_callback_message import MessageDeliveredCallbackMessage

# TODO update the JSON string below
json = "{}"
# create an instance of MessageDeliveredCallbackMessage from a JSON string
message_delivered_callback_message_instance = MessageDeliveredCallbackMessage.from_json(json)
# print the JSON string representation of the object
print(MessageDeliveredCallbackMessage.to_json())

# convert the object into a dict
message_delivered_callback_message_dict = message_delivered_callback_message_instance.to_dict()
# create an instance of MessageDeliveredCallbackMessage from a dict
message_delivered_callback_message_from_dict = MessageDeliveredCallbackMessage.from_dict(message_delivered_callback_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


