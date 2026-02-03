# MultiChannelChannelListRBMObjectAllOfContent

The content of the message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | The text associated with the message. Must be 3270 characters or less | 
**suggestions** | [**List[MultiChannelAction]**](MultiChannelAction.md) | An array of suggested actions for the recipient. | [optional] 
**media** | [**List[RbmMessageContentFile]**](RbmMessageContentFile.md) |  | 
**orientation** | [**StandaloneCardOrientationEnum**](StandaloneCardOrientationEnum.md) |  | 
**thumbnail_image_alignment** | [**ThumbnailAlignmentEnum**](ThumbnailAlignmentEnum.md) |  | 
**card_content** | [**RbmCardContent**](RbmCardContent.md) |  | 
**card_width** | [**CardWidthEnum**](CardWidthEnum.md) |  | 
**card_contents** | [**List[RbmCardContent]**](RbmCardContent.md) |  | 

## Example

```python
from bandwidth.models.multi_channel_channel_list_rbm_object_all_of_content import MultiChannelChannelListRBMObjectAllOfContent

# TODO update the JSON string below
json = "{}"
# create an instance of MultiChannelChannelListRBMObjectAllOfContent from a JSON string
multi_channel_channel_list_rbm_object_all_of_content_instance = MultiChannelChannelListRBMObjectAllOfContent.from_json(json)
# print the JSON string representation of the object
print(MultiChannelChannelListRBMObjectAllOfContent.to_json())

# convert the object into a dict
multi_channel_channel_list_rbm_object_all_of_content_dict = multi_channel_channel_list_rbm_object_all_of_content_instance.to_dict()
# create an instance of MultiChannelChannelListRBMObjectAllOfContent from a dict
multi_channel_channel_list_rbm_object_all_of_content_from_dict = MultiChannelChannelListRBMObjectAllOfContent.from_dict(multi_channel_channel_list_rbm_object_all_of_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


