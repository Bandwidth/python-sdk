# LookupErrorSchemaMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_numbers** | **List[str]** |  | [optional] 
**message** | **str** | Message describing the error | [optional] 
**code** | **int** | Error code associated with the message | [optional] 

## Example

```python
from bandwidth.models.lookup_error_schema_meta import LookupErrorSchemaMeta

# TODO update the JSON string below
json = "{}"
# create an instance of LookupErrorSchemaMeta from a JSON string
lookup_error_schema_meta_instance = LookupErrorSchemaMeta.from_json(json)
# print the JSON string representation of the object
print(LookupErrorSchemaMeta.to_json())

# convert the object into a dict
lookup_error_schema_meta_dict = lookup_error_schema_meta_instance.to_dict()
# create an instance of LookupErrorSchemaMeta from a dict
lookup_error_schema_meta_from_dict = LookupErrorSchemaMeta.from_dict(lookup_error_schema_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


