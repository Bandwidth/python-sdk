# CallRecordingMetadata


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** | The &#x60;applicationId&#x60; associated with the call | [optional] 
**account_id** | **str** | The account that placed the call | [optional] 
**call_id** | **str** | The &#x60;callId&#x60; of the call that created this recording | [optional] 
**parent_call_id** | **str, none_type** | If the call was a transferred leg, this field contains the &#x60;callId&#x60; of the call that executed the [&#x60;&lt;Transfer&gt;&#x60;](/docs/voice/bxml/transfer) | [optional] 
**recording_id** | **str** | The recording&#39;s unique ID | [optional] 
**to** | **str** | The phone number that received the call, in E.164 format (e.g. +15555555555), or if the call was to a SIP URI, the SIP URI | [optional] 
**_from** | **str** | The phone number that made the call, in E.164 format (e.g. +15555555555). | [optional] 
**transfer_caller_id** | **str, none_type** | If the call was a transferred leg, the &#x60;transferCallerId&#x60; field from the [&#x60;&lt;Transfer&gt;&#x60;](/docs/voice/bxml/transfer), if any. | [optional] 
**transfer_to** | **str, none_type** | If the call was a transferred leg, the number that the call was transferred to | [optional] 
**duration** | **str** | The duration of the recording in ISO-8601 format | [optional] 
**direction** | **str** | The direction of the call. | [optional] 
**channels** | **int** | The number of channels in the recording. Either &#x60;1&#x60; or &#x60;2&#x60; | [optional] 
**start_time** | **datetime** | The time that the recording started in ISO 8601 format | [optional] 
**end_time** | **datetime** | The time that the recording ended in ISO 8601 format | [optional] 
**file_format** | **str** | The format that the recording is stored in | [optional] 
**status** | **str** | The current status of the recording. Current values are &#39;processing&#39;, &#39;partial&#39;, &#39;complete&#39;, &#39;deleted&#39; and &#39;error&#39;. Additional states may be added in the future, so your application must be tolerant of unknown values. | [optional] 
**media_url** | **str** | The URL that can be used to download the audio recording | [optional] 
**transcription** | [**TranscriptionMetadata**](TranscriptionMetadata.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


