# SuggestionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | The text associated with the suggestion response. | [optional] 
**postback_data** | **bytearray** | Base64 payload the customer receives when the reply is clicked. | [optional] 
**paired_message_id** | **str** | Corresponding parent message ID (MT). | [optional] 

## Example

```python
from bandwidth.models.suggestion_response import SuggestionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SuggestionResponse from a JSON string
suggestion_response_instance = SuggestionResponse.from_json(json)
# print the JSON string representation of the object
print(SuggestionResponse.to_json())

# convert the object into a dict
suggestion_response_dict = suggestion_response_instance.to_dict()
# create an instance of SuggestionResponse from a dict
suggestion_response_from_dict = SuggestionResponse.from_dict(suggestion_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


