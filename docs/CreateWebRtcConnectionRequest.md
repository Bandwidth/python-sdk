# CreateWebRtcConnectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**EndpointTypeEnum**](EndpointTypeEnum.md) |  | 
**direction** | [**EndpointDirectionEnum**](EndpointDirectionEnum.md) |  | 
**event_callback_url** | **str** | The URL to send event callbacks to. | [optional] 
**event_fallback_url** | **str** | The URL to send event fallbacks to. | [optional] 
**tag** | **str** | A tag for the endpoint. | [optional] 
**connection_metadata** | **object** |  | [optional] 

## Example

```python
from bandwidth.models.create_web_rtc_connection_request import CreateWebRtcConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWebRtcConnectionRequest from a JSON string
create_web_rtc_connection_request_instance = CreateWebRtcConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(CreateWebRtcConnectionRequest.to_json())

# convert the object into a dict
create_web_rtc_connection_request_dict = create_web_rtc_connection_request_instance.to_dict()
# create an instance of CreateWebRtcConnectionRequest from a dict
create_web_rtc_connection_request_from_dict = CreateWebRtcConnectionRequest.from_dict(create_web_rtc_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


