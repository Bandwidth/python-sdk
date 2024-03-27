# CreateCallResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** | The id of the application associated with the &#x60;from&#x60; number. | 
**account_id** | **str** | The bandwidth account ID associated with the call. | 
**call_id** | **str** | Programmable Voice API Call ID. | 
**to** | **str** | Recipient of the outgoing call. | 
**var_from** | **str** | Phone number that created the outbound call. | 
**enqueued_time** | **datetime** | The time at which the call was accepted into the queue. | [optional] 
**call_url** | **str** | The URL to update this call&#39;s state. | 
**call_timeout** | **float** | The timeout (in seconds) for the callee to answer the call after it starts ringing. | [optional] 
**callback_timeout** | **float** | This is the timeout (in seconds) to use when delivering webhooks for the call. | [optional] 
**tag** | **str** | Custom tag value. | [optional] 
**answer_method** | [**CallbackMethodEnum**](CallbackMethodEnum.md) |  | 
**answer_url** | **str** | URL to deliver the &#x60;answer&#x60; event webhook. | 
**answer_fallback_method** | [**CallbackMethodEnum**](CallbackMethodEnum.md) |  | [optional] 
**answer_fallback_url** | **str** | Fallback URL to deliver the &#x60;answer&#x60; event webhook. | [optional] 
**disconnect_method** | [**CallbackMethodEnum**](CallbackMethodEnum.md) |  | 
**disconnect_url** | **str** | URL to deliver the &#x60;disconnect&#x60; event webhook. | [optional] 
**username** | **str** | Basic auth username. | [optional] 
**password** | **str** | Basic auth password. | [optional] 
**fallback_username** | **str** | Basic auth username. | [optional] 
**fallback_password** | **str** | Basic auth password. | [optional] 
**priority** | **int** | The priority of this call over other calls from your account. | [optional] 

## Example

```python
from bandwidth.models.create_call_response import CreateCallResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCallResponse from a JSON string
create_call_response_instance = CreateCallResponse.from_json(json)
# print the JSON string representation of the object
print(CreateCallResponse.to_json())

# convert the object into a dict
create_call_response_dict = create_call_response_instance.to_dict()
# create an instance of CreateCallResponse from a dict
create_call_response_form_dict = create_call_response.from_dict(create_call_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


