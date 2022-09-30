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
        self.attributes = {
            "bridgeCompleteUrl": bridge_complete_url,
            "bridgeCompleteMethod": bridge_complete_method,
            "bridgeCompleteFallbackUrl": bridge_complete_fallback_url,
            "bridgeCompleteFallbackMethod": bridge_complete_fallback_method,
            "bridgeTargetCompleteUrl": bridge_target_complete_url,
            "bridgeTargetCompleteMethod": bridge_target_complete_method,
            "bridgeTargetCompleteFallback_url": bridge_target_complete_fallback_url,
            "bridgeTargetCompleteFallbackMethod": bridge_target_complete_fallback_method,
            "username": username,
            "password": password,
            "fallbackUsername": fallback_username,
            "fallbackUassword": fallback_password,
            "tag": tag
        }
        super().__init__(
            tag="Bridge",
            content=target_call,
            attributes=self.attributes,
            nested_verbs=None
        )
