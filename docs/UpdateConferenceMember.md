# UpdateConferenceMember


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mute** | **bool** | Whether or not this member is currently muted. Members who are muted are still able to hear other participants.  Updates this member&#39;s mute status. Has no effect if omitted. | [optional] 
**hold** | **bool** | Whether or not this member is currently on hold. Members who are on hold are not able to hear or speak in the conference.  Updates this member&#39;s hold status. Has no effect if omitted. | [optional] 
**call_ids_to_coach** | **List[str]** | If this member had a value set for &#x60;callIdsToCoach&#x60; in its [Conference](/docs/voice/bxml/conference) verb or this list was added with a previous PUT request to modify the member, this is that list of calls.  Modifies the calls that this member is coaching. Has no effect if omitted. See the documentation for the [Conference](/docs/voice/bxml/conference) verb for more details about coaching.  Note that this will not add the matching calls to the conference; each call must individually execute a Conference verb to join. | [optional] 

## Example

```python
from bandwidth.models.update_conference_member import UpdateConferenceMember

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateConferenceMember from a JSON string
update_conference_member_instance = UpdateConferenceMember.from_json(json)
# print the JSON string representation of the object
print UpdateConferenceMember.to_json()

# convert the object into a dict
update_conference_member_dict = update_conference_member_instance.to_dict()
# create an instance of UpdateConferenceMember from a dict
update_conference_member_form_dict = update_conference_member.from_dict(update_conference_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


