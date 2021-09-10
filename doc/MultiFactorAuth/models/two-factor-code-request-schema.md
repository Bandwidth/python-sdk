
# Two Factor Code Request Schema

## Structure

`TwoFactorCodeRequestSchema`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `to` | `string` | Required | The phone number to send the 2fa code to. |
| `mfrom` | `string` | Required | The application phone number, the sender of the 2fa code. |
| `application_id` | `string` | Required | The application unique ID, obtained from Bandwidth. |
| `scope` | `string` | Optional | An optional field to denote what scope or action the 2fa code is addressing.  If not supplied, defaults to "2FA". |
| `message` | `string` | Required | The message format of the 2fa code.  There are three values that the system will replace "{CODE}", "{NAME}", "{SCOPE}".  The "{SCOPE}" and "{NAME} value template are optional, while "{CODE}" must be supplied.  As the name would suggest, code will be replace with the actual 2fa code.  Name is replaced with the application name, configured during provisioning of 2fa.  The scope value is the same value sent during the call and partitioned by the server. |
| `digits` | `float` | Required | The number of digits for your 2fa code.  The valid number ranges from 2 to 8, inclusively. |

## Example (as JSON)

```json
{
  "to": "to6",
  "from": "from2",
  "applicationId": "applicationId0",
  "scope": null,
  "message": "message0",
  "digits": 181.08
}
```

