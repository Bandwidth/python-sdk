# LookupErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**List[LinkSchema]**](LinkSchema.md) |  | [optional] 
**data** | **object** | The phone number lookup response data | [optional] 
**errors** | [**List[LookupErrorSchema]**](LookupErrorSchema.md) |  | [optional] 

## Example

```python
from bandwidth.models.lookup_error_response import LookupErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LookupErrorResponse from a JSON string
lookup_error_response_instance = LookupErrorResponse.from_json(json)
# print the JSON string representation of the object
print(LookupErrorResponse.to_json())

# convert the object into a dict
lookup_error_response_dict = lookup_error_response_instance.to_dict()
# create an instance of LookupErrorResponse from a dict
lookup_error_response_from_dict = LookupErrorResponse.from_dict(lookup_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


