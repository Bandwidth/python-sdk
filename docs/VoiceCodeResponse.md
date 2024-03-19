# VoiceCodeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**call_id** | **str** | Programmable Voice API Call ID. | [optional] 

## Example

```python
from bandwidth.models.voice_code_response import VoiceCodeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VoiceCodeResponse from a JSON string
voice_code_response_instance = VoiceCodeResponse.from_json(json)
# print the JSON string representation of the object
print(VoiceCodeResponse.to_json())

# convert the object into a dict
voice_code_response_dict = voice_code_response_instance.to_dict()
# create an instance of VoiceCodeResponse from a dict
voice_code_response_form_dict = voice_code_response.from_dict(voice_code_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


