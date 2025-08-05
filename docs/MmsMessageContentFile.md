# MmsMessageContentFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_url** | **str** | The URL of a media attachment.  For MMS, the API limits file size to 3.5MB. Specific carriers and channels may have a smaller limit that could cause a large file to fail, see [here](https://support.bandwidth.com/hc/en-us/articles/360014235473-What-are-the-MMS-file-size-limits) for more details. | 

## Example

```python
from bandwidth.models.mms_message_content_file import MmsMessageContentFile

# TODO update the JSON string below
json = "{}"
# create an instance of MmsMessageContentFile from a JSON string
mms_message_content_file_instance = MmsMessageContentFile.from_json(json)
# print the JSON string representation of the object
print(MmsMessageContentFile.to_json())

# convert the object into a dict
mms_message_content_file_dict = mms_message_content_file_instance.to_dict()
# create an instance of MmsMessageContentFile from a dict
mms_message_content_file_from_dict = MmsMessageContentFile.from_dict(mms_message_content_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


