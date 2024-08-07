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

from bandwidth.models.call_transcription_response import CallTranscriptionResponse

class TestCallTranscriptionResponse(unittest.TestCase):
    """CallTranscriptionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CallTranscriptionResponse:
        """Test CallTranscriptionResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        if include_optional:
            return CallTranscriptionResponse(
                account_id = '9900000',
                call_id = 'c-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85',
                transcription_id = 't-3f758f24-c7a2fc78-7c91-401a-8b2e-e542f9c40d6b',
                tracks = [{"detectedLanguage":"en-US","track":"inbound","transcript":"Hello World! This is an example.","confidence":0.9}]
            )
        else:
            return CallTranscriptionResponse(
        )

    def testCallTranscriptionResponse(self):
        """Test CallTranscriptionResponse"""
        instance = self.make_instance(True)
        assert instance is not None
        assert isinstance(instance, CallTranscriptionResponse)
        assert instance.account_id == '9900000'
        assert instance.call_id == 'c-15ac29a2-1331029c-2cb0-4a07-b215-b22865662d85'
        assert instance.transcription_id == 't-3f758f24-c7a2fc78-7c91-401a-8b2e-e542f9c40d6b'
        assert instance.tracks[0].detected_language == 'en-US'
        assert instance.tracks[0].track == 'inbound'
        assert instance.tracks[0].transcript == 'Hello World! This is an example.'
        assert instance.tracks[0].confidence == 0.9

if __name__ == '__main__':
    unittest.main()
