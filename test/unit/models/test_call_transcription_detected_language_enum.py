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

from bandwidth.models.call_transcription_detected_language_enum import CallTranscriptionDetectedLanguageEnum

class TestCallTranscriptionDetectedLanguageEnum(unittest.TestCase):
    """CallTranscriptionDetectedLanguageEnum unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCallTranscriptionDetectedLanguageEnum(self):
        """Test CallTranscriptionDetectedLanguageEnum"""
        enus = CallTranscriptionDetectedLanguageEnum('en-US')
        esus = CallTranscriptionDetectedLanguageEnum('es-US')
        frfr = CallTranscriptionDetectedLanguageEnum('fr-FR')
        assert enus == 'en-US'
        assert esus == 'es-US'
        assert frfr == 'fr-FR'

if __name__ == '__main__':
    unittest.main()
