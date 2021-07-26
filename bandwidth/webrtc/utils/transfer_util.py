"""
transfer_util.py

Method to generate the transfer BXML to connect WebRTC <-> phones

@copyright Bandwidth INC
"""

def generate_transfer_bxml(device_token, voice_call_id, sip_uri='sip:sipx.webrtc.bandwidth.com:5060'):
    """
    Returns BXML string with WebRTC a device token to perform a SIP transfer
    :param device_token: The device token
    :param voice_call_id: The Bandwidth Voice Call Id
    :param sip_uri: The SIP URI to transfer the call to 
    """
    return '<?xml version="1.0" encoding="UTF-8"?><Response>' + generate_transfer_bxml_verb(device_token, voice_call_id, sip_uri) + '</Response>'

def generate_transfer_bxml_verb(device_token, voice_call_id, sip_uri='sip:sipx.webrtc.bandwidth.com:5060'):
    """
    Returns the Transfer verb to perform the SIP transfer
    :param device_token: The device token
    :param voice_call_id: The Bandwidth Voice Call Id
    :param sip_uri: The SIP URI to transfer the call to 
    """
    return f'''<Transfer><SipUri uui="{"".join(voice_call_id.split("-")[1::])};encoding=base64,{device_token};encoding=jwt">{sip_uri}</SipUri></Transfer>'''
