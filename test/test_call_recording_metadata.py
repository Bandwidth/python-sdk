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
from bandwidth.model.call_direction_enum import CallDirectionEnum
from bandwidth.model.file_format_enum import FileFormatEnum
from bandwidth.model.transcription_metadata import TranscriptionMetadata
globals()['CallDirectionEnum'] = CallDirectionEnum
globals()['FileFormatEnum'] = FileFormatEnum
globals()['TranscriptionMetadata'] = TranscriptionMetadata
from bandwidth.model.call_recording_metadata import CallRecordingMetadata


class TestCallRecordingMetadata(unittest.TestCase):
    """CallRecordingMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCallRecordingMetadata(self):
        """Test CallRecordingMetadata"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CallRecordingMetadata()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
