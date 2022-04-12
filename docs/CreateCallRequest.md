# CreateCallRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_from** | **str** | A Bandwidth phone number on your account the call should come from (must be in E.164 format, like &#x60;+15555551212&#x60;, or be one of the following strings: &#x60;Restricted&#x60;, &#x60;Anonymous&#x60;, &#x60;Private&#x60;, or &#x60;Unavailable&#x60;). | 
**to** | **str** | The destination to call (must be an E.164 formatted number (e.g. &#x60;+15555551212&#x60;) or a SIP URI (e.g. &#x60;sip:user@server.com&#x60;)). | 
**answer_url** | **str** | The full URL to send the &lt;a href&#x3D;&#39;/docs/voice/webhooks/answer&#39;&gt;Answer&lt;/a&gt; event to when the called party answers. This endpoint should return the first &lt;a href&#x3D;&#39;/docs/voice/bxml&#39;&gt;BXML document&lt;/a&gt; to be executed in the call. | 
**application_id** | **str** | The id of the application to associate this call with, for billing purposes. | 
**uui** | **str, none_type** | A comma-separated list of &#39;User-To-User&#39; headers to be sent in the INVITE when calling a SIP URI. Each value must end with an &#39;encoding&#39; parameter as described in &lt;a href&#x3D;&#39;https://tools.ietf.org/html/rfc7433&#39;&gt;RFC 7433&lt;/a&gt;. Only &#39;jwt&#39; and &#39;base64&#39; encodings are allowed. The entire value cannot exceed 350 characters, including parameters and separators. | [optional] 
**call_timeout** | **float, none_type** | The timeout (in seconds) for the callee to answer the call after it starts ringing. If the call does not start ringing within 30s, the call will be cancelled regardless of this value.  Can be any numeric value (including decimals) between 1 and 300.&lt;br&gt;Default: 30 | [optional] 
**callback_timeout** | **float, none_type** | This is the timeout (in seconds) to use when delivering webhooks for the call. Can be any numeric value (including decimals) between 1 and 25.&lt;br&gt;Default: 15 | [optional] 
**answer_fallback_url** | **str, none_type** | A fallback url which, if provided, will be used to retry the &#x60;answer&#x60; webhook delivery in case &#x60;answerUrl&#x60; fails to respond | [optional] 
**username** | **str, none_type** | The username to send in the HTTP request to &#x60;answerUrl&#x60; and &#x60;disconnectUrl&#x60;. | [optional] 
**password** | **str, none_type** | The password to send in the HTTP request to &#x60;answerUrl&#x60; and &#x60;disconnectUrl&#x60;. | [optional] 
**fallback_username** | **str, none_type** | The username to send in the HTTP request to &#x60;answerFallbackUrl&#x60; | [optional] 
**fallback_password** | **str, none_type** | The password to send in the HTTP request to &#x60;answerFallbackUrl&#x60; | [optional] 
**answer_method** | **str, none_type** | The HTTP method to use for the request to &#x60;answerUrl&#x60;. GET or POST. Default value is POST. | [optional] 
**answer_fallback_method** | **str, none_type** | The HTTP method to use to deliver the answer callback to &#x60;answerFallbackUrl&#x60;. GET or POST. Default value is POST. | [optional] 
**disconnect_url** | **str, none_type** | The URL to send the &lt;a href&#x3D;&#39;/docs/voice/webhooks/disconnect&#39;&gt;Disconnect&lt;/a&gt; event to when the call ends. This event does not expect a BXML response. | [optional] 
**disconnect_method** | **str, none_type** | The HTTP method to use for the request to &#x60;disconnectUrl&#x60;. GET or POST. Default value is POST. | [optional] 
**tag** | **str, none_type** | A custom string that will be sent with all webhooks for this call unless overwritten by a future &lt;a href&#x3D;&#39;/docs/voice/bxml/tag&#39;&gt;&#x60;&lt;Tag&gt;&#x60;&lt;/a&gt; verb or &#x60;tag&#x60; attribute on another verb, or cleared.&lt;br&gt;&lt;br&gt;May be cleared by setting &#x60;tag&#x3D;\&quot;\&quot;&#x60;&lt;br&gt;&lt;br&gt;Max length 256 characters. | [optional] 
**machine_detection** | [**MachineDetectionConfiguration**](MachineDetectionConfiguration.md) |  | [optional] 
**priority** | **int, none_type** | The priority of this call over other calls from your account when outbound call queueing is enabled. For example, if during a call your application needs to place a new call and bridge it with the current call, you might want to create the call with priority 1 so that it will be the next call picked off your queue, ahead of other less time sensitive calls.  A lower value means higher priority, so a priority 1 call takes precedence over a priority 2 call.&lt;br&gt;Range: integer values between 1 - 5.&lt;br&gt;Default value is 5. | [optional]  if omitted the server will use the default value of 5
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


