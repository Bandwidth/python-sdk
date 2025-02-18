# TfvSubmissionWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**submission** | [**VerificationUpdateRequest**](VerificationUpdateRequest.md) |  | [optional] 

## Example

```python
from bandwidth.models.tfv_submission_wrapper import TfvSubmissionWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of TfvSubmissionWrapper from a JSON string
tfv_submission_wrapper_instance = TfvSubmissionWrapper.from_json(json)
# print the JSON string representation of the object
print(TfvSubmissionWrapper.to_json())

# convert the object into a dict
tfv_submission_wrapper_dict = tfv_submission_wrapper_instance.to_dict()
# create an instance of TfvSubmissionWrapper from a dict
tfv_submission_wrapper_from_dict = TfvSubmissionWrapper.from_dict(tfv_submission_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


