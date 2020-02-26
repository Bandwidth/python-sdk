# Bandwidth Python SDK
  
Bandwidth's API docs can be found at https://dev.bandwidth.com

Python specific docs can be found at https://dev.bandwidth.com/sdks/python.html

# Python SDK

## Download & Install

```
pip install bandwidth-sdk
```

## Initialize Bandwidth Client

```python
from bandwidth.bandwidth_client import BandwidthClient

from bandwidth.messaging.models.message_request import MessageRequest
from bandwidth.messaging.exceptions.generic_client_exception import GenericClientException
from bandwidth.messaging.exceptions.path_client_exception import PathClientException

from bandwidth.voice.models.api_create_call_request import ApiCreateCallRequest
from bandwidth.voice.models.modify_call_recording_state import ModifyCallRecordingState
from bandwidth.voice.exceptions.error_response_exception import ErrorResponseException
from bandwidth.voice.bxml.response import Response
from bandwidth.voice.bxml.verbs import *

##Initialize client
voice_basic_auth_user_name = 'username'
voice_basic_auth_password = 'password'
messaging_basic_auth_user_name = 'token'
messaging_basic_auth_password = 'secret'

bandwidth_client = BandwidthClient(
    voice_basic_auth_user_name=voice_basic_auth_user_name,
    voice_basic_auth_password=voice_basic_auth_password,
    messaging_basic_auth_user_name=messaging_basic_auth_user_name,
    messaging_basic_auth_password=messaging_basic_auth_password)
```

## Create Phone Call

```python
voice_client = bandwidth_client.voice_client.client
account_id = "1"

##Create phone call
body = ApiCreateCallRequest()
body.mfrom = "+17777777777"
body.to = "+16666666666"
body.application_id = "3-d-4-b-5"
body.answer_url = "https://test.com"

try:
    response = voice_client.create_call(account_id, body=body)
    print(response.body.call_id) #c-3f758f24-a59bb21e-4f23-4d62-afe9-53o2ls3o4saio4l
    print(response.status_code) #201
except ErrorResponseException as e:
    print(e.description) #Invalid from: must be an E164 telephone number
    print(e.response_code) #400
```

## Generate BXML

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

## Send Text Message

```python
messaging_client = bandwidth_client.messaging_client.client
account_id = "1"

body = MessageRequest()
body.application_id = "1-d-b"
body.to = ["+17777777777"]
body.mfrom = "+18888888888"
body.text = "Greetings!"

try:
    response = messaging_client.create_message(account_id, body=body)
    print(response.body.id) #1570819529611mexbyfr7ugrouuxy
    print(response.status_code) #202
except GenericClientException as e:
    print(e.description) #Your request could not be accepted.
    print(e.response_code) #400
except PathClientException as e:
    print(e.message) #Access is denied
    print(e.response_code) #403
```
