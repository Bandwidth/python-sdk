# MessageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** | The ID of the Application your from number is associated with in the Bandwidth Phone Number Dashboard. | 
**to** | **List[str]** | The phone number(s) the message should be sent to in E164 format. | 
**var_from** | **str** | One of your telephone numbers the message should come from in E164 format. | 
**text** | **str** | The contents of the text message. Must be 2048 characters or less. | [optional] 
**media** | **List[str]** | A list of URLs to include as media attachments as part of the message. Each URL can be at most 4096 characters. | [optional] 
**tag** | **str** | A custom string that will be included in callback events of the message. Max 1024 characters. | [optional] 
**priority** | [**PriorityEnum**](PriorityEnum.md) |  | [optional] 
**expiration** | **datetime** | A string with the date/time value that the message will automatically expire by. This must be a valid RFC-3339 value, e.g., 2021-03-14T01:59:26Z or 2021-03-13T20:59:26-05:00. Must be a date-time in the future. Not supported on MMS. | [optional] 

## Example

```python
from bandwidth.models.message_request import MessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MessageRequest from a JSON string
message_request_instance = MessageRequest.from_json(json)
# print the JSON string representation of the object
print(MessageRequest.to_json())

# convert the object into a dict
message_request_dict = message_request_instance.to_dict()
# create an instance of MessageRequest from a dict
message_request_form_dict = message_request.from_dict(message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


