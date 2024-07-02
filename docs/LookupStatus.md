# LookupStatus

If requestId exists, the result for that request is returned. See the Examples for details on the various responses that you can receive. Generally, if you see a Response Code of 0 in a result for a TN, information will be available for it.  Any other Response Code will indicate no information was available for the TN.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | The requestId. | [optional] 
**status** | [**LookupStatusEnum**](LookupStatusEnum.md) |  | [optional] 
**result** | [**List[LookupResult]**](LookupResult.md) | The carrier information results for the specified telephone number. | [optional] 
**failed_telephone_numbers** | **List[str]** | The telephone numbers whose lookup failed. | [optional] 

## Example

```python
from bandwidth.models.lookup_status import LookupStatus

# TODO update the JSON string below
json = "{}"
# create an instance of LookupStatus from a JSON string
lookup_status_instance = LookupStatus.from_json(json)
# print the JSON string representation of the object
print(LookupStatus.to_json())

# convert the object into a dict
lookup_status_dict = lookup_status_instance.to_dict()
# create an instance of LookupStatus from a dict
lookup_status_from_dict = LookupStatus.from_dict(lookup_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


