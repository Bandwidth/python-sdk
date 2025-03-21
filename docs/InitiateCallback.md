# InitiateCallback

The Initiate event is fired when an inbound call is received for a Telephone Number on your Account. It is sent to the URL specified in the application associated with the location (sip-peer) that the called telephone number belongs to.

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
**start_time** | **datetime** | Time the call was started, in ISO 8601 format. | [optional] 
**diversion** | [**Diversion**](Diversion.md) |  | [optional] 
**stir_shaken** | [**StirShaken**](StirShaken.md) |  | [optional] 
**uui** | **str** | The value of the &#x60;User-To-User&#x60; header to send within the initial &#x60;INVITE&#x60;. Must include the encoding parameter as specified in RFC 7433. Only &#x60;base64&#x60;, &#x60;jwt&#x60; and &#x60;hex&#x60; encoding are currently allowed. This value, including the encoding specifier, may not exceed 256 characters. | [optional] 

## Example

```python
from bandwidth.models.initiate_callback import InitiateCallback

# TODO update the JSON string below
json = "{}"
# create an instance of InitiateCallback from a JSON string
initiate_callback_instance = InitiateCallback.from_json(json)
# print the JSON string representation of the object
print(InitiateCallback.to_json())

# convert the object into a dict
initiate_callback_dict = initiate_callback_instance.to_dict()
# create an instance of InitiateCallback from a dict
initiate_callback_from_dict = InitiateCallback.from_dict(initiate_callback_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


