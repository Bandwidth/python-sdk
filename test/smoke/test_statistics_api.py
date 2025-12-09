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

    @classmethod
    def setUpClass(cls):
        configuration = Configuration(
            client_id=BW_CLIENT_ID,
            client_secret=BW_CLIENT_SECRET
        )
        cls.api_client = ApiClient(configuration)
        cls.api_instance = StatisticsApi(cls.api_client)
        cls.account_id = BW_ACCOUNT_ID

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
