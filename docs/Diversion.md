# Diversion


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | The reason for the diversion. Common values: unknown, user-busy, no-answer, unavailable, unconditional, time-of-day, do-not-disturb, deflection, follow-me, out-of-service, away. | [optional] 
**privacy** | **str** | off or full | [optional] 
**screen** | **str** | No if the number was provided by the user, yes if the number was provided by the network | [optional] 
**counter** | **str** | The number of diversions that have occurred | [optional] 
**limit** | **str** | The maximum number of diversions allowed for this session | [optional] 
**unknown** | **str** | The normal list of values is not exhaustive. Your application must be tolerant of unlisted keys and unlisted values of those keys. | [optional] 
**orig_to** | **str** | Always present. Indicates the last telephone number that the call was diverted from. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


