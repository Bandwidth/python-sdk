# CreateEndpointResponseObject


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
**token** | **str** | The json web token specific to the endpoint. Used to authenticate the client with the media gateway. | 

## Example

```python
from bandwidth.models.create_endpoint_response_object import CreateEndpointResponseObject

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEndpointResponseObject from a JSON string
create_endpoint_response_object_instance = CreateEndpointResponseObject.from_json(json)
# print the JSON string representation of the object
print(CreateEndpointResponseObject.to_json())

# convert the object into a dict
create_endpoint_response_object_dict = create_endpoint_response_object_instance.to_dict()
# create an instance of CreateEndpointResponseObject from a dict
create_endpoint_response_object_from_dict = CreateEndpointResponseObject.from_dict(create_endpoint_response_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


