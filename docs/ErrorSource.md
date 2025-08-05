# ErrorSource

Specifies relevant sources of the error, if any.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameter** | **str** | The relevant URI query parameter causing the error | [optional] 
**var_field** | **str** | The request body field that led to the error | [optional] 
**header** | **str** | The header field that contributed to the error | [optional] 
**reference** | **str** | A resource ID or path linked to the error | [optional] 

## Example

```python
from bandwidth.models.error_source import ErrorSource

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorSource from a JSON string
error_source_instance = ErrorSource.from_json(json)
# print the JSON string representation of the object
print(ErrorSource.to_json())

# convert the object into a dict
error_source_dict = error_source_instance.to_dict()
# create an instance of ErrorSource from a dict
error_source_from_dict = ErrorSource.from_dict(error_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


