# RbmSession

RCS interactive session information for the message. An interactive session is a 24-hour window covering all Rich and Rich Media messages exchanged between an RCS agent and a specific end user mobile number. It is triggered when at least 4 messages are exchanged within 24 hours, at least 2 of them mobile-originated and at least 1 mobile-terminated. Only present on `message-delivered`, `message-received` and `session-started` callbacks for RBM messages of US agents with the Conversational billing category. Omitted for all other messages.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_initiate** | **bool** | Whether the message can start an interactive session. &#x60;false&#x60; if the message is already part of an active session, or if the agent is not eligible for interactive session billing. | 
**id** | **str** | The unique identifier of the interactive session the message is part of. This is not a message ID. Omitted if the message is not part of a session. | [optional] 
**type** | **str** | The type of the interactive session. Only present on &#x60;session-started&#x60; callbacks. | [optional] 
**start_time** | **datetime** | The time the 24-hour session window opened. Only present on &#x60;session-started&#x60; callbacks. | [optional] 
**end_time** | **datetime** | The time the 24-hour session window closes. Only present on &#x60;session-started&#x60; callbacks. | [optional] 

## Example

```python
from bandwidth.models.rbm_session import RbmSession

# TODO update the JSON string below
json = "{}"
# create an instance of RbmSession from a JSON string
rbm_session_instance = RbmSession.from_json(json)
# print the JSON string representation of the object
print(RbmSession.to_json())

# convert the object into a dict
rbm_session_dict = rbm_session_instance.to_dict()
# create an instance of RbmSession from a dict
rbm_session_from_dict = RbmSession.from_dict(rbm_session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


