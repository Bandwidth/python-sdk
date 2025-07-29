# RbmLocationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** | The latitude of the client&#39;s location. | [optional] 
**longitude** | **float** | The longitude of the client&#39;s location. | [optional] 

## Example

```python
from bandwidth.models.rbm_location_response import RbmLocationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RbmLocationResponse from a JSON string
rbm_location_response_instance = RbmLocationResponse.from_json(json)
# print the JSON string representation of the object
print(RbmLocationResponse.to_json())

# convert the object into a dict
rbm_location_response_dict = rbm_location_response_instance.to_dict()
# create an instance of RbmLocationResponse from a dict
rbm_location_response_from_dict = RbmLocationResponse.from_dict(rbm_location_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


