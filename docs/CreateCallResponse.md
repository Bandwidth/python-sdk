# CreateCallResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** | The id of the application associated with the &#x60;from&#x60; number. | 
**account_id** | **str** | The bandwidth account ID associated with the call | 
**call_id** | **str** | Programmable Voice API Call ID | 
**to** | **str** | Recipient of the outgoing call | 
**_from** | **str** | Phone number that created the outbound call | 
**call_url** | **str** | The URL to update call state | 
**answer_method** | [**CallbackMethodEnum**](CallbackMethodEnum.md) |  | 
**answer_url** | **str** | URL to deliver the &#x60;answer&#x60; event webhook. | 
**disconnect_method** | [**CallbackMethodEnum**](CallbackMethodEnum.md) |  | 
**enqueued_time** | **datetime, none_type** | Time the call was accepted into the queue | [optional] 
**call_timeout** | **float** | The timeout (in seconds) for the callee to answer the call after it starts ringing. | [optional] 
**callback_timeout** | **float** | This is the timeout (in seconds) to use when delivering webhooks for the call. | [optional] 
**tag** | **str, none_type** | Custom tag value | [optional] 
**answer_fallback_method** | [**CallbackMethodEnum**](CallbackMethodEnum.md) |  | [optional] 
**answer_fallback_url** | **str, none_type** | Fallback URL to deliver the &#x60;answer&#x60; event webhook. | [optional] 
**disconnect_url** | **str, none_type** | URL to deliver the &#x60;disconnect&#x60; event webhook. | [optional] 
**username** | **str, none_type** | Basic auth username. | [optional] 
**password** | **str, none_type** | Basic auth password. | [optional] 
**fallback_username** | **str, none_type** | Basic auth username. | [optional] 
**fallback_password** | **str, none_type** | Basic auth password. | [optional] 
**priority** | **float, none_type** | The priority of this call over other calls from your account. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


