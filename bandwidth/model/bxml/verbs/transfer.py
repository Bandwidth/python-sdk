"""
transfer.py

Bandwidth's Transfer BXML verb

@copyright Bandwidth INC
"""
from typing import Union

from ..verb import Verb
from ..verbs.phone_number import PhoneNumber
from ..verbs.sip_uri import SipUri


class Transfer(Verb):

    def __init__(
        self, transfer_to: list[PhoneNumber, SipUri] = [], 
        transfer_caller_id="", call_timeout="", 
        transfer_complete_url="", transfer_complete_method="",
        transfer_complete_fallback_url="", 
        transfer_complete_fallback_method="", username="", 
        password="", fallback_username="", fallback_password="", 
        tag=""
    ):
        """Initialize a <Transfer> verb

        Args:
            transfer_to (list[PhoneNumber, SipUri], optional): _description_. Defaults to [].
            transfer_caller_id (str, optional): _description_. Defaults to "".
            call_timeout (str, optional): _description_. Defaults to "".
            transfer_complete_url (str, optional): _description_. Defaults to "".
            transfer_complete_method (str, optional): _description_. Defaults to "".
            transfer_complete_fallback_url (str, optional): _description_. Defaults to "".
            transfer_complete_fallback_method (str, optional): _description_. Defaults to "".
            username (str, optional): _description_. Defaults to "".
            password (str, optional): _description_. Defaults to "".
            fallback_username (str, optional): _description_. Defaults to "".
            fallback_password (str, optional): _description_. Defaults to "".
            tag (str, optional): _description_. Defaults to "".
        """
        self.attributes = {
            "transferCallerId": transfer_caller_id,
            "callTimeout": call_timeout,
            "transferCompleteUrl": transfer_complete_url,
            "transferCompleteMethod": transfer_complete_method,
            "transferCompleteFallbackUrl": transfer_complete_fallback_url,
            "transferCompleteFallbackMethod": transfer_complete_fallback_method,
            "username": username,
            "password": password,
            "fallbackUsername": fallback_username,
            "fallbackPassword": fallback_password,
            "tag": tag
        }
        super().__init__(
            tag="Transfer",
            content=None,
            attributes=self.attributes, 
            nested_verbs=transfer_to
        )
    
    def add_transfer_recipient(self, recipient: Union[PhoneNumber, SipUri]):
        super().add_verb(recipient)
