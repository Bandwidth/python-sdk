from bandwidth.model.bxml.response import Response
from bandwidth.model.bxml.verbs import *


def _generate_transfer_model(device_token: str, voice_call_id: str, sip_uri: str = 'sip:sipx.webrtc.bandwidth.com:5060') -> Transfer:
    """Generate a Transfer object for a WebRTC Session

    Args:
        device_token (str): The device token.
        voice_call_id (str): The Bandwidth voice Call ID.
        sip_uri (str, optional): The SIP URI to transfer the call to. Defaults to 'sip:sipx.webrtc.bandwidth.com:5060'.

    Returns:
        Transfer: Returns a Transfer BXML Verb Object
    """
    uui = "".join(voice_call_id.split("-")[1::])
    sip_uri = SipUri(
        uri=sip_uri,
        uui=f"{uui};encoding=base64,{device_token};encoding=jwt"
    )
    transfer = Transfer(
        transfer_to=[sip_uri]
    )
    return transfer


def generate_transfer_bxml_verb(device_token: str, voice_call_id: str, sip_uri: str = 'sip:sipx.webrtc.bandwidth.com:5060') -> str:
    """Returns the Transfer verb to perform the SIP transfer without the Response wrapper

    Args:
        device_token (str): The device token.
        voice_call_id (str): The Bandwidth voice Call ID.
        sip_uri (str, optional): The SIP URI to transfer the call to. Defaults to 'sip:sipx.webrtc.bandwidth.com:5060'.

    Returns:
        str: <Transfer> BXML Verb
    """
    return _generate_transfer_model(device_token, voice_call_id, sip_uri).to_bxml()


def generate_transfer_bxml(device_token: str, voice_call_id: str, sip_uri: str = 'sip:sipx.webrtc.bandwidth.com:5060') -> str:
    """Generate BXML document with WebRTC a device token to perform a SIP transfer

    Args:
        device_token (str): The device token.
        voice_call_id (str): The Bandwidth voice Call ID.
        sip_uri (str, optional): The SIP URI to transfer the call to. Defaults to 'sip:sipx.webrtc.bandwidth.com:5060'.

    Returns:
        str: BXML document with transfer BXML
    """
    response = Response()
    response.add_verb(_generate_transfer_model(device_token, voice_call_id, sip_uri))
    return response.to_bxml()
