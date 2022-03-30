# MachineDetectionConfiguration

The machine detection request used to perform <a href='/docs/voice/guides/machineDetection'>machine detection</a> on the call.<br>(Click arrow to expand machine detection options)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** | The machine detection mode. If set to &#39;async&#39;, the detection result will be sent in a &#39;machineDetectionComplete&#39; callback. If set to &#39;sync&#39;, the &#39;answer&#39; callback will wait for the machine detection to complete and will include its result. | [optional]  if omitted the server will use the default value of "async"
**detection_timeout** | **float** | The timeout used for the whole operation, in seconds. If no result is determined in this period, a callback with a &#x60;timeout&#x60; result is sent. | [optional]  if omitted the server will use the default value of 15
**silence_timeout** | **float** | If no speech is detected in this period, a callback with a &#39;silence&#39; result is sent. | [optional]  if omitted the server will use the default value of 10
**speech_threshold** | **float** | When speech has ended and a result couldn&#39;t be determined based on the audio content itself, this value is used to determine if the speaker is a machine based on the speech duration. If the length of the speech detected is greater than or equal to this threshold, the result will be &#39;answering-machine&#39;. If the length of speech detected is below this threshold, the result will be &#39;human&#39;. | [optional]  if omitted the server will use the default value of 10
**speech_end_threshold** | **float** | Amount of silence (in seconds) before assuming the callee has finished speaking. | [optional]  if omitted the server will use the default value of 5
**delay_result** | **bool** | If set to &#39;true&#39; and if an answering machine is detected, the &#39;answering-machine&#39; callback will be delayed until the machine is done speaking or until the &#39;detectionTimeout&#39; is exceeded. If false, the &#39;answering-machine&#39; result is sent immediately. | [optional]  if omitted the server will use the default value of False
**callback_url** | **str, none_type** | The URL to send the &#39;machineDetectionComplete&#39; webhook when the detection is completed. Only for &#39;async&#39; mode. | [optional] 
**callback_method** | **str, none_type** | The HTTP method to use for the request to &#x60;callbackUrl&#x60;. &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional]  if omitted the server will use the default value of "POST"
**fallback_url** | **str, none_type** | A fallback URL which, if provided, will be used to retry the machine detection complete webhook delivery in case &#x60;callbackUrl&#x60; fails to respond | [optional] 
**fallback_method** | **str, none_type** | The HTTP method to use for the request to fallbackUrl. GET or POST. | [optional]  if omitted the server will use the default value of "POST"
**username** | **str, none_type** | The username to send in the HTTP request to &#x60;callbackUrl&#x60; | [optional] 
**password** | **str, none_type** | The password to send in the HTTP request to &#x60;callbackUrl&#x60; | [optional] 
**fallback_username** | **str, none_type** | The username to send in the HTTP request to &#x60;fallbackUrl&#x60; | [optional] 
**fallback_password** | **str, none_type** | The password to send in the HTTP request to &#x60;fallbackUrl&#x60; | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


