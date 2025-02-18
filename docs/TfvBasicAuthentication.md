# TfvBasicAuthentication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**password** | **str** |  | 

## Example

```python
from bandwidth.models.tfv_basic_authentication import TfvBasicAuthentication

# TODO update the JSON string below
json = "{}"
# create an instance of TfvBasicAuthentication from a JSON string
tfv_basic_authentication_instance = TfvBasicAuthentication.from_json(json)
# print the JSON string representation of the object
print(TfvBasicAuthentication.to_json())

# convert the object into a dict
tfv_basic_authentication_dict = tfv_basic_authentication_instance.to_dict()
# create an instance of TfvBasicAuthentication from a dict
tfv_basic_authentication_from_dict = TfvBasicAuthentication.from_dict(tfv_basic_authentication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


