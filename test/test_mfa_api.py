"""
    Bandwidth

    Bandwidth's Communication APIs  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: letstalk@bandwidth.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import bandwidth
from bandwidth.api.mfa_api import MFAApi  # noqa: E501


class TestMFAApi(unittest.TestCase):
    """MFAApi unit test stubs"""

    def setUp(self):
        self.api = MFAApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_messaging_two_factor(self):
        """Test case for messaging_two_factor

        Messaging Authentication  # noqa: E501
        """
        pass

    def test_verify_two_factor(self):
        """Test case for verify_two_factor

        Verify Authentication Code  # noqa: E501
        """
        pass

    def test_voice_two_factor(self):
        """Test case for voice_two_factor

        Voice Authentication  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
