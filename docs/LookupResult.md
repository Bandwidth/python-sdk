# LookupResult

Carrier information results for the specified telephone number.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_code** | **int** | Our vendor&#39;s response code. | [optional] 
**message** | **str** | Message associated with the response code. | [optional] 
**e_164_format** | **str** | The telephone number in E.164 format. | [optional] 
**formatted** | **str** | The formatted version of the telephone number. | [optional] 
**country** | **str** | The country of the telephone number. | [optional] 
**line_type** | **str** | The line type of the telephone number. | [optional] 
**line_provider** | **str** | The messaging service provider of the telephone number. | [optional] 
**mobile_country_code** | **str** | The first half of the Home Network Identity (HNI). | [optional] 
**mobile_network_code** | **str** | The second half of the HNI. | [optional] 

## Example

```python
from bandwidth.models.lookup_result import LookupResult

# TODO update the JSON string below
json = "{}"
# create an instance of LookupResult from a JSON string
lookup_result_instance = LookupResult.from_json(json)
# print the JSON string representation of the object
print(LookupResult.to_json())

# convert the object into a dict
lookup_result_dict = lookup_result_instance.to_dict()
# create an instance of LookupResult from a dict
lookup_result_from_dict = LookupResult.from_dict(lookup_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


