"""
phone_number.py

Representation of Bandwidth's phone number BXML verb

@copyright Bandwidth INC
"""

from lxml import etree

from .base_verb import AbstractBxmlVerb

PHONE_NUMBER_TAG = "PhoneNumber"


class PhoneNumber(AbstractBxmlVerb):

    def __init__(self, number=None, transfer_answer_url=None, transfer_answer_method=None, username=None, password=None, tag=None, transfer_disconnect_url=None, transfer_disconnect_method=None):
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
        """
        self.number = number
        self.transfer_answer_url = transfer_answer_url
        self.transfer_answer_method = transfer_answer_method
        self.username = username
        self.password = password
        self.tag = tag
        self.transfer_disconnect_method = transfer_disconnect_method
        self.transfer_disconnect_url = transfer_disconnect_url

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
        return root

    def to_bxml(self):
        return etree.tostring(self.to_etree_element()).decode()
