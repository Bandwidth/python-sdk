# Page


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_size** | **int** | The number of items per page. | 
**total_elements** | **int** | The total number of items. | [optional] 
**total_pages** | **int** | The total number of pages. | [optional] 
**page_number** | **int** | The current page number. | [optional] 

## Example

```python
from bandwidth.models.page import Page

# TODO update the JSON string below
json = "{}"
# create an instance of Page from a JSON string
page_instance = Page.from_json(json)
# print the JSON string representation of the object
print(Page.to_json())

# convert the object into a dict
page_dict = page_instance.to_dict()
# create an instance of Page from a dict
page_from_dict = Page.from_dict(page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


