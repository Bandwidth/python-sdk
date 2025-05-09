# RbmMessageCarouselCard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_width** | [**CardWidthEnum**](CardWidthEnum.md) |  | 
**card_contents** | [**List[RbmCardContent]**](RbmCardContent.md) |  | 
**suggestions** | [**List[MultiChannelAction]**](MultiChannelAction.md) | An array of suggested actions for the recipient. | [optional] 

## Example

```python
from bandwidth.models.rbm_message_carousel_card import RbmMessageCarouselCard

# TODO update the JSON string below
json = "{}"
# create an instance of RbmMessageCarouselCard from a JSON string
rbm_message_carousel_card_instance = RbmMessageCarouselCard.from_json(json)
# print the JSON string representation of the object
print(RbmMessageCarouselCard.to_json())

# convert the object into a dict
rbm_message_carousel_card_dict = rbm_message_carousel_card_instance.to_dict()
# create an instance of RbmMessageCarouselCard from a dict
rbm_message_carousel_card_from_dict = RbmMessageCarouselCard.from_dict(rbm_message_carousel_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


