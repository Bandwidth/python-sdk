# BandwidthMessage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the message | [optional] 
**owner** | **str** | The Bandwidth phone number associated with the message | [optional] 
**application_id** | **str** | The application ID associated with the message | [optional] 
**time** | **str** | The datetime stamp of the message in ISO 8601 | [optional] 
**segment_count** | **int** | The number of segments the original message from the user is broken into before sending over to carrier networks | [optional] 
**direction** | **str** | The direction of the message relative to Bandwidth. Can be in or out | [optional] 
**to** | **[str]** | The phone number recipients of the message | [optional] 
**_from** | **str** | The phone number the message was sent from | [optional] 
**media** | **[str]** | The list of media URLs sent in the message. Including a &#x60;filename&#x60; field in the &#x60;Content-Disposition&#x60; header of the media linked with a URL will set the displayed file name. This is a best practice to ensure that your media has a readable file name. | [optional] 
**text** | **str** | The contents of the message | [optional] 
**tag** | **str** | The custom string set by the user | [optional] 
**priority** | **str** | The priority specified by the user | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


