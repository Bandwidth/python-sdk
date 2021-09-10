
# Call Callback

This object represents all possible fields that may be included in callbacks related to call events, including events that come from BXML verbs

## Structure

`CallCallback`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `event_type` | `string` | Optional | - |
| `event_time` | `string` | Optional | - |
| `account_id` | `string` | Optional | - |
| `application_id` | `string` | Optional | - |
| `mfrom` | `string` | Optional | - |
| `to` | `string` | Optional | - |
| `direction` | `string` | Optional | - |
| `call_id` | `string` | Optional | - |
| `call_url` | `string` | Optional | - |
| `start_time` | `string` | Optional | - |
| `answer_time` | `string` | Optional | - |
| `transfer_caller_id` | `string` | Optional | - |
| `transfer_to` | `string` | Optional | - |
| `cause` | `string` | Optional | - |
| `error_message` | `string` | Optional | - |
| `error_id` | `string` | Optional | - |
| `end_time` | `string` | Optional | - |
| `digit` | `string` | Optional | - |
| `parent_call_id` | `string` | Optional | - |
| `recording_id` | `string` | Optional | - |
| `duration` | `string` | Optional | - |
| `file_format` | `string` | Optional | - |
| `media_url` | `string` | Optional | - |
| `tag` | `string` | Optional | - |
| `channels` | `int` | Optional | - |
| `status` | `string` | Optional | - |
| `digits` | `string` | Optional | - |
| `terminating_digit` | `string` | Optional | - |
| `transcription` | [`Transcription`](/doc/Voice/models/transcription.md) | Optional | - |
| `diversion` | [`Diversion`](/doc/Voice/models/diversion.md) | Optional | - |

## Example (as JSON)

```json
{
  "eventType": null,
  "eventTime": null,
  "accountId": null,
  "applicationId": null,
  "from": null,
  "to": null,
  "direction": null,
  "callId": null,
  "callUrl": null,
  "startTime": null,
  "answerTime": null,
  "transferCallerId": null,
  "transferTo": null,
  "cause": null,
  "errorMessage": null,
  "errorId": null,
  "endTime": null,
  "digit": null,
  "parentCallId": null,
  "recordingId": null,
  "duration": null,
  "fileFormat": null,
  "mediaUrl": null,
  "tag": null,
  "channels": null,
  "status": null,
  "digits": null,
  "terminatingDigit": null,
  "transcription": null,
  "diversion": null
}
```

