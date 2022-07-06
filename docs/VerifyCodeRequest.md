# VerifyCodeRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | **str** | The phone number to send the mfa code to. | 
**expiration_time_in_minutes** | **float** | The time period, in minutes, to validate the mfa code.  By setting this to 3 minutes, it will mean any code generated within the last 3 minutes are still valid.  The valid range for expiration time is between 0 and 15 minutes, exclusively and inclusively, respectively. | 
**code** | **str** | The generated mfa code to check if valid. | 
**scope** | **str** | An optional field to denote what scope or action the mfa code is addressing.  If not supplied, defaults to \&quot;2FA\&quot;. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


