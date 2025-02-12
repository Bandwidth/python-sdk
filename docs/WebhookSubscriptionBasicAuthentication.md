# WebhookSubscriptionBasicAuthentication

Basic authentication credentials are not required, but if present, both username and password must be provided.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**password** | **str** |  | 

## Example

```python
from bandwidth.models.webhook_subscription_basic_authentication import WebhookSubscriptionBasicAuthentication

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSubscriptionBasicAuthentication from a JSON string
webhook_subscription_basic_authentication_instance = WebhookSubscriptionBasicAuthentication.from_json(json)
# print the JSON string representation of the object
print(WebhookSubscriptionBasicAuthentication.to_json())

# convert the object into a dict
webhook_subscription_basic_authentication_dict = webhook_subscription_basic_authentication_instance.to_dict()
# create an instance of WebhookSubscriptionBasicAuthentication from a dict
webhook_subscription_basic_authentication_from_dict = WebhookSubscriptionBasicAuthentication.from_dict(webhook_subscription_basic_authentication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


