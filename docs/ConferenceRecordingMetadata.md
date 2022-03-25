# ConferenceRecordingMetadata


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | Your account ID | [optional] 
**conference_id** | **str** | The unique, Bandwidth-generated ID of the conference that was recorded | [optional] 
**name** | **str** | The user-specified name of the conference that was recorded | [optional] 
**recording_id** | **str** | The unique ID of this recording | [optional] 
**duration** | **str** | The duration of the recording in ISO-8601 format | [optional] 
**channels** | **int** | Always &#x60;1&#x60; for conference recordings; multi-channel recordings are not supported on conferences. | [optional] 
**start_time** | **datetime** | The time that the recording started in ISO-8601 format | [optional] 
**end_time** | **datetime** | The time that the recording ended in ISO-8601 format | [optional] 
**file_format** | **str** | The format that the recording is stored in | [optional] 
**status** | **str** | The current status of the recording. Current possible values are &#39;processing&#39;, &#39;partial&#39;, &#39;complete&#39;, &#39;deleted&#39;, and &#39;error&#39;. Additional states may be added in the future, so your application must be tolerant of unknown values. | [optional] 
**media_url** | **str, none_type** | The URL that can be used to download the recording. Only present if the recording is finished and may be downloaded. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


