
# Conference Recording Metadata

## Structure

`ConferenceRecordingMetadata`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id` | `string` | Optional | - |
| `conference_id` | `string` | Optional | - |
| `name` | `string` | Optional | - |
| `recording_id` | `string` | Optional | - |
| `duration` | `string` | Optional | Format is ISO-8601 |
| `channels` | `int` | Optional | - |
| `start_time` | `datetime` | Optional | - |
| `end_time` | `datetime` | Optional | - |
| `file_format` | [`FileFormatEnum`](/doc/Voice/models/file-format-enum.md) | Optional | - |
| `status` | `string` | Optional | The current status of the recording. Current possible values are 'processing', 'partial', 'complete', 'deleted', and 'error'. Additional states may be added in the future, so your application must be tolerant of unknown values. |
| `media_url` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "accountId": null,
  "conferenceId": null,
  "name": null,
  "recordingId": null,
  "duration": null,
  "channels": null,
  "startTime": null,
  "endTime": null,
  "fileFormat": null,
  "status": null,
  "mediaUrl": null
}
```

