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
from bandwidth.models.transcription_list import TranscriptionList  # noqa: E501
from bandwidth.rest import ApiException

class TestTranscriptionList(unittest.TestCase):
    """TranscriptionList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TranscriptionList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TranscriptionList`
        """
        model = bandwidth.models.transcription_list.TranscriptionList()  # noqa: E501
        if include_optional :
            return TranscriptionList(
                transcripts = [
                    bandwidth.models.transcription.transcription(
                        text = 'Nice talking to you, friend!', 
                        confidence = 0.9, )
                    ]
            )
        else :
            return TranscriptionList(
        )
        """

    def testTranscriptionList(self):
        """Test TranscriptionList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
