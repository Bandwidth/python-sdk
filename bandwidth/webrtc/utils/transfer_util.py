"""
transfer_util.py

Method to generate the transfer BXML to connect WebRTC <-> phones

@copyright Bandwidth INC
"""

def generate_transfer_bxml(deviceToken, sip_uri='sip:sipx.webrtc.bandwidth.com:5060'):
    """
    Returns BXML string with WebRTC a device token to perform a SIP transfer
    """
    return f'''
<?xml version="1.0" encoding="UTF-8" ?>
<Transfer>
    <SipUri uui="{deviceToken};encoding=jwt">{sip_uri}</SipUri>
</Transfer>'''
