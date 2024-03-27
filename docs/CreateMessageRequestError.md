# CreateMessageRequestError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**description** | **str** |  | 
**field_errors** | [**List[FieldError]**](FieldError.md) |  | [optional] 

## Example

```python
from bandwidth.models.create_message_request_error import CreateMessageRequestError

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMessageRequestError from a JSON string
create_message_request_error_instance = CreateMessageRequestError.from_json(json)
# print the JSON string representation of the object
print(CreateMessageRequestError.to_json())

# convert the object into a dict
create_message_request_error_dict = create_message_request_error_instance.to_dict()
# create an instance of CreateMessageRequestError from a dict
create_message_request_error_form_dict = create_message_request_error.from_dict(create_message_request_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


