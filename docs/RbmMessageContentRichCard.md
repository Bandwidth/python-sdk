# RbmMessageContentRichCard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**orientation** | [**StandaloneCardOrientationEnum**](StandaloneCardOrientationEnum.md) |  | 
**thumbnail_image_alignment** | [**ThumbnailAlignmentEnum**](ThumbnailAlignmentEnum.md) |  | 
**card_content** | [**RbmCardContent**](RbmCardContent.md) |  | 
**suggestions** | [**List[MultiChannelAction]**](MultiChannelAction.md) | An array of suggested actions for the recipient. | [optional] 
**card_width** | [**CardWidthEnum**](CardWidthEnum.md) |  | 
**card_contents** | [**List[RbmCardContent]**](RbmCardContent.md) |  | 

## Example

```python
from bandwidth.models.rbm_message_content_rich_card import RbmMessageContentRichCard

# TODO update the JSON string below
json = "{}"
# create an instance of RbmMessageContentRichCard from a JSON string
rbm_message_content_rich_card_instance = RbmMessageContentRichCard.from_json(json)
# print the JSON string representation of the object
print(RbmMessageContentRichCard.to_json())

# convert the object into a dict
rbm_message_content_rich_card_dict = rbm_message_content_rich_card_instance.to_dict()
# create an instance of RbmMessageContentRichCard from a dict
rbm_message_content_rich_card_from_dict = RbmMessageContentRichCard.from_dict(rbm_message_content_rich_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


