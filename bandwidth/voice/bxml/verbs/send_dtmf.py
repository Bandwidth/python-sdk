"""
send_dtmf.py

Representation of Bandwidth's send dtmf BXML verb

@copyright Bandwidth INC
"""

from lxml import etree

from .base_verb import AbstractBxmlVerb

SEND_DTMF_TAG = "SendDtmf"


class SendDtmf(AbstractBxmlVerb):

    def __init__(self, dtmf):
        """
        Initializes the SendDtmf class with the dtmf parameter

        :param str dtmf: The dtmf to build the SendDtmf verb
        """
        self.dtmf = dtmf

    def to_bxml(self):
        root = etree.Element(SEND_DTMF_TAG)
        root.text = self.dtmf
        return etree.tostring(root).decode()
