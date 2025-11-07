# CreateAsyncBulkLookupResponseData

The phone number lookup response data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | The phone number lookup request ID from Bandwidth. | [optional] 
**status** | [**InProgressLookupStatusEnum**](InProgressLookupStatusEnum.md) |  | [optional] 

## Example

```python
from bandwidth.models.create_async_bulk_lookup_response_data import CreateAsyncBulkLookupResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAsyncBulkLookupResponseData from a JSON string
create_async_bulk_lookup_response_data_instance = CreateAsyncBulkLookupResponseData.from_json(json)
# print the JSON string representation of the object
print(CreateAsyncBulkLookupResponseData.to_json())

# convert the object into a dict
create_async_bulk_lookup_response_data_dict = create_async_bulk_lookup_response_data_instance.to_dict()
# create an instance of CreateAsyncBulkLookupResponseData from a dict
create_async_bulk_lookup_response_data_from_dict = CreateAsyncBulkLookupResponseData.from_dict(create_async_bulk_lookup_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


