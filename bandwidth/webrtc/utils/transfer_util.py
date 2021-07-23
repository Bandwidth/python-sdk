"""
transfer_util.py

Method to generate the transfer BXML to connect WebRTC <-> phones

@copyright Bandwidth INC
"""

def generate_transfer_bxml(device_token: str, voice_call_id: str, sip_uri: str ='sip:sipx.webrtc.bandwidth.com:5060'):
    """
    Returns BXML string with WebRTC a device token to perform a SIP transfer
    """
    return '<?xml version="1.0" encoding="UTF-8"?><Response>' + generate_transfer_bxml_verb(device_token, voice_call_id, sip_uri) + '</Response>'

def generate_transfer_bxml_verb(device_token: str, voice_call_id: str, sip_uri: str ='sip:sipx.webrtc.bandwidth.com:5060'):
    """
    Returns the Transfer verb to perform the SIP transfer
    """
    return f'''<Transfer><SipUri uui="{voice_call_id};encoding=base64,{device_token};encoding=jwt">{sip_uri}</SipUri></Transfer>'''
