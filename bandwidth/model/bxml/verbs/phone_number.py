"""
phone_number.py

Bandwidth's PhoneNumber BXML verb

@copyright Bandwidth INC
"""
from ..verb import Verb


class PhoneNumber(Verb):

    def __init__(
        self, number: str, transfer_answer_url: str=None, transfer_answer_method: str=None,
        transfer_answer_fallback_url: str=None, transfer_answer_fallback_method: str=None,
        transfer_disconnect_url: str=None, transfer_disconnect_method: str=None, username: str=None,
        password: str=None, fallback_username: str=None, fallback_password: str=None, tag: str=None
    ):
        """Initialize a <PhoneNumber> verb

        Args:
            phone_number (str): A phone number to transfer the call to. Value must be in E.164 format (e.g. +15555555555).
            transfer_answer_url (str, optional): URL, if any, to send the Transfer Answer event to and request BXML to be executed for the called party before the call is bridged. May be a relative URL. Defaults to None.
            transfer_answer_method (str, optional): The HTTP method to use for the request to transferAnswerUrl. GET or POST. Default value is POST. Defaults to None.
            transfer_answer_fallback_url (str, optional): A fallback url which, if provided, will be used to retry the Transfer Answer callback delivery in case transferAnswerUrl fails to respond. Defaults to None.
            transfer_answer_fallback_method (str, optional): The HTTP method to use to deliver the Transfer Answer callback to transferAnswerFallbackUrl. GET or POST. Default value is POST. Defaults to None.
            transfer_disconnect_url (str, optional): URL, if any, to send the Transfer Disconnect event to. This event will be sent regardless of how the transfer ends and may not be responded to with BXML. May be a relative URL. Defaults to None.
            transfer_disconnect_method (str, optional): The HTTP method to use for the request to transferDisconnectUrl. GET or POST. Default value is POST. Defaults to Defaults to Defaults to None.
            username (str, optional): The username to send in the HTTP request to transferAnswerUrl and transferDisconnectUrl. Defaults to Defaults to None.
            password (str, optional): The password to send in the HTTP request to transferAnswerUrl and transferDisconnectUrl. Defaults to Defaults to None.
            fallback_username (str, optional): The username to send in the HTTP request to transferAnswerFallbackUrl. Defaults to None.
            fallback_password (str, optional): The password to send in the HTTP request to transferAnswerFallbackUrl. Defaults to None.
            tag (str, optional):  A custom string that will be sent with these and all future callbacks unless overwritten by a future tag attribute or cleared. May be cleared by setting tag="" Max length 256 characters. Defaults to None.
        """
        self.attributes = {
            "fallbackPassword": fallback_password,
            "fallbackUsername": fallback_username,
            "password": password,
            "tag": tag,
            "transferAnswerFallbackMethod": transfer_answer_fallback_method,
            "transferAnswerFallbackUrl": transfer_answer_fallback_url,
            "transferAnswerMethod": transfer_answer_method,
            "transferAnswerUrl": transfer_answer_url,
            "transferDisconnectMethod": transfer_disconnect_method,
            "transferDisconnectUrl": transfer_disconnect_url,
            "username": username
        }
        super().__init__(
            tag="PhoneNumber",
            content=number,
            attributes=self.attributes, 
            nested_verbs=None
        )
    
    def add_verb(self, verb: Verb):
        """Adding verbs is not allowed for <PhoneNumber>

        Args:
            verb (Verb): BXML verb

        Raises:
            AttributeError: This method is not allowed for <PhoneNumber>
        """
        raise AttributeError('Adding verbs is not supported by <PhoneNumber>')
