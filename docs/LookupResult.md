# LookupResult

Carrier information results for the specified telephone number.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_number** | **str** | The telephone number in E.164 format. | [optional] 
**line_type** | [**LineTypeEnum**](LineTypeEnum.md) |  | [optional] 
**messaging_provider** | **str** | The messaging service provider of the telephone number. | [optional] 
**voice_provider** | **str** | The voice service provider of the telephone number. | [optional] 
**country_code_a3** | **str** | The country code of the telephone number in ISO 3166-1 alpha-3 format. | [optional] 
**deactivation_reporter** | **str** | [DNI-Only](#section/DNI-Only). The carrier that reported a deactivation event for this phone number.  | [optional] 
**deactivation_date** | **str** | [DNI-Only](#section/DNI-Only). The datetime the carrier reported a deactivation event. | [optional] 
**deactivation_event** | [**DeactivationEventEnum**](DeactivationEventEnum.md) |  | [optional] 
**latest_message_delivery_status** | [**LatestMessageDeliveryStatusEnum**](LatestMessageDeliveryStatusEnum.md) |  | [optional] 
**initial_message_delivery_status_date** | **date** | [DNI-Only](#section/DNI-Only). The date the phone number entered the status described in &#x60;latestMessageDeliveryStatus&#x60;.  Think of this as the \&quot;start time\&quot; for that status. Value resets every time the &#x60;latestMessageDeliveryStatus&#x60; changes. | [optional] 
**latest_message_delivery_status_date** | **date** | [DNI-Only](#section/DNI-Only). The date bandwidth last received delivery status information for this phone number.  Use this field to understand how up-to-date the &#x60;latestMessageDeliveryStatus&#x60; is. Value resets every time the &#x60;latestMessageDeliveryStatus&#x60; changes. | [optional] 

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


