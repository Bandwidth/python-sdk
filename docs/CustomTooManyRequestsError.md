# CustomTooManyRequestsError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**description** | **str** |  | 

## Example

```python
from bandwidth.models.custom_too_many_requests_error import CustomTooManyRequestsError

# TODO update the JSON string below
json = "{}"
# create an instance of CustomTooManyRequestsError from a JSON string
custom_too_many_requests_error_instance = CustomTooManyRequestsError.from_json(json)
# print the JSON string representation of the object
print(CustomTooManyRequestsError.to_json())

# convert the object into a dict
custom_too_many_requests_error_dict = custom_too_many_requests_error_instance.to_dict()
# create an instance of CustomTooManyRequestsError from a dict
custom_too_many_requests_error_from_dict = CustomTooManyRequestsError.from_dict(custom_too_many_requests_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


