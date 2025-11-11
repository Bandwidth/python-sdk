# SyncLookupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_numbers** | **List[str]** | Telephone numbers in E.164 format. | 

## Example

```python
from bandwidth.models.sync_lookup_request import SyncLookupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SyncLookupRequest from a JSON string
sync_lookup_request_instance = SyncLookupRequest.from_json(json)
# print the JSON string representation of the object
print(SyncLookupRequest.to_json())

# convert the object into a dict
sync_lookup_request_dict = sync_lookup_request_instance.to_dict()
# create an instance of SyncLookupRequest from a dict
sync_lookup_request_from_dict = SyncLookupRequest.from_dict(sync_lookup_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


