# BusinessEntityTypeEnum

The type of registered business.  **Note: As of October 19th, 2026 submissions using a value other than `SOLE_PROPRIETOR` must provide a value for `businessRegistrationNumber`, `businessRegistrationType`, and `businessRegistrationIssuingCountry`.  Submissions using `SOLE_PROPRIETOR` must _omit_ `businessRegistrationNumber`, `businessRegistrationType`, and `businessRegistrationIssuingCountry`. Failure to adhere to these constraints will result in a 400 Bad Request rejection.** 

## Enum

* `SOLE_PROPRIETOR` (value: `'SOLE_PROPRIETOR'`)

* `PRIVATE_PROFIT` (value: `'PRIVATE_PROFIT'`)

* `PUBLIC_PROFIT` (value: `'PUBLIC_PROFIT'`)

* `NON_PROFIT` (value: `'NON_PROFIT'`)

* `GOVERNMENT` (value: `'GOVERNMENT'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


