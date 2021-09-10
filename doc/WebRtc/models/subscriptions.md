
# Subscriptions

## Structure

`Subscriptions`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `session_id` | `string` | Required | Session the subscriptions are associated with<br><br>If this is the only field, the subscriber will be subscribed to all participants in the session (including any participants that are later added to the session) |
| `participants` | [`List of ParticipantSubscription`](/doc/WebRtc/models/participant-subscription.md) | Optional | Subset of participants to subscribe to in the session. Optional. |

## Example (as JSON)

```json
{
  "sessionId": "d8886aad-b956-4e1b-b2f4-d7c9f8162772"
}
```

