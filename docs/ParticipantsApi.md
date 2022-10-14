# bandwidth.ParticipantsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_participant**](ParticipantsApi.md#create_participant) | **POST** /accounts/{accountId}/participants | Create Participant
[**delete_participant**](ParticipantsApi.md#delete_participant) | **DELETE** /accounts/{accountId}/participants/{participantId} | Delete Participant
[**get_participant**](ParticipantsApi.md#get_participant) | **GET** /accounts/{accountId}/participants/{participantId} | Get Participant


# **create_participant**
> CreateParticipantResponse create_participant(account_id)

Create Participant

Create a new participant under this account. Participants are idempotent, so relevant parameters must be set in this function if desired.

### Example

* Basic Authentication (Basic):

```python
import time
import bandwidth
from bandwidth.api import participants_api
from bandwidth.model.request_error import RequestError
from bandwidth.model.unauthorized_request import UnauthorizedRequest
from bandwidth.model.create_participant_request import CreateParticipantRequest
from bandwidth.model.forbidden_request import ForbiddenRequest
from bandwidth.model.create_participant_response import CreateParticipantResponse
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with bandwidth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = participants_api.ParticipantsApi(api_client)
    account_id = "9900000" # str | Account ID
    create_participant_request = CreateParticipantRequest(
        callback_url="https://example.com/callback",
        publish_permissions=[
            PublishPermissionsEnum("["VIDEO","AUDIO"]"),
        ],
        tag="participant1",
        device_api_version=DeviceApiVersionEnum("V3"),
    ) # CreateParticipantRequest | Create participant request body. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Participant
        api_response = api_instance.create_participant(account_id)
        pprint(api_response)
    except bandwidth.ApiException as e:
        print("Exception when calling ParticipantsApi->create_participant: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Participant
        api_response = api_instance.create_participant(account_id, create_participant_request=create_participant_request)
        pprint(api_response)
    except bandwidth.ApiException as e:
        print("Exception when calling ParticipantsApi->create_participant: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID |
 **create_participant_request** | [**CreateParticipantRequest**](CreateParticipantRequest.md)| Create participant request body. | [optional]

### Return type

[**CreateParticipantResponse**](CreateParticipantResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_participant**
> delete_participant(account_id, participant_id)

Delete Participant

Delete participant by ID.

### Example

* Basic Authentication (Basic):

```python
import time
import bandwidth
from bandwidth.api import participants_api
from bandwidth.model.request_error import RequestError
from bandwidth.model.unauthorized_request import UnauthorizedRequest
from bandwidth.model.forbidden_request import ForbiddenRequest
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with bandwidth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = participants_api.ParticipantsApi(api_client)
    account_id = "9900000" # str | Account ID
    participant_id = "62e0ecb9-0b1b-5115-aae4-4f36123d6bb1" # str | Participant ID

    # example passing only required values which don't have defaults set
    try:
        # Delete Participant
        api_instance.delete_participant(account_id, participant_id)
    except bandwidth.ApiException as e:
        print("Exception when calling ParticipantsApi->delete_participant: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID |
 **participant_id** | **str**| Participant ID |

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_participant**
> Participant get_participant(account_id, participant_id)

Get Participant

Get participant by ID.

### Example

* Basic Authentication (Basic):

```python
import time
import bandwidth
from bandwidth.api import participants_api
from bandwidth.model.request_error import RequestError
from bandwidth.model.unauthorized_request import UnauthorizedRequest
from bandwidth.model.participant import Participant
from bandwidth.model.forbidden_request import ForbiddenRequest
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with bandwidth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = participants_api.ParticipantsApi(api_client)
    account_id = "9900000" # str | Account ID
    participant_id = "62e0ecb9-0b1b-5115-aae4-4f36123d6bb1" # str | Participant ID

    # example passing only required values which don't have defaults set
    try:
        # Get Participant
        api_response = api_instance.get_participant(account_id, participant_id)
        pprint(api_response)
    except bandwidth.ApiException as e:
        print("Exception when calling ParticipantsApi->get_participant: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID |
 **participant_id** | **str**| Participant ID |

### Return type

[**Participant**](Participant.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
