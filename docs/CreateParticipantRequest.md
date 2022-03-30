# CreateParticipantRequest

Create a participant object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_url** | **str, none_type** | Full callback url to use for notifications about this participant | [optional] 
**publish_permissions** | **[str]** | Defines if this participant can publish audio or video | [optional] 
**tag** | **str** | User defined tag to associate with the participant | [optional] 
**device_api_version** | **str** | Optional field to define the device api version of this participant | [optional]  if omitted the server will use the default value of "V2"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


