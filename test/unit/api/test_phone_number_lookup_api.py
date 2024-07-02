# coding: utf-8

"""
    Bandwidth

    Bandwidth's Communication APIs

    The version of the OpenAPI document: 1.0.0
    Contact: letstalk@bandwidth.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hamcrest import *
from test.utils.env_variables import *
from bandwidth import ApiClient, Configuration
from bandwidth.api.phone_number_lookup_api import PhoneNumberLookupApi
from bandwidth.models.lookup_request import LookupRequest
from bandwidth.models.create_lookup_response import CreateLookupResponse
from bandwidth.models.lookup_status_enum import LookupStatusEnum
from bandwidth.models.lookup_status import LookupStatus
from bandwidth.models.lookup_result import LookupResult


class TestPhoneNumberLookupApi(unittest.TestCase):
    """PhoneNumberLookupApi unit test stubs"""

    def setUp(self) -> None:
        configuration = Configuration(
            username=BW_USERNAME,
            password=BW_PASSWORD,
            host='http://127.0.0.1:4010',
            ignore_operation_servers=True
        )
        api_client = ApiClient(configuration)
        self.phone_number_lookup_api_instance = PhoneNumberLookupApi(api_client)

    def test_create_lookup(self) -> None:
        """Test case for create_lookup

        Create Lookup
        """
        lookup_request = LookupRequest(tns=[BW_NUMBER])

        response = self.phone_number_lookup_api_instance.create_lookup_with_http_info(BW_ACCOUNT_ID, lookup_request)

        assert_that(response.status_code, equal_to(202))
        assert_that(response.data, instance_of(CreateLookupResponse))
        assert_that(response.data.request_id, has_length(36))
        assert_that(response.data.status, is_in(LookupStatusEnum))

    def test_get_lookup_status(self) -> None:
        """Test case for get_lookup_status

        Get Lookup Request Status
        """
        response = self.phone_number_lookup_api_instance.get_lookup_status_with_http_info(
            BW_ACCOUNT_ID,
            'request-id',
            _headers={'Prefer': 'example=lookupMultipleNumbersPartialCompleteExample'}
        )

        assert_that(response.status_code, equal_to(200))
        assert_that(response.data, instance_of(LookupStatus))
        assert_that(response.data.request_id, has_length(36))
        assert_that(response.data.status, is_in(LookupStatusEnum))
        assert_that(response.data.result, instance_of(list))
        assert_that(response.data.result[0], instance_of(LookupResult))
        assert_that(response.data.result[0].response_code, instance_of(int))
        assert_that(response.data.result[0].message, instance_of(str))
        assert_that(response.data.result[0].e_164_format, has_length(12))
        assert_that(response.data.result[0].formatted, has_length(14))
        assert_that(response.data.result[0].country, instance_of(str))
        assert_that(response.data.result[0].line_type, instance_of(str))
        assert_that(response.data.result[0].line_provider, instance_of(str))
        assert_that(response.data.result[0].mobile_country_code, instance_of(str))
        assert_that(response.data.result[0].mobile_network_code, instance_of(str))
        assert_that(response.data.failed_telephone_numbers, instance_of(list))
        assert_that(response.data.failed_telephone_numbers[0], instance_of(str))


if __name__ == '__main__':
    unittest.main()
