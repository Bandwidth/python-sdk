# SipConnectionMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_address** | **str** | The IP address of the SIP connection. | [optional] 
**port** | **int** | The port of the SIP connection. | [optional] 
**credentials** | [**SipCredentials**](SipCredentials.md) |  | [optional] 
**uui_header** | **str** | The User-to-User Information header for the SIP connection. | [optional] 

## Example

```python
from bandwidth.models.sip_connection_metadata import SipConnectionMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of SipConnectionMetadata from a JSON string
sip_connection_metadata_instance = SipConnectionMetadata.from_json(json)
# print the JSON string representation of the object
print(SipConnectionMetadata.to_json())

# convert the object into a dict
sip_connection_metadata_dict = sip_connection_metadata_instance.to_dict()
# create an instance of SipConnectionMetadata from a dict
sip_connection_metadata_from_dict = SipConnectionMetadata.from_dict(sip_connection_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


