# EndpointResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**List[Link]**](Link.md) |  | 
**data** | [**Endpoint**](Endpoint.md) |  | 
**errors** | [**List[Error]**](Error.md) |  | 

## Example

```python
from bandwidth.models.endpoint_response import EndpointResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointResponse from a JSON string
endpoint_response_instance = EndpointResponse.from_json(json)
# print the JSON string representation of the object
print(EndpointResponse.to_json())

# convert the object into a dict
endpoint_response_dict = endpoint_response_instance.to_dict()
# create an instance of EndpointResponse from a dict
endpoint_response_from_dict = EndpointResponse.from_dict(endpoint_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


