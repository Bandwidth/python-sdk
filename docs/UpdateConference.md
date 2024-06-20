# UpdateConference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ConferenceStateEnum**](ConferenceStateEnum.md) |  | [optional] 
**redirect_url** | **str** | The URL to send the [conferenceRedirect](/docs/voice/webhooks/conferenceRedirect) event which will provide new BXML. Not allowed if &#x60;state&#x60; is &#x60;completed&#x60;, but required if &#x60;state&#x60; is &#x60;active&#x60;. | [optional] 
**redirect_method** | [**RedirectMethodEnum**](RedirectMethodEnum.md) |  | [optional] 
**username** | **str** | Basic auth username. | [optional] 
**password** | **str** | Basic auth password. | [optional] 
**redirect_fallback_url** | **str** | A fallback url which, if provided, will be used to retry the &#x60;conferenceRedirect&#x60; webhook delivery in case &#x60;redirectUrl&#x60; fails to respond.  Not allowed if &#x60;state&#x60; is &#x60;completed&#x60;. | [optional] 
**redirect_fallback_method** | [**RedirectMethodEnum**](RedirectMethodEnum.md) |  | [optional] 
**fallback_username** | **str** | Basic auth username. | [optional] 
**fallback_password** | **str** | Basic auth password. | [optional] 

## Example

```python
from bandwidth.models.update_conference import UpdateConference

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateConference from a JSON string
update_conference_instance = UpdateConference.from_json(json)
# print the JSON string representation of the object
print(UpdateConference.to_json())

# convert the object into a dict
update_conference_dict = update_conference_instance.to_dict()
# create an instance of UpdateConference from a dict
update_conference_from_dict = UpdateConference.from_dict(update_conference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


