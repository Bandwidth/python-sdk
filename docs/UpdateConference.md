# UpdateConference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ConferenceStateEnum**](ConferenceStateEnum.md) |  | [optional] 
**redirect_url** | **str, none_type** | The URL to send the [conferenceRedirect](/docs/voice/webhooks/conferenceRedirect) event which will provide new BXML. Not allowed if &#x60;state&#x60; is &#x60;completed&#x60;, but required if &#x60;state&#x60; is &#x60;active&#x60; | [optional] 
**redirect_method** | [**RedirectMethodEnum**](RedirectMethodEnum.md) |  | [optional] 
**username** | **str, none_type** | Basic auth username. | [optional] 
**password** | **str, none_type** | Basic auth password. | [optional] 
**redirect_fallback_url** | **str, none_type** | A fallback url which, if provided, will be used to retry the &#x60;conferenceRedirect&#x60; webhook delivery in case &#x60;redirectUrl&#x60; fails to respond.  Not allowed if &#x60;state&#x60; is &#x60;completed&#x60;. | [optional] 
**redirect_fallback_method** | [**RedirectMethodEnum**](RedirectMethodEnum.md) |  | [optional] 
**fallback_username** | **str, none_type** | Basic auth username. | [optional] 
**fallback_password** | **str, none_type** | Basic auth password. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


