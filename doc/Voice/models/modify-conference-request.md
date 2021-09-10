
# Modify Conference Request

## Structure

`ModifyConferenceRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | [`StatusEnum`](/doc/Voice/models/status-enum.md) | Optional | - |
| `redirect_url` | `string` | Optional | - |
| `redirect_fallback_url` | `string` | Optional | - |
| `redirect_method` | [`RedirectMethodEnum`](/doc/Voice/models/redirect-method-enum.md) | Optional | - |
| `redirect_fallback_method` | [`RedirectFallbackMethodEnum`](/doc/Voice/models/redirect-fallback-method-enum.md) | Optional | - |
| `username` | `string` | Optional | - |
| `password` | `string` | Optional | - |
| `fallback_username` | `string` | Optional | - |
| `fallback_password` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "status": null,
  "redirectUrl": null,
  "redirectFallbackUrl": null,
  "redirectMethod": null,
  "redirectFallbackMethod": null,
  "username": null,
  "password": null,
  "fallbackUsername": null,
  "fallbackPassword": null
}
```

