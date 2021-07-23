"""
transfer_util.py

Method to generate the transfer BXML to connect WebRTC <-> phones

@copyright Bandwidth INC
"""

def generate_transfer_bxml(device_token: str, voice_call_id: str, sip_uri: str ='sip:sipx.webrtc.bandwidth.com:5060'):
    """
    Returns BXML string with WebRTC a device token to perform a SIP transfer
    :param device_token: The device token
    :param voice_call_id: The voice call id, used for debugging
    :param sip_uri: The uri of the sipx, if not specified it will take the default value
    """
    return '<?xml version="1.0" encoding="UTF-8"?><Response>' + generate_transfer_bxml_verb(device_token, voice_call_id, sip_uri) + '</Response>'

def generate_transfer_bxml_verb(device_token: str, voice_call_id: str, sip_uri: str ='sip:sipx.webrtc.bandwidth.com:5060'):
    """
    Returns the Transfer verb to perform the SIP transfer
    :param device_token: The device token
    :param voice_call_id: The voice call id, used for debugging
    :param sip_uri: The uri of the sipx, if not specified it will take the default value 
    """
    return f'''<Transfer><SipUri uui="{"".join(voice_call_id.split("-")[1::])};encoding=base64,{device_token};encoding=jwt">{sip_uri}</SipUri></Transfer>'''
