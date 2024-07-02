# UpdateCallRecording


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | [**RecordingStateEnum**](RecordingStateEnum.md) |  | 

## Example

```python
from bandwidth.models.update_call_recording import UpdateCallRecording

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCallRecording from a JSON string
update_call_recording_instance = UpdateCallRecording.from_json(json)
# print the JSON string representation of the object
print(UpdateCallRecording.to_json())

# convert the object into a dict
update_call_recording_dict = update_call_recording_instance.to_dict()
# create an instance of UpdateCallRecording from a dict
update_call_recording_from_dict = UpdateCallRecording.from_dict(update_call_recording_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


