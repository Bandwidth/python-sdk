# Getting Started with bandwidth

Bandwidth's set of APIs

## Install the Package

The package is compatible with Python versions ```2 >=2.7.9``` and ```3 >=3.4```.
Install the package from PyPi using the following pip command:

```python
pip install bandwidth-sdk==5.1.1
```

You can also view the package at:
https://pypi.python.org/pypi/bandwidth-sdk

## Initialize the API Client

The following parameters are configurable for the API Client.

| Parameter | Type | Description |
|  --- | --- | --- |
| `messaging_basic_auth_user_name` | `string` | The username to use with basic authentication |
| `messaging_basic_auth_password` | `string` | The password to use with basic authentication |
| `voice_basic_auth_user_name` | `string` | The username to use with basic authentication |
| `voice_basic_auth_password` | `string` | The password to use with basic authentication |
| `environment` | Environment | The API environment. <br> **Default: `Environment.PRODUCTION`** |
| `timeout` | `float` | The value to use for connection timeout. <br> **Default: 60** |
| `max_retries` | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 3** |
| `backoff_factor` | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 0** |

The API client can be initialized as following.

```python
from bandwidth.bandwidth_client import BandwidthClient

client = BandwidthClient(
    messaging_basic_auth_user_name='MessagingBasicAuthUserName',
    messaging_basic_auth_password='MessagingBasicAuthPassword',
    voice_basic_auth_user_name='VoiceBasicAuthUserName',
    voice_basic_auth_password='VoiceBasicAuthPassword',
    environment = Environment.PRODUCTION,)
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

## Authorization

This API does not require authentication.

## API Reference

### List of APIs

*

