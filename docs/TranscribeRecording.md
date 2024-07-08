# TranscribeRecording


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_url** | **str** | The URL to send the [TranscriptionAvailable](/docs/voice/webhooks/transcriptionAvailable) event to. You should not include sensitive or personally-identifiable information in the callbackUrl field! Always use the proper username and password fields for authorization. | [optional] 
**callback_method** | [**CallbackMethodEnum**](CallbackMethodEnum.md) |  | [optional] [default to CallbackMethodEnum.POST]
**username** | **str** | Basic auth username. | [optional] 
**password** | **str** | Basic auth password. | [optional] 
**tag** | **str** | (optional) The tag specified on call creation. If no tag was specified or it was previously cleared, this field will not be present. | [optional] 
**callback_timeout** | **float** | This is the timeout (in seconds) to use when delivering the webhook to &#x60;callbackUrl&#x60;. Can be any numeric value (including decimals) between 1 and 25. | [optional] [default to 15]
**detect_language** | **bool** | A boolean value to indicate that the recording may not be in English, and the transcription service will need to detect the dominant language the recording is in and transcribe accordingly. Current supported languages are English, French, and Spanish. | [optional] [default to False]

## Example

```python
from bandwidth.models.transcribe_recording import TranscribeRecording

# TODO update the JSON string below
json = "{}"
# create an instance of TranscribeRecording from a JSON string
transcribe_recording_instance = TranscribeRecording.from_json(json)
# print the JSON string representation of the object
print(TranscribeRecording.to_json())

# convert the object into a dict
transcribe_recording_dict = transcribe_recording_instance.to_dict()
# create an instance of TranscribeRecording from a dict
transcribe_recording_from_dict = TranscribeRecording.from_dict(transcribe_recording_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


