# TelephoneNumber


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**telephone_number** | **str** | Simple Telephone Number. | [optional] 

## Example

```python
from bandwidth.models.telephone_number import TelephoneNumber

# TODO update the JSON string below
json = "{}"
# create an instance of TelephoneNumber from a JSON string
telephone_number_instance = TelephoneNumber.from_json(json)
# print the JSON string representation of the object
print(TelephoneNumber.to_json())

# convert the object into a dict
telephone_number_dict = telephone_number_instance.to_dict()
# create an instance of TelephoneNumber from a dict
telephone_number_from_dict = TelephoneNumber.from_dict(telephone_number_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


