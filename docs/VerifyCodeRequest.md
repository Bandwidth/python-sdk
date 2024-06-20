# VerifyCodeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | **str** | The phone number to send the mfa code to. | 
**scope** | **str** | An optional field to denote what scope or action the mfa code is addressing.  If not supplied, defaults to \&quot;2FA\&quot;. | [optional] 
**expiration_time_in_minutes** | **float** | The time period, in minutes, to validate the mfa code.  By setting this to 3 minutes, it will mean any code generated within the last 3 minutes are still valid.  The valid range for expiration time is between 0 and 15 minutes, exclusively and inclusively, respectively. | 
**code** | **str** | The generated mfa code to check if valid. | 

## Example

```python
from bandwidth.models.verify_code_request import VerifyCodeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyCodeRequest from a JSON string
verify_code_request_instance = VerifyCodeRequest.from_json(json)
# print the JSON string representation of the object
print(VerifyCodeRequest.to_json())

# convert the object into a dict
verify_code_request_dict = verify_code_request_instance.to_dict()
# create an instance of VerifyCodeRequest from a dict
verify_code_request_from_dict = VerifyCodeRequest.from_dict(verify_code_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


