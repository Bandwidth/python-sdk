"""
    Bandwidth

    Bandwidth's Communication APIs  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: letstalk@bandwidth.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import bandwidth
from bandwidth.model.callback_method_enum import CallbackMethodEnum
from bandwidth.model.machine_detection_mode_enum import MachineDetectionModeEnum
globals()['CallbackMethodEnum'] = CallbackMethodEnum
globals()['MachineDetectionModeEnum'] = MachineDetectionModeEnum
from bandwidth.model.machine_detection_configuration import MachineDetectionConfiguration


class TestMachineDetectionConfiguration(unittest.TestCase):
    """MachineDetectionConfiguration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMachineDetectionConfiguration(self):
        """Test MachineDetectionConfiguration"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MachineDetectionConfiguration()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
