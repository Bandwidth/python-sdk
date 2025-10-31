# LookupErrorSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Validation error code | [optional] 
**description** | **str** | Description of validation error | [optional] 
**type** | **str** | Type of validation error | [optional] 
**meta** | [**LookupErrorSchemaMeta**](LookupErrorSchemaMeta.md) |  | [optional] 

## Example

```python
from bandwidth.models.lookup_error_schema import LookupErrorSchema

# TODO update the JSON string below
json = "{}"
# create an instance of LookupErrorSchema from a JSON string
lookup_error_schema_instance = LookupErrorSchema.from_json(json)
# print the JSON string representation of the object
print(LookupErrorSchema.to_json())

# convert the object into a dict
lookup_error_schema_dict = lookup_error_schema_instance.to_dict()
# create an instance of LookupErrorSchema from a dict
lookup_error_schema_from_dict = LookupErrorSchema.from_dict(lookup_error_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


