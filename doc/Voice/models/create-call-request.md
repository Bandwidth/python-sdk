
# Create Call Request

## Structure

`CreateCallRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mfrom` | `string` | Required | Format is E164 |
| `to` | `string` | Required | Format is E164 or SIP URI |
| `uui` | `string` | Optional | A comma-separated list of 'User-To-User' headers to be sent in the INVITE when calling a SIP URI. Each value must end with an 'encoding' parameter as described in https://tools.ietf.org/html/rfc7433. Only 'jwt' and 'base64' encodings are allowed. The entire value cannot exceed 350 characters, including parameters and separators. |
| `call_timeout` | `float` | Optional | - |
| `callback_timeout` | `float` | Optional | - |
| `answer_url` | `string` | Required | - |
| `answer_fallback_url` | `string` | Optional | - |
| `username` | `string` | Optional | - |
| `password` | `string` | Optional | - |
| `fallback_username` | `string` | Optional | - |
| `fallback_password` | `string` | Optional | - |
| `answer_method` | [`AnswerMethodEnum`](/doc/Voice/models/answer-method-enum.md) | Optional | - |
| `answer_fallback_method` | [`AnswerFallbackMethodEnum`](/doc/Voice/models/answer-fallback-method-enum.md) | Optional | - |
| `disconnect_url` | `string` | Optional | - |
| `disconnect_method` | [`DisconnectMethodEnum`](/doc/Voice/models/disconnect-method-enum.md) | Optional | - |
| `tag` | `string` | Optional | - |
| `application_id` | `string` | Required | - |
| `machine_detection` | [`MachineDetectionRequest`](/doc/Voice/models/machine-detection-request.md) | Optional | - |

## Example (as JSON)

```json
{
  "from": "+15555555555",
  "to": "+15555555555, sip:john@doe.com",
  "answerUrl": null,
  "applicationId": null
}
```

