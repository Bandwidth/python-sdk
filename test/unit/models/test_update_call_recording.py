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

from bandwidth.models.update_call_recording import UpdateCallRecording

class TestUpdateCallRecording(unittest.TestCase):
    """UpdateCallRecording unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateCallRecording:
        """Test UpdateCallRecording
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateCallRecording`
        """
        model = UpdateCallRecording()
        if include_optional:
            return UpdateCallRecording(
                state = 'paused'
            )
        else:
            return UpdateCallRecording(
                state = 'paused',
        )
        """

    def testUpdateCallRecording(self):
        """Test UpdateCallRecording"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
