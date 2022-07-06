# TranscribeRecording


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_url** | **str** | The URL to send the [TranscriptionAvailable](/docs/voice/webhooks/transcriptionAvailable) event to. You should not include sensitive or personally-identifiable information in the callbackUrl field! Always use the proper username and password fields for authorization. | [optional] 
**callback_method** | [**CallbackMethodEnum**](CallbackMethodEnum.md) |  | [optional] 
**username** | **str, none_type** | Basic auth username. | [optional] 
**password** | **str, none_type** | Basic auth password. | [optional] 
**tag** | **str, none_type** | A custom string that will be sent with the webhook to &#x60;callbackUrl&#x60;. | [optional] 
**callback_timeout** | **float, none_type** | This is the timeout (in seconds) to use when delivering the webhook to &#x60;callbackUrl&#x60;. Can be any numeric value (including decimals) between 1 and 25. | [optional]  if omitted the server will use the default value of 15
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


