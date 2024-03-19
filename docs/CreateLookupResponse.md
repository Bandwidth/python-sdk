# CreateLookupResponse

The request has been accepted for processing but not yet finished and in a terminal state (COMPLETE, PARTIAL_COMPLETE, or FAILED).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | The phone number lookup request ID from Bandwidth. | [optional] 
**status** | [**LookupStatusEnum**](LookupStatusEnum.md) |  | [optional] 

## Example

```python
from bandwidth.models.create_lookup_response import CreateLookupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateLookupResponse from a JSON string
create_lookup_response_instance = CreateLookupResponse.from_json(json)
# print the JSON string representation of the object
print(CreateLookupResponse.to_json())

# convert the object into a dict
create_lookup_response_dict = create_lookup_response_instance.to_dict()
# create an instance of CreateLookupResponse from a dict
create_lookup_response_form_dict = create_lookup_response.from_dict(create_lookup_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


