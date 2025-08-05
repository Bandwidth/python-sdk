# CreateMultiChannelMessageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**List[Link]**](Link.md) |  | [optional] 
**data** | [**MultiChannelMessageResponseData**](MultiChannelMessageResponseData.md) |  | [optional] 
**errors** | [**List[ErrorObject]**](ErrorObject.md) |  | [optional] 

## Example

```python
from bandwidth.models.create_multi_channel_message_response import CreateMultiChannelMessageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMultiChannelMessageResponse from a JSON string
create_multi_channel_message_response_instance = CreateMultiChannelMessageResponse.from_json(json)
# print the JSON string representation of the object
print(CreateMultiChannelMessageResponse.to_json())

# convert the object into a dict
create_multi_channel_message_response_dict = create_multi_channel_message_response_instance.to_dict()
# create an instance of CreateMultiChannelMessageResponse from a dict
create_multi_channel_message_response_from_dict = CreateMultiChannelMessageResponse.from_dict(create_multi_channel_message_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


