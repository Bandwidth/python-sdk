# Bandwidth Python SDK

[![Test](https://github.com/Bandwidth/python-sdk/actions/workflows/test.yaml/badge.svg)](https://github.com/Bandwidth/python-sdk/actions/workflows/test.yaml)

| **OS** | **Python** |
|:---:|:---:|
| Windows 2016 | 3.6, 3.7, 3.8, 3.9 |
| Windows 2019 | 3.6, 3.7, 3.8, 3.9 |
| Ubuntu 18.04 | 3.6, 3.7, 3.8, 3.9 |
| Ubuntu 20.04 | 3.6, 3.7, 3.8, 3.9 |


## Getting Started

### Installation

```
pip install bandwidth-sdk
```

### Initialize

```python
from bandwidth.bandwidth_client import BandwidthClient

from bandwidth.messaging.models.message_request import MessageRequest
from bandwidth.messaging.exceptions.messaging_exception import MessagingException

from bandwidth.voice.models.create_call_request import CreateCallRequest
from bandwidth.voice.exceptions.api_error_exception import ApiErrorException
from bandwidth.voice.bxml.response import Response
from bandwidth.voice.bxml.verbs import *

from bandwidth.multifactorauth.models.two_factor_code_request_schema import TwoFactorCodeRequestSchema
from bandwidth.multifactorauth.models.two_factor_verify_request_schema import TwoFactorVerifyRequestSchema

from bandwidth.phonenumberlookup.controllers.api_controller import APIController, ApiResponse, APIException
from bandwidth.phonenumberlookup.models.accounts_tnlookup_request import AccountsTnlookupRequest

from bandwidth.webrtc.models.session import Session
from bandwidth.webrtc.models.participant import Participant
from bandwidth.webrtc.models.publish_permission_enum import PublishPermissionEnum

bandwidth_client = BandwidthClient(
    voice_basic_auth_user_name='username',
    voice_basic_auth_password='password',
    messaging_basic_auth_user_name='username',
    messaging_basic_auth_password='password',
    multi_factor_auth_basic_auth_user_name='username',
    multi_factor_auth_basic_auth_password='password',
    phone_number_lookup_basic_auth_user_name='username',
    phone_number_lookup_basic_auth_password='password',
    web_rtc_basic_auth_user_name='username',
    web_rtc_basic_auth_password='password'
)
account_id = "12345"
```

### Create A Phone Call

```python
voice_client = bandwidth_client.voice_client.client

##Create phone call
body = CreateCallRequest()
body.mfrom = "+17777777777"
body.to = "+16666666666"
body.application_id = "3-d-4-b-5"
body.answer_url = "https://test.com"

try:
    response = voice_client.create_call(account_id, body=body)
    print(response.body.call_id) #c-3f758f24-a59bb21e-4f23-4d62-afe9-53o2ls3o4saio4l
    print(response.status_code) #201
except ApiErrorResponseException as e:
    print(e.description) #Invalid from: must be an E164 telephone number
    print(e.response_code) #400
```

### Send A Text Message

```python
messaging_client = bandwidth_client.messaging_client.client

body = MessageRequest()
body.application_id = "1-d-b"
body.to = ["+17777777777"]
body.mfrom = "+18888888888"
body.text = "Greetings!"

try:
    response = messaging_client.create_message(account_id, body)
    print(response.body.id) #1570819529611mexbyfr7ugrouuxy
    print(response.status_code) #202
except MessagingException as e:
    print(e.description) #Your request could not be accepted.
    print(e.response_code) #400
```

### Create BXML

```python
response = Response()
speak_sentence = SpeakSentence(
    sentence="Test",
    voice="susan",
    locale="en_US",
    gender="female"
)

response.add_verb(speak_sentence)
print(response.to_bxml())
```

### Create A MFA Request

```python
auth_client = bandwidth_client.multi_factor_auth_client.client

from_phone = "+18888888888"
to_phone = "+17777777777"
messaging_application_id = "1-d-b"
scope = "scope"
digits = 6

body = TwoFactorCodeRequestSchema(
    mfrom = from_phone,
    to = to_phone,
    application_id = messaging_application_id,
    scope = scope,
    digits = digits,
    message = "Your temporary {NAME} {SCOPE} code is {CODE}"
)
auth_client.create_messaging_two_factor(account_id, body)

code = "123456" #This is the user input to validate

body = TwoFactorVerifyRequestSchema(
    to = to_phone,
    application_id = application_id,
    scope = scope,
    code = code,
    expiration_time_in_minutes = 3
)
response = auth_client.create_verify_two_factor(account_id, body)
print("Auth status: " + str(response.body.valid))
```

### Perform a TN Lookup Request

```python
tnLookup_controller = bandwidth_client.phone_number_lookup_client.client
body = AccountsTnlookupRequest()
body.tns = ['+19195551234']

try:
    response = tnLookup_controller.create_tn_lookup_request(account_id, body)
    print(response.status_code)

except APIException as e:
    print("Error:", e.response_code)

requestId = response.body.request_id    # "1234-abcd-5678-efgh"

try:
    response = tnLookup_controller.get_tn_lookup_result(account_id, requestId)
    print(response)

except APIException as e:
    print("Error:", e.response_code)
```

### WebRtc Participant & Session Management

```python
web_rtc_client = bandwidth_client.web_rtc_client.client

create_session_body = Session()
create_session_body.tag = 'new-session'

create_session_response = web_rtc_client.create_session(account_id, create_session_body)
session_id = create_session_response.body.id

create_participant_body = Participant()
create_participant_body.publish_permissions = [
    PublishPermissionEnum.AUDIO,
    PublishPermissionEnum.VIDEO
]
create_participant_body.callback_url = "https://sample.com"

create_participant_response = web_rtc_client.create_participant(account_id, create_participant_body)
participant_id = create_participant_response.body.participant.id

web_rtc_client.add_participant_to_session(account_id, session_id, participant_id)
```

## Supported Python Versions

This package can be used with Python >= 3.0

## Documentation

Documentation for this package can be found at https://dev.bandwidth.com/sdks/python.html

## Credentials

Information for credentials for this package can be found at https://dev.bandwidth.com/guides/accountCredentials.html
