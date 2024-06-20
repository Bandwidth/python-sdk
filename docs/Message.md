# Message


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the message. | [optional] 
**owner** | **str** | The Bandwidth phone number associated with the message. | [optional] 
**application_id** | **str** | The application ID associated with the message. | [optional] 
**time** | **datetime** | The datetime stamp of the message in ISO 8601 | [optional] 
**segment_count** | **int** | The number of segments the original message from the user is broken into before sending over to carrier networks. | [optional] 
**direction** | [**MessageDirectionEnum**](MessageDirectionEnum.md) |  | [optional] 
**to** | **List[str]** | The phone number recipients of the message. | [optional] 
**var_from** | **str** | The phone number the message was sent from. | [optional] 
**media** | **List[str]** | The list of media URLs sent in the message. Including a &#x60;filename&#x60; field in the &#x60;Content-Disposition&#x60; header of the media linked with a URL will set the displayed file name. This is a best practice to ensure that your media has a readable file name. | [optional] 
**text** | **str** | The contents of the message. | [optional] 
**tag** | **str** | The custom string set by the user. | [optional] 
**priority** | [**PriorityEnum**](PriorityEnum.md) |  | [optional] 
**expiration** | **datetime** | The expiration date-time set by the user. | [optional] 

## Example

```python
from bandwidth.models.message import Message

# TODO update the JSON string below
json = "{}"
# create an instance of Message from a JSON string
message_instance = Message.from_json(json)
# print the JSON string representation of the object
print(Message.to_json())

# convert the object into a dict
message_dict = message_instance.to_dict()
# create an instance of Message from a dict
message_from_dict = Message.from_dict(message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


