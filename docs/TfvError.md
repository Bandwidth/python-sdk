# TfvError

A generic error object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**errors** | **object** | Each key of this errors object refers to a field of the submitted object (using dot notation for nested objects), with the field being a key to an array of one or more errors for that field. | [optional] 

## Example

```python
from bandwidth.models.tfv_error import TfvError

# TODO update the JSON string below
json = "{}"
# create an instance of TfvError from a JSON string
tfv_error_instance = TfvError.from_json(json)
# print the JSON string representation of the object
print(TfvError.to_json())

# convert the object into a dict
tfv_error_dict = tfv_error_instance.to_dict()
# create an instance of TfvError from a dict
tfv_error_from_dict = TfvError.from_dict(tfv_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


