# Error1Source


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameter** | **str** | The URI parameter that caused the error. | [optional] 
**var_field** | **str** | The request body field that caused the error. | [optional] 
**header** | **str** | The header that caused the error. | [optional] 
**reference** | **str** | The resource ID or path to the resource (or non-existent resource) causing the error. | [optional] 

## Example

```python
from bandwidth.models.error1_source import Error1Source

# TODO update the JSON string below
json = "{}"
# create an instance of Error1Source from a JSON string
error1_source_instance = Error1Source.from_json(json)
# print the JSON string representation of the object
print(Error1Source.to_json())

# convert the object into a dict
error1_source_dict = error1_source_instance.to_dict()
# create an instance of Error1Source from a dict
error1_source_from_dict = Error1Source.from_dict(error1_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


