"""
phone_number.py

Representation of Bandwidth's phone number BXML verb

@copyright Bandwidth INC
"""

from lxml import etree

from .base_verb import AbstractBxmlVerb

PHONE_NUMBER_TAG = "PhoneNumber"


class PhoneNumber(AbstractBxmlVerb):

    def __init__(self, number=None, transfer_answer_url=None, transfer_answer_method=None,
                username=None, password=None, tag=None, transfer_disconnect_url=None, transfer_disconnect_method=None,
                transfer_answer_fallback_url=None, transfer_answer_fallback_method=None,
                fallback_username=None, fallback_password=None):
        """
        Initializes the PhoneNumber class with the following parameters

        :param str number: The phone number
        :param str transfer_answer_url: The url to send the transfer event to
        :param str transfer_answer_method: The http method of the transfer event request
        :param str transfer_disconnect_url: The url to send the transfer disconnect event to
        :param str transfer_disconnect_method: The http method of the transfer disconnect event request
        :param str username: The username to authenticate on the transfer event url
        :param str password: The password to authenticate on the transfer event url
        :param str tag: Custom string sent in the callback
        :param str transfer_answer_fallback_url: URL for fallback events
        :param str transfer_answer_fallback_method: HTTP method for fallback events
        :param str fallback_username: Basic auth username for fallback events
        :param str fallback_password: Basic auth password for fallback events
        """
        self.number = number
        self.transfer_answer_url = transfer_answer_url
        self.transfer_answer_method = transfer_answer_method
        self.username = username
        self.password = password
        self.tag = tag
        self.transfer_disconnect_method = transfer_disconnect_method
        self.transfer_disconnect_url = transfer_disconnect_url
        self.transfer_answer_fallback_url = transfer_answer_fallback_url
        self.transfer_answer_fallback_method = transfer_answer_fallback_method
        self.fallback_username = fallback_username
        self.fallback_password = fallback_password

    def to_etree_element(self):
        """
        Converts the class into an etree element. Used for other verb classes to build xml

        :return etree.Element: The etree Element representing this class
        """
        root = etree.Element(PHONE_NUMBER_TAG)
        if self.number is not None:
            root.text = self.number
        if self.transfer_answer_url is not None:
            root.set("transferAnswerUrl", self.transfer_answer_url)
        if self.transfer_answer_method is not None:
            root.set("transferAnswerMethod", self.transfer_answer_method)
        if self.username is not None:
            root.set("username", self.username)
        if self.password is not None:
            root.set("password", self.password)
        if self.tag is not None:
            root.set("tag", self.tag)
        if self.transfer_disconnect_method is not None:
            root.set("transferDisconnectMethod", self.transfer_disconnect_method)
        if self.transfer_disconnect_url is not None:
            root.set("transferDisconnectUrl", self.transfer_disconnect_url)
        if self.transfer_answer_fallback_url is not None:
            root.set("transferAnswerFallbackUrl", self.transfer_answer_fallback_url)
        if self.transfer_answer_fallback_method is not None:
            root.set("transferAnswerFallbackMethod", self.transfer_answer_fallback_method)
        if self.fallback_username is not None:
            root.set("fallbackUsername", self.fallback_username)
        if self.fallback_password is not None:
            root.set("fallbackPassword", self.fallback_password)
        return root

    def to_bxml(self):
        return etree.tostring(self.to_etree_element()).decode()
