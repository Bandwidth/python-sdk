"""
custom_param.py

Representation of Bandwidth's StartTranscription BXML verb

@license MIT
"""

from lxml import etree

from .base_verb import AbstractBxmlVerb

CUSTOM_PARAM_TAG = "CustomParam"


class CustomParam(AbstractBxmlVerb):
    def __init__(
            self,
            name: str,
            value: str,
    ):
        """
        Initializes the CustomParam class
        :param name: The name of this parameter, up to 256 characters.
        :param value: The value of this parameter, up to 2048 characters.
        """
        self.name = name
        self.value = value

    def to_etree_element(self):
        root = etree.Element(CUSTOM_PARAM_TAG)
        root.set("name", self.name)
        root.set("value", self.value)
        return root

    def to_bxml(self):
        root = etree.Element(CUSTOM_PARAM_TAG)
        return etree.tostring(root).decode()
