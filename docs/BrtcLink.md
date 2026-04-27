# BrtcLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The full URL of the link. | [optional] 
**rel** | **str** | The relationship of the link to the current resource. | [optional] 
**method** | **str** | The HTTP method to use when making the request. | [optional] 

## Example

```python
from bandwidth.models.brtc_link import BrtcLink

# TODO update the JSON string below
json = "{}"
# create an instance of BrtcLink from a JSON string
brtc_link_instance = BrtcLink.from_json(json)
# print the JSON string representation of the object
print(BrtcLink.to_json())

# convert the object into a dict
brtc_link_dict = brtc_link_instance.to_dict()
# create an instance of BrtcLink from a dict
brtc_link_from_dict = BrtcLink.from_dict(brtc_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


