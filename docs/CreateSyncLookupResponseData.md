# CreateSyncLookupResponseData

The phone number lookup response data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | The phone number lookup request ID from Bandwidth. | [optional] 
**status** | [**CompletedLookupStatusEnum**](CompletedLookupStatusEnum.md) |  | [optional] 
**results** | [**List[LookupResult]**](LookupResult.md) | The carrier information results for the specified telephone numbers. | [optional] 

## Example

```python
from bandwidth.models.create_sync_lookup_response_data import CreateSyncLookupResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSyncLookupResponseData from a JSON string
create_sync_lookup_response_data_instance = CreateSyncLookupResponseData.from_json(json)
# print the JSON string representation of the object
print(CreateSyncLookupResponseData.to_json())

# convert the object into a dict
create_sync_lookup_response_data_dict = create_sync_lookup_response_data_instance.to_dict()
# create an instance of CreateSyncLookupResponseData from a dict
create_sync_lookup_response_data_from_dict = CreateSyncLookupResponseData.from_dict(create_sync_lookup_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


