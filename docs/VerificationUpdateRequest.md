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
**business_registration_number** | **str** | Government-issued business identifying number.  **Note: As of October 19th, 2026 this field will be required when &#x60;businessEntityType&#x60; is _not_ &#x60;SOLE_PROPRIETOR&#x60;. If this field is provided, &#x60;businessRegistrationType&#x60; and &#x60;businessRegistrationIssuingCountry&#x60; are also required.**  | [optional] 
**business_registration_type** | [**BusinessRegistrationTypeEnum**](BusinessRegistrationTypeEnum.md) |  | [optional] 
**business_entity_type** | [**BusinessEntityTypeEnum**](BusinessEntityTypeEnum.md) |  | [optional] 
**business_registration_issuing_country** | **str** | The country issuing the business registration in ISO-3166-1 alpha-3 format. Alpha-2 format is accepted by the API, but alpha-3 is highly encouraged.  **Note: As of October 19th, 2026 this field will be required when &#x60;businessRegistrationNumber&#x60; is provided.**  | Registration Type     | Supported Countries                | |----------------------|------------------------------------| | EIN                  | USA                                | | CBN                  | CAN                                | | NEQ                  | CAN                                | | PROVINCIAL_NUMBER    | CAN                                | | CRN                  | GBR, HKG                           | | VAT                  | GBR, IRL, BRA, NLD                 | | ACN                  | AUS                                | | ABN                  | AUS                                | | BRN                  | HKG                                | | SIREN                | FRA                                | | SIRET                | FRA                                | | NZBN                 | NZL                                | | UST_IDNR             | DEU                                | | CIF                  | ESP                                | | NIF                  | ESP                                | | CNPJ                 | BRA                                | | UID                  | CHE                                | | OTHER                | Must Provide Country Code          | | [optional] 
**help_message_response** | **str** | A message that gets sent to users requesting help. | [optional] 
**age_gated_content** | **bool** | Indicates whether the content is age-gated. | [optional] 
**cv_token** | **str** | The token provided by Campaign Verify to validate your political use case. Only required for 527 political organizations. If you are not a 527 political organization, this field should be omitted. Supplying an empty string will likely result in rejection. | [optional] 

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


