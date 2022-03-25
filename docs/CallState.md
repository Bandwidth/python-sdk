# CallState


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**call_id** | **str** |  | [optional] 
**parent_call_id** | **str, none_type** | The A-leg call id, set only if this call is the B-leg of a [&#x60;&lt;Transfer&gt;&#x60;](/docs/voice/bxml/transfer). | [optional] 
**application_id** | **str** | The application id associated  with the call. | [optional] 
**account_id** | **str** | The account id associated with the call. | [optional] 
**to** | **str** | The phone number that received the call, in E.164 format (e.g. +15555555555), or if the call was to a SIP URI, the SIP URI | [optional] 
**_from** | **str** | The phone number that made the call, in E.164 format (e.g. +15555555555). | [optional] 
**direction** | **str** | The direction of the call. Either &#x60;inbound&#x60; or &#x60;outbound&#x60;. | [optional] 
**state** | **str** | The current state of the call. Current possible values are &#39;queued&#39;, &#39;initiated&#39;, &#39;answered&#39; and &#39;disconnected&#39;. Additional states may be added in the future, so your application must be tolerant of unknown values. | [optional] 
**identity** | **str, none_type** | The value of the &#x60;Identity&#x60; header from the inbound invite request. Only present for inbound calls and if the account is configured to forward this header. | [optional] 
**stir_shaken** | **{str: (str,)}, none_type** | For inbound calls, the Bandwidth STIR/SHAKEN implementation will verify the information provided in the inbound invite request &#x60;Identity&#x60; header. The verification status is stored in the call state &#x60;stirShaken&#x60; property as follows.  | Property          | Description | |:------------------|:------------| | verstat | (optional) The verification status indicating whether the verification was successful or not. Possible values are &#x60;TN-Verification-Passed&#x60; or &#x60;TN-Verification-Failed&#x60;. | | attestationIndicator | (optional) The attestation level verified by Bandwidth. Possible values are &#x60;A&#x60; (full), &#x60;B&#x60; (partial) or &#x60;C&#x60; (gateway). | | originatingId | (optional) A unique origination identifier. |  More information: [Understanding STIR/SHAKEN](https://www.bandwidth.com/regulations/stir-shaken)  | [optional] 
**enqueued_time** | **datetime, none_type** | If &lt;a href&#x3D;&#39;/docs/voice/rateLimits&#39;&gt;outbound call queueing&lt;/a&gt; is enabled and this is an outbound call, the time this call was placed in queue. | [optional] 
**start_time** | **datetime, none_type** | The time the call was initiated, in ISO 8601 format. &#x60;null&#x60; if the call is still in your queue. | [optional] 
**answer_time** | **datetime, none_type** | Populated once the call has been answered, with the time in ISO 8601 format. | [optional] 
**end_time** | **datetime, none_type** | Populated once the call has ended, with the time in ISO 8601 format. | [optional] 
**disconnect_cause** | **str, none_type** | Populated once the call has ended, with the reason the call ended. See above for possible values. | [optional] 
**error_message** | **str, none_type** | Populated only if the call ended with an error, with text explaining the reason. | [optional] 
**error_id** | **str, none_type** | Populated only if the call ended with an error, with a Bandwidth internal id that references the error event. | [optional] 
**last_update** | **datetime** | The last time the call had a state update, in ISO 8601 format. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


