# StirShaken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verstat** | **str** | (optional) The verification status indicating whether the verification was successful or not. Possible values are TN-Verification-Passed and TN-Verification-Failed. | [optional] 
**attestation_indicator** | **str** | (optional) The attestation level verified by Bandwidth. Possible values are A (full), B (partial) or C (gateway). | [optional] 
**originating_id** | **str** | (optional) A unique origination identifier. | [optional] 

## Example

```python
from bandwidth.models.stir_shaken import StirShaken

# TODO update the JSON string below
json = "{}"
# create an instance of StirShaken from a JSON string
stir_shaken_instance = StirShaken.from_json(json)
# print the JSON string representation of the object
print(StirShaken.to_json())

# convert the object into a dict
stir_shaken_dict = stir_shaken_instance.to_dict()
# create an instance of StirShaken from a dict
stir_shaken_from_dict = StirShaken.from_dict(stir_shaken_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


