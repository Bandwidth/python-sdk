
# Conference State

## Structure

`ConferenceState`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | - |
| `name` | `string` | Optional | - |
| `created_time` | `datetime` | Optional | - |
| `completed_time` | `datetime` | Optional | - |
| `conference_event_url` | `string` | Optional | - |
| `conference_event_method` | [`ConferenceEventMethodEnum`](/doc/Voice/models/conference-event-method-enum.md) | Optional | - |
| `tag` | `string` | Optional | - |
| `active_members` | [`List of ConferenceMemberState`](/doc/Voice/models/conference-member-state.md) | Optional | - |

## Example (as JSON)

```json
{
  "id": null,
  "name": null,
  "createdTime": null,
  "completedTime": null,
  "conferenceEventUrl": null,
  "conferenceEventMethod": null,
  "tag": null,
  "activeMembers": null
}
```

