# CodeRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | **str** | The phone number to send the mfa code to. | 
**_from** | **str** | The application phone number, the sender of the mfa code. | 
**application_id** | **str** | The application unique ID, obtained from Bandwidth. | 
**message** | **str** | The message format of the mfa code.  There are three values that the system will replace \&quot;{CODE}\&quot;, \&quot;{NAME}\&quot;, \&quot;{SCOPE}\&quot;.  The \&quot;{SCOPE}\&quot; and \&quot;{NAME} value template are optional, while \&quot;{CODE}\&quot; must be supplied.  As the name would suggest, code will be replace with the actual mfa code.  Name is replaced with the application name, configured during provisioning of mfa.  The scope value is the same value sent during the call and partitioned by the server. | 
**digits** | **int** | The number of digits for your mfa code.  The valid number ranges from 2 to 8, inclusively. | 
**scope** | **str** | An optional field to denote what scope or action the mfa code is addressing.  If not supplied, defaults to \&quot;2FA\&quot;. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


