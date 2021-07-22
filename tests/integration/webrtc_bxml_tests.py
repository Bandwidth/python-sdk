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
        expected = '<?xml version="1.0" encoding="UTF-8"?><Response><Transfer><SipUri uui="asdf;encoding=jwt">sip:sipx.webrtc.bandwidth.com:5060</SipUri></Transfer></Response>'
        actual = generate_transfer_bxml('asdf')
        self.assertEqual(actual, expected)
    
    def test_generate_transfer_bxml_verb(self):
        expected = '<Transfer><SipUri uui="asdf;encoding=jwt">sip:sipx.webrtc.bandwidth.com:5060</SipUri></Transfer>'
        actual = generate_transfer_bxml_verb('asdf')
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
