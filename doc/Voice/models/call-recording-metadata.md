
# Call Recording Metadata

## Structure

`CallRecordingMetadata`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `application_id` | `string` | Optional | - |
| `account_id` | `string` | Optional | - |
| `call_id` | `string` | Optional | - |
| `parent_call_id` | `string` | Optional | - |
| `recording_id` | `string` | Optional | - |
| `to` | `string` | Optional | - |
| `mfrom` | `string` | Optional | - |
| `transfer_caller_id` | `string` | Optional | - |
| `transfer_to` | `string` | Optional | - |
| `duration` | `string` | Optional | Format is ISO-8601 |
| `direction` | [`DirectionEnum`](/doc/Voice/models/direction-enum.md) | Optional | - |
| `channels` | `int` | Optional | - |
| `start_time` | `datetime` | Optional | - |
| `end_time` | `datetime` | Optional | - |
| `file_format` | [`FileFormatEnum`](/doc/Voice/models/file-format-enum.md) | Optional | - |
| `status` | `string` | Optional | The current status of the recording. Current values are 'processing', 'partial', 'complete', 'deleted' and 'error'. Additional states may be added in the future, so your application must be tolerant of unknown values. |
| `media_url` | `string` | Optional | - |
| `transcription` | [`TranscriptionMetadata`](/doc/Voice/models/transcription-metadata.md) | Optional | - |

## Example (as JSON)

```json
{
  "applicationId": null,
  "accountId": null,
  "callId": null,
  "parentCallId": null,
  "recordingId": null,
  "to": null,
  "from": null,
  "transferCallerId": null,
  "transferTo": null,
  "duration": null,
  "direction": null,
  "channels": null,
  "startTime": null,
  "endTime": null,
  "fileFormat": null,
  "status": null,
  "mediaUrl": null,
  "transcription": null
}
```

