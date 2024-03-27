# PageInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prev_page** | **str** | The link to the previous page for pagination. | [optional] 
**next_page** | **str** | The link to the next page for pagination. | [optional] 
**prev_page_token** | **str** | The isolated pagination token for the previous page. | [optional] 
**next_page_token** | **str** | The isolated pagination token for the next page. | [optional] 

## Example

```python
from bandwidth.models.page_info import PageInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PageInfo from a JSON string
page_info_instance = PageInfo.from_json(json)
# print the JSON string representation of the object
print(PageInfo.to_json())

# convert the object into a dict
page_info_dict = page_info_instance.to_dict()
# create an instance of PageInfo from a dict
page_info_form_dict = page_info.from_dict(page_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


