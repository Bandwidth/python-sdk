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

from bandwidth.models.call_transcription_track_enum import CallTranscriptionTrackEnum

class TestCallTranscriptionTrackEnum(unittest.TestCase):
    """CallTranscriptionTrackEnum unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCallTranscriptionTrackEnum(self):
        """Test CallTranscriptionTrackEnum"""
        inbound = CallTranscriptionTrackEnum('inbound')
        outbound = CallTranscriptionTrackEnum('outbound')
        assert inbound == 'inbound'
        assert outbound == 'outbound'

if __name__ == '__main__':
    unittest.main()
