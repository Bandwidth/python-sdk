# bandwidth-sdk
Bandwidth's Communication APIs

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://dev.bandwidth.com](https://dev.bandwidth.com)

## Requirements.

Python >=3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import bandwidth
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import bandwidth
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import bandwidth
from pprint import pprint
from bandwidth.api import calls_api
from bandwidth.model.call_state import CallState
from bandwidth.model.create_call import CreateCall
from bandwidth.model.create_call_response import CreateCallResponse
from bandwidth.model.update_call import UpdateCall
from bandwidth.model.voice_api_error import VoiceApiError
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = bandwidth.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = bandwidth.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)


# Enter a context with an instance of the API client
with bandwidth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = calls_api.CallsApi(api_client)
    account_id = "9900000" # str | Your Bandwidth Account ID
    create_call = CreateCall(
        to="+19195551234",
        _from="+19195554321",
        uui="eyJhbGciOiJIUzI1NiJ9.WyJoaSJd.-znkjYyCkgz4djmHUPSXl9YrJ6Nix_XvmlwKGFh5ERM;encoding=jwt,aGVsbG8gd29ybGQ=;encoding=base64",
        application_id="1234-qwer-5679-tyui",
        answer_url="https://www.myCallbackServer.com/webhooks/answer",
        answer_method=CallbackMethodEnum("POST"),
        username=Username("mySecretUsername"),
        password=Password("mySecretPassword1!"),
        answer_fallback_url="https://www.myFallbackServer.com/webhooks/answer",
        answer_fallback_method=CallbackMethodEnum("POST"),
        fallback_username=Username("mySecretUsername"),
        fallback_password=Password("mySecretPassword1!"),
        disconnect_url="disconnect_url_example",
        disconnect_method=CallbackMethodEnum("POST"),
        call_timeout=30,
        callback_timeout=15,
        machine_detection=MachineDetectionConfiguration(
            mode=MachineDetectionModeEnum("async"),
            detection_timeout=15,
            silence_timeout=10,
            speech_threshold=10,
            speech_end_threshold=5,
            machine_speech_end_threshold=5,
            delay_result=False,
            callback_url="https://myServer.com/bandwidth/webhooks/machineDetectionComplete",
            callback_method=CallbackMethodEnum("POST"),
            username=Username("mySecretUsername"),
            password=Password("mySecretPassword1!"),
            fallback_url="https://myFallbackServer.com/bandwidth/webhooks/machineDetectionComplete",
            fallback_method=CallbackMethodEnum("POST"),
            fallback_username=Username("mySecretUsername"),
            fallback_password=Password("mySecretPassword1!"),
        ),
        priority=5,
        tag="tag_example",
    ) # CreateCall | JSON object containing information to create an outbound call

    try:
        # Create Call
        api_response = api_instance.create_call(account_id, create_call)
        pprint(api_response)
    except bandwidth.ApiException as e:
        print("Exception when calling CallsApi->create_call: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CallsApi* | [**create_call**](docs/CallsApi.md#create_call) | **POST** /accounts/{accountId}/calls | Create Call
*CallsApi* | [**get_call_state**](docs/CallsApi.md#get_call_state) | **GET** /accounts/{accountId}/calls/{callId} | Get Call State Information
*CallsApi* | [**update_call**](docs/CallsApi.md#update_call) | **POST** /accounts/{accountId}/calls/{callId} | Update Call
*CallsApi* | [**update_call_bxml**](docs/CallsApi.md#update_call_bxml) | **PUT** /accounts/{accountId}/calls/{callId}/bxml | Update Call BXML
*ConferencesApi* | [**download_conference_recording**](docs/ConferencesApi.md#download_conference_recording) | **GET** /accounts/{accountId}/conferences/{conferenceId}/recordings/{recordingId}/media | Download Conference Recording
*ConferencesApi* | [**get_conference**](docs/ConferencesApi.md#get_conference) | **GET** /accounts/{accountId}/conferences/{conferenceId} | Get Conference Information
*ConferencesApi* | [**get_conference_member**](docs/ConferencesApi.md#get_conference_member) | **GET** /accounts/{accountId}/conferences/{conferenceId}/members/{memberId} | Get Conference Member
*ConferencesApi* | [**get_conference_recording**](docs/ConferencesApi.md#get_conference_recording) | **GET** /accounts/{accountId}/conferences/{conferenceId}/recordings/{recordingId} | Get Conference Recording Information
*ConferencesApi* | [**list_conference_recordings**](docs/ConferencesApi.md#list_conference_recordings) | **GET** /accounts/{accountId}/conferences/{conferenceId}/recordings | Get Conference Recordings
*ConferencesApi* | [**list_conferences**](docs/ConferencesApi.md#list_conferences) | **GET** /accounts/{accountId}/conferences | Get Conferences
*ConferencesApi* | [**update_conference**](docs/ConferencesApi.md#update_conference) | **POST** /accounts/{accountId}/conferences/{conferenceId} | Update Conference
*ConferencesApi* | [**update_conference_bxml**](docs/ConferencesApi.md#update_conference_bxml) | **PUT** /accounts/{accountId}/conferences/{conferenceId}/bxml | Update Conference BXML
*ConferencesApi* | [**update_conference_member**](docs/ConferencesApi.md#update_conference_member) | **PUT** /accounts/{accountId}/conferences/{conferenceId}/members/{memberId} | Update Conference Member
*MFAApi* | [**generate_messaging_code**](docs/MFAApi.md#generate_messaging_code) | **POST** /accounts/{accountId}/code/messaging | Messaging Authentication Code
*MFAApi* | [**generate_voice_code**](docs/MFAApi.md#generate_voice_code) | **POST** /accounts/{accountId}/code/voice | Voice Authentication Code
*MFAApi* | [**verify_code**](docs/MFAApi.md#verify_code) | **POST** /accounts/{accountId}/code/verify | Verify Authentication Code
*MediaApi* | [**delete_media**](docs/MediaApi.md#delete_media) | **DELETE** /users/{accountId}/media/{mediaId} | Delete Media
*MediaApi* | [**get_media**](docs/MediaApi.md#get_media) | **GET** /users/{accountId}/media/{mediaId} | Get Media
*MediaApi* | [**list_media**](docs/MediaApi.md#list_media) | **GET** /users/{accountId}/media | List Media
*MediaApi* | [**upload_media**](docs/MediaApi.md#upload_media) | **PUT** /users/{accountId}/media/{mediaId} | Upload Media
*MessagesApi* | [**create_message**](docs/MessagesApi.md#create_message) | **POST** /users/{accountId}/messages | Create Message
*MessagesApi* | [**list_messages**](docs/MessagesApi.md#list_messages) | **GET** /users/{accountId}/messages | List Messages
*ParticipantsApi* | [**create_participant**](docs/ParticipantsApi.md#create_participant) | **POST** /accounts/{accountId}/participants | Create Participant
*ParticipantsApi* | [**delete_participant**](docs/ParticipantsApi.md#delete_participant) | **DELETE** /accounts/{accountId}/participants/{participantId} | Delete Participant
*ParticipantsApi* | [**get_participant**](docs/ParticipantsApi.md#get_participant) | **GET** /accounts/{accountId}/participants/{participantId} | Get Participant
*PhoneNumberLookupApi* | [**create_lookup**](docs/PhoneNumberLookupApi.md#create_lookup) | **POST** /accounts/{accountId}/tnlookup | Create Lookup
*PhoneNumberLookupApi* | [**get_lookup_status**](docs/PhoneNumberLookupApi.md#get_lookup_status) | **GET** /accounts/{accountId}/tnlookup/{requestId} | Get Lookup Request Status
*RecordingsApi* | [**delete_call_transcription**](docs/RecordingsApi.md#delete_call_transcription) | **DELETE** /accounts/{accountId}/calls/{callId}/recordings/{recordingId}/transcription | Delete Transcription
*RecordingsApi* | [**delete_recording**](docs/RecordingsApi.md#delete_recording) | **DELETE** /accounts/{accountId}/calls/{callId}/recordings/{recordingId} | Delete Recording
*RecordingsApi* | [**delete_recording_media**](docs/RecordingsApi.md#delete_recording_media) | **DELETE** /accounts/{accountId}/calls/{callId}/recordings/{recordingId}/media | Delete Recording Media
*RecordingsApi* | [**download_call_recording**](docs/RecordingsApi.md#download_call_recording) | **GET** /accounts/{accountId}/calls/{callId}/recordings/{recordingId}/media | Download Recording
*RecordingsApi* | [**get_call_recording**](docs/RecordingsApi.md#get_call_recording) | **GET** /accounts/{accountId}/calls/{callId}/recordings/{recordingId} | Get Call Recording
*RecordingsApi* | [**get_call_transcription**](docs/RecordingsApi.md#get_call_transcription) | **GET** /accounts/{accountId}/calls/{callId}/recordings/{recordingId}/transcription | Get Transcription
*RecordingsApi* | [**list_account_call_recordings**](docs/RecordingsApi.md#list_account_call_recordings) | **GET** /accounts/{accountId}/recordings | Get Call Recordings
*RecordingsApi* | [**list_call_recordings**](docs/RecordingsApi.md#list_call_recordings) | **GET** /accounts/{accountId}/calls/{callId}/recordings | List Call Recordings
*RecordingsApi* | [**transcribe_call_recording**](docs/RecordingsApi.md#transcribe_call_recording) | **POST** /accounts/{accountId}/calls/{callId}/recordings/{recordingId}/transcription | Create Transcription Request
*RecordingsApi* | [**update_call_recording_state**](docs/RecordingsApi.md#update_call_recording_state) | **PUT** /accounts/{accountId}/calls/{callId}/recording | Update Recording
*SessionsApi* | [**add_participant_to_session**](docs/SessionsApi.md#add_participant_to_session) | **PUT** /accounts/{accountId}/sessions/{sessionId}/participants/{participantId} | Add Participant to Session
*SessionsApi* | [**create_session**](docs/SessionsApi.md#create_session) | **POST** /accounts/{accountId}/sessions | Create Session
*SessionsApi* | [**delete_session**](docs/SessionsApi.md#delete_session) | **DELETE** /accounts/{accountId}/sessions/{sessionId} | Delete Session
*SessionsApi* | [**get_participant_subscriptions**](docs/SessionsApi.md#get_participant_subscriptions) | **GET** /accounts/{accountId}/sessions/{sessionId}/participants/{participantId}/subscriptions | Get Participant Subscriptions
*SessionsApi* | [**get_session**](docs/SessionsApi.md#get_session) | **GET** /accounts/{accountId}/sessions/{sessionId} | Get Session
*SessionsApi* | [**list_session_participants**](docs/SessionsApi.md#list_session_participants) | **GET** /accounts/{accountId}/sessions/{sessionId}/participants | List Participants in Session
*SessionsApi* | [**remove_participant_from_session**](docs/SessionsApi.md#remove_participant_from_session) | **DELETE** /accounts/{accountId}/sessions/{sessionId}/participants/{participantId} | Remove Participant from Session
*SessionsApi* | [**update_participant_subscriptions**](docs/SessionsApi.md#update_participant_subscriptions) | **PUT** /accounts/{accountId}/sessions/{sessionId}/participants/{participantId}/subscriptions | Update Participant Subscriptions
*StatisticsApi* | [**get_statistics**](docs/StatisticsApi.md#get_statistics) | **GET** /accounts/{accountId}/statistics | Get Account Statistics


## Documentation For Models

 - [AccountStatistics](docs/AccountStatistics.md)
 - [AnswerCallback](docs/AnswerCallback.md)
 - [BridgeCompleteCallback](docs/BridgeCompleteCallback.md)
 - [BridgeTargetCompleteCallback](docs/BridgeTargetCompleteCallback.md)
 - [CallDirectionEnum](docs/CallDirectionEnum.md)
 - [CallRecordingMetadata](docs/CallRecordingMetadata.md)
 - [CallState](docs/CallState.md)
 - [CallStateEnum](docs/CallStateEnum.md)
 - [CallbackMethodEnum](docs/CallbackMethodEnum.md)
 - [CodeRequest](docs/CodeRequest.md)
 - [Conference](docs/Conference.md)
 - [ConferenceCompletedCallback](docs/ConferenceCompletedCallback.md)
 - [ConferenceCreatedCallback](docs/ConferenceCreatedCallback.md)
 - [ConferenceMember](docs/ConferenceMember.md)
 - [ConferenceMemberExitCallback](docs/ConferenceMemberExitCallback.md)
 - [ConferenceMemberJoinCallback](docs/ConferenceMemberJoinCallback.md)
 - [ConferenceRecordingAvailableCallback](docs/ConferenceRecordingAvailableCallback.md)
 - [ConferenceRecordingMetadata](docs/ConferenceRecordingMetadata.md)
 - [ConferenceRedirectCallback](docs/ConferenceRedirectCallback.md)
 - [ConferenceStateEnum](docs/ConferenceStateEnum.md)
 - [CreateCall](docs/CreateCall.md)
 - [CreateCallResponse](docs/CreateCallResponse.md)
 - [CreateLookupResponse](docs/CreateLookupResponse.md)
 - [CreateMessageRequestError](docs/CreateMessageRequestError.md)
 - [CreateParticipantRequest](docs/CreateParticipantRequest.md)
 - [CreateParticipantResponse](docs/CreateParticipantResponse.md)
 - [DeferredResult](docs/DeferredResult.md)
 - [DeviceApiVersionEnum](docs/DeviceApiVersionEnum.md)
 - [DisconenctCallback](docs/DisconenctCallback.md)
 - [Diversion](docs/Diversion.md)
 - [DtmfCallback](docs/DtmfCallback.md)
 - [FieldError](docs/FieldError.md)
 - [FileFormatEnum](docs/FileFormatEnum.md)
 - [ForbiddenRequest](docs/ForbiddenRequest.md)
 - [GatherCallback](docs/GatherCallback.md)
 - [InitiateCallback](docs/InitiateCallback.md)
 - [ListMessageDirectionEnum](docs/ListMessageDirectionEnum.md)
 - [ListMessageItem](docs/ListMessageItem.md)
 - [LookupRequest](docs/LookupRequest.md)
 - [LookupResult](docs/LookupResult.md)
 - [LookupStatus](docs/LookupStatus.md)
 - [LookupStatusEnum](docs/LookupStatusEnum.md)
 - [MachineDetectionCompleteCallback](docs/MachineDetectionCompleteCallback.md)
 - [MachineDetectionConfiguration](docs/MachineDetectionConfiguration.md)
 - [MachineDetectionModeEnum](docs/MachineDetectionModeEnum.md)
 - [Media](docs/Media.md)
 - [Message](docs/Message.md)
 - [MessageDirectionEnum](docs/MessageDirectionEnum.md)
 - [MessageRequest](docs/MessageRequest.md)
 - [MessageStatusEnum](docs/MessageStatusEnum.md)
 - [MessageTypeEnum](docs/MessageTypeEnum.md)
 - [MessagesList](docs/MessagesList.md)
 - [MessagingCodeResponse](docs/MessagingCodeResponse.md)
 - [MessagingRequestError](docs/MessagingRequestError.md)
 - [MfaForbiddenRequestError](docs/MfaForbiddenRequestError.md)
 - [MfaRequestError](docs/MfaRequestError.md)
 - [MfaUnauthorizedRequestError](docs/MfaUnauthorizedRequestError.md)
 - [PageInfo](docs/PageInfo.md)
 - [Participant](docs/Participant.md)
 - [ParticipantSubscription](docs/ParticipantSubscription.md)
 - [Password](docs/Password.md)
 - [PriorityEnum](docs/PriorityEnum.md)
 - [PublishPermissionsEnum](docs/PublishPermissionsEnum.md)
 - [RecordingAvailableCallback](docs/RecordingAvailableCallback.md)
 - [RecordingCompleteCallback](docs/RecordingCompleteCallback.md)
 - [RecordingStateEnum](docs/RecordingStateEnum.md)
 - [RedirectCallback](docs/RedirectCallback.md)
 - [RedirectMethodEnum](docs/RedirectMethodEnum.md)
 - [RequestError](docs/RequestError.md)
 - [Session](docs/Session.md)
 - [StirShaken](docs/StirShaken.md)
 - [Subscriptions](docs/Subscriptions.md)
 - [Tag](docs/Tag.md)
 - [TnLookupRequestError](docs/TnLookupRequestError.md)
 - [TranscribeRecording](docs/TranscribeRecording.md)
 - [Transcription](docs/Transcription.md)
 - [TranscriptionAvailableCallback](docs/TranscriptionAvailableCallback.md)
 - [TranscriptionList](docs/TranscriptionList.md)
 - [TranscriptionMetadata](docs/TranscriptionMetadata.md)
 - [TransferAnswerCallback](docs/TransferAnswerCallback.md)
 - [TransferCompleteCallback](docs/TransferCompleteCallback.md)
 - [TransferDisconnectCallback](docs/TransferDisconnectCallback.md)
 - [UnauthorizedRequest](docs/UnauthorizedRequest.md)
 - [UpdateCall](docs/UpdateCall.md)
 - [UpdateCallRecording](docs/UpdateCallRecording.md)
 - [UpdateConference](docs/UpdateConference.md)
 - [UpdateConferenceMember](docs/UpdateConferenceMember.md)
 - [Username](docs/Username.md)
 - [VerifyCodeRequest](docs/VerifyCodeRequest.md)
 - [VerifyCodeResponse](docs/VerifyCodeResponse.md)
 - [VoiceApiError](docs/VoiceApiError.md)
 - [VoiceCodeResponse](docs/VoiceCodeResponse.md)


## Documentation For Authorization


## Basic

- **Type**: HTTP basic authentication


## Author

letstalk@bandwidth.com


## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in bandwidth.apis and bandwidth.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from bandwidth.api.default_api import DefaultApi`
- `from bandwidth.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import bandwidth
from bandwidth.apis import *
from bandwidth.models import *
```

