# RbmActionViewLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**RbmActionTypeEnum**](RbmActionTypeEnum.md) |  | 
**text** | **str** | Displayed text for user to click | 
**postback_data** | **bytearray** | Base64 payload the customer receives when the reply is clicked. | 
**latitude** | **float** | The latitude of the location. | 
**longitude** | **float** | The longitude of the location. | 
**label** | **str** | The label of the location. | [optional] 

## Example

```python
from bandwidth.models.rbm_action_view_location import RbmActionViewLocation

# TODO update the JSON string below
json = "{}"
# create an instance of RbmActionViewLocation from a JSON string
rbm_action_view_location_instance = RbmActionViewLocation.from_json(json)
# print the JSON string representation of the object
print(RbmActionViewLocation.to_json())

# convert the object into a dict
rbm_action_view_location_dict = rbm_action_view_location_instance.to_dict()
# create an instance of RbmActionViewLocation from a dict
rbm_action_view_location_from_dict = RbmActionViewLocation.from_dict(rbm_action_view_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


