# bandwidth.MFAApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_messaging_code**](MFAApi.md#generate_messaging_code) | **POST** /accounts/{accountId}/code/messaging | Messaging Authentication Code
[**generate_voice_code**](MFAApi.md#generate_voice_code) | **POST** /accounts/{accountId}/code/voice | Voice Authentication Code
[**verify_code**](MFAApi.md#verify_code) | **POST** /accounts/{accountId}/code/verify | Verify Authentication Code


# **generate_messaging_code**
> MessagingCodeResponse generate_messaging_code(account_id, code_request)

Messaging Authentication Code

Send an MFA code via text message (SMS).

### Example

* Basic Authentication (Basic):

```python
import time
import bandwidth
from bandwidth.api import mfa_api
from bandwidth.model.code_request import CodeRequest
from bandwidth.model.messaging_code_response import MessagingCodeResponse
from bandwidth.model.mfa_forbidden_request_error import MfaForbiddenRequestError
from bandwidth.model.mfa_request_error import MfaRequestError
from bandwidth.model.mfa_unauthorized_request_error import MfaUnauthorizedRequestError
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
    api_instance = mfa_api.MFAApi(api_client)
    account_id = "accountId_example" # str | Bandwidth Account ID with Voice service enabled.
    code_request = CodeRequest(
        to="+19195551234",
        _from="+19195554321",
        application_id="66fd98ae-ac8d-a00f-7fcd-ba3280aeb9b1",
        scope="2FA",
        message="Your temporary {NAME} {SCOPE} code is {CODE}",
        digits=6,
    ) # CodeRequest | MFA code request body.

    # example passing only required values which don't have defaults set
    try:
        # Messaging Authentication Code
        api_response = api_instance.generate_messaging_code(account_id, code_request)
        pprint(api_response)
    except bandwidth.ApiException as e:
        print("Exception when calling MFAApi->generate_messaging_code: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Bandwidth Account ID with Voice service enabled. |
 **code_request** | [**CodeRequest**](CodeRequest.md)| MFA code request body. |

### Return type

[**MessagingCodeResponse**](MessagingCodeResponse.md)

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

# **generate_voice_code**
> VoiceCodeResponse generate_voice_code(account_id, code_request)

Voice Authentication Code

Send an MFA Code via a phone call.

### Example

* Basic Authentication (Basic):

```python
import time
import bandwidth
from bandwidth.api import mfa_api
from bandwidth.model.code_request import CodeRequest
from bandwidth.model.mfa_forbidden_request_error import MfaForbiddenRequestError
from bandwidth.model.voice_code_response import VoiceCodeResponse
from bandwidth.model.mfa_request_error import MfaRequestError
from bandwidth.model.mfa_unauthorized_request_error import MfaUnauthorizedRequestError
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
    api_instance = mfa_api.MFAApi(api_client)
    account_id = "accountId_example" # str | Bandwidth Account ID with Voice service enabled.
    code_request = CodeRequest(
        to="+19195551234",
        _from="+19195554321",
        application_id="66fd98ae-ac8d-a00f-7fcd-ba3280aeb9b1",
        scope="2FA",
        message="Your temporary {NAME} {SCOPE} code is {CODE}",
        digits=6,
    ) # CodeRequest | MFA code request body.

    # example passing only required values which don't have defaults set
    try:
        # Voice Authentication Code
        api_response = api_instance.generate_voice_code(account_id, code_request)
        pprint(api_response)
    except bandwidth.ApiException as e:
        print("Exception when calling MFAApi->generate_voice_code: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Bandwidth Account ID with Voice service enabled. |
 **code_request** | [**CodeRequest**](CodeRequest.md)| MFA code request body. |

### Return type

[**VoiceCodeResponse**](VoiceCodeResponse.md)

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

# **verify_code**
> VerifyCodeResponse verify_code(account_id, verify_code_request)

Verify Authentication Code

Verify a previously sent MFA code.

### Example

* Basic Authentication (Basic):

```python
import time
import bandwidth
from bandwidth.api import mfa_api
from bandwidth.model.verify_code_response import VerifyCodeResponse
from bandwidth.model.verify_code_request import VerifyCodeRequest
from bandwidth.model.mfa_forbidden_request_error import MfaForbiddenRequestError
from bandwidth.model.mfa_request_error import MfaRequestError
from bandwidth.model.mfa_unauthorized_request_error import MfaUnauthorizedRequestError
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
    api_instance = mfa_api.MFAApi(api_client)
    account_id = "accountId_example" # str | Bandwidth Account ID with Voice service enabled.
    verify_code_request = VerifyCodeRequest(
        to="+19195551234",
        scope="2FA",
        expiration_time_in_minutes=3,
        code="123456",
    ) # VerifyCodeRequest | MFA code verify request body.

    # example passing only required values which don't have defaults set
    try:
        # Verify Authentication Code
        api_response = api_instance.verify_code(account_id, verify_code_request)
        pprint(api_response)
    except bandwidth.ApiException as e:
        print("Exception when calling MFAApi->verify_code: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Bandwidth Account ID with Voice service enabled. |
 **verify_code_request** | [**VerifyCodeRequest**](VerifyCodeRequest.md)| MFA code verify request body. |

### Return type

[**VerifyCodeResponse**](VerifyCodeResponse.md)

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
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

