# MmsMessageContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | The contents of the text message. Must be 2048 characters or less. | [optional] 
**media** | [**List[MmsMessageContentFile]**](MmsMessageContentFile.md) |  | [optional] 

## Example

```python
from bandwidth.models.mms_message_content import MmsMessageContent

# TODO update the JSON string below
json = "{}"
# create an instance of MmsMessageContent from a JSON string
mms_message_content_instance = MmsMessageContent.from_json(json)
# print the JSON string representation of the object
print(MmsMessageContent.to_json())

# convert the object into a dict
mms_message_content_dict = mms_message_content_instance.to_dict()
# create an instance of MmsMessageContent from a dict
mms_message_content_from_dict = MmsMessageContent.from_dict(mms_message_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


