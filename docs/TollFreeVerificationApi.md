# bandwidth.TollFreeVerificationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_webhook_subscription**](TollFreeVerificationApi.md#create_webhook_subscription) | **POST** /accounts/{accountId}/tollFreeVerification/webhooks/subscriptions | Create Webhook Subscription
[**delete_verification_request**](TollFreeVerificationApi.md#delete_verification_request) | **DELETE** /accounts/{accountId}/phoneNumbers/{phoneNumber}/tollFreeVerification | Delete a Toll-Free Verification Submission
[**delete_webhook_subscription**](TollFreeVerificationApi.md#delete_webhook_subscription) | **DELETE** /accounts/{accountId}/tollFreeVerification/webhooks/subscriptions/{id} | Delete Webhook Subscription
[**get_toll_free_verification_status**](TollFreeVerificationApi.md#get_toll_free_verification_status) | **GET** /accounts/{accountId}/phoneNumbers/{phoneNumber}/tollFreeVerification | Get Toll-Free Verification Status
[**list_toll_free_use_cases**](TollFreeVerificationApi.md#list_toll_free_use_cases) | **GET** /tollFreeVerification/useCases | List Toll-Free Use Cases
[**list_webhook_subscriptions**](TollFreeVerificationApi.md#list_webhook_subscriptions) | **GET** /accounts/{accountId}/tollFreeVerification/webhooks/subscriptions | List Webhook Subscriptions
[**request_toll_free_verification**](TollFreeVerificationApi.md#request_toll_free_verification) | **POST** /accounts/{accountId}/tollFreeVerification | Request Toll-Free Verification
[**update_toll_free_verification_request**](TollFreeVerificationApi.md#update_toll_free_verification_request) | **PUT** /accounts/{accountId}/phoneNumbers/{phoneNumber}/tollFreeVerification | Update Toll-Free Verification Request
[**update_webhook_subscription**](TollFreeVerificationApi.md#update_webhook_subscription) | **PUT** /accounts/{accountId}/tollFreeVerification/webhooks/subscriptions/{id} | Update Webhook Subscription


# **create_webhook_subscription**
> WebhookSubscription create_webhook_subscription(account_id, webhook_subscription_request_schema)

Create Webhook Subscription

Create a new webhook subscription (this webhook will be called for every update on every submission).
In addition to a `callbackUrl`, this subscription can provide optional HTTP basic authentication credentials (a username and a password).
The returned subscription object will contain an ID that can be used to modify or delete the subscription at a later time.

### Example

* Basic Authentication (Basic):

```python
import bandwidth
from bandwidth.models.webhook_subscription import WebhookSubscription
from bandwidth.models.webhook_subscription_request_schema import WebhookSubscriptionRequestSchema
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
    api_instance = bandwidth.TollFreeVerificationApi(api_client)
    account_id = '9900000' # str | Your Bandwidth Account ID.
    webhook_subscription_request_schema = bandwidth.WebhookSubscriptionRequestSchema() # WebhookSubscriptionRequestSchema | Information about a webhook that Bandwidth should send upon the completion of event customer is trying to subscribe to.

    try:
        # Create Webhook Subscription
        api_response = api_instance.create_webhook_subscription(account_id, webhook_subscription_request_schema)
        print("The response of TollFreeVerificationApi->create_webhook_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TollFreeVerificationApi->create_webhook_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Your Bandwidth Account ID. | 
 **webhook_subscription_request_schema** | [**WebhookSubscriptionRequestSchema**](WebhookSubscriptionRequestSchema.md)| Information about a webhook that Bandwidth should send upon the completion of event customer is trying to subscribe to. | 

### Return type

[**WebhookSubscription**](WebhookSubscription.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Cannot find the requested resource. |  -  |
**405** | Method Not Allowed |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_verification_request**
> delete_verification_request(account_id, phone_number)

Delete a Toll-Free Verification Submission

Delete a toll-free verification submission for a toll-free number.

### Example

* Basic Authentication (Basic):

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
    api_instance = bandwidth.TollFreeVerificationApi(api_client)
    account_id = '9900000' # str | Your Bandwidth Account ID.
    phone_number = '+18885555555' # str | Valid Toll-Free telephone number in E.164 format.

    try:
        # Delete a Toll-Free Verification Submission
        api_instance.delete_verification_request(account_id, phone_number)
    except Exception as e:
        print("Exception when calling TollFreeVerificationApi->delete_verification_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Your Bandwidth Account ID. | 
 **phone_number** | **str**| Valid Toll-Free telephone number in E.164 format. | 

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
**404** | Cannot find the requested resource. |  -  |
**405** | Method Not Allowed |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webhook_subscription**
> delete_webhook_subscription(account_id, id)

Delete Webhook Subscription

Delete a webhook subscription by ID.

### Example

* Basic Authentication (Basic):

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
    api_instance = bandwidth.TollFreeVerificationApi(api_client)
    account_id = '9900000' # str | Your Bandwidth Account ID.
    id = '7bt57JcsVYJrN9K1OcV1Nu' # str | Webhook subscription ID

    try:
        # Delete Webhook Subscription
        api_instance.delete_webhook_subscription(account_id, id)
    except Exception as e:
        print("Exception when calling TollFreeVerificationApi->delete_webhook_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Your Bandwidth Account ID. | 
 **id** | **str**| Webhook subscription ID | 

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
**404** | Cannot find the requested resource. |  -  |
**405** | Method Not Allowed |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_toll_free_verification_status**
> TfvStatus get_toll_free_verification_status(account_id, phone_number)

Get Toll-Free Verification Status

Gets the verification status for a phone number that is provisioned to your account.
Submission information will be appended to the response if it is available.

### Example

* Basic Authentication (Basic):

```python
import bandwidth
from bandwidth.models.tfv_status import TfvStatus
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
    api_instance = bandwidth.TollFreeVerificationApi(api_client)
    account_id = '9900000' # str | Your Bandwidth Account ID.
    phone_number = '+18885555555' # str | Valid Toll-Free telephone number in E.164 format.

    try:
        # Get Toll-Free Verification Status
        api_response = api_instance.get_toll_free_verification_status(account_id, phone_number)
        print("The response of TollFreeVerificationApi->get_toll_free_verification_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TollFreeVerificationApi->get_toll_free_verification_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Your Bandwidth Account ID. | 
 **phone_number** | **str**| Valid Toll-Free telephone number in E.164 format. | 

### Return type

[**TfvStatus**](TfvStatus.md)

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
**404** | Cannot find the requested resource. |  -  |
**405** | Method Not Allowed |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_toll_free_use_cases**
> List[str] list_toll_free_use_cases()

List Toll-Free Use Cases

Lists valid toll-free use cases.

### Example

* Basic Authentication (Basic):

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
    api_instance = bandwidth.TollFreeVerificationApi(api_client)

    try:
        # List Toll-Free Use Cases
        api_response = api_instance.list_toll_free_use_cases()
        print("The response of TollFreeVerificationApi->list_toll_free_use_cases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TollFreeVerificationApi->list_toll_free_use_cases: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[str]**

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
**404** | Cannot find the requested resource. |  -  |
**405** | Method Not Allowed |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_webhook_subscriptions**
> WebhookSubscriptionsListBody list_webhook_subscriptions(account_id)

List Webhook Subscriptions

Lists all webhook subscriptions that are registered to receive status updates for the toll-free verification requests submitted under this account (password will not be returned through this API
If `basicAuthentication` is defined, the `password` property of that object will be null).

### Example

* Basic Authentication (Basic):

```python
import bandwidth
from bandwidth.models.webhook_subscriptions_list_body import WebhookSubscriptionsListBody
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
    api_instance = bandwidth.TollFreeVerificationApi(api_client)
    account_id = '9900000' # str | Your Bandwidth Account ID.

    try:
        # List Webhook Subscriptions
        api_response = api_instance.list_webhook_subscriptions(account_id)
        print("The response of TollFreeVerificationApi->list_webhook_subscriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TollFreeVerificationApi->list_webhook_subscriptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Your Bandwidth Account ID. | 

### Return type

[**WebhookSubscriptionsListBody**](WebhookSubscriptionsListBody.md)

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
**405** | Method Not Allowed |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_toll_free_verification**
> request_toll_free_verification(account_id, verification_request)

Request Toll-Free Verification

Submit a request for verification of a toll-free phone number.

### Example

* Basic Authentication (Basic):

```python
import bandwidth
from bandwidth.models.verification_request import VerificationRequest
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
    api_instance = bandwidth.TollFreeVerificationApi(api_client)
    account_id = '9900000' # str | Your Bandwidth Account ID.
    verification_request = bandwidth.VerificationRequest() # VerificationRequest | Request for verification of a toll-free phone number.

    try:
        # Request Toll-Free Verification
        api_instance.request_toll_free_verification(account_id, verification_request)
    except Exception as e:
        print("Exception when calling TollFreeVerificationApi->request_toll_free_verification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Your Bandwidth Account ID. | 
 **verification_request** | [**VerificationRequest**](VerificationRequest.md)| Request for verification of a toll-free phone number. | 

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
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**405** | Method Not Allowed |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_toll_free_verification_request**
> update_toll_free_verification_request(account_id, phone_number, tfv_submission_wrapper)

Update Toll-Free Verification Request

Updates a toll-free verification request.
Submissions are only eligible for resubmission for 7 days within being processed and if resubmission is allowed (resubmitAllowed field is true).

### Example

* Basic Authentication (Basic):

```python
import bandwidth
from bandwidth.models.tfv_submission_wrapper import TfvSubmissionWrapper
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
    api_instance = bandwidth.TollFreeVerificationApi(api_client)
    account_id = '9900000' # str | Your Bandwidth Account ID.
    phone_number = '+18885555555' # str | Valid Toll-Free telephone number in E.164 format.
    tfv_submission_wrapper = bandwidth.TfvSubmissionWrapper() # TfvSubmissionWrapper | Update a request for verification of a toll-free phone number.

    try:
        # Update Toll-Free Verification Request
        api_instance.update_toll_free_verification_request(account_id, phone_number, tfv_submission_wrapper)
    except Exception as e:
        print("Exception when calling TollFreeVerificationApi->update_toll_free_verification_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Your Bandwidth Account ID. | 
 **phone_number** | **str**| Valid Toll-Free telephone number in E.164 format. | 
 **tfv_submission_wrapper** | [**TfvSubmissionWrapper**](TfvSubmissionWrapper.md)| Update a request for verification of a toll-free phone number. | 

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
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**405** | Method Not Allowed |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webhook_subscription**
> WebhookSubscription update_webhook_subscription(account_id, id, webhook_subscription_request_schema)

Update Webhook Subscription

Update an existing webhook subscription (`callbackUrl` and `basicAuthentication` can be updated).

### Example

* Basic Authentication (Basic):

```python
import bandwidth
from bandwidth.models.webhook_subscription import WebhookSubscription
from bandwidth.models.webhook_subscription_request_schema import WebhookSubscriptionRequestSchema
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
    api_instance = bandwidth.TollFreeVerificationApi(api_client)
    account_id = '9900000' # str | Your Bandwidth Account ID.
    id = '7bt57JcsVYJrN9K1OcV1Nu' # str | Webhook subscription ID
    webhook_subscription_request_schema = bandwidth.WebhookSubscriptionRequestSchema() # WebhookSubscriptionRequestSchema | Information about a webhook that Bandwidth should send upon the completion of event customer is trying to subscribe to.

    try:
        # Update Webhook Subscription
        api_response = api_instance.update_webhook_subscription(account_id, id, webhook_subscription_request_schema)
        print("The response of TollFreeVerificationApi->update_webhook_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TollFreeVerificationApi->update_webhook_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Your Bandwidth Account ID. | 
 **id** | **str**| Webhook subscription ID | 
 **webhook_subscription_request_schema** | [**WebhookSubscriptionRequestSchema**](WebhookSubscriptionRequestSchema.md)| Information about a webhook that Bandwidth should send upon the completion of event customer is trying to subscribe to. | 

### Return type

[**WebhookSubscription**](WebhookSubscription.md)

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
**404** | Cannot find the requested resource. |  -  |
**405** | Method Not Allowed |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

