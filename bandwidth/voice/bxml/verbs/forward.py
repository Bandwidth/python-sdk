"""
forward.py

Representation of Bandwidth's forward BXML verb

@copyright Bandwidth INC
"""

from lxml import etree

from .base_verb import AbstractBxmlVerb

FORWARD_TAG = "Forward"


class Forward(AbstractBxmlVerb):

    def __init__(self, to=None, from_=None, call_timeout=None, diversion_treatment=None, diversion_reason=None):
        """
        Initializes the Forward class with the following parameters

        :param str to: The phone number destination of the call
        :param str from_: The phone number that the recipient will receive the call from
        :param int call_timeout: The number of seconds to wait before timing out the call
        :param str diversion_treatment: The diversion treatment for the call
        :param str diversion_reason: The diversion reason for the call
        """
        self.to = to
        self.from_ = from_
        self.call_timeout = str(call_timeout)
        self.diversion_treatment = diversion_treatment
        self.diversion_reason = diversion_reason

    def to_bxml(self):
        root = etree.Element(FORWARD_TAG)
        if self.to is not None:
            root.set("to", self.to)
        if self.call_timeout is not None:
            root.set("callTimeout", self.call_timeout)
        if self.from_ is not None:
            root.set("from", self.from_)
        if self.diversion_treatment is not None:
            root.set("diversionTreatment", self.diversion_treatment)
        if self.diversion_reason is not None:
            root.set("diversionReason", self.diversion_reason)
        return etree.tostring(root).decode()
