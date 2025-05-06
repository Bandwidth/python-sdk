# RbmMessageContentFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_url** | **str** | The URL of the media file. 100MB is the maximum file size. | 
**thumbnail_url** | **str** | The URL of the thumbnail image. Applies only to video file media. | [optional] 

## Example

```python
from bandwidth.models.rbm_message_content_file import RbmMessageContentFile

# TODO update the JSON string below
json = "{}"
# create an instance of RbmMessageContentFile from a JSON string
rbm_message_content_file_instance = RbmMessageContentFile.from_json(json)
# print the JSON string representation of the object
print(RbmMessageContentFile.to_json())

# convert the object into a dict
rbm_message_content_file_dict = rbm_message_content_file_instance.to_dict()
# create an instance of RbmMessageContentFile from a dict
rbm_message_content_file_from_dict = RbmMessageContentFile.from_dict(rbm_message_content_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


