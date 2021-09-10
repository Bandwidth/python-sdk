
# Bandwidth Message

## Structure

`BandwidthMessage`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | The id of the message |
| `owner` | `string` | Optional | The Bandwidth phone number associated with the message |
| `application_id` | `string` | Optional | The application ID associated with the message |
| `time` | `string` | Optional | The datetime stamp of the message in ISO 8601 |
| `segment_count` | `int` | Optional | The number of segments the original message from the user is broken into before sending over to carrier networks |
| `direction` | `string` | Optional | The direction of the message relative to Bandwidth. Can be in or out |
| `to` | `List of string` | Optional | The phone number recipients of the message<br>**Constraints**: *Unique Items Required* |
| `mfrom` | `string` | Optional | The phone number the message was sent from |
| `media` | `List of string` | Optional | The list of media URLs sent in the message. Including a `filename` field in the `Content-Disposition` header of the media linked with a URL will set the displayed file name. This is a best practice to ensure that your media has a readable file name.<br>**Constraints**: *Unique Items Required* |
| `text` | `string` | Optional | The contents of the message |
| `tag` | `string` | Optional | The custom string set by the user |
| `priority` | `string` | Optional | The priority specified by the user |

## Example (as JSON)

```json
{
  "id": null,
  "owner": null,
  "applicationId": null,
  "time": null,
  "segmentCount": null,
  "direction": null,
  "to": null,
  "from": null,
  "media": null,
  "text": null,
  "tag": null,
  "priority": null
}
```

