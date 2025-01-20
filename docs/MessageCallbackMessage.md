# MessageCallbackMessage

Message payload schema within a MessageCallback

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
**media** | **List[str]** | Optional media, applicable only for mms | [optional] 
**priority** | [**PriorityEnum**](PriorityEnum.md) |  | [optional] 

## Example

```python
from bandwidth.models.message_callback_message import MessageCallbackMessage

# TODO update the JSON string below
json = "{}"
# create an instance of MessageCallbackMessage from a JSON string
message_callback_message_instance = MessageCallbackMessage.from_json(json)
# print the JSON string representation of the object
print(MessageCallbackMessage.to_json())

# convert the object into a dict
message_callback_message_dict = message_callback_message_instance.to_dict()
# create an instance of MessageCallbackMessage from a dict
message_callback_message_from_dict = MessageCallbackMessage.from_dict(message_callback_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


