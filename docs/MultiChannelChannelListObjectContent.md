# MultiChannelChannelListObjectContent

The content of the message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | The contents of the text message. Must be 2048 characters or less. | 
**suggestions** | [**List[MultiChannelAction]**](MultiChannelAction.md) | An array of suggested actions for the recipient. | [optional] 
**media** | [**List[MmsMessageContentFile]**](MmsMessageContentFile.md) |  | 
**orientation** | [**StandaloneCardOrientationEnum**](StandaloneCardOrientationEnum.md) |  | 
**thumbnail_image_alignment** | [**ThumbnailAlignmentEnum**](ThumbnailAlignmentEnum.md) |  | 
**card_content** | [**RbmCardContent**](RbmCardContent.md) |  | 
**card_width** | [**CardWidthEnum**](CardWidthEnum.md) |  | 
**card_contents** | [**List[RbmCardContent]**](RbmCardContent.md) |  | 

## Example

```python
from bandwidth.models.multi_channel_channel_list_object_content import MultiChannelChannelListObjectContent

# TODO update the JSON string below
json = "{}"
# create an instance of MultiChannelChannelListObjectContent from a JSON string
multi_channel_channel_list_object_content_instance = MultiChannelChannelListObjectContent.from_json(json)
# print the JSON string representation of the object
print(MultiChannelChannelListObjectContent.to_json())

# convert the object into a dict
multi_channel_channel_list_object_content_dict = multi_channel_channel_list_object_content_instance.to_dict()
# create an instance of MultiChannelChannelListObjectContent from a dict
multi_channel_channel_list_object_content_from_dict = MultiChannelChannelListObjectContent.from_dict(multi_channel_channel_list_object_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


