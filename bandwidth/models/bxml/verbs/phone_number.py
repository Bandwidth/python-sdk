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
        password: str=None, fallback_username: str=None, fallback_password: str=None, tag: str=None,
        uui: str=None
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
            uui (str, optional):  A comma-separated list of 'User-To-User' headers to be sent in the INVITE. The entire value cannot exceed 350 characters, including parameters and separators. Defaults to None.
        """
        self.number = number
        self.transfer_answer_url = transfer_answer_url
        self.transfer_answer_method = transfer_answer_method
        self.transfer_answer_fallback_url = transfer_answer_fallback_url
        self.transfer_answer_fallback_method = transfer_answer_fallback_method
        self.transfer_disconnect_url = transfer_disconnect_url
        self.transfer_disconnect_method = transfer_disconnect_method
        self.username = username
        self.password = password
        self.fallback_username = fallback_username
        self.fallback_password = fallback_password
        self.tag = tag
        self.uui = uui
        super().__init__(
            tag="PhoneNumber",
            content=self.number
        )

    @property
    def _attributes(self):
        return {
            "transferAnswerUrl": self.transfer_answer_url,
            "transferAnswerMethod": self.transfer_answer_method,
            "transferAnswerFallbackUrl": self.transfer_answer_fallback_url,
            "transferAnswerFallbackMethod": self.transfer_answer_fallback_method,
            "transferDisconnectUrl": self.transfer_disconnect_url,
            "transferDisconnectMethod": self.transfer_disconnect_method,
            "username": self.username,
            "password": self.password,
            "fallbackUsername": self.fallback_username,
            "fallbackPassword": self.fallback_password,
            "tag": self.tag,
            "uui": self.uui
        }
