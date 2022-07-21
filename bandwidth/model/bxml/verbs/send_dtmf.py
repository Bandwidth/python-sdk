"""
send_dtmf.py

Representation of Bandwidth's send dtmf BXML verb

@copyright Bandwidth INC
"""

from lxml import etree

from .base_verb import AbstractBxmlVerb

SEND_DTMF_TAG = "SendDtmf"


class SendDtmf(AbstractBxmlVerb):

    def __init__(self, dtmf, tone_duration=None, tone_interval=None):
        """
        Initializes the SendDtmf class with the dtmf parameter

        :param str dtmf: The dtmf to build the SendDtmf verb
        :param double tone_duration: The length in milliseconds of each DTMF tone
        :param double tone_interval: The duration of silence in milliseconds following each DTMF tone
        """
        self.dtmf = dtmf
        self.tone_duration = tone_duration
        self.tone_interval = tone_interval

    def to_bxml(self):
        root = etree.Element(SEND_DTMF_TAG)
        root.text = self.dtmf
        if self.tone_duration is not None:
            root.set("toneDuration", str(self.tone_duration))
        if self.tone_interval is not None:
            root.set("toneInterval", str(self.tone_interval))

        return etree.tostring(root).decode()
