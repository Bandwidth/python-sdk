# MfaForbiddenRequestError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | The message containing the reason behind the request being forbidden. | [optional] 

## Example

```python
from bandwidth.models.mfa_forbidden_request_error import MfaForbiddenRequestError

# TODO update the JSON string below
json = "{}"
# create an instance of MfaForbiddenRequestError from a JSON string
mfa_forbidden_request_error_instance = MfaForbiddenRequestError.from_json(json)
# print the JSON string representation of the object
print(MfaForbiddenRequestError.to_json())

# convert the object into a dict
mfa_forbidden_request_error_dict = mfa_forbidden_request_error_instance.to_dict()
# create an instance of MfaForbiddenRequestError from a dict
mfa_forbidden_request_error_form_dict = mfa_forbidden_request_error.from_dict(mfa_forbidden_request_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


