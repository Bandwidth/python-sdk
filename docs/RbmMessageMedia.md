# RbmMessageMedia


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**media** | [**List[RbmMessageContentFile]**](RbmMessageContentFile.md) |  | 
**suggestions** | [**List[MultiChannelAction]**](MultiChannelAction.md) | An array of suggested actions for the recipient. | [optional] 

## Example

```python
from bandwidth.models.rbm_message_media import RbmMessageMedia

# TODO update the JSON string below
json = "{}"
# create an instance of RbmMessageMedia from a JSON string
rbm_message_media_instance = RbmMessageMedia.from_json(json)
# print the JSON string representation of the object
print(RbmMessageMedia.to_json())

# convert the object into a dict
rbm_message_media_dict = rbm_message_media_instance.to_dict()
# create an instance of RbmMessageMedia from a dict
rbm_message_media_from_dict = RbmMessageMedia.from_dict(rbm_message_media_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


