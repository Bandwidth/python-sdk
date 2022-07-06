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

    def test_generate_messaging_code(self):
        """Test case for generate_messaging_code

        Messaging Authentication Code  # noqa: E501
        """
        pass

    def test_generate_voice_code(self):
        """Test case for generate_voice_code

        Voice Authentication Code  # noqa: E501
        """
        pass

    def test_verify_code(self):
        """Test case for verify_code

        Verify Authentication Code  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
