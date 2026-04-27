# BrtcError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for the error. | [optional] 
**type** | **str** | The type of error. | 
**description** | **str** | A description of the error. | 
**code** | **str** | A code that uniquely identifies the error. | [optional] 
**source** | [**BrtcErrorSource**](BrtcErrorSource.md) |  | [optional] 

## Example

```python
from bandwidth.models.brtc_error import BrtcError

# TODO update the JSON string below
json = "{}"
# create an instance of BrtcError from a JSON string
brtc_error_instance = BrtcError.from_json(json)
# print the JSON string representation of the object
print(BrtcError.to_json())

# convert the object into a dict
brtc_error_dict = brtc_error_instance.to_dict()
# create an instance of BrtcError from a dict
brtc_error_from_dict = BrtcError.from_dict(brtc_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


