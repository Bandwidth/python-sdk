# bandwidth.SessionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_participant_to_session**](SessionsApi.md#add_participant_to_session) | **PUT** /accounts/{accountId}/sessions/{sessionId}/participants/{participantId} | Add Participant to Session
[**create_session**](SessionsApi.md#create_session) | **POST** /accounts/{accountId}/sessions | Create Session
[**delete_session**](SessionsApi.md#delete_session) | **DELETE** /accounts/{accountId}/sessions/{sessionId} | Delete Session
[**get_participant_subscriptions**](SessionsApi.md#get_participant_subscriptions) | **GET** /accounts/{accountId}/sessions/{sessionId}/participants/{participantId}/subscriptions | Get Participant Subscriptions
[**get_session**](SessionsApi.md#get_session) | **GET** /accounts/{accountId}/sessions/{sessionId} | Get Session
[**list_session_participants**](SessionsApi.md#list_session_participants) | **GET** /accounts/{accountId}/sessions/{sessionId}/participants | List Participants in Session
[**remove_participant_from_session**](SessionsApi.md#remove_participant_from_session) | **DELETE** /accounts/{accountId}/sessions/{sessionId}/participants/{participantId} | Remove Participant from Session
[**update_participant_subscriptions**](SessionsApi.md#update_participant_subscriptions) | **PUT** /accounts/{accountId}/sessions/{sessionId}/participants/{participantId}/subscriptions | Update Participant Subscriptions


# **add_participant_to_session**
> add_participant_to_session(account_id, session_id, participant_id)

Add Participant to Session

Add a participant to a session.  Subscriptions can optionally be provided as part of this call. 

### Example

* Basic Authentication (Basic):

```python
import time
import bandwidth
from bandwidth.api import sessions_api
from bandwidth.model.request_error import RequestError
from bandwidth.model.unauthorized_request import UnauthorizedRequest
from bandwidth.model.forbidden_request import ForbiddenRequest
from bandwidth.model.subscriptions import Subscriptions
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
    api_instance = sessions_api.SessionsApi(api_client)
    account_id = "9900000" # str | Account ID
    session_id = "cb5054ee-a69b-41ac-9ab2-04d6370826b4" # str | Session ID
    participant_id = "62e0ecb9-0b1b-5115-aae4-4f36123d6bb1" # str | Participant ID
    subscriptions = Subscriptions(
        session_id="d8886aad-b956-4e1b-b2f4-d7c9f8162772",
        participants=[
            ParticipantSubscription(
                participant_id="568749d5-04d5-483d-adf5-deac7dd3d521",
                stream_aliases=["alias_1","alias_2"],
            ),
        ],
    ) # Subscriptions | The Body describes an optional set of subscriptions to apply to the participant.  Calling this endpoint with no/empty body will only add the participant to the session, and will not subscribe the Participant to any media.  The request body for this endpoint is OPTIONAL and provided as a convenience to avoid additional calls to the Update Participant Subscriptions endpoint. --- If a body is provided it will result in direct control over what Participants are subscribed to.    - if the participants Array is provided and not empty, that list of Participants will be subscribed To   - if the participants Array is missing or empty, and the sessionId is provided, the participant will be subscribed to the session, including all subsequent changes to the membership of the session   - if the sessionId and the participant Array are both missing or empty, no subscriptions will be created (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add Participant to Session
        api_instance.add_participant_to_session(account_id, session_id, participant_id)
    except bandwidth.ApiException as e:
        print("Exception when calling SessionsApi->add_participant_to_session: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add Participant to Session
        api_instance.add_participant_to_session(account_id, session_id, participant_id, subscriptions=subscriptions)
    except bandwidth.ApiException as e:
        print("Exception when calling SessionsApi->add_participant_to_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID |
 **session_id** | **str**| Session ID |
 **participant_id** | **str**| Participant ID |
 **subscriptions** | [**Subscriptions**](Subscriptions.md)| The Body describes an optional set of subscriptions to apply to the participant.  Calling this endpoint with no/empty body will only add the participant to the session, and will not subscribe the Participant to any media.  The request body for this endpoint is OPTIONAL and provided as a convenience to avoid additional calls to the Update Participant Subscriptions endpoint. --- If a body is provided it will result in direct control over what Participants are subscribed to.    - if the participants Array is provided and not empty, that list of Participants will be subscribed To   - if the participants Array is missing or empty, and the sessionId is provided, the participant will be subscribed to the session, including all subsequent changes to the membership of the session   - if the sessionId and the participant Array are both missing or empty, no subscriptions will be created | [optional]

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_session**
> Session create_session(account_id)

Create Session

Create a new session. Sessions are idempotent, so relevant parameters must be set in this function if desired.

### Example

* Basic Authentication (Basic):

```python
import time
import bandwidth
from bandwidth.api import sessions_api
from bandwidth.model.request_error import RequestError
from bandwidth.model.unauthorized_request import UnauthorizedRequest
from bandwidth.model.forbidden_request import ForbiddenRequest
from bandwidth.model.session import Session
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
    api_instance = sessions_api.SessionsApi(api_client)
    account_id = "9900000" # str | Account ID
    session = Session(
        id="75c21163-e110-41bc-bd76-1bb428ec85d5",
        tag="session1",
    ) # Session | Create session request body. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Session
        api_response = api_instance.create_session(account_id)
        pprint(api_response)
    except bandwidth.ApiException as e:
        print("Exception when calling SessionsApi->create_session: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Session
        api_response = api_instance.create_session(account_id, session=session)
        pprint(api_response)
    except bandwidth.ApiException as e:
        print("Exception when calling SessionsApi->create_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID |
 **session** | [**Session**](Session.md)| Create session request body. | [optional]

### Return type

[**Session**](Session.md)

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

# **delete_session**
> delete_session(account_id, session_id)

Delete Session

Delete session by ID.

### Example

* Basic Authentication (Basic):

```python
import time
import bandwidth
from bandwidth.api import sessions_api
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
    api_instance = sessions_api.SessionsApi(api_client)
    account_id = "9900000" # str | Account ID
    session_id = "cb5054ee-a69b-41ac-9ab2-04d6370826b4" # str | Session ID

    # example passing only required values which don't have defaults set
    try:
        # Delete Session
        api_instance.delete_session(account_id, session_id)
    except bandwidth.ApiException as e:
        print("Exception when calling SessionsApi->delete_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID |
 **session_id** | **str**| Session ID |

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

# **get_participant_subscriptions**
> Subscriptions get_participant_subscriptions(account_id, session_id, participant_id)

Get Participant Subscriptions

Get a participant's subscriptions.

### Example

* Basic Authentication (Basic):

```python
import time
import bandwidth
from bandwidth.api import sessions_api
from bandwidth.model.request_error import RequestError
from bandwidth.model.unauthorized_request import UnauthorizedRequest
from bandwidth.model.forbidden_request import ForbiddenRequest
from bandwidth.model.subscriptions import Subscriptions
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
    api_instance = sessions_api.SessionsApi(api_client)
    account_id = "9900000" # str | Account ID
    session_id = "cb5054ee-a69b-41ac-9ab2-04d6370826b4" # str | Session ID
    participant_id = "62e0ecb9-0b1b-5115-aae4-4f36123d6bb1" # str | Participant ID

    # example passing only required values which don't have defaults set
    try:
        # Get Participant Subscriptions
        api_response = api_instance.get_participant_subscriptions(account_id, session_id, participant_id)
        pprint(api_response)
    except bandwidth.ApiException as e:
        print("Exception when calling SessionsApi->get_participant_subscriptions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID |
 **session_id** | **str**| Session ID |
 **participant_id** | **str**| Participant ID |

### Return type

[**Subscriptions**](Subscriptions.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_session**
> Session get_session(account_id, session_id)

Get Session

Get session by ID.

### Example

* Basic Authentication (Basic):

```python
import time
import bandwidth
from bandwidth.api import sessions_api
from bandwidth.model.request_error import RequestError
from bandwidth.model.unauthorized_request import UnauthorizedRequest
from bandwidth.model.forbidden_request import ForbiddenRequest
from bandwidth.model.session import Session
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
    api_instance = sessions_api.SessionsApi(api_client)
    account_id = "9900000" # str | Account ID
    session_id = "cb5054ee-a69b-41ac-9ab2-04d6370826b4" # str | Session ID

    # example passing only required values which don't have defaults set
    try:
        # Get Session
        api_response = api_instance.get_session(account_id, session_id)
        pprint(api_response)
    except bandwidth.ApiException as e:
        print("Exception when calling SessionsApi->get_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID |
 **session_id** | **str**| Session ID |

### Return type

[**Session**](Session.md)

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

# **list_session_participants**
> [Participant] list_session_participants(account_id, session_id)

List Participants in Session

List participants in a session.

### Example

* Basic Authentication (Basic):

```python
import time
import bandwidth
from bandwidth.api import sessions_api
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
    api_instance = sessions_api.SessionsApi(api_client)
    account_id = "9900000" # str | Account ID
    session_id = "cb5054ee-a69b-41ac-9ab2-04d6370826b4" # str | Session ID

    # example passing only required values which don't have defaults set
    try:
        # List Participants in Session
        api_response = api_instance.list_session_participants(account_id, session_id)
        pprint(api_response)
    except bandwidth.ApiException as e:
        print("Exception when calling SessionsApi->list_session_participants: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID |
 **session_id** | **str**| Session ID |

### Return type

[**[Participant]**](Participant.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_participant_from_session**
> remove_participant_from_session(account_id, session_id, participant_id)

Remove Participant from Session

Remove a participant from a session. This will automatically remove any subscriptions the participant has associated with this session.

### Example

* Basic Authentication (Basic):

```python
import time
import bandwidth
from bandwidth.api import sessions_api
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
    api_instance = sessions_api.SessionsApi(api_client)
    account_id = "9900000" # str | Account ID
    session_id = "cb5054ee-a69b-41ac-9ab2-04d6370826b4" # str | Session ID
    participant_id = "62e0ecb9-0b1b-5115-aae4-4f36123d6bb1" # str | Participant ID

    # example passing only required values which don't have defaults set
    try:
        # Remove Participant from Session
        api_instance.remove_participant_from_session(account_id, session_id, participant_id)
    except bandwidth.ApiException as e:
        print("Exception when calling SessionsApi->remove_participant_from_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID |
 **session_id** | **str**| Session ID |
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

# **update_participant_subscriptions**
> update_participant_subscriptions(account_id, session_id, participant_id)

Update Participant Subscriptions

Update a participant's subscriptions. This is a full update that will replace the participant's subscriptions. It allows subscription to the entire Session, a subset list of Participants in that Session, or specific media streams on any of the listed Participants. First call `getParticipantSubscriptions` if you need the current subscriptions. Calling this API with no `Subscriptions` object to remove all subscriptions.

### Example

* Basic Authentication (Basic):

```python
import time
import bandwidth
from bandwidth.api import sessions_api
from bandwidth.model.request_error import RequestError
from bandwidth.model.unauthorized_request import UnauthorizedRequest
from bandwidth.model.forbidden_request import ForbiddenRequest
from bandwidth.model.subscriptions import Subscriptions
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
    api_instance = sessions_api.SessionsApi(api_client)
    account_id = "9900000" # str | Account ID
    session_id = "cb5054ee-a69b-41ac-9ab2-04d6370826b4" # str | Session ID
    participant_id = "62e0ecb9-0b1b-5115-aae4-4f36123d6bb1" # str | Participant ID
    subscriptions = Subscriptions(
        session_id="d8886aad-b956-4e1b-b2f4-d7c9f8162772",
        participants=[
            ParticipantSubscription(
                participant_id="568749d5-04d5-483d-adf5-deac7dd3d521",
                stream_aliases=["alias_1","alias_2"],
            ),
        ],
    ) # Subscriptions | The body describes the desired subscriptions for the Participant. --- If a body is provided it will result in direct control over what Participants are subscribed to.    - if the participants Array is provided and not empty, that list of Participants will be subscribed To   - if the participants Array is missing or empty, and the sessionId is provided, the participant will be subscribed to the session, including all subsequent changes to the membership of the session   - if the sessionId and the participant Array are both missing or empty, no subscriptions will be created (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Participant Subscriptions
        api_instance.update_participant_subscriptions(account_id, session_id, participant_id)
    except bandwidth.ApiException as e:
        print("Exception when calling SessionsApi->update_participant_subscriptions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Participant Subscriptions
        api_instance.update_participant_subscriptions(account_id, session_id, participant_id, subscriptions=subscriptions)
    except bandwidth.ApiException as e:
        print("Exception when calling SessionsApi->update_participant_subscriptions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account ID |
 **session_id** | **str**| Session ID |
 **participant_id** | **str**| Participant ID |
 **subscriptions** | [**Subscriptions**](Subscriptions.md)| The body describes the desired subscriptions for the Participant. --- If a body is provided it will result in direct control over what Participants are subscribed to.    - if the participants Array is provided and not empty, that list of Participants will be subscribed To   - if the participants Array is missing or empty, and the sessionId is provided, the participant will be subscribed to the session, including all subsequent changes to the membership of the session   - if the sessionId and the participant Array are both missing or empty, no subscriptions will be created | [optional]

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
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

