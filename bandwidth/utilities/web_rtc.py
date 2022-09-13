from bandwidth.model.bxml.response import Response
from bandwidth.model.bxml.verbs import *


def generate_transfer_verb(device_token: str, voice_call_id: str, sip_uri: str = 'sip:sipx.webrtc.bandwidth.com:5060') -> str:
    """Returns the Transfer verb to perform the SIP transfer without the Response wrapper

    Args:
        device_token (str): The device token.
        voice_call_id (str): The Bandwidth voice Call ID.
        sip_uri (str, optional): The SIP URI to transfer the call to. Defaults to 'sip:sipx.webrtc.bandwidth.com:5060'.

    Returns:
        str: <Transfer> BXML Verb
    """
    uui = "".join(voice_call_id.split("-")[1::])
    sip_uri = SipUri(
        uui=f"{uui};encoding=base64,{device_token};encoding=jwt",
        uri=sip_uri
    )
    transfer = Transfer(
        sip_uris=[sip_uri]

    )
    return transfer.to_bxml()


def generate_transfer_bxml(device_token: str, voice_call_id: str, sip_uri: str = 'sip:sipx.webrtc.bandwidth.com:5060') -> str:
    """Generate BXML document with WebRTC a device token to perform a SIP transfer

    Args:
        device_token (str): The device token.
        voice_call_id (str): The Bandwidth voice Call ID.
        sip_uri (str, optional): The SIP URI to transfer the call to. Defaults to 'sip:sipx.webrtc.bandwidth.com:5060'.

    Returns:
        str: BXML document with transfer BXML
    """
    uui = "".join(voice_call_id.split("-")[1::])
    transfer_bxml = Response()
    sip_uri = SipUri(
        uui=f"{uui};encoding=base64,{device_token};encoding=jwt",
        uri=sip_uri
    )
    transfer = Transfer(
        sip_uris=[sip_uri]
    )
    transfer_bxml.add_verb(transfer)
    return transfer_bxml.to_bxml()
