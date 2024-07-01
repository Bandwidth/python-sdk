# Conference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The Bandwidth-generated conference ID. | [optional] 
**name** | **str** | The name of the conference, as specified by your application. | [optional] 
**created_time** | **datetime** | The time the conference was initiated, in ISO 8601 format. | [optional] 
**completed_time** | **datetime** | The time the conference was terminated, in ISO 8601 format. | [optional] 
**conference_event_url** | **str** | The URL to send the conference-related events. | [optional] 
**conference_event_method** | [**CallbackMethodEnum**](CallbackMethodEnum.md) |  | [optional] 
**tag** | **str** | The custom string attached to the conference that will be sent with callbacks. | [optional] 
**active_members** | [**List[ConferenceMember]**](ConferenceMember.md) | A list of active members of the conference. Omitted if this is a response to the [Get Conferences endpoint](/apis/voice#tag/Conferences/operation/listConferences). | [optional] 

## Example

```python
from bandwidth.models.conference import Conference

# TODO update the JSON string below
json = "{}"
# create an instance of Conference from a JSON string
conference_instance = Conference.from_json(json)
# print the JSON string representation of the object
print(Conference.to_json())

# convert the object into a dict
conference_dict = conference_instance.to_dict()
# create an instance of Conference from a dict
conference_from_dict = Conference.from_dict(conference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


