"""
start_stream.py

Representation of Bandwidth's start stream BXML verb

@copyright Bandwidth INC
"""

from lxml import etree

from .base_verb import AbstractBxmlVerb

STOP_STREAM_TAG = "StopStream"


class StopStream(AbstractBxmlVerb):

    def __init__(self, name):
        """
        Initializes the PlayAudio class with the following parameters

        :param str name: The name of the stream to stop
        """
        self.name = name

    def to_etree_element(self):
        """
        Converts the class into an etree element. Used for other verb classes to build xml

        :return etree.Element: The etree Element representing this class
        """
        root = etree.Element(STOP_STREAM_TAG)
        root.set("name", self.name)
        return root

    def to_bxml(self):
        return etree.tostring(self.to_etree_element()).decode()
