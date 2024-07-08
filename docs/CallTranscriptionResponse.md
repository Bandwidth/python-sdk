# CallTranscriptionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The user account associated with the call. | [optional] 
**call_id** | **str** | The call id associated with the event. | [optional] 
**transcription_id** | **str** | The programmable voice API transcription ID. | [optional] 
**tracks** | [**List[CallTranscription]**](CallTranscription.md) |  | [optional] 

## Example

```python
from bandwidth.models.call_transcription_response import CallTranscriptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CallTranscriptionResponse from a JSON string
call_transcription_response_instance = CallTranscriptionResponse.from_json(json)
# print the JSON string representation of the object
print(CallTranscriptionResponse.to_json())

# convert the object into a dict
call_transcription_response_dict = call_transcription_response_instance.to_dict()
# create an instance of CallTranscriptionResponse from a dict
call_transcription_response_from_dict = CallTranscriptionResponse.from_dict(call_transcription_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


