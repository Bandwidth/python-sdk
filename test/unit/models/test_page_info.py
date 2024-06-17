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

from bandwidth.models.page_info import PageInfo

class TestPageInfo(unittest.TestCase):
    """PageInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PageInfo:
        """Test PageInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PageInfo`
        """
        model = PageInfo()
        if include_optional:
            return PageInfo(
                prev_page = 'https://messaging.bandwidth.com/api/v2/users/accountId/messages?messageStatus=DLR_EXPIRED&nextPage=DLAPE902',
                next_page = 'https://messaging.bandwidth.com/api/v2/users/accountId/messages?messageStatus=DLR_EXPIRED&prevPage=GL83PD3C',
                prev_page_token = 'DLAPE902',
                next_page_token = 'GL83PD3C'
            )
        else:
            return PageInfo(
        )
        """

    def testPageInfo(self):
        """Test PageInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()