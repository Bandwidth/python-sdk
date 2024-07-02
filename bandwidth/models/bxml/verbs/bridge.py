"""
bridge.py

Bandwidth's Bridge BXML verb

@copyright Bandwidth INC
"""
from ..verb import Verb


class Bridge(Verb):

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
            target_call (str): String containing the callId of the call to be bridged.
            bridge_complete_url (str, optional): URL to send the Bridge Complete event to and request new BXML.
                If this attribute is specified, then Verbs following the <Bridge> verb will be ignored and the BXML returned in this webhook is executed on the call.
                If this attribute is not specified then no webhook will be sent, and execution of the verbs following the <Bridge> verb continues. May be a relative URL. Defaults to None.
            bridge_complete_method (str, optional): The HTTP method to use for the request to bridgeCompleteUrl. GET or POST. Default value is POST.
            bridge_complete_fallback_url (str, optional): A fallback url which, if provided, will be used to retry the Bridge Complete webhook delivery in case bridgeCompleteUrl fails to respond. Defaults to None.
            bridge_complete_fallback_method (str, optional): The HTTP method to use to deliver the Bridge Complete webhook to bridgeCompleteFallbackUrl. GET or POST. Default value is POST.
            bridge_target_complete_url (str, optional):URL to send the Bridge Target Complete event to and request new BXML.
                If this attribute is specified, then the BXML returned in this webhook is executed on the target call.
                If this attribute is not specified then no webhook will be sent, and the target call will be hung up. May be a relative URL. Defaults to None.
            bridge_target_complete_method (str, optional): The HTTP method to use for the request to bridgeTargetCompleteUrl. GET or POST. Default value is POST.
            bridge_target_complete_fallback_url (str, optional): A fallback url which, if provided, will be used to retry the Bridge Target Complete webhook delivery in case bridgeTargetCompleteUrl fails to respond. Defaults to None.
            bridge_target_complete_fallback_method (str, optional): The HTTP method to use to deliver the Bridge Target Complete webhook to bridgeTargetCompleteFallbackUrl. GET or POST. Default value is POST.
            username (str, optional): The username to send in the HTTP request to bridgeCompleteUrl and to bridgeTargetCompleteUrl. Defaults to None.
            password (str, optional): The password to send in the HTTP request to bridgeCompleteUrl and to bridgeTargetCompleteUrl. Defaults to None.
            fallback_username (str, optional): The username to send in the HTTP request to bridgeCompleteFallbackUrl and to bridgeTargetCompleteFallbackUrl. Defaults to None.
            fallback_password (str, optional): The password to send in the HTTP request to bridgeCompleteFallbackUrl and to bridgeTargetCompleteFallbackUrl. Defaults to None.
            tag (str, optional): A custom string that will be sent with the bridgeComplete webhook and all future webhooks of the call unless overwritten by a future tag attribute or <Tag> verb, or cleared. May be cleared by setting tag="". Max length 256 characters. Defaults to None.
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
        super().__init__(
            tag="Bridge",
            content=self.target_call,
        )

    @property
    def _attributes(self):
        return {
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
