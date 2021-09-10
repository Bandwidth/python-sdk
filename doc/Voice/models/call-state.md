
# Call State

## Structure

`CallState`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `call_id` | `string` | Optional | - |
| `parent_call_id` | `string` | Optional | - |
| `application_id` | `string` | Optional | - |
| `account_id` | `string` | Optional | - |
| `to` | `string` | Optional | - |
| `mfrom` | `string` | Optional | - |
| `direction` | `string` | Optional | - |
| `state` | `string` | Optional | The current state of the call. Current possible values are 'initiated', 'answered' and 'disconnected'. Additional states may be added in the future, so your application must be tolerant of unknown values. |
| `identity` | `string` | Optional | - |
| `stir_shaken` | `dict` | Optional | - |
| `start_time` | `datetime` | Optional | - |
| `answer_time` | `datetime` | Optional | - |
| `end_time` | `datetime` | Optional | - |
| `disconnect_cause` | `string` | Optional | The reason the call was disconnected, or null if the call is still active. Current values are 'cancel', 'timeout', 'busy', 'rejected', 'hangup', 'invalid-bxml', 'callback-error', 'application-error', 'error', 'account-limit', 'node-capacity-exceeded' and 'unknown'. Additional causes may be added in the future, so your application must be tolerant of unknown values. |
| `error_message` | `string` | Optional | - |
| `error_id` | `string` | Optional | - |
| `last_update` | `datetime` | Optional | - |

## Example (as JSON)

```json
{
  "callId": null,
  "parentCallId": null,
  "applicationId": null,
  "accountId": null,
  "to": null,
  "from": null,
  "direction": null,
  "state": null,
  "identity": null,
  "stirShaken": null,
  "startTime": null,
  "answerTime": null,
  "endTime": null,
  "disconnectCause": null,
  "errorMessage": null,
  "errorId": null,
  "lastUpdate": null
}
```

