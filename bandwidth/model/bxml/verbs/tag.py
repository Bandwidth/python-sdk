"""
play_audio.py

Representation of Bandwidth's play audio BXML verb

@copyright Bandwidth INC
"""

from lxml import etree

from .base_verb import AbstractBxmlVerb

TAG_TAG = "Tag"


class Tag(AbstractBxmlVerb):

    def __init__(self, tag=None):
        """
        Initializes the Tag class with the following parameters

        :param str tag: The tag to set the call to 
        """
        self.tag = tag

    def to_etree_element(self):
        """
        Converts the class into an etree element. Used for other verb classes to build xml

        :return etree.Element: The etree Element representing this class
        """
        root = etree.Element(TAG_TAG)
        if self.tag is not None:
            root.text = self.tag
        return root

    def to_bxml(self):
        return etree.tostring(self.to_etree_element()).decode()
