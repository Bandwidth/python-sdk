# MfaRequestError


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | A message describing the error with your request. | [optional] 
**request_id** | **str** | The associated requestId from AWS. | [optional] 

## Example

```python
from bandwidth.models.mfa_request_error import MfaRequestError

# TODO update the JSON string below
json = "{}"
# create an instance of MfaRequestError from a JSON string
mfa_request_error_instance = MfaRequestError.from_json(json)
# print the JSON string representation of the object
print MfaRequestError.to_json()

# convert the object into a dict
mfa_request_error_dict = mfa_request_error_instance.to_dict()
# create an instance of MfaRequestError from a dict
mfa_request_error_form_dict = mfa_request_error.from_dict(mfa_request_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


