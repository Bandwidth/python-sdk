# ModifyConferenceRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Setting the conference state to &#x60;completed&#x60; ends the conference and ejects all members | [optional]  if omitted the server will use the default value of "active"
**redirect_url** | **str, none_type** | The URL to send the [conferenceRedirect](/docs/voice/webhooks/conferenceRedirect) event which will provide new BXML. Not allowed if &#x60;state&#x60; is &#x60;completed&#x60;, but required if &#x60;state&#x60; is &#x60;active&#x60; | [optional] 
**redirect_fallback_url** | **str, none_type** | A fallback url which, if provided, will be used to retry the &#x60;conferenceRedirect&#x60; webhook delivery in case &#x60;redirectUrl&#x60; fails to respond.  Not allowed if &#x60;state&#x60; is &#x60;completed&#x60;. | [optional] 
**redirect_method** | **str, none_type** | The HTTP method to use for the request to &#x60;redirectUrl&#x60;. Not allowed if &#x60;state&#x60; is &#x60;completed&#x60;. | [optional] 
**redirect_fallback_method** | **str, none_type** | The HTTP method to use for the request to &#x60;redirectFallbackUrl&#x60;. Not allowed if &#x60;state&#x60; is &#x60;completed&#x60;. | [optional] 
**username** | **str, none_type** | The username to send in the HTTP request to &#x60;redirectUrl&#x60;. | [optional] 
**password** | **str, none_type** | The password to send in the HTTP request to &#x60;redirectUrl&#x60;. | [optional] 
**fallback_username** | **str, none_type** | The username to send in the HTTP request to &#x60;redirectFallbackUrl&#x60;. | [optional] 
**fallback_password** | **str, none_type** | The password to send in the HTTP request to &#x60;redirectFallbackUrl&#x60;. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


