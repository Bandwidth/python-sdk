
# Bandwidth Message Item

## Structure

`BandwidthMessageItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `message_id` | `string` | Optional | The message id |
| `account_id` | `string` | Optional | The account id of the message |
| `source_tn` | `string` | Optional | The source phone number of the message |
| `destination_tn` | `string` | Optional | The recipient phone number of the message |
| `message_status` | `string` | Optional | The status of the message |
| `message_direction` | `string` | Optional | The direction of the message relative to Bandwidth. INBOUND or OUTBOUND |
| `message_type` | `string` | Optional | The type of message. sms or mms |
| `segment_count` | `int` | Optional | The number of segments the message was sent as |
| `error_code` | `int` | Optional | The numeric error code of the message |
| `receive_time` | `string` | Optional | The ISO 8601 datetime of the message |
| `carrier_name` | `string` | Optional | The name of the carrier. Not currently supported for MMS, coming soon |
| `message_size` | `int` | Optional | The size of the message including message content and headers |
| `message_length` | `int` | Optional | The length of the message content |
| `attachment_count` | `int` | Optional | The number of attachments the message has |
| `recipient_count` | `int` | Optional | The number of recipients the message has |
| `campaign_class` | `string` | Optional | The campaign class of the message, if it has one |

## Example (as JSON)

```json
{
  "messageId": null,
  "accountId": null,
  "sourceTn": null,
  "destinationTn": null,
  "messageStatus": null,
  "messageDirection": null,
  "messageType": null,
  "segmentCount": null,
  "errorCode": null,
  "receiveTime": null,
  "carrierName": null,
  "messageSize": null,
  "messageLength": null,
  "attachmentCount": null,
  "recipientCount": null,
  "campaignClass": null
}
```

