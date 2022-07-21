# LookupStatus

If requestId exists, the result for that request is returned. See the Examples for details on the various responses that you can receive. Generally, if you see a Response Code of 0 in a result for a TN, information will be available for it.  Any other Response Code will indicate no information was available for the TN.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | The requestId. | [optional] 
**status** | [**LookupStatusEnum**](LookupStatusEnum.md) |  | [optional] 
**result** | [**[LookupResult]**](LookupResult.md) | The carrier information results for the specified telephone number. | [optional] 
**failed_telephone_numbers** | **[str]** | The telephone numbers whose lookup failed. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


