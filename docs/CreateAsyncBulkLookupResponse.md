# CreateAsyncBulkLookupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**List[LinkSchema]**](LinkSchema.md) | Links for pagination (if applicable) | [optional] 
**data** | [**CreateAsyncBulkLookupResponseData**](CreateAsyncBulkLookupResponseData.md) |  | [optional] 
**errors** | [**List[LookupErrorSchema]**](LookupErrorSchema.md) |  | [optional] 

## Example

```python
from bandwidth.models.create_async_bulk_lookup_response import CreateAsyncBulkLookupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAsyncBulkLookupResponse from a JSON string
create_async_bulk_lookup_response_instance = CreateAsyncBulkLookupResponse.from_json(json)
# print the JSON string representation of the object
print(CreateAsyncBulkLookupResponse.to_json())

# convert the object into a dict
create_async_bulk_lookup_response_dict = create_async_bulk_lookup_response_instance.to_dict()
# create an instance of CreateAsyncBulkLookupResponse from a dict
create_async_bulk_lookup_response_from_dict = CreateAsyncBulkLookupResponse.from_dict(create_async_bulk_lookup_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


