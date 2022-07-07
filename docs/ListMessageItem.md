# ListMessageItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** | The message id | [optional] 
**account_id** | **str** | The account id associated with this message. | [optional] 
**source_tn** | **str** | The source phone number of the message. | [optional] 
**destination_tn** | **str** | The recipient phone number of the message. | [optional] 
**message_status** | [**MessageStatusEnum**](MessageStatusEnum.md) |  | [optional] 
**message_direction** | [**ListMessageDirectionEnum**](ListMessageDirectionEnum.md) |  | [optional] 
**message_type** | [**MessageTypeEnum**](MessageTypeEnum.md) |  | [optional] 
**segment_count** | **int** | The number of segments the message was sent as. | [optional] 
**error_code** | **int** | The numeric error code of the message. | [optional] 
**receive_time** | **str** | The ISO 8601 datetime of the message. | [optional] 
**carrier_name** | **str** | The name of the carrier. Not currently supported for MMS coming soon. | [optional] 
**message_size** | **int, none_type** | The size of the message including message content and headers. | [optional] 
**message_length** | **int** | The length of the message content. | [optional] 
**attachment_count** | **int, none_type** | The number of attachments the message has. | [optional] 
**recipient_count** | **int, none_type** | The number of recipients the message has. | [optional] 
**campaign_class** | **str, none_type** | The campaign class of the message if it has one. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


