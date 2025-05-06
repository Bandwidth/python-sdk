# MultiChannelChannelListObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** | The sender ID of the message. This could be an alphanumeric sender ID. | 
**application_id** | **str** | The ID of the Application your from number or senderId is associated with in the Bandwidth Phone Number Dashboard. | 
**channel** | [**MultiChannelMessageChannelEnum**](MultiChannelMessageChannelEnum.md) |  | 
**content** | [**MultiChannelChannelListObjectContent**](MultiChannelChannelListObjectContent.md) |  | 

## Example

```python
from bandwidth.models.multi_channel_channel_list_object import MultiChannelChannelListObject

# TODO update the JSON string below
json = "{}"
# create an instance of MultiChannelChannelListObject from a JSON string
multi_channel_channel_list_object_instance = MultiChannelChannelListObject.from_json(json)
# print the JSON string representation of the object
print(MultiChannelChannelListObject.to_json())

# convert the object into a dict
multi_channel_channel_list_object_dict = multi_channel_channel_list_object_instance.to_dict()
# create an instance of MultiChannelChannelListObject from a dict
multi_channel_channel_list_object_from_dict = MultiChannelChannelListObject.from_dict(multi_channel_channel_list_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


