# AnswerCallback

The Answer event is sent to the answerUrl specified in the createCall request when an outbound call is answered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | **str** | The event type, value can be one of the following: answer, bridgeComplete, bridgeTargetComplete, conferenceCreated, conferenceRedirect, conferenceMemberJoin, conferenceMemberExit, conferenceCompleted, conferenceRecordingAvailable, disconnect, dtmf, gather, initiate, machineDetectionComplete, recordingComplete, recordingAvailable, redirect, transcriptionAvailable, transferAnswer, transferComplete, transferDisconnect. | [optional] 
**event_time** | **datetime** | The approximate UTC date and time when the event was generated by the Bandwidth server, in ISO 8601 format. This may not be exactly the time of event execution. | [optional] 
**account_id** | **str** | The user account associated with the call. | [optional] 
**application_id** | **str** | The id of the application associated with the call. | [optional] 
**var_from** | **str** | The provided identifier of the caller. Must be a phone number in E.164 format (e.g. +15555555555). | [optional] 
**to** | **str** | The phone number that received the call, in E.164 format (e.g. +15555555555). | [optional] 
**direction** | [**CallDirectionEnum**](CallDirectionEnum.md) |  | [optional] 
**call_id** | **str** | The call id associated with the event. | [optional] 
**call_url** | **str** | The URL of the call associated with the event. | [optional] 
**enqueued_time** | **datetime** | (optional) If call queueing is enabled and this is an outbound call, time the call was queued, in ISO 8601 format. | [optional] 
**start_time** | **datetime** | Time the call was started, in ISO 8601 format. | [optional] 
**answer_time** | **datetime** | Time the call was answered, in ISO 8601 format. | [optional] 
**tag** | **str** | (optional) The tag specified on call creation. If no tag was specified or it was previously cleared, this field will not be present. | [optional] 
**machine_detection_result** | [**MachineDetectionResult**](MachineDetectionResult.md) |  | [optional] 

## Example

```python
from bandwidth.models.answer_callback import AnswerCallback

# TODO update the JSON string below
json = "{}"
# create an instance of AnswerCallback from a JSON string
answer_callback_instance = AnswerCallback.from_json(json)
# print the JSON string representation of the object
print(AnswerCallback.to_json())

# convert the object into a dict
answer_callback_dict = answer_callback_instance.to_dict()
# create an instance of AnswerCallback from a dict
answer_callback_from_dict = AnswerCallback.from_dict(answer_callback_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


