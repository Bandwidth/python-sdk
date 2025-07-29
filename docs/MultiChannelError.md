# MultiChannelError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**List[Link]**](Link.md) |  | [optional] 
**data** | **object** |  | [optional] 
**errors** | [**List[ErrorObject]**](ErrorObject.md) |  | [optional] 

## Example

```python
from bandwidth.models.multi_channel_error import MultiChannelError

# TODO update the JSON string below
json = "{}"
# create an instance of MultiChannelError from a JSON string
multi_channel_error_instance = MultiChannelError.from_json(json)
# print the JSON string representation of the object
print(MultiChannelError.to_json())

# convert the object into a dict
multi_channel_error_dict = multi_channel_error_instance.to_dict()
# create an instance of MultiChannelError from a dict
multi_channel_error_from_dict = MultiChannelError.from_dict(multi_channel_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


