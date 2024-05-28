# CallTranscriptionMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transcription_id** | **str** | The programmable voice API transcription ID. | [optional] 
**transcription_url** | **str** | A URL that may be used to retrieve the transcription itself. This points to the [Get Call Transcription](/apis/voice/#operation/getCallTranscription) endpoint. | [optional] 

## Example

```python
from bandwidth.models.call_transcription_metadata import CallTranscriptionMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of CallTranscriptionMetadata from a JSON string
call_transcription_metadata_instance = CallTranscriptionMetadata.from_json(json)
# print the JSON string representation of the object
print(CallTranscriptionMetadata.to_json())

# convert the object into a dict
call_transcription_metadata_dict = call_transcription_metadata_instance.to_dict()
# create an instance of CallTranscriptionMetadata from a dict
call_transcription_metadata_form_dict = call_transcription_metadata.from_dict(call_transcription_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


