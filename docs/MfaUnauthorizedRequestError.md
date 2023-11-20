# MfaUnauthorizedRequestError


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Unauthorized | [optional] 

## Example

```python
from bandwidth.models.mfa_unauthorized_request_error import MfaUnauthorizedRequestError

# TODO update the JSON string below
json = "{}"
# create an instance of MfaUnauthorizedRequestError from a JSON string
mfa_unauthorized_request_error_instance = MfaUnauthorizedRequestError.from_json(json)
# print the JSON string representation of the object
print MfaUnauthorizedRequestError.to_json()

# convert the object into a dict
mfa_unauthorized_request_error_dict = mfa_unauthorized_request_error_instance.to_dict()
# create an instance of MfaUnauthorizedRequestError from a dict
mfa_unauthorized_request_error_form_dict = mfa_unauthorized_request_error.from_dict(mfa_unauthorized_request_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


