# CallTranscription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detected_language** | [**CallTranscriptionDetectedLanguageEnum**](CallTranscriptionDetectedLanguageEnum.md) |  | [optional] 
**track** | [**CallTranscriptionTrackEnum**](CallTranscriptionTrackEnum.md) |  | [optional] 
**transcript** | **str** | The transcription itself. | [optional] 
**confidence** | **float** | How confident the transcription engine was in transcribing the associated audio (from &#x60;0&#x60; to &#x60;1&#x60;). | [optional] 

## Example

```python
from bandwidth.models.call_transcription import CallTranscription

# TODO update the JSON string below
json = "{}"
# create an instance of CallTranscription from a JSON string
call_transcription_instance = CallTranscription.from_json(json)
# print the JSON string representation of the object
print(CallTranscription.to_json())

# convert the object into a dict
call_transcription_dict = call_transcription_instance.to_dict()
# create an instance of CallTranscription from a dict
call_transcription_from_dict = CallTranscription.from_dict(call_transcription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


