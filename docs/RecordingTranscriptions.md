# RecordingTranscriptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transcripts** | [**List[Transcription]**](Transcription.md) |  | [optional] 

## Example

```python
from bandwidth.models.recording_transcriptions import RecordingTranscriptions

# TODO update the JSON string below
json = "{}"
# create an instance of RecordingTranscriptions from a JSON string
recording_transcriptions_instance = RecordingTranscriptions.from_json(json)
# print the JSON string representation of the object
print(RecordingTranscriptions.to_json())

# convert the object into a dict
recording_transcriptions_dict = recording_transcriptions_instance.to_dict()
# create an instance of RecordingTranscriptions from a dict
recording_transcriptions_form_dict = recording_transcriptions.from_dict(recording_transcriptions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


