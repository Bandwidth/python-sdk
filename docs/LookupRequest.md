# LookupRequest

Create phone number lookup request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tns** | **List[str]** |  | 

## Example

```python
from bandwidth.models.lookup_request import LookupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LookupRequest from a JSON string
lookup_request_instance = LookupRequest.from_json(json)
# print the JSON string representation of the object
print(LookupRequest.to_json())

# convert the object into a dict
lookup_request_dict = lookup_request_instance.to_dict()
# create an instance of LookupRequest from a dict
lookup_request_from_dict = LookupRequest.from_dict(lookup_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


