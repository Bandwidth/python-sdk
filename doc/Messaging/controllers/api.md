# API

```python
client_controller = client.messaging_client.client
```

## Class Name

`APIController`

## Methods

* [List Media](/doc/Messaging/controllers/api.md#list-media)
* [Get Media](/doc/Messaging/controllers/api.md#get-media)
* [Upload Media](/doc/Messaging/controllers/api.md#upload-media)
* [Delete Media](/doc/Messaging/controllers/api.md#delete-media)
* [Get Messages](/doc/Messaging/controllers/api.md#get-messages)
* [Create Message](/doc/Messaging/controllers/api.md#create-message)


# List Media

Gets a list of your media files. No query parameters are supported.

```python
def list_media(self,
              account_id,
              continuation_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id` | `string` | Template, Required | User's account ID |
| `continuation_token` | `string` | Header, Optional | Continuation token used to retrieve subsequent media. |

## Response Type

[`List of Media`]($m/Messaging/Media)

## Example Usage

```python
account_id = '900000'
continuation_token = '12345'

result = client_controller.list_media(account_id, continuation_token)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | 400 Request is malformed or invalid | [`MessagingException`]($m/Messaging/MessagingException) |
| 401 | 401 The specified user does not have access to the account | [`MessagingException`]($m/Messaging/MessagingException) |
| 403 | 403 The user does not have access to this API | [`MessagingException`]($m/Messaging/MessagingException) |
| 404 | 404 Path not found | [`MessagingException`]($m/Messaging/MessagingException) |
| 415 | 415 The content-type of the request is incorrect | [`MessagingException`]($m/Messaging/MessagingException) |
| 429 | 429 The rate limit has been reached | [`MessagingException`]($m/Messaging/MessagingException) |


# Get Media

Downloads a media file you previously uploaded.

```python
def get_media(self,
             account_id,
             media_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id` | `string` | Template, Required | User's account ID |
| `media_id` | `string` | Template, Required | Media ID to retrieve<br>**Constraints**: *Pattern*: `.+` |

## Response Type

`binary`

## Example Usage

```python
account_id = '900000'
media_id = '0a610655-ba58'

result = client_controller.get_media(account_id, media_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | 400 Request is malformed or invalid | [`MessagingException`]($m/Messaging/MessagingException) |
| 401 | 401 The specified user does not have access to the account | [`MessagingException`]($m/Messaging/MessagingException) |
| 403 | 403 The user does not have access to this API | [`MessagingException`]($m/Messaging/MessagingException) |
| 404 | 404 Path not found | [`MessagingException`]($m/Messaging/MessagingException) |
| 415 | 415 The content-type of the request is incorrect | [`MessagingException`]($m/Messaging/MessagingException) |
| 429 | 429 The rate limit has been reached | [`MessagingException`]($m/Messaging/MessagingException) |


# Upload Media

Uploads a file the normal HTTP way. You may add headers to the request in order to provide some control to your media-file.

```python
def upload_media(self,
                account_id,
                media_id,
                body,
                content_type='application/octet-stream',
                cache_control=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id` | `string` | Template, Required | User's account ID |
| `media_id` | `string` | Template, Required | The user supplied custom media ID<br>**Constraints**: *Pattern*: `.+` |
| `body` | `typing.BinaryIO` | Body, Required | - |
| `content_type` | `string` | Header, Optional | The media type of the entity-body<br>**Default**: `'application/octet-stream'` |
| `cache_control` | `string` | Header, Optional | General-header field is used to specify directives that MUST be obeyed by all caching mechanisms along the request/response chain. |

## Response Type

`void`

## Example Usage

```python
account_id = '900000'
media_id = 'my-media-id'
body = FileWrapper(open('dummy_file', 'rb'), 'optional-content-type')
content_type = 'audio/wav'
cache_control = 'no-cache'

result = client_controller.upload_media(account_id, media_id, body, content_type, cache_control)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | 400 Request is malformed or invalid | [`MessagingException`]($m/Messaging/MessagingException) |
| 401 | 401 The specified user does not have access to the account | [`MessagingException`]($m/Messaging/MessagingException) |
| 403 | 403 The user does not have access to this API | [`MessagingException`]($m/Messaging/MessagingException) |
| 404 | 404 Path not found | [`MessagingException`]($m/Messaging/MessagingException) |
| 415 | 415 The content-type of the request is incorrect | [`MessagingException`]($m/Messaging/MessagingException) |
| 429 | 429 The rate limit has been reached | [`MessagingException`]($m/Messaging/MessagingException) |


# Delete Media

Deletes a media file from Bandwidth API server. Make sure you don't have any application scripts still using the media before you delete. If you accidentally delete a media file, you can immediately upload a new file with the same name.

```python
def delete_media(self,
                account_id,
                media_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id` | `string` | Template, Required | User's account ID |
| `media_id` | `string` | Template, Required | The media ID to delete<br>**Constraints**: *Pattern*: `.+` |

## Response Type

`void`

## Example Usage

```python
account_id = '900000'
media_id = 'tjdla-4562ld'

result = client_controller.delete_media(account_id, media_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | 400 Request is malformed or invalid | [`MessagingException`]($m/Messaging/MessagingException) |
| 401 | 401 The specified user does not have access to the account | [`MessagingException`]($m/Messaging/MessagingException) |
| 403 | 403 The user does not have access to this API | [`MessagingException`]($m/Messaging/MessagingException) |
| 404 | 404 Path not found | [`MessagingException`]($m/Messaging/MessagingException) |
| 415 | 415 The content-type of the request is incorrect | [`MessagingException`]($m/Messaging/MessagingException) |
| 429 | 429 The rate limit has been reached | [`MessagingException`]($m/Messaging/MessagingException) |


# Get Messages

Gets a list of messages based on query parameters.

```python
def get_messages(self,
                account_id,
                message_id=None,
                source_tn=None,
                destination_tn=None,
                message_status=None,
                error_code=None,
                from_date_time=None,
                to_date_time=None,
                page_token=None,
                limit=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id` | `string` | Template, Required | User's account ID |
| `message_id` | `string` | Query, Optional | The ID of the message to search for. Special characters need to be encoded using URL encoding |
| `source_tn` | `string` | Query, Optional | The phone number that sent the message |
| `destination_tn` | `string` | Query, Optional | The phone number that received the message |
| `message_status` | `string` | Query, Optional | The status of the message. One of RECEIVED, QUEUED, SENDING, SENT, FAILED, DELIVERED, ACCEPTED, UNDELIVERED |
| `error_code` | `int` | Query, Optional | The error code of the message |
| `from_date_time` | `string` | Query, Optional | The start of the date range to search in ISO 8601 format. Uses the message receive time. The date range to search in is currently 14 days. |
| `to_date_time` | `string` | Query, Optional | The end of the date range to search in ISO 8601 format. Uses the message receive time. The date range to search in is currently 14 days. |
| `page_token` | `string` | Query, Optional | A base64 encoded value used for pagination of results |
| `limit` | `int` | Query, Optional | The maximum records requested in search result. Default 100. The sum of limit and after cannot be more than 10000 |

## Response Type

[`BandwidthMessagesList`]($m/Messaging/BandwidthMessagesList)

## Example Usage

```python
account_id = '900000'
message_id = '9e0df4ca-b18d-40d7-a59f-82fcdf5ae8e6'
source_tn = '%2B15554443333'
destination_tn = '%2B15554443333'
message_status = 'RECEIVED'
error_code = 9902
from_date_time = '2016-09-14T18:20:16.000Z'
to_date_time = '2016-09-14T18:20:16.000Z'
page_token = 'gdEewhcJLQRB5'
limit = 50

result = client_controller.get_messages(account_id, message_id, source_tn, destination_tn, message_status, error_code, from_date_time, to_date_time, page_token, limit)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | 400 Request is malformed or invalid | [`MessagingException`]($m/Messaging/MessagingException) |
| 401 | 401 The specified user does not have access to the account | [`MessagingException`]($m/Messaging/MessagingException) |
| 403 | 403 The user does not have access to this API | [`MessagingException`]($m/Messaging/MessagingException) |
| 404 | 404 Path not found | [`MessagingException`]($m/Messaging/MessagingException) |
| 415 | 415 The content-type of the request is incorrect | [`MessagingException`]($m/Messaging/MessagingException) |
| 429 | 429 The rate limit has been reached | [`MessagingException`]($m/Messaging/MessagingException) |


# Create Message

Endpoint for sending text messages and picture messages using V2 messaging.

```python
def create_message(self,
                  account_id,
                  body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id` | `string` | Template, Required | User's account ID |
| `body` | [`MessageRequest`]($m/Messaging/MessageRequest) | Body, Required | - |

## Response Type

[`BandwidthMessage`]($m/Messaging/BandwidthMessage)

## Example Usage

```python
account_id = '900000'
body = MessageRequest()
body.application_id = '93de2206-9669-4e07-948d-329f4b722ee2'
body.to = ['+15554443333', '+15552223333']
body.mfrom = '+15551113333'

result = client_controller.create_message(account_id, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | 400 Request is malformed or invalid | [`MessagingException`]($m/Messaging/MessagingException) |
| 401 | 401 The specified user does not have access to the account | [`MessagingException`]($m/Messaging/MessagingException) |
| 403 | 403 The user does not have access to this API | [`MessagingException`]($m/Messaging/MessagingException) |
| 404 | 404 Path not found | [`MessagingException`]($m/Messaging/MessagingException) |
| 415 | 415 The content-type of the request is incorrect | [`MessagingException`]($m/Messaging/MessagingException) |
| 429 | 429 The rate limit has been reached | [`MessagingException`]($m/Messaging/MessagingException) |

