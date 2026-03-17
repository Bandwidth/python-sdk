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
**business_registration_number** | **str** | Government-issued business identifying number.  **Note:** If this field is provided, it is strongly recommended to also provide &#x60;businessRegistrationType&#x60; and &#x60;businessRegistrationIssuingCountry&#x60;. Submissions missing these fields have a high likelihood of rejection.  | [optional] 
**business_registration_type** | [**BusinessRegistrationTypeEnum**](BusinessRegistrationTypeEnum.md) |  | [optional] 
**business_registration_issuing_country** | **str** | The country issuing the business registration in ISO-3166-1 alpha-3 format. Alpha-2 country codes are acceptable, but the application will convert them to alpha-3 when received, so alpha-3 is encouraged.  **Note:** If this field is omitted but &#x60;businessRegistrationType&#x60; is provided, the application will attempt to infer the country based on the registration type. However, if the application cannot confidently infer the country, the submission may be rejected. To ensure the highest likelihood of acceptance, it is recommended to provide both &#x60;businessRegistrationType&#x60; and &#x60;businessRegistrationIssuingCountry&#x60;.  | Registration Type     | Supported Countries                | |----------------------|------------------------------------| | EIN                  | USA                                | | CBN                  | CAN                                | | NEQ                  | CAN                                | | PROVINCIAL_NUMBER    | CAN                                | | CRN                  | GBR, HKG                           | | VAT                  | GBR, IRL, BRA, NLD                 | | ACN                  | AUS                                | | ABN                  | AUS                                | | BRN                  | HKG                                | | SIREN                | FRA                                | | SIRET                | FRA                                | | NZBN                 | NZL                                | | UST_IDNR             | DEU                                | | CIF                  | ESP                                | | NIF                  | ESP                                | | CNPJ                 | BRA                                | | UID                  | CHE                                | | OTHER                | Must Provide Country Code          | | [optional] 
**business_entity_type** | [**BusinessEntityTypeEnum**](BusinessEntityTypeEnum.md) |  | 
**help_message_response** | **str** | A message that gets sent to users requesting help. | [optional] 
**age_gated_content** | **bool** | Indicates whether the content is age-gated. | [optional] 
**cv_token** | **str** | The token provided by Campaign Verify to validate your political use case. Only required for 527 political organizations. If you are not a 527 political organization, this field should be omitted. Supplying an empty string will likely result in rejection. | [optional] 

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


