# Subscriptions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** | Session the subscriptions are associated with. If this is the only field, the subscriber will be subscribed to all participants in the session (including any participants that are later added to the session). Upon creation of a Participant, returns as an empty object. | [optional] 
**participants** | [**[ParticipantSubscription]**](ParticipantSubscription.md) | (optional) A list of participants  in the session that will be subscribed to. Returns empty if used during the creation of a Participant.  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


