"""
start_stream.py

Representation of Bandwidth's start stream BXML verb

@copyright Bandwidth INC
"""

from lxml import etree

from .base_verb import AbstractBxmlVerb

STREAM_PARAM_TAG = "StreamParam"


class StreamParam(AbstractBxmlVerb):

    def __init__(self, name, value):
        """
        Initializes the StreamParam class with the following parameters

        :param str name: The name of this parameter, up to 256 characters.
        :param str value: The value of this parameter, up to 2048 characters.
        """
        self.name = name
        self.value = value

    def to_etree_element(self):
        """
        Converts the class into an etree element. Used for other verb classes to build xml

        :return etree.Element: The etree Element representing this class
        """
        root = etree.Element(STREAM_PARAM_TAG)
        root.set("name", self.name)
        root.set("value", self.value)
        return root

    def to_bxml(self):
        return etree.tostring(self.to_etree_element()).decode()
