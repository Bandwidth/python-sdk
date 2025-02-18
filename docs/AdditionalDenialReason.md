# AdditionalDenialReason


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **int** | Reason code for denial. | 
**reason** | **str** | Explanation for why a verification request was declined. | 
**resubmit_allowed** | **bool** | Whether a Toll-Free Verification request qualifies for resubmission via PUT. | 

## Example

```python
from bandwidth.models.additional_denial_reason import AdditionalDenialReason

# TODO update the JSON string below
json = "{}"
# create an instance of AdditionalDenialReason from a JSON string
additional_denial_reason_instance = AdditionalDenialReason.from_json(json)
# print the JSON string representation of the object
print(AdditionalDenialReason.to_json())

# convert the object into a dict
additional_denial_reason_dict = additional_denial_reason_instance.to_dict()
# create an instance of AdditionalDenialReason from a dict
additional_denial_reason_from_dict = AdditionalDenialReason.from_dict(additional_denial_reason_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


