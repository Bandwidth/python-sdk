"""
redirect.py

Representation of Bandwidth's redirect BXML verb

@copyright Bandwidth INC
"""

from lxml import etree

from .base_verb import AbstractBxmlVerb

REDIRECT_TAG = "Redirect"


class Redirect(AbstractBxmlVerb):

    def __init__(self, redirect_url=None, redirect_method=None, tag=None, username=None, password=None,
                redirect_fallback_url=None, redirect_fallback_method=None,
                fallback_username=None, fallback_password=None):
        """
        Initializes the Redirect class with the following parameters

        :param str redirect_url: The url to retrieve the next BXML
        :param str redirect_method: The HTTP method used to retrieve the next url
        :param str tag: Optional tag to include in the callback
        :param str username: Username for http authentication on the redirect url
        :param str password: Password for http authentication on the redirect url
        :param str redirect_fallback_url: URL for fallback events
        :param str redirect_fallback_method: HTTP method for fallback events
        :param str fallback_username: Basic auth username for fallback events
        :param str fallback_password: Basic auth password for fallback events
        """
        self.redirect_url = redirect_url
        self.redirect_method = redirect_method
        self.tag = tag
        self.username = username
        self.password = password
        self.redirect_fallback_url = redirect_fallback_url
        self.redirect_fallback_method = redirect_fallback_method
        self.fallback_username = fallback_username
        self.fallback_password = fallback_password

    def to_bxml(self):
        root = etree.Element(REDIRECT_TAG)
        if self.redirect_url is not None:
            root.set("redirectUrl", self.redirect_url)
        if self.redirect_method is not None:
            root.set("redirectMethod", self.redirect_method)
        if self.tag is not None:
            root.set("tag", self.tag)
        if self.username is not None:
            root.set("username", self.username)
        if self.password is not None:
            root.set("password", self.password)
        if self.redirect_fallback_url is not None:
            root.set("redirectFallbackUrl", self.redirect_fallback_url)
        if self.redirect_fallback_method is not None:
            root.set("redirectFallbackMethod", self.redirect_fallback_method)
        if self.fallback_username is not None:
            root.set("fallbackUsername", self.fallback_username)
        if self.fallback_password is not None:
            root.set("fallbackPassword", self.fallback_password)
        return etree.tostring(root).decode()
