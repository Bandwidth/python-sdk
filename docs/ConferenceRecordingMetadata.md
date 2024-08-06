# ConferenceRecordingMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The user account associated with the call. | [optional] 
**conference_id** | **str** | The unique, Bandwidth-generated ID of the conference that was recorded | [optional] 
**name** | **str** | The user-specified name of the conference that was recorded | [optional] 
**recording_id** | **str** | The unique ID of this recording | [optional] 
**duration** | **str** | The duration of the recording in ISO-8601 format | [optional] 
**channels** | **int** | Always &#x60;1&#x60; for conference recordings; multi-channel recordings are not supported on conferences. | [optional] 
**start_time** | **datetime** | Time the call was started, in ISO 8601 format. | [optional] 
**end_time** | **datetime** | The time that the recording ended in ISO-8601 format | [optional] 
**file_format** | [**FileFormatEnum**](FileFormatEnum.md) |  | [optional] 
**status** | **str** | The current status of the process. For recording, current possible values are &#39;processing&#39;, &#39;partial&#39;, &#39;complete&#39;, &#39;deleted&#39;, and &#39;error&#39;. For transcriptions, current possible values are &#39;none&#39;, &#39;processing&#39;, &#39;available&#39;, &#39;error&#39;, &#39;timeout&#39;, &#39;file-size-too-big&#39;, and &#39;file-size-too-small&#39;. Additional states may be added in the future, so your application must be tolerant of unknown values. | [optional] 
**media_url** | **str** | The URL that can be used to download the recording. Only present if the recording is finished and may be downloaded. | [optional] 
**recording_name** | **str** | A name to identify this recording. | [optional] 

## Example

```python
from bandwidth.models.conference_recording_metadata import ConferenceRecordingMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ConferenceRecordingMetadata from a JSON string
conference_recording_metadata_instance = ConferenceRecordingMetadata.from_json(json)
# print the JSON string representation of the object
print(ConferenceRecordingMetadata.to_json())

# convert the object into a dict
conference_recording_metadata_dict = conference_recording_metadata_instance.to_dict()
# create an instance of ConferenceRecordingMetadata from a dict
conference_recording_metadata_from_dict = ConferenceRecordingMetadata.from_dict(conference_recording_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


