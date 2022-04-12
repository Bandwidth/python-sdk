# bandwidth.MFAApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**messaging_two_factor**](MFAApi.md#messaging_two_factor) | **POST** /accounts/{accountId}/code/messaging | Messaging Authentication
[**verify_two_factor**](MFAApi.md#verify_two_factor) | **POST** /accounts/{accountId}/code/verify | Verify Authentication Code
[**voice_two_factor**](MFAApi.md#voice_two_factor) | **POST** /accounts/{accountId}/code/voice | Voice Authentication


# **messaging_two_factor**
> TwoFactorMessagingResponse messaging_two_factor(account_id, two_factor_code_request_schema)

Messaging Authentication

Multi-Factor authentication with Bandwidth Messaging services. Allows a user to send an MFA code via a text message (SMS).

### Example

* Basic Authentication (httpBasic):

```python
import time
import bandwidth
from bandwidth.api import mfa_api
from bandwidth.model.two_factor_messaging_response import TwoFactorMessagingResponse
from bandwidth.model.unauthorized_request import UnauthorizedRequest
from bandwidth.model.error_with_request import ErrorWithRequest
from bandwidth.model.forbidden_request import ForbiddenRequest
from bandwidth.model.two_factor_code_request_schema import TwoFactorCodeRequestSchema
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

# Configure HTTP basic authorization: httpBasic
configuration = bandwidth.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with bandwidth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mfa_api.MFAApi(api_client)
    account_id = "accountId_example" # str | Bandwidth Account ID with Messaging service enabled
    two_factor_code_request_schema = TwoFactorCodeRequestSchema(
        to="to_example",
        _from="_from_example",
        application_id="application_id_example",
        scope="scope_example",
        message="message_example",
        digits=3.14,
    ) # TwoFactorCodeRequestSchema | 

    # example passing only required values which don't have defaults set
    try:
        # Messaging Authentication
        api_response = api_instance.messaging_two_factor(account_id, two_factor_code_request_schema)
        pprint(api_response)
    except bandwidth.ApiException as e:
        print("Exception when calling MFAApi->messaging_two_factor: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Bandwidth Account ID with Messaging service enabled |
 **two_factor_code_request_schema** | [**TwoFactorCodeRequestSchema**](TwoFactorCodeRequestSchema.md)|  |

### Return type

[**TwoFactorMessagingResponse**](TwoFactorMessagingResponse.md)

### Authorization

[httpBasic](../README.md#httpBasic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | If there is any issue with values passed in by the user |  -  |
**401** | Authentication is either incorrect or not present |  -  |
**403** | The user is not authorized to access this resource |  -  |
**500** | An internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_two_factor**
> TwoFactorVerifyCodeResponse verify_two_factor(account_id, two_factor_verify_request_schema)

Verify Authentication Code

Allows a user to verify an MFA code.

### Example

* Basic Authentication (httpBasic):

```python
import time
import bandwidth
from bandwidth.api import mfa_api
from bandwidth.model.two_factor_verify_request_schema import TwoFactorVerifyRequestSchema
from bandwidth.model.unauthorized_request import UnauthorizedRequest
from bandwidth.model.error_with_request import ErrorWithRequest
from bandwidth.model.forbidden_request import ForbiddenRequest
from bandwidth.model.two_factor_verify_code_response import TwoFactorVerifyCodeResponse
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

# Configure HTTP basic authorization: httpBasic
configuration = bandwidth.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with bandwidth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mfa_api.MFAApi(api_client)
    account_id = "accountId_example" # str | Bandwidth Account ID with Two-Factor enabled
    two_factor_verify_request_schema = TwoFactorVerifyRequestSchema(
        to="to_example",
        application_id="application_id_example",
        scope="scope_example",
        expiration_time_in_minutes=3.14,
        code="code_example",
    ) # TwoFactorVerifyRequestSchema | 

    # example passing only required values which don't have defaults set
    try:
        # Verify Authentication Code
        api_response = api_instance.verify_two_factor(account_id, two_factor_verify_request_schema)
        pprint(api_response)
    except bandwidth.ApiException as e:
        print("Exception when calling MFAApi->verify_two_factor: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Bandwidth Account ID with Two-Factor enabled |
 **two_factor_verify_request_schema** | [**TwoFactorVerifyRequestSchema**](TwoFactorVerifyRequestSchema.md)|  |

### Return type

[**TwoFactorVerifyCodeResponse**](TwoFactorVerifyCodeResponse.md)

### Authorization

[httpBasic](../README.md#httpBasic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | If there is any issue with values passed in by the user |  -  |
**401** | Authentication is either incorrect or not present |  -  |
**403** | The user is not authorized to access this resource |  -  |
**429** | The user has made too many bad requests and is temporarily locked out |  -  |
**500** | An internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **voice_two_factor**
> TwoFactorVoiceResponse voice_two_factor(account_id, two_factor_code_request_schema)

Voice Authentication

Multi-Factor authentication with Bandwidth Voice services. Allows for a user to send an MFA code via a phone call.

### Example

* Basic Authentication (httpBasic):

```python
import time
import bandwidth
from bandwidth.api import mfa_api
from bandwidth.model.unauthorized_request import UnauthorizedRequest
from bandwidth.model.error_with_request import ErrorWithRequest
from bandwidth.model.forbidden_request import ForbiddenRequest
from bandwidth.model.two_factor_code_request_schema import TwoFactorCodeRequestSchema
from bandwidth.model.two_factor_voice_response import TwoFactorVoiceResponse
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

# Configure HTTP basic authorization: httpBasic
configuration = bandwidth.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with bandwidth.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mfa_api.MFAApi(api_client)
    account_id = "accountId_example" # str | Bandwidth Account ID with Voice service enabled
    two_factor_code_request_schema = TwoFactorCodeRequestSchema(
        to="to_example",
        _from="_from_example",
        application_id="application_id_example",
        scope="scope_example",
        message="message_example",
        digits=3.14,
    ) # TwoFactorCodeRequestSchema | 

    # example passing only required values which don't have defaults set
    try:
        # Voice Authentication
        api_response = api_instance.voice_two_factor(account_id, two_factor_code_request_schema)
        pprint(api_response)
    except bandwidth.ApiException as e:
        print("Exception when calling MFAApi->voice_two_factor: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Bandwidth Account ID with Voice service enabled |
 **two_factor_code_request_schema** | [**TwoFactorCodeRequestSchema**](TwoFactorCodeRequestSchema.md)|  |

### Return type

[**TwoFactorVoiceResponse**](TwoFactorVoiceResponse.md)

### Authorization

[httpBasic](../README.md#httpBasic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | If there is any issue with values passed in by the user |  -  |
**401** | Authentication is either incorrect or not present |  -  |
**403** | The user is not authorized to access this resource |  -  |
**500** | An internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

