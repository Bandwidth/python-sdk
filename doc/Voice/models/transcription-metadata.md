
# Transcription Metadata

## Structure

`TranscriptionMetadata`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | - |
| `status` | `string` | Optional | The current status of the transcription. Current values are 'none', 'processing', 'available', 'error', 'timeout', 'file-size-too-big', and 'file-size-too-small'. Additional states may be added in the future, so your application must be tolerant of unknown values. |
| `completed_time` | `string` | Optional | - |
| `url` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "id": null,
  "status": null,
  "completedTime": null,
  "url": null
}
```

