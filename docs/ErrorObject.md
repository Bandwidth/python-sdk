# ErrorObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | A concise summary of the error used for categorization. | 
**description** | **str** | A detailed explanation of the error. | 
**source** | [**ErrorSource**](ErrorSource.md) |  | 

## Example

```python
from bandwidth.models.error_object import ErrorObject

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorObject from a JSON string
error_object_instance = ErrorObject.from_json(json)
# print the JSON string representation of the object
print(ErrorObject.to_json())

# convert the object into a dict
error_object_dict = error_object_instance.to_dict()
# create an instance of ErrorObject from a dict
error_object_from_dict = ErrorObject.from_dict(error_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


