# MultiChannelChannelListOwnerObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner** | **str** | The Bandwidth senderId associated with the message. Identical to &#39;from&#39;. | 

## Example

```python
from bandwidth.models.multi_channel_channel_list_owner_object import MultiChannelChannelListOwnerObject

# TODO update the JSON string below
json = "{}"
# create an instance of MultiChannelChannelListOwnerObject from a JSON string
multi_channel_channel_list_owner_object_instance = MultiChannelChannelListOwnerObject.from_json(json)
# print the JSON string representation of the object
print(MultiChannelChannelListOwnerObject.to_json())

# convert the object into a dict
multi_channel_channel_list_owner_object_dict = multi_channel_channel_list_owner_object_instance.to_dict()
# create an instance of MultiChannelChannelListOwnerObject from a dict
multi_channel_channel_list_owner_object_from_dict = MultiChannelChannelListOwnerObject.from_dict(multi_channel_channel_list_owner_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


