"""
sip_uri.py

Bandwidth's SipUri BXML verb

@copyright Bandwidth INC
"""
from ..verb import Verb


class SipUri(Verb):

    def __init__(
        self, uri, uui="", transfer_answer_url="", transfer_answer_method="",
        transfer_answer_fallback_url="", transfer_answer_fallback_method="",
        transfer_disconnect_url="", transfer_disconnect_method="", username="",
        password="", fallback_username="", fallback_password="", tag=""
    ):
        """Initialize a <SipUri> verb

        Args:
            uri (_type_): The value of the User-To-User header to send within the initial INVITE. Must include the encoding parameter as specified in RFC 7433. Only base64 and jwt encoding are currently allowed. This value, including the encoding specifier, may not exceed 256 characters.
            uui (str, optional): _description_. Defaults to "".
            transfer_answer_url (str, optional): _description_. Defaults to "".
            transfer_answer_method (str, optional): _description_. Defaults to "".
            transfer_answer_fallback_url (str, optional): _description_. Defaults to "".
            transfer_answer_fallback_method (str, optional): _description_. Defaults to "".
            transfer_disconnect_url (str, optional): _description_. Defaults to "".
            transfer_disconnect_method (str, optional): _description_. Defaults to "".
            username (str, optional): _description_. Defaults to "".
            password (str, optional): _description_. Defaults to "".
            fallback_username (str, optional): _description_. Defaults to "".
            fallback_password (str, optional): _description_. Defaults to "".
            tag (str, optional): _description_. Defaults to "".
        """
        self.attributes = {
            "uui": uui,
            "transferAnswerUrl": transfer_answer_url,
            "transferAnswerMethod": transfer_answer_method,
            "transferAnswerFallbackUrl": transfer_answer_fallback_url,
            "transferAnswerFallbackMethod": transfer_answer_fallback_method,
            "transferDisconnectUrl": transfer_disconnect_url,
            "transferDisconnectMethod": transfer_disconnect_method,
            "username": username,
            "password": password,
            "fallbackUsername": fallback_username,
            "fallbackPassword": fallback_password,
            "tag": tag
        }
        super().__init__(
            tag="SipUri",
            content=uri,
            attributes=self.attributes, 
            nested_verbs=None
        )
    
    def add_verb(self, verb: Verb):
        """Adding verbs is not allowed for <SipUri>

        Args:
            verb (Verb): BXML verb

        Raises:
            AttributeError: This method is not allowed for <SipUri>
        """
        raise AttributeError('Adding verbs is not supported by <SipUri>')
