
# Machine Detection Request

## Structure

`MachineDetectionRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mode` | [`ModeEnum`](/doc/Voice/models/mode-enum.md) | Optional | The machine detection mode. If set to 'async', the detection result will be sent in a 'machineDetectionComplete' callback. If set to 'sync', the 'answer' callback will wait for the machine detection to complete and will include its result. Default is 'async'. |
| `detection_timeout` | `float` | Optional | Total amount of time (in seconds) before giving up. |
| `silence_timeout` | `float` | Optional | If no speech is detected in this period, a callback with a 'silence' result is sent. Default is 10 seconds. |
| `speech_threshold` | `float` | Optional | When speech has ended and a result couldn't be determined based on the audio content itself, this value is used to determine if the speaker is a machine based on the speech duration. If the length of the speech detected is greater than or equal to this threshold, the result will be 'answering-machine'. If the length of speech detected is below this threshold, the result will be 'human'. Default is 10 seconds. |
| `speech_end_threshold` | `float` | Optional | Amount of silence (in seconds) before assuming the callee has finished speaking. |
| `delay_result` | `bool` | Optional | If set to 'true' and if an answering machine is detected, the 'answering-machine' callback will be delayed until the machine is done speaking or until the 'detectionTimeout' is exceeded. If false, the 'answering-machine' result is sent immediately. Default is 'false'. |
| `callback_url` | `string` | Optional | The URL to send the 'machineDetectionComplete' callback when the detection is completed. Only for 'async' mode. |
| `callback_method` | [`CallbackMethodEnum`](/doc/Voice/models/callback-method-enum.md) | Optional | - |
| `fallback_url` | `string` | Optional | - |
| `fallback_method` | [`FallbackMethodEnum`](/doc/Voice/models/fallback-method-enum.md) | Optional | - |
| `username` | `string` | Optional | - |
| `password` | `string` | Optional | - |
| `fallback_username` | `string` | Optional | - |
| `fallback_password` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "mode": null,
  "detectionTimeout": null,
  "silenceTimeout": null,
  "speechThreshold": null,
  "speechEndThreshold": null,
  "delayResult": null,
  "callbackUrl": null,
  "callbackMethod": null,
  "fallbackUrl": null,
  "fallbackMethod": null,
  "username": null,
  "password": null,
  "fallbackUsername": null,
  "fallbackPassword": null
}
```

