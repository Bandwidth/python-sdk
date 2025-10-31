# CreateSyncLookupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**List[LinkSchema]**](LinkSchema.md) |  | [optional] 
**data** | [**CreateSyncLookupResponseData**](CreateSyncLookupResponseData.md) |  | [optional] 
**errors** | [**List[LookupErrorSchema]**](LookupErrorSchema.md) |  | [optional] 

## Example

```python
from bandwidth.models.create_sync_lookup_response import CreateSyncLookupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSyncLookupResponse from a JSON string
create_sync_lookup_response_instance = CreateSyncLookupResponse.from_json(json)
# print the JSON string representation of the object
print(CreateSyncLookupResponse.to_json())

# convert the object into a dict
create_sync_lookup_response_dict = create_sync_lookup_response_instance.to_dict()
# create an instance of CreateSyncLookupResponse from a dict
create_sync_lookup_response_from_dict = CreateSyncLookupResponse.from_dict(create_sync_lookup_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


