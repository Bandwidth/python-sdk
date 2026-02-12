# Endpoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint_id** | **str** | The unique ID of the endpoint. | 
**type** | [**EndpointTypeEnum**](EndpointTypeEnum.md) |  | 
**status** | [**EndpointStatusEnum**](EndpointStatusEnum.md) |  | 
**creation_timestamp** | **datetime** | The time the endpoint was created. In ISO-8601 format. | 
**expiration_timestamp** | **datetime** | The time the endpoint token will expire. In ISO-8601 format. Tokens last 24 hours. | 
**tag** | **str** | A tag for the endpoint. | [optional] 
**devices** | [**List[Device]**](Device.md) |  | [optional] 

## Example

```python
from bandwidth.models.endpoint import Endpoint

# TODO update the JSON string below
json = "{}"
# create an instance of Endpoint from a JSON string
endpoint_instance = Endpoint.from_json(json)
# print the JSON string representation of the object
print(Endpoint.to_json())

# convert the object into a dict
endpoint_dict = endpoint_instance.to_dict()
# create an instance of Endpoint from a dict
endpoint_from_dict = Endpoint.from_dict(endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


