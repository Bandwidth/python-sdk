"""
phone_number.py

Bandwidth's PhoneNumber BXML verb

@copyright Bandwidth INC
"""
from ..verb import Verb


class PhoneNumber(Verb):

    def __init__(
        self, number, transfer_answer_url="", transfer_answer_method="",
        transfer_answer_fallback_url="", transfer_answer_fallback_method="",
        transfer_disconnect_url="", transfer_disconnect_method="", username="",
        password="", fallback_username="", fallback_password="", tag=""
    ):
        """Initialize a <PhoneNumber> verb

        Args:
            phone_number (_type_): _description_
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
