# CodeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | **str** | The phone number to send the mfa code to. | 
**var_from** | **str** | The application phone number, the sender of the mfa code. | 
**application_id** | **str** | The application unique ID, obtained from Bandwidth. | 
**scope** | **str** | An optional field to denote what scope or action the mfa code is addressing.  If not supplied, defaults to \&quot;2FA\&quot;. | [optional] 
**message** | **str** | The message format of the mfa code.  There are three values that the system will replace \&quot;{CODE}\&quot;, \&quot;{NAME}\&quot;, \&quot;{SCOPE}\&quot;.  The \&quot;{SCOPE}\&quot; and \&quot;{NAME} value template are optional, while \&quot;{CODE}\&quot; must be supplied.  As the name would suggest, code will be replace with the actual mfa code.  Name is replaced with the application name, configured during provisioning of mfa.  The scope value is the same value sent during the call and partitioned by the server. | 
**digits** | **int** | The number of digits for your mfa code.  The valid number ranges from 2 to 8, inclusively. | 

## Example

```python
from bandwidth.models.code_request import CodeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CodeRequest from a JSON string
code_request_instance = CodeRequest.from_json(json)
# print the JSON string representation of the object
print(CodeRequest.to_json())

# convert the object into a dict
code_request_dict = code_request_instance.to_dict()
# create an instance of CodeRequest from a dict
code_request_from_dict = CodeRequest.from_dict(code_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


