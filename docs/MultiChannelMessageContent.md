# MultiChannelMessageContent

The structure of the content field of a multichannel message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | [optional] 
**media** | [**RbmMessageContentFile**](RbmMessageContentFile.md) |  | [optional] 

## Example

```python
from bandwidth.models.multi_channel_message_content import MultiChannelMessageContent

# TODO update the JSON string below
json = "{}"
# create an instance of MultiChannelMessageContent from a JSON string
multi_channel_message_content_instance = MultiChannelMessageContent.from_json(json)
# print the JSON string representation of the object
print(MultiChannelMessageContent.to_json())

# convert the object into a dict
multi_channel_message_content_dict = multi_channel_message_content_instance.to_dict()
# create an instance of MultiChannelMessageContent from a dict
multi_channel_message_content_from_dict = MultiChannelMessageContent.from_dict(multi_channel_message_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


