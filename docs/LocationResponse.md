# LocationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** | The latitude of the client&#39;s location. | [optional] 
**longitude** | **float** | The longitude of the client&#39;s location. | [optional] 

## Example

```python
from bandwidth.models.location_response import LocationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LocationResponse from a JSON string
location_response_instance = LocationResponse.from_json(json)
# print the JSON string representation of the object
print(LocationResponse.to_json())

# convert the object into a dict
location_response_dict = location_response_instance.to_dict()
# create an instance of LocationResponse from a dict
location_response_from_dict = LocationResponse.from_dict(location_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


