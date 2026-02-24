# SipCredentials


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | The username for the SIP connection. | [optional] 
**password** | **str** | The password for the SIP connection. | [optional] 

## Example

```python
from bandwidth.models.sip_credentials import SipCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of SipCredentials from a JSON string
sip_credentials_instance = SipCredentials.from_json(json)
# print the JSON string representation of the object
print(SipCredentials.to_json())

# convert the object into a dict
sip_credentials_dict = sip_credentials_instance.to_dict()
# create an instance of SipCredentials from a dict
sip_credentials_from_dict = SipCredentials.from_dict(sip_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


