# VerificationUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_address** | [**Address**](Address.md) |  | 
**business_contact** | [**Contact**](Contact.md) |  | 
**message_volume** | **int** | Estimated monthly volume of messages from the toll-free number. | 
**use_case** | **str** | The category of the use case. | 
**use_case_summary** | **str** | A general idea of the use case and customer. | 
**production_message_content** | **str** | Example of message content. | 
**opt_in_workflow** | [**OptInWorkflow**](OptInWorkflow.md) |  | 
**additional_information** | **str** | Any additional information. | [optional] 
**isv_reseller** | **str** | ISV name. | [optional] 
**privacy_policy_url** | **str** | The Toll-Free Verification request privacy policy URL. | [optional] 
**terms_and_conditions_url** | **str** | The Toll-Free Verification request terms and conditions policy URL. | [optional] 
**business_dba** | **str** | The company &#39;Doing Business As&#39;. | [optional] 

## Example

```python
from bandwidth.models.verification_update_request import VerificationUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VerificationUpdateRequest from a JSON string
verification_update_request_instance = VerificationUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(VerificationUpdateRequest.to_json())

# convert the object into a dict
verification_update_request_dict = verification_update_request_instance.to_dict()
# create an instance of VerificationUpdateRequest from a dict
verification_update_request_from_dict = VerificationUpdateRequest.from_dict(verification_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


