# AsyncLookupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_numbers** | **List[str]** | Telephone numbers in E.164 format. | 

## Example

```python
from bandwidth.models.async_lookup_request import AsyncLookupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncLookupRequest from a JSON string
async_lookup_request_instance = AsyncLookupRequest.from_json(json)
# print the JSON string representation of the object
print(AsyncLookupRequest.to_json())

# convert the object into a dict
async_lookup_request_dict = async_lookup_request_instance.to_dict()
# create an instance of AsyncLookupRequest from a dict
async_lookup_request_from_dict = AsyncLookupRequest.from_dict(async_lookup_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


