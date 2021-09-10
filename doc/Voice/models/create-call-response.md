
# Create Call Response

## Structure

`CreateCallResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id` | `string` | Required | - |
| `call_id` | `string` | Required | - |
| `application_id` | `string` | Required | - |
| `to` | `string` | Required | - |
| `mfrom` | `string` | Required | - |
| `start_time` | `datetime` | Optional | - |
| `call_url` | `string` | Required | - |
| `call_timeout` | `float` | Optional | - |
| `callback_timeout` | `float` | Optional | - |
| `answer_url` | `string` | Required | - |
| `answer_method` | [`AnswerMethodEnum`](/doc/Voice/models/answer-method-enum.md) | Required | - |
| `answer_fallback_url` | `string` | Optional | - |
| `answer_fallback_method` | [`AnswerFallbackMethodEnum`](/doc/Voice/models/answer-fallback-method-enum.md) | Optional | - |
| `disconnect_url` | `string` | Optional | - |
| `disconnect_method` | [`DisconnectMethodEnum`](/doc/Voice/models/disconnect-method-enum.md) | Required | - |
| `username` | `string` | Optional | - |
| `password` | `string` | Optional | - |
| `fallback_username` | `string` | Optional | - |
| `fallback_password` | `string` | Optional | - |
| `tag` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "accountId": "accountId0",
  "callId": "callId0",
  "applicationId": "applicationId0",
  "to": "to6",
  "from": "from2",
  "startTime": null,
  "callUrl": "callUrl2",
  "callTimeout": null,
  "callbackTimeout": null,
  "answerUrl": "answerUrl8",
  "answerMethod": "POST",
  "answerFallbackUrl": null,
  "answerFallbackMethod": null,
  "disconnectUrl": null,
  "disconnectMethod": "POST",
  "username": null,
  "password": null,
  "fallbackUsername": null,
  "fallbackPassword": null,
  "tag": null
}
```

