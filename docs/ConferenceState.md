# ConferenceState


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The Bandwidth-generated conference ID | [optional] 
**name** | **str** | The name of the conference, as specified by your application | [optional] 
**created_time** | **datetime** | The time the conference was initiated, in ISO 8601 format. | [optional] 
**completed_time** | **datetime, none_type** | The time the conference was terminated, in ISO 8601 format. | [optional] 
**conference_event_url** | **str, none_type** | The URL to send the conference-related events. | [optional] 
**conference_event_method** | **str, none_type** | The HTTP method used for the requests to &#x60;conferenceEventUrl&#x60;. | [optional] 
**tag** | **str, none_type** | The custom string attached to the conference that will be sent with callbacks. | [optional] 
**active_members** | [**[ConferenceMemberState], none_type**](ConferenceMemberState.md) | A list of active members of the conference. Omitted if this is a response to the [Get Conferences endpoint](/apis/voice/#operation/getConferences) | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


