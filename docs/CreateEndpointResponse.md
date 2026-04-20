# CreateEndpointResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**List[Link]**](Link.md) |  | 
**data** | [**CreateEndpointResponseData**](CreateEndpointResponseData.md) |  | 
**errors** | [**List[Error]**](Error.md) |  | 

## Example

```python
from bandwidth.models.create_endpoint_response import CreateEndpointResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEndpointResponse from a JSON string
create_endpoint_response_instance = CreateEndpointResponse.from_json(json)
# print the JSON string representation of the object
print(CreateEndpointResponse.to_json())

# convert the object into a dict
create_endpoint_response_dict = create_endpoint_response_instance.to_dict()
# create an instance of CreateEndpointResponse from a dict
create_endpoint_response_from_dict = CreateEndpointResponse.from_dict(create_endpoint_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


