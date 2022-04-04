# ModifyCallRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str, none_type** | The call state. Possible values:&lt;br&gt;&#x60;active&#x60; to redirect the call (default)&lt;br&gt;&#x60;completed&#x60; to hang up the call if it is answered, cancel it if it is an unanswered outbound call, or reject it if it an unanswered inbound call | [optional]  if omitted the server will use the default value of "active"
**redirect_url** | **str, none_type** | The URL to send the [Redirect](/docs/voice/bxml/redirect) event to which will provide new BXML&lt;br&gt;&lt;br&gt;Required if &#x60;state&#x60; is &#x60;active&#x60;&lt;br&gt;&lt;br&gt;Not allowed if &#x60;state&#x60; is &#x60;completed&#x60; | [optional] 
**redirect_fallback_url** | **str, none_type** | A fallback url which, if provided, will be used to retry the redirect callback delivery in case &#x60;redirectUrl&#x60; fails to respond | [optional] 
**redirect_method** | **str, none_type** | The HTTP method to use for the request to &#x60;redirectUrl&#x60;. GET or POST. Default value is POST.&lt;br&gt;&lt;br&gt;Not allowed if &#x60;state&#x60; is &#x60;completed&#x60; | [optional] 
**redirect_fallback_method** | **str, none_type** | The HTTP method to use to deliver the redirect callback to &#x60;redirectFallbackUrl&#x60;. GET or POST. Default value is POST. | [optional] 
**username** | **str, none_type** | The username to send in the HTTP request to &#x60;redirectUrl&#x60; | [optional] 
**password** | **str, none_type** | The password to send in the HTTP request to &#x60;redirectUrl&#x60; | [optional] 
**fallback_username** | **str, none_type** | The username to send in the HTTP request to &#x60;redirectFallbackUrl&#x60; | [optional] 
**fallback_password** | **str, none_type** | The password to send in the HTTP request to &#x60;redirectFallbackUrl&#x60; | [optional] 
**tag** | **str, none_type** | A custom string that will be sent with this and all future callbacks unless overwritten by a future &#x60;tag&#x60; attribute or [&#x60;&lt;Tag&gt;&#x60;](/docs/voice/bxml/tag) verb, or cleared.&lt;br&gt;&lt;br&gt;May be cleared by setting &#x60;tag&#x3D;\&quot;\&quot;&#x60;&lt;br&gt;&lt;br&gt;Max length 256 characters.&lt;br&gt;&lt;br&gt;Not allowed if &#x60;state&#x60; is &#x60;completed&#x60; | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


