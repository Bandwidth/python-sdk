# TranscribeRecordingRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_url** | **str** | The URL to send the [TranscriptionAvailable](/docs/voice/webhooks/transcriptionAvailable) event to. You should not include sensitive or personally-identifiable information in the callbackUrl field! Always use the proper username and password fields for authorization. | [optional] 
**callback_method** | **str, none_type** | The HTTP method to use for the request to &#x60;callbackUrl&#x60;. GET or POST. Default value is POST. | [optional] 
**username** | **str, none_type** | The username to send in the HTTP request to &#x60;callbackUrl&#x60;. | [optional] 
**password** | **str, none_type** | The password to send in the HTTP request to &#x60;callbackUrl&#x60;. | [optional] 
**tag** | **str, none_type** | A custom string that will be sent with the webhook to &#x60;callbackUrl&#x60;. | [optional] 
**callback_timeout** | **float, none_type** | This is the timeout (in seconds) to use when delivering the webhook to &#x60;callbackUrl&#x60;. Can be any numeric value (including decimals) between 1 and 25.&lt;br&gt;Default: 15 | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


