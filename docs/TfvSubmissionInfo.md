# TfvSubmissionInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_address** | [**Address**](Address.md) |  | [optional] 
**business_contact** | [**Contact**](Contact.md) |  | [optional] 
**message_volume** | **int** | Estimated monthly volume of messages from the toll-free number. | [optional] 
**use_case** | **str** | The category of the use case. | [optional] 
**use_case_summary** | **str** | A general idea of the use case and customer. | [optional] 
**production_message_content** | **str** | Example of message content. | [optional] 
**opt_in_workflow** | [**OptInWorkflow**](OptInWorkflow.md) |  | [optional] 
**additional_information** | **str** | Any additional information. | [optional] 
**isv_reseller** | **str** | ISV name. | [optional] 
**privacy_policy_url** | **str** | The Toll-Free Verification request privacy policy URL. | [optional] 
**terms_and_conditions_url** | **str** | The Toll-Free Verification request terms and conditions policy URL. | [optional] 
**business_dba** | **str** | The company &#39;Doing Business As&#39;. | [optional] 
**business_registration_number** | **str** | Government-issued business identifying number. | [optional] 
**business_registration_type** | [**BusinessRegistrationTypeEnum**](BusinessRegistrationTypeEnum.md) |  | [optional] 
**business_registration_issuing_country** | [**BusinessRegistrationIssuingCountryEnum**](BusinessRegistrationIssuingCountryEnum.md) |  | [optional] 
**business_entity_type** | [**BusinessEntityTypeEnum**](BusinessEntityTypeEnum.md) |  | [optional] 

## Example

```python
from bandwidth.models.tfv_submission_info import TfvSubmissionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TfvSubmissionInfo from a JSON string
tfv_submission_info_instance = TfvSubmissionInfo.from_json(json)
# print the JSON string representation of the object
print(TfvSubmissionInfo.to_json())

# convert the object into a dict
tfv_submission_info_dict = tfv_submission_info_instance.to_dict()
# create an instance of TfvSubmissionInfo from a dict
tfv_submission_info_from_dict = TfvSubmissionInfo.from_dict(tfv_submission_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


