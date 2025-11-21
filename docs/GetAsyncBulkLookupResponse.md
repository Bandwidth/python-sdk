# GetAsyncBulkLookupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**List[LinkSchema]**](LinkSchema.md) |  | [optional] 
**data** | [**GetAsyncBulkLookupResponseData**](GetAsyncBulkLookupResponseData.md) |  | [optional] 
**errors** | [**List[LookupErrorSchema]**](LookupErrorSchema.md) |  | [optional] 

## Example

```python
from bandwidth.models.get_async_bulk_lookup_response import GetAsyncBulkLookupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAsyncBulkLookupResponse from a JSON string
get_async_bulk_lookup_response_instance = GetAsyncBulkLookupResponse.from_json(json)
# print the JSON string representation of the object
print(GetAsyncBulkLookupResponse.to_json())

# convert the object into a dict
get_async_bulk_lookup_response_dict = get_async_bulk_lookup_response_instance.to_dict()
# create an instance of GetAsyncBulkLookupResponse from a dict
get_async_bulk_lookup_response_from_dict = GetAsyncBulkLookupResponse.from_dict(get_async_bulk_lookup_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


