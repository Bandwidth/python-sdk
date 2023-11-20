# VoiceApiError


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from bandwidth.models.voice_api_error import VoiceApiError

# TODO update the JSON string below
json = "{}"
# create an instance of VoiceApiError from a JSON string
voice_api_error_instance = VoiceApiError.from_json(json)
# print the JSON string representation of the object
print VoiceApiError.to_json()

# convert the object into a dict
voice_api_error_dict = voice_api_error_instance.to_dict()
# create an instance of VoiceApiError from a dict
voice_api_error_form_dict = voice_api_error.from_dict(voice_api_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


