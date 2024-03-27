# MessagesList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** | The total number of messages matched by the search. When the request has limitTotalCount set to true this value is limited to 10,000. | [optional] 
**page_info** | [**PageInfo**](PageInfo.md) |  | [optional] 
**messages** | [**List[ListMessageItem]**](ListMessageItem.md) |  | [optional] 

## Example

```python
from bandwidth.models.messages_list import MessagesList

# TODO update the JSON string below
json = "{}"
# create an instance of MessagesList from a JSON string
messages_list_instance = MessagesList.from_json(json)
# print the JSON string representation of the object
print(MessagesList.to_json())

# convert the object into a dict
messages_list_dict = messages_list_instance.to_dict()
# create an instance of MessagesList from a dict
messages_list_form_dict = messages_list.from_dict(messages_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


