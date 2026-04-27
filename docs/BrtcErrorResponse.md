# BrtcErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**List[BrtcLink]**](BrtcLink.md) |  | 
**data** | **object** |  | 
**errors** | [**List[BrtcError]**](BrtcError.md) |  | 

## Example

```python
from bandwidth.models.brtc_error_response import BrtcErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BrtcErrorResponse from a JSON string
brtc_error_response_instance = BrtcErrorResponse.from_json(json)
# print the JSON string representation of the object
print(BrtcErrorResponse.to_json())

# convert the object into a dict
brtc_error_response_dict = brtc_error_response_instance.to_dict()
# create an instance of BrtcErrorResponse from a dict
brtc_error_response_from_dict = BrtcErrorResponse.from_dict(brtc_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


