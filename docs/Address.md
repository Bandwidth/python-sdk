# Address


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the business using the toll-free number. | 
**addr1** | **str** | The address of the business using the toll-free number. | 
**addr2** | **str** | The address of the business using the toll-free number. | [optional] 
**city** | **str** | The city of the business using the toll-free number. | 
**state** | **str** | The state of the business using the toll-free number. | 
**zip** | **str** | The zip of the business using the toll-free number. | 
**url** | **str** | The website of the business using the toll-free number. | 

## Example

```python
from bandwidth.models.address import Address

# TODO update the JSON string below
json = "{}"
# create an instance of Address from a JSON string
address_instance = Address.from_json(json)
# print the JSON string representation of the object
print(Address.to_json())

# convert the object into a dict
address_dict = address_instance.to_dict()
# create an instance of Address from a dict
address_from_dict = Address.from_dict(address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


