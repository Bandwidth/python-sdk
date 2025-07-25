# BlockedWebhook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | User&#39;s account ID. | [optional] 
**phone_number** | **str** | Toll-free telephone number in E.164 format. | [optional] 
**status** | [**TfvCallbackStatusEnum**](TfvCallbackStatusEnum.md) |  | [optional] 
**internal_ticket_number** | **str** | Unique identifier (UUID) generated by Bandwidth to assist in tracking the verification status of a toll-free number. | [optional] 
**blocked** | **bool** | Whether a Toll-Free Verification is blocked. This attribute will only be defined when the number is blocked. | [optional] 
**blocked_reason** | **str** | The reason why the Toll-Free Verification is blocked. This attribute will only be defined when the number is blocked. | [optional] 

## Example

```python
from bandwidth.models.blocked_webhook import BlockedWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of BlockedWebhook from a JSON string
blocked_webhook_instance = BlockedWebhook.from_json(json)
# print the JSON string representation of the object
print(BlockedWebhook.to_json())

# convert the object into a dict
blocked_webhook_dict = blocked_webhook_instance.to_dict()
# create an instance of BlockedWebhook from a dict
blocked_webhook_from_dict = BlockedWebhook.from_dict(blocked_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


