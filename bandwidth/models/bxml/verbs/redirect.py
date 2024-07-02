"""
redirect.py

Bandwidth's Redirect BXML verb

@copyright Bandwidth INC
"""
from ..verb import Verb


class Redirect(Verb):

    def __init__(
        self, redirect_url: str, redirect_method: str = None,
        redirect_fallback_url: str = None,
        redirect_fallback_method: str = None, username: str = None,
        password: str = None, fallback_username: str = None,
        fallback_password: str = None, tag: str = None
    ):
        """Initialize a <Redirect> verb

        Args:
            redirect_url (str): URL to request new BXML from. A Redirect event will be sent to this endpoint. May be a relative URL. Defaults to None.
            redirect_method (str, optional): The HTTP method to use for the request to redirectUrl. GET or POST. Defaults to None.
            redirect_fallback_url (str, optional): A fallback url which, if provided, will be used to retry the Redirect callback delivery in case redirectUrl fails to respond. Defaults to None.
            redirect_fallback_method (str, optional): The HTTP method to use to deliver the Redirect callback to redirectFallbackUrl. GET or POST. Default value is POST. Defaults to None.
            username (str, optional): The username to send in the HTTP request to redirectUrl. Defaults to None.
            password (str, optional): The password to send in the HTTP request to redirectUrl. Defaults to None.
            fallback_username (str, optional): The username to send in the HTTP request to redirectFallbackUrl. Defaults to None.
            fallback_password (str, optional): The password to send in the HTTP request to redirectFallbackUrl. Defaults to None.
            tag (str, optional): A custom string that will be sent with this and all future callbacks unless overwritten by a future tag attribute or <Tag> verb, or cleared. May be cleared by setting tag="". Max length 256 characters. Defaults to None.
        """
        self.redirect_url = redirect_url
        self.redirect_method = redirect_method
        self.redirect_fallback_url = redirect_fallback_url
        self.redirect_fallback_method = redirect_fallback_method
        self.username = username
        self.password = password
        self.fallback_username = fallback_username
        self.fallback_password = fallback_password
        self.tag = tag
        super().__init__(tag="Redirect")

    @property
    def _attributes(self):
        return {
            "redirectUrl": self.redirect_url,
            "redirectMethod": self.redirect_method,
            "redirectFallbackUrl": self.redirect_fallback_url,
            "redirectFallbackMethod": self.redirect_fallback_method,
            "username": self.username,
            "password": self.password,
            "fallbackUsername": self.fallback_username,
            "fallbackPassword": self.fallback_password,
            "tag": self.tag,
        }
