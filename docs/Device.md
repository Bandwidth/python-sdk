# Device


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **str** | The unique ID of the device. | 
**device_name** | **str** | The name of the device. | [optional] 
**status** | [**DeviceStatusEnum**](DeviceStatusEnum.md) |  | 
**creation_timestamp** | **datetime** | The time the device was created. In ISO-8601 format. | 

## Example

```python
from bandwidth.models.device import Device

# TODO update the JSON string below
json = "{}"
# create an instance of Device from a JSON string
device_instance = Device.from_json(json)
# print the JSON string representation of the object
print(Device.to_json())

# convert the object into a dict
device_dict = device_instance.to_dict()
# create an instance of Device from a dict
device_from_dict = Device.from_dict(device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


