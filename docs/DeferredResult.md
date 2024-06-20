# DeferredResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **object** |  | [optional] 
**set_or_expired** | **bool** |  | [optional] 

## Example

```python
from bandwidth.models.deferred_result import DeferredResult

# TODO update the JSON string below
json = "{}"
# create an instance of DeferredResult from a JSON string
deferred_result_instance = DeferredResult.from_json(json)
# print the JSON string representation of the object
print(DeferredResult.to_json())

# convert the object into a dict
deferred_result_dict = deferred_result_instance.to_dict()
# create an instance of DeferredResult from a dict
deferred_result_from_dict = DeferredResult.from_dict(deferred_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


