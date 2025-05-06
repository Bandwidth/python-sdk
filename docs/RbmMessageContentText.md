# RbmMessageContentText


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | The text associated with the message. Must be 3270 characters or less | 
**suggestions** | [**List[MultiChannelAction]**](MultiChannelAction.md) | An array of suggested actions for the recipient. | [optional] 

## Example

```python
from bandwidth.models.rbm_message_content_text import RbmMessageContentText

# TODO update the JSON string below
json = "{}"
# create an instance of RbmMessageContentText from a JSON string
rbm_message_content_text_instance = RbmMessageContentText.from_json(json)
# print the JSON string representation of the object
print(RbmMessageContentText.to_json())

# convert the object into a dict
rbm_message_content_text_dict = rbm_message_content_text_instance.to_dict()
# create an instance of RbmMessageContentText from a dict
rbm_message_content_text_from_dict = RbmMessageContentText.from_dict(rbm_message_content_text_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


