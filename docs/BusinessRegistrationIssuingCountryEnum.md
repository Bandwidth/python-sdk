# BusinessRegistrationIssuingCountryEnum

The country issuing the business registration in ISO-3166-1 alpha-3 format. Alpha-2 country codes are acceptable, but the application will convert them to alpha-3 when received, so alpha-3 is encouraged.  **Note:** If this field is omitted but `businessRegistrationType` is provided, the application will attempt to infer the country based on the registration type. However, if the application cannot confidently infer the country, the submission may be rejected. To ensure the highest likelihood of acceptance, it is recommended to provide both `businessRegistrationType` and `businessRegistrationIssuingCountry`.  | Registration Type     | Supported Countries                | |----------------------|------------------------------------| | EIN                  | USA                                | | CBN                  | CAN                                | | NEQ                  | CAN                                | | PROVINCIAL_NUMBER    | CAN                                | | CRN                  | GBR, HKG                           | | VAT                  | GBR, IRL, BRA, NLD                 | | ACN                  | AUS                                | | ABN                  | AUS                                | | BRN                  | HKG                                | | SIREN                | FRA                                | | SIRET                | FRA                                | | NZBN                 | NZL                                | | UST_IDNR             | DEU                                | | CIF                  | ESP                                | | NIF                  | ESP                                | | CNPJ                 | BRA                                | | UID                  | CHE                                | | OTHER                | Must Provide Country Code          |

## Enum

* `USA` (value: `'USA'`)

* `CAN` (value: `'CAN'`)

* `HKG` (value: `'HKG'`)

* `GBR` (value: `'GBR'`)

* `IRL` (value: `'IRL'`)

* `BRA` (value: `'BRA'`)

* `NLD` (value: `'NLD'`)

* `AUS` (value: `'AUS'`)

* `FRA` (value: `'FRA'`)

* `NZL` (value: `'NZL'`)

* `DEU` (value: `'DEU'`)

* `ESP` (value: `'ESP'`)

* `CHE` (value: `'CHE'`)

* `CYP` (value: `'CYP'`)

* `IND` (value: `'IND'`)

* `CHN` (value: `'CHN'`)

* `BGR` (value: `'BGR'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


