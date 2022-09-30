"""
bridge.py

Bandwidth's Bridge BXML verb

@copyright Bandwidth INC
"""
from ..terminal_verb import TerminalVerb


class Bridge(TerminalVerb):

    def __init__(
        self, target_call: str, bridge_complete_url: str=None,
        bridge_complete_method: str=None,
        bridge_complete_fallback_url: str=None,
        bridge_complete_fallback_method: str=None,
        bridge_target_complete_url: str=None,
        bridge_target_complete_method: str=None,
        bridge_target_complete_fallback_url: str=None,
        bridge_target_complete_fallback_method: str=None,
        username: str=None, password: str=None,
        fallback_username: str=None, fallback_password: str=None,
        tag: str=None
    ):
        """Initialize a <Bridge> verb

        Args:
            target_call (str): _description_
            bridge_complete_url (str, optional): _description_. Defaults to None.
            bridge_complete_method (str, optional): _description_. Defaults to None.
            bridge_complete_fallback_url (str, optional): _description_. Defaults to None.
            bridge_complete_fallback_method (str, optional): _description_. Defaults to None.
            bridge_target_complete_url (str, optional): _description_. Defaults to None.
            bridge_target_complete_method (str, optional): _description_. Defaults to None.
            bridge_target_complete_fallback_url (str, optional): _description_. Defaults to None.
            bridge_target_complete_fallback_method (str, optional): _description_. Defaults to None.
            username (str, optional): _description_. Defaults to None.
            password (str, optional): _description_. Defaults to None.
            fallback_username (str, optional): _description_. Defaults to None.
            fallback_password (str, optional): _description_. Defaults to None.
            tag (str, optional): _description_. Defaults to None.
        """
        self.target_call = target_call
        self.bridge_complete_url = bridge_complete_url
        self.bridge_complete_method = bridge_complete_method
        self.bridge_complete_fallback_url = bridge_complete_fallback_url
        self.bridge_complete_fallback_method = bridge_complete_fallback_method
        self.bridge_target_complete_url = bridge_target_complete_url
        self.bridge_target_complete_method = bridge_target_complete_method
        self.bridge_target_complete_fallback_url = bridge_target_complete_fallback_url
        self.bridge_target_complete_fallback_method = bridge_target_complete_fallback_method
        self.username = username
        self.password = password
        self.fallback_username = fallback_username
        self.fallback_password = fallback_password
        self.tag = tag
        self.attributes = {
            "bridgeCompleteUrl": self.bridge_complete_url,
            "bridgeCompleteMethod": self.bridge_complete_method,
            "bridgeCompleteFallbackUrl": self.bridge_complete_fallback_url,
            "bridgeCompleteFallbackMethod": self.bridge_complete_fallback_method,
            "bridgeTargetCompleteUrl": self.bridge_target_complete_url,
            "bridgeTargetCompleteMethod": self.bridge_target_complete_method,
            "bridgeTargetCompleteFallback_url": self.bridge_target_complete_fallback_url,
            "bridgeTargetCompleteFallbackMethod": self.bridge_target_complete_fallback_method,
            "username": self.username,
            "password": self.password,
            "fallbackUsername": self.fallback_username,
            "fallbackPassword": self.fallback_password,
            "tag": self.tag
        }
        super().__init__(
            tag="Bridge",
            content=self.target_call,
            attributes=self.attributes,
            nested_verbs=None
        )
