# MessageRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** | The ID of the Application your from number is associated with in the Bandwidth Phone Number Dashboard. | 
**to** | **[str]** | The phone number(s) the message should be sent to in E164 format | 
**_from** | **str** | One of your telephone numbers the message should come from in E164 format | 
**text** | **str** | The contents of the text message. Must be 2048 characters or less. | [optional] 
**media** | **[str]** | A list of URLs to include as media attachments as part of the message. | [optional] 
**tag** | **str** | A custom string that will be included in callback events of the message. Max 1024 characters | [optional] 
**priority** | **str** | The message&#39;s priority, currently for toll-free or short code SMS only. Messages with a priority value of &#x60;\&quot;high\&quot;&#x60; are given preference over your other traffic. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


