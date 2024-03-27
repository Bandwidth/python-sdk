# TnLookupRequestError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A description of what validation error occurred. | [optional] 

## Example

```python
from bandwidth.models.tn_lookup_request_error import TnLookupRequestError

# TODO update the JSON string below
json = "{}"
# create an instance of TnLookupRequestError from a JSON string
tn_lookup_request_error_instance = TnLookupRequestError.from_json(json)
# print the JSON string representation of the object
print(TnLookupRequestError.to_json())

# convert the object into a dict
tn_lookup_request_error_dict = tn_lookup_request_error_instance.to_dict()
# create an instance of TnLookupRequestError from a dict
tn_lookup_request_error_form_dict = tn_lookup_request_error.from_dict(tn_lookup_request_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


