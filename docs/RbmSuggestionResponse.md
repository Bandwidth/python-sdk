# RbmSuggestionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | The text associated with the suggestion response. | [optional] 
**postback_data** | **bytearray** | Base64 payload the customer receives when the reply is clicked. | [optional] 

## Example

```python
from bandwidth.models.rbm_suggestion_response import RbmSuggestionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RbmSuggestionResponse from a JSON string
rbm_suggestion_response_instance = RbmSuggestionResponse.from_json(json)
# print the JSON string representation of the object
print(RbmSuggestionResponse.to_json())

# convert the object into a dict
rbm_suggestion_response_dict = rbm_suggestion_response_instance.to_dict()
# create an instance of RbmSuggestionResponse from a dict
rbm_suggestion_response_from_dict = RbmSuggestionResponse.from_dict(rbm_suggestion_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


