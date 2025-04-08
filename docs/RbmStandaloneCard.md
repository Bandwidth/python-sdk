# RbmStandaloneCard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**orientation** | [**StandaloneCardOrientationEnum**](StandaloneCardOrientationEnum.md) |  | 
**thumbnail_image_alignment** | [**ThumbnailAlignmentEnum**](ThumbnailAlignmentEnum.md) |  | 
**card_content** | [**RbmCardContent**](RbmCardContent.md) |  | 
**suggestions** | [**List[MultiChannelAction]**](MultiChannelAction.md) | An array of suggested actions for the recipient. | [optional] 

## Example

```python
from bandwidth.models.rbm_standalone_card import RbmStandaloneCard

# TODO update the JSON string below
json = "{}"
# create an instance of RbmStandaloneCard from a JSON string
rbm_standalone_card_instance = RbmStandaloneCard.from_json(json)
# print the JSON string representation of the object
print(RbmStandaloneCard.to_json())

# convert the object into a dict
rbm_standalone_card_dict = rbm_standalone_card_instance.to_dict()
# create an instance of RbmStandaloneCard from a dict
rbm_standalone_card_from_dict = RbmStandaloneCard.from_dict(rbm_standalone_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


