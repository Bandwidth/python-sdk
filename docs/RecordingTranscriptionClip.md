# RecordingTranscriptionClip


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**speaker** | **int** | Zero-based index identifying the speaker. | [optional] 
**text** | **str** | The transcribed text of this clip. | [optional] 
**confidence** | **float** | How confident the transcription engine was in transcribing this clip (from &#x60;0.0&#x60; to &#x60;1.0&#x60;). | [optional] 
**start_time_seconds** | **float** | The start time of this clip within the recording, in seconds. | [optional] 
**end_time_seconds** | **float** | The end time of this clip within the recording, in seconds. | [optional] 

## Example

```python
from bandwidth.models.recording_transcription_clip import RecordingTranscriptionClip

# TODO update the JSON string below
json = "{}"
# create an instance of RecordingTranscriptionClip from a JSON string
recording_transcription_clip_instance = RecordingTranscriptionClip.from_json(json)
# print the JSON string representation of the object
print(RecordingTranscriptionClip.to_json())

# convert the object into a dict
recording_transcription_clip_dict = recording_transcription_clip_instance.to_dict()
# create an instance of RecordingTranscriptionClip from a dict
recording_transcription_clip_from_dict = RecordingTranscriptionClip.from_dict(recording_transcription_clip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


