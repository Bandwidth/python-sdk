# RbmActionDial


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**RbmActionTypeEnum**](RbmActionTypeEnum.md) |  | 
**text** | **str** | Displayed text for user to click | 
**post_back_data** | **bytearray** | Base64 payload the customer receives when the reply is clicked. | 
**phone_number** | **str** | The phone number to dial. Must be E164 format. | 

## Example

```python
from bandwidth.models.rbm_action_dial import RbmActionDial

# TODO update the JSON string below
json = "{}"
# create an instance of RbmActionDial from a JSON string
rbm_action_dial_instance = RbmActionDial.from_json(json)
# print the JSON string representation of the object
print(RbmActionDial.to_json())

# convert the object into a dict
rbm_action_dial_dict = rbm_action_dial_instance.to_dict()
# create an instance of RbmActionDial from a dict
rbm_action_dial_from_dict = RbmActionDial.from_dict(rbm_action_dial_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


