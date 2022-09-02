# CallRecordingMetadata


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** | The id of the application associated with the call. | [optional] 
**account_id** | **str** | The user account associated with the call. | [optional] 
**call_id** | **str** | The call id associated with the event. | [optional] 
**parent_call_id** | **str** | (optional) If the event is related to the B leg of a &lt;Transfer&gt;, the call id of the original call leg that executed the &lt;Transfer&gt;. Otherwise, this field will not be present. | [optional] 
**recording_id** | **str** | The unique ID of this recording | [optional] 
**to** | **str** | The phone number that received the call, in E.164 format (e.g. +15555555555). | [optional] 
**_from** | **str** | The provided identifier of the caller: can be a phone number in E.164 format (e.g. +15555555555) or one of Private, Restricted, Unavailable, or Anonymous. | [optional] 
**transfer_caller_id** | **str** | The phone number used as the from field of the B-leg call, in E.164 format (e.g. +15555555555) or one of Restricted, Anonymous, Private, or Unavailable. | [optional] 
**transfer_to** | **str** | The phone number used as the to field of the B-leg call, in E.164 format (e.g. +15555555555). | [optional] 
**duration** | **str** | The duration of the recording in ISO-8601 format | [optional] 
**direction** | [**CallDirectionEnum**](CallDirectionEnum.md) |  | [optional] 
**channels** | **int** | Always &#x60;1&#x60; for conference recordings; multi-channel recordings are not supported on conferences. | [optional] 
**start_time** | **datetime** | Time the call was started, in ISO 8601 format. | [optional] 
**end_time** | **datetime** | The time that the recording ended in ISO-8601 format | [optional] 
**file_format** | [**FileFormatEnum**](FileFormatEnum.md) |  | [optional] 
**status** | **str** | The current status of the process. For recording, current possible values are &#39;processing&#39;, &#39;partial&#39;, &#39;complete&#39;, &#39;deleted&#39;, and &#39;error&#39;. For transcriptions, current possible values are &#39;none&#39;, &#39;processing&#39;, &#39;available&#39;, &#39;error&#39;, &#39;timeout&#39;, &#39;file-size-too-big&#39;, and &#39;file-size-too-small&#39;. Additional states may be added in the future, so your application must be tolerant of unknown values. | [optional] 
**media_url** | **str, none_type** | The URL that can be used to download the recording. Only present if the recording is finished and may be downloaded. | [optional] 
**transcription** | [**TranscriptionMetadata**](TranscriptionMetadata.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


