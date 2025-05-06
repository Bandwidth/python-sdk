# RbmCardContentMedia


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_url** | **str** | The URL of the media file. 100MB is the maximum file size. | 
**thumbnail_url** | **str** | The URL of the thumbnail image. Applies only to video file media. | [optional] 
**height** | [**RbmMediaHeightEnum**](RbmMediaHeightEnum.md) |  | 

## Example

```python
from bandwidth.models.rbm_card_content_media import RbmCardContentMedia

# TODO update the JSON string below
json = "{}"
# create an instance of RbmCardContentMedia from a JSON string
rbm_card_content_media_instance = RbmCardContentMedia.from_json(json)
# print the JSON string representation of the object
print(RbmCardContentMedia.to_json())

# convert the object into a dict
rbm_card_content_media_dict = rbm_card_content_media_instance.to_dict()
# create an instance of RbmCardContentMedia from a dict
rbm_card_content_media_from_dict = RbmCardContentMedia.from_dict(rbm_card_content_media_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


