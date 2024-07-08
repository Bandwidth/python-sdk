# Transcription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | The transcribed text | [optional] 
**confidence** | **float** | The confidence on the recognized content, ranging from &#x60;0.0&#x60; to &#x60;1.0&#x60; with &#x60;1.0&#x60; being the highest confidence. | [optional] 

## Example

```python
from bandwidth.models.transcription import Transcription

# TODO update the JSON string below
json = "{}"
# create an instance of Transcription from a JSON string
transcription_instance = Transcription.from_json(json)
# print the JSON string representation of the object
print(Transcription.to_json())

# convert the object into a dict
transcription_dict = transcription_instance.to_dict()
# create an instance of Transcription from a dict
transcription_from_dict = Transcription.from_dict(transcription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


