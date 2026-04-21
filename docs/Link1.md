# Link1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The full URL of the link. | [optional] 
**rel** | **str** | The relationship of the link to the current resource. | [optional] 
**method** | **str** | The HTTP method to use when making the request. | [optional] 

## Example

```python
from bandwidth.models.link1 import Link1

# TODO update the JSON string below
json = "{}"
# create an instance of Link1 from a JSON string
link1_instance = Link1.from_json(json)
# print the JSON string representation of the object
print(Link1.to_json())

# convert the object into a dict
link1_dict = link1_instance.to_dict()
# create an instance of Link1 from a dict
link1_from_dict = Link1.from_dict(link1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


