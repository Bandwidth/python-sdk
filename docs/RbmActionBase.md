# RbmActionBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**RbmActionTypeEnum**](RbmActionTypeEnum.md) |  | 
**text** | **str** | Displayed text for user to click | 
**postback_data** | **bytearray** | Base64 payload the customer receives when the reply is clicked. | 

## Example

```python
from bandwidth.models.rbm_action_base import RbmActionBase

# TODO update the JSON string below
json = "{}"
# create an instance of RbmActionBase from a JSON string
rbm_action_base_instance = RbmActionBase.from_json(json)
# print the JSON string representation of the object
print(RbmActionBase.to_json())

# convert the object into a dict
rbm_action_base_dict = rbm_action_base_instance.to_dict()
# create an instance of RbmActionBase from a dict
rbm_action_base_from_dict = RbmActionBase.from_dict(rbm_action_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


