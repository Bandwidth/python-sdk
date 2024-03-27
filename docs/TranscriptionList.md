# TranscriptionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transcripts** | [**List[Transcription]**](Transcription.md) |  | [optional] 

## Example

```python
from bandwidth.models.transcription_list import TranscriptionList

# TODO update the JSON string below
json = "{}"
# create an instance of TranscriptionList from a JSON string
transcription_list_instance = TranscriptionList.from_json(json)
# print the JSON string representation of the object
print(TranscriptionList.to_json())

# convert the object into a dict
transcription_list_dict = transcription_list_instance.to_dict()
# create an instance of TranscriptionList from a dict
transcription_list_form_dict = transcription_list.from_dict(transcription_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


