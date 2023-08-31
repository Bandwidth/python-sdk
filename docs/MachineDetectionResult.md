# MachineDetectionResult

(optional) if machine detection was requested in sync mode, the result will be specified here. Possible values are the same as the async counterpart: Machine Detection Complete

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Possible values are answering-machine, human, silence, timeout, or error. | [optional] 
**duration** | **str** | The amount of time it took to determine the result. | [optional] 

## Example

```python
from bandwidth.models.machine_detection_result import MachineDetectionResult

# TODO update the JSON string below
json = "{}"
# create an instance of MachineDetectionResult from a JSON string
machine_detection_result_instance = MachineDetectionResult.from_json(json)
# print the JSON string representation of the object
print MachineDetectionResult.to_json()

# convert the object into a dict
machine_detection_result_dict = machine_detection_result_instance.to_dict()
# create an instance of MachineDetectionResult from a dict
machine_detection_result_form_dict = machine_detection_result.from_dict(machine_detection_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


