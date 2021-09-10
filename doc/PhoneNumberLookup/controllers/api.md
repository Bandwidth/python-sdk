# API

```python
client_controller = client.phone_number_lookup_client.client
```

## Class Name

`APIController`

## Methods

* [Create Lookup Request](/doc/PhoneNumberLookup/controllers/api.md#create-lookup-request)
* [Get Lookup Request Status](/doc/PhoneNumberLookup/controllers/api.md#get-lookup-request-status)


# Create Lookup Request

Create a TN Lookup Order.

```python
def create_lookup_request(self,
                         account_id,
                         body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id` | `string` | Template, Required | The ID of the Bandwidth account that the user belongs to. |
| `body` | [`OrderRequest`]($m/PhoneNumberLookup/OrderRequest) | Body, Required | - |

## Response Type

[`OrderResponse`]($m/PhoneNumberLookup/OrderResponse)

## Example Usage

```python
account_id = '9998887'
body = OrderRequest()
body.tns = ['19196104420']

result = client_controller.create_lookup_request(account_id, body)
```

## Example Response *(as JSON)*

```json
{
  "requestId": "004223a0-8b17-41b1-bf81-20732adf5590",
  "status": "IN_PROGRESS"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request. Ensure that your request payload is properly formatted and that the telephone numbers used are valid. | [`AccountsTnlookup400ErrorException`]($m/PhoneNumberLookup/Accounts%20Tnlookup%20400%20Error) |
| 401 | Unauthorized. Ensure that you are using the proper credentials for the environment you are accessing, your user has the proper role assigned to it, and that your Bandwidth account is enabled for TN Lookup access. | `APIException` |
| 415 | Invalid content-type. Ensure that your content-type header is set to application/json. | `APIException` |
| 429 | Too Many Requests. Reduce the amount of requests that you are sending in order to avoid receiving this status code. | `APIException` |
| 500 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 501 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 502 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 503 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 504 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 505 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 506 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 507 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 508 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 509 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 510 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 511 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 512 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 513 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 514 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 515 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 516 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 517 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 518 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 519 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 520 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 521 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 522 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 523 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 524 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 525 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 526 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 527 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 528 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 529 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 530 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 531 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 532 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 533 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 534 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 535 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 536 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 537 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 538 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 539 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 540 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 541 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 542 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 543 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 544 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 545 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 546 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 547 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 548 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 549 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 550 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 551 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 552 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 553 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 554 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 555 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 556 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 557 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 558 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 559 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 560 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 561 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 562 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 563 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 564 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 565 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 566 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 567 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 568 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 569 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 570 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 571 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 572 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 573 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 574 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 575 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 576 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 577 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 578 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 579 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 580 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 581 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 582 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 583 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 584 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 585 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 586 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 587 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 588 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 589 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 590 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 591 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 592 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 593 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 594 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 595 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 596 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 597 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 598 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 599 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |


# Get Lookup Request Status

Query an existing TN Lookup Order.

```python
def get_lookup_request_status(self,
                             account_id,
                             request_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id` | `string` | Template, Required | The ID of the Bandwidth account that the user belongs to. |
| `request_id` | `string` | Template, Required | - |

## Response Type

[`OrderStatus`]($m/PhoneNumberLookup/OrderStatus)

## Example Usage

```python
account_id = '9998887'
request_id = 'requestId2'

result = client_controller.get_lookup_request_status(account_id, request_id)
```

## Example Response *(as JSON)*

```json
{
  "requestId": "004223a0-8b17-41b1-bf81-20732adf5590",
  "status": "IN_PROGRESS"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request. Ensure that you have set the requestId as a URL path parameter. | `APIException` |
| 401 | Unauthorized. Ensure that you are using the proper credentials for the environment you are accessing, your user has the proper role assigned to it, and that your Bandwidth account is enabled for TN Lookup access. | `APIException` |
| 404 | RequestId not found. Ensure that the requestId used in the URL path is valid and maps to a previous request that was submitted. | `APIException` |
| 429 | Too Many Requests. Reduce the amount of requests that you are sending in order to avoid receiving this status code. | `APIException` |
| 500 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 501 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 502 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 503 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 504 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 505 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 506 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 507 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 508 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 509 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 510 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 511 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 512 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 513 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 514 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 515 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 516 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 517 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 518 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 519 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 520 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 521 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 522 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 523 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 524 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 525 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 526 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 527 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 528 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 529 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 530 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 531 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 532 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 533 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 534 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 535 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 536 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 537 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 538 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 539 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 540 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 541 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 542 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 543 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 544 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 545 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 546 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 547 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 548 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 549 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 550 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 551 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 552 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 553 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 554 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 555 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 556 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 557 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 558 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 559 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 560 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 561 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 562 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 563 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 564 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 565 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 566 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 567 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 568 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 569 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 570 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 571 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 572 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 573 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 574 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 575 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 576 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 577 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 578 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 579 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 580 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 581 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 582 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 583 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 584 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 585 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 586 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 587 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 588 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 589 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 590 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 591 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 592 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 593 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 594 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 595 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 596 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 597 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 598 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |
| 599 | Unexpected error. Please contact Bandwidth Support if your requests are receiving this status code for an extended period of time. | `APIException` |

