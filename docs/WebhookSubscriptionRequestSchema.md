# WebhookSubscriptionRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basic_authentication** | [**TfvBasicAuthentication**](TfvBasicAuthentication.md) |  | [optional] 
**callback_url** | **str** | Callback URL to receive status updates from Bandwidth. When a webhook subscription is registered with Bandwidth under a given account ID, it will be used to send status updates for all requests submitted under that account ID. | 
**shared_secret_key** | **str** | An ASCII string submitted by the user as a shared secret key for generating an HMAC header for callbacks. | [optional] 

## Example

```python
from bandwidth.models.webhook_subscription_request_schema import WebhookSubscriptionRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSubscriptionRequestSchema from a JSON string
webhook_subscription_request_schema_instance = WebhookSubscriptionRequestSchema.from_json(json)
# print the JSON string representation of the object
print(WebhookSubscriptionRequestSchema.to_json())

# convert the object into a dict
webhook_subscription_request_schema_dict = webhook_subscription_request_schema_instance.to_dict()
# create an instance of WebhookSubscriptionRequestSchema from a dict
webhook_subscription_request_schema_from_dict = WebhookSubscriptionRequestSchema.from_dict(webhook_subscription_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


