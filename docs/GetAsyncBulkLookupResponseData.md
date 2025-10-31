# GetAsyncBulkLookupResponseData

The phone number lookup response data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | The phone number lookup request ID from Bandwidth. | [optional] 
**status** | [**InProgressLookupStatusEnum**](InProgressLookupStatusEnum.md) |  | [optional] 
**results** | [**List[LookupResult]**](LookupResult.md) | The carrier information results for the specified telephone number. | [optional] 

## Example

```python
from bandwidth.models.get_async_bulk_lookup_response_data import GetAsyncBulkLookupResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetAsyncBulkLookupResponseData from a JSON string
get_async_bulk_lookup_response_data_instance = GetAsyncBulkLookupResponseData.from_json(json)
# print the JSON string representation of the object
print(GetAsyncBulkLookupResponseData.to_json())

# convert the object into a dict
get_async_bulk_lookup_response_data_dict = get_async_bulk_lookup_response_data_instance.to_dict()
# create an instance of GetAsyncBulkLookupResponseData from a dict
get_async_bulk_lookup_response_data_from_dict = GetAsyncBulkLookupResponseData.from_dict(get_async_bulk_lookup_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


