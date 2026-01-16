# EndpointEvent

An event that occurred on an endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint_id** | **str** | The unique ID of the endpoint. | 
**type** | [**EndpointTypeEnum**](EndpointTypeEnum.md) |  | 
**status** | [**EndpointStatusEnum**](EndpointStatusEnum.md) |  | 
**creation_timestamp** | **datetime** | The time the endpoint was created. In ISO-8601 format. | 
**expiration_timestamp** | **datetime** | The time the endpoint token will expire. In ISO-8601 format. Tokens last 24 hours. | 
**tag** | **str** | A tag for the endpoint. | [optional] 
**event_time** | **datetime** | The time the event occurred. In ISO-8601 format. | 
**event_type** | [**EndpointEventTypeEnum**](EndpointEventTypeEnum.md) |  | 
**device** | [**Device**](Device.md) |  | [optional] 

## Example

```python
from bandwidth.models.endpoint_event import EndpointEvent

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointEvent from a JSON string
endpoint_event_instance = EndpointEvent.from_json(json)
# print the JSON string representation of the object
print(EndpointEvent.to_json())

# convert the object into a dict
endpoint_event_dict = endpoint_event_instance.to_dict()
# create an instance of EndpointEvent from a dict
endpoint_event_from_dict = EndpointEvent.from_dict(endpoint_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


