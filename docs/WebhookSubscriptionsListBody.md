# WebhookSubscriptionsListBody

A list of all webhook subscriptions registered for this account ID for this particular feature (unpaginated).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**LinksObject**](LinksObject.md) |  | [optional] 
**errors** | [**List[Error]**](Error.md) |  | [optional] 
**data** | [**List[WebhookSubscription]**](WebhookSubscription.md) |  | 

## Example

```python
from bandwidth.models.webhook_subscriptions_list_body import WebhookSubscriptionsListBody

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSubscriptionsListBody from a JSON string
webhook_subscriptions_list_body_instance = WebhookSubscriptionsListBody.from_json(json)
# print the JSON string representation of the object
print(WebhookSubscriptionsListBody.to_json())

# convert the object into a dict
webhook_subscriptions_list_body_dict = webhook_subscriptions_list_body_instance.to_dict()
# create an instance of WebhookSubscriptionsListBody from a dict
webhook_subscriptions_list_body_from_dict = WebhookSubscriptionsListBody.from_dict(webhook_subscriptions_list_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


