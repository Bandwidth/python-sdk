
# Modify Call Request

## Structure

`ModifyCallRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `state` | [`StateEnum`](/doc/Voice/models/state-enum.md) | Optional | **Default**: `'active'`<br>*Default: `'active'`* |
| `redirect_url` | `string` | Optional | Required if state is 'active' |
| `redirect_fallback_url` | `string` | Optional | - |
| `redirect_method` | [`RedirectMethodEnum`](/doc/Voice/models/redirect-method-enum.md) | Optional | - |
| `redirect_fallback_method` | [`RedirectFallbackMethodEnum`](/doc/Voice/models/redirect-fallback-method-enum.md) | Optional | - |
| `username` | `string` | Optional | - |
| `password` | `string` | Optional | - |
| `fallback_username` | `string` | Optional | - |
| `fallback_password` | `string` | Optional | - |
| `tag` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "state": null,
  "redirectUrl": null,
  "redirectFallbackUrl": null,
  "redirectMethod": null,
  "redirectFallbackMethod": null,
  "username": null,
  "password": null,
  "fallbackUsername": null,
  "fallbackPassword": null,
  "tag": null
}
```

