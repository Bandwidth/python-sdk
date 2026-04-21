# Error1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for the error. | [optional] 
**type** | **str** | The type of error. | 
**description** | **str** | A description of the error. | 
**code** | **str** | A code that uniquely identifies the error. | [optional] 
**source** | [**Error1Source**](Error1Source.md) |  | [optional] 

## Example

```python
from bandwidth.models.error1 import Error1

# TODO update the JSON string below
json = "{}"
# create an instance of Error1 from a JSON string
error1_instance = Error1.from_json(json)
# print the JSON string representation of the object
print(Error1.to_json())

# convert the object into a dict
error1_dict = error1_instance.to_dict()
# create an instance of Error1 from a dict
error1_from_dict = Error1.from_dict(error1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


