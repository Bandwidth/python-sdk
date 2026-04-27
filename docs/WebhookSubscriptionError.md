# WebhookSubscriptionError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**telephone_numbers** | [**List[TelephoneNumber]**](TelephoneNumber.md) |  | [optional] 

## Example

```python
from bandwidth.models.webhook_subscription_error import WebhookSubscriptionError

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSubscriptionError from a JSON string
webhook_subscription_error_instance = WebhookSubscriptionError.from_json(json)
# print the JSON string representation of the object
print(WebhookSubscriptionError.to_json())

# convert the object into a dict
webhook_subscription_error_dict = webhook_subscription_error_instance.to_dict()
# create an instance of WebhookSubscriptionError from a dict
webhook_subscription_error_from_dict = WebhookSubscriptionError.from_dict(webhook_subscription_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


