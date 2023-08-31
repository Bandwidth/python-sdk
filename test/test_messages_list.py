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
from bandwidth.models.messages_list import MessagesList  # noqa: E501
from bandwidth.rest import ApiException

class TestMessagesList(unittest.TestCase):
    """MessagesList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MessagesList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MessagesList`
        """
        model = bandwidth.models.messages_list.MessagesList()  # noqa: E501
        if include_optional :
            return MessagesList(
                total_count = 100, 
                page_info = bandwidth.models.page_info.PageInfo(
                    prev_page = 'https://messaging.bandwidth.com/api/v2/users/accountId/messages?messageStatus=DLR_EXPIRED&nextPage=DLAPE902', 
                    next_page = 'https://messaging.bandwidth.com/api/v2/users/accountId/messages?messageStatus=DLR_EXPIRED&prevPage=GL83PD3C', 
                    prev_page_token = 'DLAPE902', 
                    next_page_token = 'GL83PD3C', ), 
                messages = [
                    bandwidth.models.list_message_item.listMessageItem(
                        message_id = '1589228074636lm4k2je7j7jklbn2', 
                        account_id = '9900000', 
                        source_tn = '+15554443333', 
                        destination_tn = '+15554442222', 
                        message_status = 'RECEIVED', 
                        message_direction = 'INBOUND', 
                        message_type = 'sms', 
                        segment_count = 1, 
                        error_code = 9902, 
                        receive_time = '2020-04-07T14:03:07Z', 
                        carrier_name = 'other', 
                        message_size = 27, 
                        message_length = 18, 
                        attachment_count = 1, 
                        recipient_count = 1, 
                        campaign_class = 'T', 
                        campaign_id = 'CJEUMDK', )
                    ]
            )
        else :
            return MessagesList(
        )
        """

    def testMessagesList(self):
        """Test MessagesList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
