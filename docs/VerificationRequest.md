# VerificationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_address** | [**Address**](Address.md) |  | 
**business_contact** | [**Contact**](Contact.md) |  | 
**message_volume** | **int** | Estimated monthly volume of messages from the toll-free number. | 
**phone_numbers** | **List[str]** |  | 
**use_case** | **str** | The category of the use case. | 
**use_case_summary** | **str** | A general idea of the use case and customer. | 
**production_message_content** | **str** | Example of message content. | 
**opt_in_workflow** | [**OptInWorkflow**](OptInWorkflow.md) |  | 
**additional_information** | **str** | Any additional information. | [optional] 
**isv_reseller** | **str** | ISV name. | [optional] 
**privacy_policy_url** | **str** | The Toll-Free Verification request privacy policy URL. | [optional] 
**terms_and_conditions_url** | **str** | The Toll-Free Verification request terms and conditions policy URL. | [optional] 
**business_dba** | **str** | The company &#39;Doing Business As&#39;. | [optional] 
**business_registration_number** | **str** | US Federal Tax ID Number (EIN) or Canada Business Number (CBN). Optional until early 2026. If a value is provided for this field, a value must be provided for &#x60;businessRegistrationType&#x60; and &#x60;businessEntityType&#x60;. Available starting October 1st, 2025. | [optional] 
**business_registration_type** | [**BusinessRegistrationTypeEnum**](BusinessRegistrationTypeEnum.md) |  | [optional] 
**business_entity_type** | [**BusinessEntityTypeEnum**](BusinessEntityTypeEnum.md) |  | [optional] 
**help_message_response** | **str** | A message that gets sent to users requesting help. | [optional] 
**age_gated_content** | **bool** | Indicates whether the content is age-gated. | [optional] 

## Example

```python
from bandwidth.models.verification_request import VerificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VerificationRequest from a JSON string
verification_request_instance = VerificationRequest.from_json(json)
# print the JSON string representation of the object
print(VerificationRequest.to_json())

# convert the object into a dict
verification_request_dict = verification_request_instance.to_dict()
# create an instance of VerificationRequest from a dict
verification_request_from_dict = VerificationRequest.from_dict(verification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


