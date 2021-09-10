
# Accounts Participants Response

## Structure

`AccountsParticipantsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `participant` | [`Participant`](/doc/WebRtc/models/participant.md) | Optional | A participant object |
| `token` | `string` | Optional | Auth token for the returned participant<br><br>This should be passed to the participant so that they can connect to the platform |

## Example (as JSON)

```json
{
  "participant": null,
  "token": null
}
```

