# Endpoints


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint_id** | **str** | The unique ID of the endpoint. | 
**type** | [**EndpointTypeEnum**](EndpointTypeEnum.md) |  | 
**status** | [**EndpointStatusEnum**](EndpointStatusEnum.md) |  | 
**creation_timestamp** | **datetime** | The time the endpoint was created. In ISO-8601 format. | 
**expiration_timestamp** | **datetime** | The time the endpoint token will expire. In ISO-8601 format. Tokens last 24 hours. | 
**tag** | **str** | A tag for the endpoint. | [optional] 

## Example

```python
from bandwidth.models.endpoints import Endpoints

# TODO update the JSON string below
json = "{}"
# create an instance of Endpoints from a JSON string
endpoints_instance = Endpoints.from_json(json)
# print the JSON string representation of the object
print(Endpoints.to_json())

# convert the object into a dict
endpoints_dict = endpoints_instance.to_dict()
# create an instance of Endpoints from a dict
endpoints_from_dict = Endpoints.from_dict(endpoints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


