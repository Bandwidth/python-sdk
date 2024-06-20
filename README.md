# bandwidth-sdk
Bandwidth's Communication APIs

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 15.0.0
- Generator version: 7.6.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://dev.bandwidth.com](https://dev.bandwidth.com)

## Requirements.

Python 3.7+

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

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import bandwidth
from bandwidth.rest import ApiException
from pprint import pprint

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
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)


# Enter a context with an instance of the API client
with bandwidth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bandwidth.CallsApi(api_client)
    account_id = '9900000' # str | Your Bandwidth Account ID.
    create_call = bandwidth.CreateCall() # CreateCall | JSON object containing information to create an outbound call

    try:
        # Create Call
        api_response = api_instance.create_call(account_id, create_call)
        print("The response of CallsApi->create_call:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CallsApi->create_call: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CallsApi* | [**create_call**](docs/CallsApi.md#create_call) | **POST** /accounts/{accountId}/calls | Create Call
*CallsApi* | [**get_call_state**](docs/CallsApi.md#get_call_state) | **GET** /accounts/{accountId}/calls/{callId} | Get Call State Information
*CallsApi* | [**list_calls**](docs/CallsApi.md#list_calls) | **GET** /accounts/{accountId}/calls | Get Calls
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
*PhoneNumberLookupApi* | [**create_lookup**](docs/PhoneNumberLookupApi.md#create_lookup) | **POST** /accounts/{accountId}/tnlookup | Create Lookup
*PhoneNumberLookupApi* | [**get_lookup_status**](docs/PhoneNumberLookupApi.md#get_lookup_status) | **GET** /accounts/{accountId}/tnlookup/{requestId} | Get Lookup Request Status
*RecordingsApi* | [**delete_recording**](docs/RecordingsApi.md#delete_recording) | **DELETE** /accounts/{accountId}/calls/{callId}/recordings/{recordingId} | Delete Recording
*RecordingsApi* | [**delete_recording_media**](docs/RecordingsApi.md#delete_recording_media) | **DELETE** /accounts/{accountId}/calls/{callId}/recordings/{recordingId}/media | Delete Recording Media
*RecordingsApi* | [**delete_recording_transcription**](docs/RecordingsApi.md#delete_recording_transcription) | **DELETE** /accounts/{accountId}/calls/{callId}/recordings/{recordingId}/transcription | Delete Transcription
*RecordingsApi* | [**download_call_recording**](docs/RecordingsApi.md#download_call_recording) | **GET** /accounts/{accountId}/calls/{callId}/recordings/{recordingId}/media | Download Recording
*RecordingsApi* | [**get_call_recording**](docs/RecordingsApi.md#get_call_recording) | **GET** /accounts/{accountId}/calls/{callId}/recordings/{recordingId} | Get Call Recording
*RecordingsApi* | [**get_recording_transcription**](docs/RecordingsApi.md#get_recording_transcription) | **GET** /accounts/{accountId}/calls/{callId}/recordings/{recordingId}/transcription | Get Transcription
*RecordingsApi* | [**list_account_call_recordings**](docs/RecordingsApi.md#list_account_call_recordings) | **GET** /accounts/{accountId}/recordings | Get Call Recordings
*RecordingsApi* | [**list_call_recordings**](docs/RecordingsApi.md#list_call_recordings) | **GET** /accounts/{accountId}/calls/{callId}/recordings | List Call Recordings
*RecordingsApi* | [**transcribe_call_recording**](docs/RecordingsApi.md#transcribe_call_recording) | **POST** /accounts/{accountId}/calls/{callId}/recordings/{recordingId}/transcription | Create Transcription Request
*RecordingsApi* | [**update_call_recording_state**](docs/RecordingsApi.md#update_call_recording_state) | **PUT** /accounts/{accountId}/calls/{callId}/recording | Update Recording
*StatisticsApi* | [**get_statistics**](docs/StatisticsApi.md#get_statistics) | **GET** /accounts/{accountId}/statistics | Get Account Statistics
*TranscriptionsApi* | [**delete_real_time_transcription**](docs/TranscriptionsApi.md#delete_real_time_transcription) | **DELETE** /accounts/{accountId}/calls/{callId}/transcriptions/{transcriptionId} | Delete a specific transcription
*TranscriptionsApi* | [**get_real_time_transcription**](docs/TranscriptionsApi.md#get_real_time_transcription) | **GET** /accounts/{accountId}/calls/{callId}/transcriptions/{transcriptionId} | Retrieve a specific transcription
*TranscriptionsApi* | [**list_real_time_transcriptions**](docs/TranscriptionsApi.md#list_real_time_transcriptions) | **GET** /accounts/{accountId}/calls/{callId}/transcriptions | Enumerate transcriptions made with StartTranscription


## Documentation For Models

 - [AccountStatistics](docs/AccountStatistics.md)
 - [AnswerCallback](docs/AnswerCallback.md)
 - [BridgeCompleteCallback](docs/BridgeCompleteCallback.md)
 - [BridgeTargetCompleteCallback](docs/BridgeTargetCompleteCallback.md)
 - [CallDirectionEnum](docs/CallDirectionEnum.md)
 - [CallRecordingMetadata](docs/CallRecordingMetadata.md)
 - [CallState](docs/CallState.md)
 - [CallStateEnum](docs/CallStateEnum.md)
 - [CallTranscription](docs/CallTranscription.md)
 - [CallTranscriptionMetadata](docs/CallTranscriptionMetadata.md)
 - [CallTranscriptionResponse](docs/CallTranscriptionResponse.md)
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
 - [DeferredResult](docs/DeferredResult.md)
 - [DisconnectCallback](docs/DisconnectCallback.md)
 - [Diversion](docs/Diversion.md)
 - [DtmfCallback](docs/DtmfCallback.md)
 - [FieldError](docs/FieldError.md)
 - [FileFormatEnum](docs/FileFormatEnum.md)
 - [GatherCallback](docs/GatherCallback.md)
 - [InboundMessageCallback](docs/InboundMessageCallback.md)
 - [InboundMessageCallbackMessage](docs/InboundMessageCallbackMessage.md)
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
 - [MachineDetectionResult](docs/MachineDetectionResult.md)
 - [Media](docs/Media.md)
 - [Message](docs/Message.md)
 - [MessageDeliveredCallback](docs/MessageDeliveredCallback.md)
 - [MessageDeliveredCallbackMessage](docs/MessageDeliveredCallbackMessage.md)
 - [MessageDirectionEnum](docs/MessageDirectionEnum.md)
 - [MessageFailedCallback](docs/MessageFailedCallback.md)
 - [MessageFailedCallbackMessage](docs/MessageFailedCallbackMessage.md)
 - [MessageRequest](docs/MessageRequest.md)
 - [MessageSendingCallback](docs/MessageSendingCallback.md)
 - [MessageSendingCallbackMessage](docs/MessageSendingCallbackMessage.md)
 - [MessageStatusEnum](docs/MessageStatusEnum.md)
 - [MessageTypeEnum](docs/MessageTypeEnum.md)
 - [MessagesList](docs/MessagesList.md)
 - [MessagingCodeResponse](docs/MessagingCodeResponse.md)
 - [MessagingRequestError](docs/MessagingRequestError.md)
 - [MfaForbiddenRequestError](docs/MfaForbiddenRequestError.md)
 - [MfaRequestError](docs/MfaRequestError.md)
 - [MfaUnauthorizedRequestError](docs/MfaUnauthorizedRequestError.md)
 - [PageInfo](docs/PageInfo.md)
 - [PriorityEnum](docs/PriorityEnum.md)
 - [RecordingAvailableCallback](docs/RecordingAvailableCallback.md)
 - [RecordingCompleteCallback](docs/RecordingCompleteCallback.md)
 - [RecordingStateEnum](docs/RecordingStateEnum.md)
 - [RecordingTranscriptionMetadata](docs/RecordingTranscriptionMetadata.md)
 - [RecordingTranscriptions](docs/RecordingTranscriptions.md)
 - [RedirectCallback](docs/RedirectCallback.md)
 - [RedirectMethodEnum](docs/RedirectMethodEnum.md)
 - [StirShaken](docs/StirShaken.md)
 - [Tag](docs/Tag.md)
 - [TnLookupRequestError](docs/TnLookupRequestError.md)
 - [TranscribeRecording](docs/TranscribeRecording.md)
 - [Transcription](docs/Transcription.md)
 - [TranscriptionAvailableCallback](docs/TranscriptionAvailableCallback.md)
 - [TransferAnswerCallback](docs/TransferAnswerCallback.md)
 - [TransferCompleteCallback](docs/TransferCompleteCallback.md)
 - [TransferDisconnectCallback](docs/TransferDisconnectCallback.md)
 - [UpdateCall](docs/UpdateCall.md)
 - [UpdateCallRecording](docs/UpdateCallRecording.md)
 - [UpdateConference](docs/UpdateConference.md)
 - [UpdateConferenceMember](docs/UpdateConferenceMember.md)
 - [VerifyCodeRequest](docs/VerifyCodeRequest.md)
 - [VerifyCodeResponse](docs/VerifyCodeResponse.md)
 - [VoiceApiError](docs/VoiceApiError.md)
 - [VoiceCodeResponse](docs/VoiceCodeResponse.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="Basic"></a>
### Basic

- **Type**: HTTP basic authentication


## Author

letstalk@bandwidth.com


