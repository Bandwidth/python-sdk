"""
Integration test for Bandwidth's Statistics API
"""
import unittest
import logging

from hamcrest import *
from bandwidth import ApiClient, Configuration
from bandwidth.api.statistics_api import StatisticsApi
from bandwidth.models import AccountStatistics
from test.utils.env_variables import *


class TestStatisticsApi(unittest.TestCase):
    """StatisticsApi integration Test
    """

    def setUp(self):
        configuration = Configuration(
            username=BW_USERNAME,
            password=BW_PASSWORD
        )
        self.api_client = ApiClient(configuration)
        self.api_instance = StatisticsApi(self.api_client)
        self.account_id = BW_ACCOUNT_ID

    def test_get_statistics(self):
        api_response_with_http_info = self.api_instance.get_statistics_with_http_info(self.account_id)

        logging.debug(api_response_with_http_info)
        assert_that(api_response_with_http_info.status_code, equal_to(200))

        api_response = self.api_instance.get_statistics(self.account_id)
        assert_that(api_response, instance_of(AccountStatistics))
        assert_that(api_response, has_properties(
            'current_call_queue_size', instance_of(int),
            'max_call_queue_size', instance_of(int)
        ))

if __name__ == '__main__':
    unittest.main()
