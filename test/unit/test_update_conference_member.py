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
from bandwidth.models.update_conference_member import UpdateConferenceMember  # noqa: E501
from bandwidth.rest import ApiException

class TestUpdateConferenceMember(unittest.TestCase):
    """UpdateConferenceMember unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UpdateConferenceMember
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateConferenceMember`
        """
        model = bandwidth.models.update_conference_member.UpdateConferenceMember()  # noqa: E501
        if include_optional :
            return UpdateConferenceMember(
                mute = False, 
                hold = False, 
                call_ids_to_coach = ["c-25ac29a2-1331029c-2cb0-4a07-b215-b22865662d85"]
            )
        else :
            return UpdateConferenceMember(
        )
        """

    def testUpdateConferenceMember(self):
        """Test UpdateConferenceMember"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
