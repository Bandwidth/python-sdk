# UpdateCall


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | [**CallStateEnum**](CallStateEnum.md) |  | [optional] 
**redirect_url** | **str** | The URL to send the [Redirect](/docs/voice/bxml/redirect) event to which will provide new BXML.  Required if &#x60;state&#x60; is &#x60;active&#x60;.  Not allowed if &#x60;state&#x60; is &#x60;completed&#x60;. | [optional] 
**redirect_method** | [**RedirectMethodEnum**](RedirectMethodEnum.md) |  | [optional] 
**username** | **str** | Basic auth username. | [optional] 
**password** | **str** | Basic auth password. | [optional] 
**redirect_fallback_url** | **str** | A fallback url which, if provided, will be used to retry the redirect callback delivery in case &#x60;redirectUrl&#x60; fails to respond. | [optional] 
**redirect_fallback_method** | [**RedirectMethodEnum**](RedirectMethodEnum.md) |  | [optional] 
**fallback_username** | **str** | Basic auth username. | [optional] 
**fallback_password** | **str** | Basic auth password. | [optional] 
**tag** | **str** | A custom string that will be sent with this and all future callbacks unless overwritten by a future &#x60;tag&#x60; attribute or [&#x60;&lt;Tag&gt;&#x60;](/docs/voice/bxml/tag) verb, or cleared.  May be cleared by setting &#x60;tag&#x3D;\&quot;\&quot;&#x60;.  Max length 256 characters.  Not allowed if &#x60;state&#x60; is &#x60;completed&#x60;. | [optional] 

## Example

```python
from bandwidth.models.update_call import UpdateCall

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCall from a JSON string
update_call_instance = UpdateCall.from_json(json)
# print the JSON string representation of the object
print(UpdateCall.to_json())

# convert the object into a dict
update_call_dict = update_call_instance.to_dict()
# create an instance of UpdateCall from a dict
update_call_from_dict = UpdateCall.from_dict(update_call_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


