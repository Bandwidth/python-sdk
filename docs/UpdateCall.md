# UpdateCall


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | [**CallStateEnum**](CallStateEnum.md) |  | [optional] 
**redirect_url** | **str, none_type** | The URL to send the [Redirect](/docs/voice/bxml/redirect) event to which will provide new BXML.  Required if &#x60;state&#x60; is &#x60;active&#x60;.  Not allowed if &#x60;state&#x60; is &#x60;completed&#x60;. | [optional] 
**redirect_method** | [**RedirectMethodEnum**](RedirectMethodEnum.md) |  | [optional] 
**username** | [**Username**](Username.md) |  | [optional] 
**password** | [**Password**](Password.md) |  | [optional] 
**redirect_fallback_url** | **str, none_type** | A fallback url which, if provided, will be used to retry the redirect callback delivery in case &#x60;redirectUrl&#x60; fails to respond | [optional] 
**redirect_fallback_method** | [**RedirectMethodEnum**](RedirectMethodEnum.md) |  | [optional] 
**fallback_username** | [**Username**](Username.md) |  | [optional] 
**fallback_password** | [**Password**](Password.md) |  | [optional] 
**tag** | **str, none_type** | A custom string that will be sent with this and all future callbacks unless overwritten by a future &#x60;tag&#x60; attribute or [&#x60;&lt;Tag&gt;&#x60;](/docs/voice/bxml/tag) verb, or cleared.  May be cleared by setting &#x60;tag&#x3D;\&quot;\&quot;&#x60;.  Max length 256 characters.  Not allowed if &#x60;state&#x60; is &#x60;completed&#x60;. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


