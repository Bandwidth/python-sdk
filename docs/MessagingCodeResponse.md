# MessagingCodeResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** | Messaging API Message ID. | [optional] 

## Example

```python
from bandwidth.models.messaging_code_response import MessagingCodeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MessagingCodeResponse from a JSON string
messaging_code_response_instance = MessagingCodeResponse.from_json(json)
# print the JSON string representation of the object
print MessagingCodeResponse.to_json()

# convert the object into a dict
messaging_code_response_dict = messaging_code_response_instance.to_dict()
# create an instance of MessagingCodeResponse from a dict
messaging_code_response_form_dict = messaging_code_response.from_dict(messaging_code_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


