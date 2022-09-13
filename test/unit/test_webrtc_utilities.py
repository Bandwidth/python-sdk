from bandwidth.utilities.web_rtc import *


class TestWebRtcUtilities:
    """
    Class for the WebRTC Utilities Tests
    """

    def test_generate_transfer_bxml(self):
        expected = '<?xml version="1.0" encoding="UTF-8"?><Response><Transfer><SipUri uui="93d6f3c0be5845960b744fa28015d8ede84bd1a4;encoding=base64,asdf;encoding=jwt">sip:sipx.webrtc.bandwidth.com:5060</SipUri></Transfer></Response>'
        actual = generate_transfer_bxml(
            'asdf', 'c-93d6f3c0-be584596-0b74-4fa2-8015-d8ede84bd1a4')
        assert actual == expected

    def test_generate_transfer_verb(self):
        expected = '<Transfer><SipUri uui="93d6f3c0be5845960b744fa28015d8ede84bd1a4;encoding=base64,asdf;encoding=jwt">sip:sipx.webrtc.bandwidth.com:5060</SipUri></Transfer>'
        actual = generate_transfer_verb(
            'asdf', 'c-93d6f3c0-be584596-0b74-4fa2-8015-d8ede84bd1a4')
        assert actual == expected
