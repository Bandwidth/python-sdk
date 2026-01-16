# CreateEndpointRequestBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**EndpointTypeEnum**](EndpointTypeEnum.md) |  | 
**direction** | [**EndpointDirectionEnum**](EndpointDirectionEnum.md) |  | 
**event_callback_url** | **str** | The URL to send event callbacks to. | [optional] 
**event_fallback_url** | **str** | The URL to send event fallbacks to. | [optional] 
**tag** | **str** | A tag for the endpoint. | [optional] 

## Example

```python
from bandwidth.models.create_endpoint_request_base import CreateEndpointRequestBase

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEndpointRequestBase from a JSON string
create_endpoint_request_base_instance = CreateEndpointRequestBase.from_json(json)
# print the JSON string representation of the object
print(CreateEndpointRequestBase.to_json())

# convert the object into a dict
create_endpoint_request_base_dict = create_endpoint_request_base_instance.to_dict()
# create an instance of CreateEndpointRequestBase from a dict
create_endpoint_request_base_from_dict = CreateEndpointRequestBase.from_dict(create_endpoint_request_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


