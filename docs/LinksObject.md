# LinksObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | **str** | The first (or only) page of results matching the query. | [optional] 
**next** | **str** | If more results exist than specified by &#39;size&#39;, this link returns the next page of &#39;size&#39; results. | [optional] 
**previous** | **str** | If the results are more than one page, this link returns the previous page of &#39;size&#39; results. | [optional] 
**last** | **str** | If more results exist than specified by &#39;size&#39;, this link return the last page of result. | [optional] 

## Example

```python
from bandwidth.models.links_object import LinksObject

# TODO update the JSON string below
json = "{}"
# create an instance of LinksObject from a JSON string
links_object_instance = LinksObject.from_json(json)
# print the JSON string representation of the object
print(LinksObject.to_json())

# convert the object into a dict
links_object_dict = links_object_instance.to_dict()
# create an instance of LinksObject from a dict
links_object_from_dict = LinksObject.from_dict(links_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


