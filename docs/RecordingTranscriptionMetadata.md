# RecordingTranscriptionMetadata

If the recording was transcribed, metadata about the transcription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique transcription ID | [optional] 
**status** | **str** | The current status of the process. For recording, current possible values are &#39;processing&#39;, &#39;partial&#39;, &#39;complete&#39;, &#39;deleted&#39;, and &#39;error&#39;. For transcriptions, current possible values are &#39;none&#39;, &#39;processing&#39;, &#39;available&#39;, &#39;error&#39;, &#39;timeout&#39;, &#39;file-size-too-big&#39;, and &#39;file-size-too-small&#39;. Additional states may be added in the future, so your application must be tolerant of unknown values. | [optional] 
**completed_time** | **datetime** | The time that the transcription was completed | [optional] 
**url** | **str** | The URL of the [transcription](#operation/getCallTranscription) | [optional] 

## Example

```python
from bandwidth.models.recording_transcription_metadata import RecordingTranscriptionMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of RecordingTranscriptionMetadata from a JSON string
recording_transcription_metadata_instance = RecordingTranscriptionMetadata.from_json(json)
# print the JSON string representation of the object
print(RecordingTranscriptionMetadata.to_json())

# convert the object into a dict
recording_transcription_metadata_dict = recording_transcription_metadata_instance.to_dict()
# create an instance of RecordingTranscriptionMetadata from a dict
recording_transcription_metadata_from_dict = RecordingTranscriptionMetadata.from_dict(recording_transcription_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


