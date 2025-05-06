# SmsMessageContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | The contents of the text message. Must be 2048 characters or less. | 

## Example

```python
from bandwidth.models.sms_message_content import SmsMessageContent

# TODO update the JSON string below
json = "{}"
# create an instance of SmsMessageContent from a JSON string
sms_message_content_instance = SmsMessageContent.from_json(json)
# print the JSON string representation of the object
print(SmsMessageContent.to_json())

# convert the object into a dict
sms_message_content_dict = sms_message_content_instance.to_dict()
# create an instance of SmsMessageContent from a dict
sms_message_content_from_dict = SmsMessageContent.from_dict(sms_message_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


