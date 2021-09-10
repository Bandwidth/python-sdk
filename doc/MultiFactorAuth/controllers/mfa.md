# MFA

```python
mfa_controller = client.multi_factor_auth_client.mfa
```

## Class Name

`MFAController`

## Methods

* [Create Voice Two Factor](/doc/MultiFactorAuth/controllers/mfa.md#create-voice-two-factor)
* [Create Messaging Two Factor](/doc/MultiFactorAuth/controllers/mfa.md#create-messaging-two-factor)
* [Create Verify Two Factor](/doc/MultiFactorAuth/controllers/mfa.md#create-verify-two-factor)


# Create Voice Two Factor

Multi-Factor authentication with Bandwidth Voice services. Allows for a user to send an MFA code via a phone call.

```python
def create_voice_two_factor(self,
                           account_id,
                           body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id` | `string` | Template, Required | Bandwidth Account ID with Voice service enabled |
| `body` | [`TwoFactorCodeRequestSchema`]($m/MultiFactorAuth/TwoFactorCodeRequestSchema) | Body, Required | - |

## Response Type

[`TwoFactorVoiceResponse`]($m/MultiFactorAuth/TwoFactorVoiceResponse)

## Example Usage

```python
account_id = 'accountId0'
body = TwoFactorCodeRequestSchema()
body.to = 'to0'
body.mfrom = 'from6'
body.application_id = 'applicationId6'
body.message = 'message6'
body.digits = 45.32

result = mfa_controller.create_voice_two_factor(account_id, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | If there is any issue with values passed in by the user | [`ErrorWithRequestException`]($m/MultiFactorAuth/ErrorWithRequest) |
| 401 | Authentication is either incorrect or not present | [`UnauthorizedRequestException`]($m/MultiFactorAuth/UnauthorizedRequest) |
| 403 | The user is not authorized to access this resource | [`ForbiddenRequestException`]($m/MultiFactorAuth/ForbiddenRequest) |
| 500 | An internal server error occurred | [`ErrorWithRequestException`]($m/MultiFactorAuth/ErrorWithRequest) |


# Create Messaging Two Factor

Multi-Factor authentication with Bandwidth Messaging services. Allows a user to send an MFA code via a text message (SMS).

```python
def create_messaging_two_factor(self,
                               account_id,
                               body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id` | `string` | Template, Required | Bandwidth Account ID with Messaging service enabled |
| `body` | [`TwoFactorCodeRequestSchema`]($m/MultiFactorAuth/TwoFactorCodeRequestSchema) | Body, Required | - |

## Response Type

[`TwoFactorMessagingResponse`]($m/MultiFactorAuth/TwoFactorMessagingResponse)

## Example Usage

```python
account_id = 'accountId0'
body = TwoFactorCodeRequestSchema()
body.to = 'to0'
body.mfrom = 'from6'
body.application_id = 'applicationId6'
body.message = 'message6'
body.digits = 45.32

result = mfa_controller.create_messaging_two_factor(account_id, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | If there is any issue with values passed in by the user | [`ErrorWithRequestException`]($m/MultiFactorAuth/ErrorWithRequest) |
| 401 | Authentication is either incorrect or not present | [`UnauthorizedRequestException`]($m/MultiFactorAuth/UnauthorizedRequest) |
| 403 | The user is not authorized to access this resource | [`ForbiddenRequestException`]($m/MultiFactorAuth/ForbiddenRequest) |
| 500 | An internal server error occurred | [`ErrorWithRequestException`]($m/MultiFactorAuth/ErrorWithRequest) |


# Create Verify Two Factor

Allows a user to verify an MFA code.

```python
def create_verify_two_factor(self,
                            account_id,
                            body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id` | `string` | Template, Required | Bandwidth Account ID with Two-Factor enabled |
| `body` | [`TwoFactorVerifyRequestSchema`]($m/MultiFactorAuth/TwoFactorVerifyRequestSchema) | Body, Required | - |

## Response Type

[`TwoFactorVerifyCodeResponse`]($m/MultiFactorAuth/TwoFactorVerifyCodeResponse)

## Example Usage

```python
account_id = 'accountId0'
body = TwoFactorVerifyRequestSchema()
body.to = 'to0'
body.application_id = 'applicationId6'
body.expiration_time_in_minutes = 166.8
body.code = 'code4'

result = mfa_controller.create_verify_two_factor(account_id, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | If there is any issue with values passed in by the user | [`ErrorWithRequestException`]($m/MultiFactorAuth/ErrorWithRequest) |
| 401 | Authentication is either incorrect or not present | [`UnauthorizedRequestException`]($m/MultiFactorAuth/UnauthorizedRequest) |
| 403 | The user is not authorized to access this resource | [`ForbiddenRequestException`]($m/MultiFactorAuth/ForbiddenRequest) |
| 429 | The user has made too many bad requests and is temporarily locked out | [`ErrorWithRequestException`]($m/MultiFactorAuth/ErrorWithRequest) |
| 500 | An internal server error occurred | [`ErrorWithRequestException`]($m/MultiFactorAuth/ErrorWithRequest) |

