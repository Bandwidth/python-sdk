# BrtcErrorSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameter** | **str** | The URI parameter that caused the error. | [optional] 
**var_field** | **str** | The request body field that caused the error. | [optional] 
**header** | **str** | The header that caused the error. | [optional] 
**reference** | **str** | The resource ID or path to the resource (or non-existent resource) causing the error. | [optional] 

## Example

```python
from bandwidth.models.brtc_error_source import BrtcErrorSource

# TODO update the JSON string below
json = "{}"
# create an instance of BrtcErrorSource from a JSON string
brtc_error_source_instance = BrtcErrorSource.from_json(json)
# print the JSON string representation of the object
print(BrtcErrorSource.to_json())

# convert the object into a dict
brtc_error_source_dict = brtc_error_source_instance.to_dict()
# create an instance of BrtcErrorSource from a dict
brtc_error_source_from_dict = BrtcErrorSource.from_dict(brtc_error_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


