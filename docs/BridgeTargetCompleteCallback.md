# BridgeTargetCompleteCallback

If the originating call leaves the <Bridge>, then this callback is sent to the bridgeTargetCompleteUrl, and the BXML returned in it is executed on the target call. If this webhook is sent, the Bridge Complete webhook is NOT sent.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | **str** | The event type, value can be one of the following: answer, bridgeComplete, bridgeTargetComplete, conferenceCreated, conferenceRedirect, conferenceMemberJoin, conferenceMemberExit, conferenceCompleted, conferenceRecordingAvailable, disconnect, dtmf, gather, initiate, machineDetectionComplete, recordingComplete, recordingAvailable, redirect, transcriptionAvailable, transferAnswer, transferComplete, transferDisconnect. | [optional] 
**event_time** | **datetime** | The approximate UTC date and time when the event was generated by the Bandwidth server, in ISO 8601 format. This may not be exactly the time of event execution. | [optional] 
**account_id** | **str** | The user account associated with the call. | [optional] 
**application_id** | **str** | The id of the application associated with the call. | [optional] 
**var_from** | **str** | The provided identifier of the caller: can be a phone number in E.164 format (e.g. +15555555555) or one of Private, Restricted, Unavailable, or Anonymous. | [optional] 
**to** | **str** | The phone number that received the call, in E.164 format (e.g. +15555555555). | [optional] 
**direction** | [**CallDirectionEnum**](CallDirectionEnum.md) |  | [optional] 
**call_id** | **str** | The call id associated with the event. | [optional] 
**call_url** | **str** | The URL of the call associated with the event. | [optional] 
**enqueued_time** | **datetime** | (optional) If call queueing is enabled and this is an outbound call, time the call was queued, in ISO 8601 format. | [optional] 
**start_time** | **datetime** | Time the call was started, in ISO 8601 format. | [optional] 
**answer_time** | **datetime** | Time the call was answered, in ISO 8601 format. | [optional] 
**tag** | **str** | (optional) The tag specified on call creation. If no tag was specified or it was previously cleared, this field will not be present. | [optional] 

## Example

```python
from bandwidth.models.bridge_target_complete_callback import BridgeTargetCompleteCallback

# TODO update the JSON string below
json = "{}"
# create an instance of BridgeTargetCompleteCallback from a JSON string
bridge_target_complete_callback_instance = BridgeTargetCompleteCallback.from_json(json)
# print the JSON string representation of the object
print BridgeTargetCompleteCallback.to_json()

# convert the object into a dict
bridge_target_complete_callback_dict = bridge_target_complete_callback_instance.to_dict()
# create an instance of BridgeTargetCompleteCallback from a dict
bridge_target_complete_callback_form_dict = bridge_target_complete_callback.from_dict(bridge_target_complete_callback_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

