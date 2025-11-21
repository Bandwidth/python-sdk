# LinkSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | URI of the link. | [optional] 
**rel** | **str** | Specifies the relationship between this link and the resource. | [optional] 
**method** | **str** | HTTP method to be used. | [optional] 

## Example

```python
from bandwidth.models.link_schema import LinkSchema

# TODO update the JSON string below
json = "{}"
# create an instance of LinkSchema from a JSON string
link_schema_instance = LinkSchema.from_json(json)
# print the JSON string representation of the object
print(LinkSchema.to_json())

# convert the object into a dict
link_schema_dict = link_schema_instance.to_dict()
# create an instance of LinkSchema from a dict
link_schema_from_dict = LinkSchema.from_dict(link_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


