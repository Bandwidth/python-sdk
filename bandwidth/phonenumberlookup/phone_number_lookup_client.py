# -*- coding: utf-8 -*-

"""
bandwidth

This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from bandwidth.decorators import lazy_property
from bandwidth.configuration import Configuration
from bandwidth.configuration import Environment
from bandwidth.phonenumberlookup.controllers.api_controller\
    import APIController


class PhoneNumberLookupClient(object):

    @lazy_property
    def client(self):
        return APIController(self.config)

    def __init__(self, timeout=60, max_retries=0, backoff_factor=2,
                 retry_statuses=[408, 413, 429, 500, 502, 503, 504, 521, 522, 524, 408, 413, 429, 500, 502, 503, 504, 521, 522, 524],
                 retry_methods=['GET', 'PUT', 'GET', 'PUT'],
                 environment=Environment.PRODUCTION,
                 base_url='https://www.example.com',
                 messaging_basic_auth_user_name='TODO: Replace',
                 messaging_basic_auth_password='TODO: Replace',
                 multi_factor_auth_basic_auth_user_name='TODO: Replace',
                 multi_factor_auth_basic_auth_password='TODO: Replace',
                 phone_number_lookup_basic_auth_user_name='TODO: Replace',
                 phone_number_lookup_basic_auth_password='TODO: Replace',
                 voice_basic_auth_user_name='TODO: Replace',
                 voice_basic_auth_password='TODO: Replace',
                 web_rtc_basic_auth_user_name='TODO: Replace',
                 web_rtc_basic_auth_password='TODO: Replace', config=None):
        if config is None:
            self.config = Configuration(timeout=timeout,
                                        max_retries=max_retries,
                                        backoff_factor=backoff_factor,
                                        retry_statuses=retry_statuses,
                                        retry_methods=retry_methods,
                                        environment=environment,
                                        base_url=base_url,
                                        messaging_basic_auth_user_name=messaging_basic_auth_user_name,
                                        messaging_basic_auth_password=messaging_basic_auth_password,
                                        multi_factor_auth_basic_auth_user_name=multi_factor_auth_basic_auth_user_name,
                                        multi_factor_auth_basic_auth_password=multi_factor_auth_basic_auth_password,
                                        phone_number_lookup_basic_auth_user_name=phone_number_lookup_basic_auth_user_name,
                                        phone_number_lookup_basic_auth_password=phone_number_lookup_basic_auth_password,
                                        voice_basic_auth_user_name=voice_basic_auth_user_name,
                                        voice_basic_auth_password=voice_basic_auth_password,
                                        web_rtc_basic_auth_user_name=web_rtc_basic_auth_user_name,
                                        web_rtc_basic_auth_password=web_rtc_basic_auth_password)
        else:
            self.config = config
