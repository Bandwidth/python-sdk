"""
transfer.py

Representation of Bandwidth's transfer BXML verb

@copyright Bandwidth INC
"""

from lxml import etree

from .base_verb import AbstractBxmlVerb

TRANSFER_TAG = "Transfer"


class Transfer(AbstractBxmlVerb):

    def __init__(self, transfer_caller_id=None, call_timeout=None, tag=None, transfer_complete_url=None,
                transfer_complete_method=None, username=None, password=None, diversion_treatment=None,
                diversion_reason=None, phone_numbers=None,
                transfer_complete_fallback_url=None, transfer_complete_fallback_method=None,
                fallback_username=None, fallback_password=None):
        """
        Initializes the Transfer class with the following parameters
        
        :param str transfer_caller_id: The phone number to make the transfer
        :param int call_timeout: The number of seconds to wait before timing out the transfer
        :param str tag: Custom tag to be included in callbacks
        :param str transfer_complete_url: The url to receive the transfer complete callback
        :param str transfer_complete_method: The HTTP method used to send the transfer complete callback
        :param str username: The username to authenticate on the transfer complete url
        :param str password: The password to authenticate on the transfer complete url
        :param str diversion_treatment: The diversion treatment for the call
        :param str diversion_reason: The diversion reason for the call
        :param list<PhoneNumber> phone_numbers: The numbers to receive the transferred call
        :param str transfer_complete_fallback_url: URL for fallback events
        :param str transfer_complete_fallback_method: HTTP method for fallback events
        :param str fallback_username: Basic auth username for fallback events
        :param str fallback_password: Basic auth password for fallback events
        """
        self.transfer_caller_id = transfer_caller_id
        self.call_timeout = call_timeout
        self.tag = tag
        self.transfer_complete_url = transfer_complete_url
        self.transfer_complete_method = transfer_complete_method
        self.username = username
        self.password = password
        self.diversion_treatment = diversion_treatment
        self.diversion_reason = diversion_reason
        self.phone_numbers = phone_numbers
        self.transfer_complete_fallback_url = transfer_complete_fallback_url
        self.transfer_complete_fallback_method = transfer_complete_fallback_method
        self.fallback_username = fallback_username
        self.fallback_password = fallback_password

    def to_bxml(self):
        root = etree.Element(TRANSFER_TAG)
        if self.transfer_caller_id is not None:
            root.set("transferCallerId", self.transfer_caller_id)
        if self.call_timeout is not None:
            root.set("callTimeout", str(self.call_timeout))
        if self.tag is not None:
            root.set("tag", self.tag)
        if self.transfer_complete_url is not None:
            root.set("transferCompleteUrl", self.transfer_complete_url)
        if self.transfer_complete_method is not None:
            root.set("transferCompleteMethod", self.transfer_complete_method)
        if self.username is not None:
            root.set("username", self.username)
        if self.password is not None:
            root.set("password", self.password)
        if self.diversion_treatment is not None:
            root.set("diversionTreatment", self.diversion_treatment)
        if self.diversion_reason is not None:
            root.set("diversionReason", self.diversion_reason)
        if self.transfer_complete_fallback_url is not None:
            root.set("transferCompleteFallbackUrl", self.transfer_complete_fallback_url)
        if self.transfer_complete_fallback_method is not None:
            root.set("transferCompleteFallbackMethod", self.transfer_complete_fallback_method)
        if self.fallback_username is not None:
            root.set("fallbackUsername", self.fallback_username)
        if self.fallback_password is not None:
            root.set("fallbackPassword", self.fallback_password)
        if self.phone_numbers is not None:
            for phone_number in self.phone_numbers:
                root.append(phone_number.to_etree_element())
        return etree.tostring(root).decode()
