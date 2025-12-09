# RbmActionOpenUrl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**RbmActionTypeEnum**](RbmActionTypeEnum.md) |  | 
**text** | **str** | Displayed text for user to click | 
**postback_data** | **bytearray** | Base64 payload the customer receives when the reply is clicked. | 
**url** | **str** | The URL to open in browser. | 
**application** | [**RbmOpenUrlEnum**](RbmOpenUrlEnum.md) |  | [optional] 
**webview_view_mode** | [**RbmVebViewEnum**](RbmVebViewEnum.md) |  | [optional] 

## Example

```python
from bandwidth.models.rbm_action_open_url import RbmActionOpenUrl

# TODO update the JSON string below
json = "{}"
# create an instance of RbmActionOpenUrl from a JSON string
rbm_action_open_url_instance = RbmActionOpenUrl.from_json(json)
# print the JSON string representation of the object
print(RbmActionOpenUrl.to_json())

# convert the object into a dict
rbm_action_open_url_dict = rbm_action_open_url_instance.to_dict()
# create an instance of RbmActionOpenUrl from a dict
rbm_action_open_url_from_dict = RbmActionOpenUrl.from_dict(rbm_action_open_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


