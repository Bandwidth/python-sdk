# MessagingRequestError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**description** | **str** |  | 

## Example

```python
from bandwidth.models.messaging_request_error import MessagingRequestError

# TODO update the JSON string below
json = "{}"
# create an instance of MessagingRequestError from a JSON string
messaging_request_error_instance = MessagingRequestError.from_json(json)
# print the JSON string representation of the object
print(MessagingRequestError.to_json())

# convert the object into a dict
messaging_request_error_dict = messaging_request_error_instance.to_dict()
# create an instance of MessagingRequestError from a dict
messaging_request_error_from_dict = MessagingRequestError.from_dict(messaging_request_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


