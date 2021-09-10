
# Client Class Documentation

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| `messaging_basic_auth_user_name` | `string` | The username to use with basic authentication |
| `messaging_basic_auth_password` | `string` | The password to use with basic authentication |
| `multi_factor_auth_basic_auth_user_name` | `string` | The username to use with basic authentication |
| `multi_factor_auth_basic_auth_password` | `string` | The password to use with basic authentication |
| `phone_number_lookup_basic_auth_user_name` | `string` | The username to use with basic authentication |
| `phone_number_lookup_basic_auth_password` | `string` | The password to use with basic authentication |
| `voice_basic_auth_user_name` | `string` | The username to use with basic authentication |
| `voice_basic_auth_password` | `string` | The password to use with basic authentication |
| `web_rtc_basic_auth_user_name` | `string` | The username to use with basic authentication |
| `web_rtc_basic_auth_password` | `string` | The password to use with basic authentication |
| `base_url` | `string` | *Default*: `'https://www.example.com'` |
| `environment` | Environment | The API environment. <br> **Default: `Environment.PRODUCTION`** |
| `timeout` | `float` | The value to use for connection timeout. <br> **Default: 60** |
| `max_retries` | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| `backoff_factor` | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| `retry_statuses` | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524, 408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| `retry_methods` | `Array of string` | The http methods on which retry is to be done. <br> **Default: ['GET', 'PUT', 'GET', 'PUT']** |

The API client can be initialized as follows:

```python
from bandwidth.bandwidth_client import BandwidthClient
from bandwidth.configuration import Environment

client = BandwidthClient(
    messaging_basic_auth_user_name='MessagingBasicAuthUserName',
    messaging_basic_auth_password='MessagingBasicAuthPassword',
    multi_factor_auth_basic_auth_user_name='MultiFactorAuthBasicAuthUserName',
    multi_factor_auth_basic_auth_password='MultiFactorAuthBasicAuthPassword',
    phone_number_lookup_basic_auth_user_name='PhoneNumberLookupBasicAuthUserName',
    phone_number_lookup_basic_auth_password='PhoneNumberLookupBasicAuthPassword',
    voice_basic_auth_user_name='VoiceBasicAuthUserName',
    voice_basic_auth_password='VoiceBasicAuthPassword',
    web_rtc_basic_auth_user_name='WebRtcBasicAuthUserName',
    web_rtc_basic_auth_password='WebRtcBasicAuthPassword',
    environment=Environment.PRODUCTION,
    base_url = 'https://www.example.com',)
```

API calls return an `ApiResponse` object that includes the following fields:

| Field | Description |
|  --- | --- |
| `status_code` | Status code of the HTTP response |
| `reason_phrase` | Reason phrase of the HTTP response |
| `headers` | Headers of the HTTP response as a dictionary |
| `text` | The body of the HTTP response as a string |
| `request` | HTTP request info |
| `errors` | Errors, if they exist |
| `body` | The deserialized body of the HTTP response |

## bandwidth Client

The gateway for the SDK. This class acts as a factory for the Controllers and also holds the configuration of the SDK.

