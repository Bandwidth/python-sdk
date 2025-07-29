# MultiChannelMessageResponseDataChannelListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** | The sender ID of the message. This could be an alphanumeric sender ID. | 
**application_id** | **str** | The ID of the Application your from number or senderId is associated with in the Bandwidth Phone Number Dashboard. | 
**channel** | [**MultiChannelMessageChannelEnum**](MultiChannelMessageChannelEnum.md) |  | 
**content** | [**MultiChannelChannelListObjectContent**](MultiChannelChannelListObjectContent.md) |  | 
**owner** | **str** | The Bandwidth senderId associated with the message. Identical to &#39;from&#39;. | 

## Example

```python
from bandwidth.models.multi_channel_message_response_data_channel_list_inner import MultiChannelMessageResponseDataChannelListInner

# TODO update the JSON string below
json = "{}"
# create an instance of MultiChannelMessageResponseDataChannelListInner from a JSON string
multi_channel_message_response_data_channel_list_inner_instance = MultiChannelMessageResponseDataChannelListInner.from_json(json)
# print the JSON string representation of the object
print(MultiChannelMessageResponseDataChannelListInner.to_json())

# convert the object into a dict
multi_channel_message_response_data_channel_list_inner_dict = multi_channel_message_response_data_channel_list_inner_instance.to_dict()
# create an instance of MultiChannelMessageResponseDataChannelListInner from a dict
multi_channel_message_response_data_channel_list_inner_from_dict = MultiChannelMessageResponseDataChannelListInner.from_dict(multi_channel_message_response_data_channel_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


