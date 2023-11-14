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
import datetime

import bandwidth
from bandwidth.models.machine_detection_configuration import MachineDetectionConfiguration  # noqa: E501
from bandwidth.rest import ApiException

class TestMachineDetectionConfiguration(unittest.TestCase):
    """MachineDetectionConfiguration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MachineDetectionConfiguration
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MachineDetectionConfiguration`
        """
        model = bandwidth.models.machine_detection_configuration.MachineDetectionConfiguration()  # noqa: E501
        if include_optional :
            return MachineDetectionConfiguration(
                mode = 'async', 
                detection_timeout = 15, 
                silence_timeout = 10, 
                speech_threshold = 10, 
                speech_end_threshold = 5, 
                machine_speech_end_threshold = 5, 
                delay_result = False, 
                callback_url = 'https://myServer.example/bandwidth/webhooks/machineDetectionComplete', 
                callback_method = 'POST', 
                username = 'mySecretUsername', 
                password = 'mySecretPassword1!', 
                fallback_url = 'https://myFallbackServer.example/bandwidth/webhooks/machineDetectionComplete', 
                fallback_method = 'POST', 
                fallback_username = 'mySecretUsername', 
                fallback_password = 'mySecretPassword1!'
            )
        else :
            return MachineDetectionConfiguration(
        )
        """

    def testMachineDetectionConfiguration(self):
        """Test MachineDetectionConfiguration"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()