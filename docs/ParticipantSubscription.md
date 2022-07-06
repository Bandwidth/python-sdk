# ParticipantSubscription


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**participant_id** | **str** | The Participant the subscriber will be subscribed to | 
**stream_aliases** | **[str]** | (optional) An array of specific streamAliases owned by the Participant that the subscriber will be subscribed to. Background: A streamAlias is created by a WebRTC client when it connects and declares a name for the related stream. The client is responsible for informing the application of any created streamAliases to enable the application to subscribe to specific streamAliases. Subscribing to a &#x60;streamAlias&#x60; that does not exist is undefined. If the array is empty all aliases are assumed. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


