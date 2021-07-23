"""
webrtc_bxml_tests.py

Unit tests for WebRtc's BXML

@copyright Bandwidth INC
"""
from bandwidth.webrtc.utils import *

import unittest


class WebRtcBxmlTests(unittest.TestCase):
    """
    Class for the WebRtc BXML tests
    """
    def test_generate_transfer_bxml(self):
        expected = '<?xml version="1.0" encoding="UTF-8"?><Response><Transfer><SipUri uui="93d6f3c0be5845960b744fa28015d8ede84bd1a4;encoding=base64,asdf;encoding=jwt">sip:sipx.webrtc.bandwidth.com:5060</SipUri></Transfer></Response>'
        actual = generate_transfer_bxml('asdf', 'c-93d6f3c0-be584596-0b74-4fa2-8015-d8ede84bd1a4')
        self.assertEqual(actual, expected)
    
    def test_generate_transfer_bxml_verb(self):
        expected = '<Transfer><SipUri uui="93d6f3c0be5845960b744fa28015d8ede84bd1a4;encoding=base64,asdf;encoding=jwt">sip:sipx.webrtc.bandwidth.com:5060</SipUri></Transfer>'
        actual = generate_transfer_bxml_verb('asdf', 'c-93d6f3c0-be584596-0b74-4fa2-8015-d8ede84bd1a4')
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
