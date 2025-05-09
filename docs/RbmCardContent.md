# RbmCardContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title of the card. Must be 200 characters or less. | [optional] 
**description** | **str** | The description of the card. Must be 2000 characters or less. | [optional] 
**media** | [**RbmCardContentMedia**](RbmCardContentMedia.md) |  | [optional] 
**suggestions** | [**List[MultiChannelAction]**](MultiChannelAction.md) | An array of suggested actions for the recipient that will be displayed on the rich card. | [optional] 

## Example

```python
from bandwidth.models.rbm_card_content import RbmCardContent

# TODO update the JSON string below
json = "{}"
# create an instance of RbmCardContent from a JSON string
rbm_card_content_instance = RbmCardContent.from_json(json)
# print the JSON string representation of the object
print(RbmCardContent.to_json())

# convert the object into a dict
rbm_card_content_dict = rbm_card_content_instance.to_dict()
# create an instance of RbmCardContent from a dict
rbm_card_content_from_dict = RbmCardContent.from_dict(rbm_card_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


