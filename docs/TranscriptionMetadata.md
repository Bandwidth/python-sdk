# TranscriptionMetadata

If the recording was transcribed, metadata about the transcription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique transcription ID | [optional] 
**status** | **str** | The current status of the process. For recording, current possible values are &#39;processing&#39;, &#39;partial&#39;, &#39;complete&#39;, &#39;deleted&#39;, and &#39;error&#39;. For transcriptions, current possible values are &#39;none&#39;, &#39;processing&#39;, &#39;available&#39;, &#39;error&#39;, &#39;timeout&#39;, &#39;file-size-too-big&#39;, and &#39;file-size-too-small&#39;. Additional states may be added in the future, so your application must be tolerant of unknown values. | [optional] 
**completed_time** | **str** | The time that the transcription was completed | [optional] 
**url** | **str** | The URL of the [transcription](#operation/getCallTranscription) | [optional] 

## Example

```python
from bandwidth.models.transcription_metadata import TranscriptionMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of TranscriptionMetadata from a JSON string
transcription_metadata_instance = TranscriptionMetadata.from_json(json)
# print the JSON string representation of the object
print(TranscriptionMetadata.to_json())

# convert the object into a dict
transcription_metadata_dict = transcription_metadata_instance.to_dict()
# create an instance of TranscriptionMetadata from a dict
transcription_metadata_form_dict = transcription_metadata.from_dict(transcription_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


