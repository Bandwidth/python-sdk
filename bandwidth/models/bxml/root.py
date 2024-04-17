"""
root.py

Defines the base verb class for all BXML roots

@copyright Bandwidth INC
"""
import re
from typing import List
import xml.etree.ElementTree as ET

from bandwidth.models.bxml.verb import Verb


class Root:
    """Base class for BXML roots
    """
    ssml_regex = r"&lt;([a-zA-Z//].*?)&gt;"

    def __init__(self, tag: str, nested_verbs: List[Verb] = None):
        """Initialize instance of class

        Args:
            tag (str): The XML element name
            nested_verbs (list[BxmlVerb], optional): List of nested BXML verbs. Defaults to None.
        """
        self._tag = tag
        self._nested_verbs = nested_verbs
        if not self._nested_verbs:
            self._nested_verbs = []

    def __len__(self) -> int:
        """Override default len method. Returns length of _nested_verbs array

        Returns:
            int: Length of self._nested_verbs
        """
        return len(self._nested_verbs)

    def __getitem__(self, position: int) -> Verb:
        """Override default getitem method. Makes the object iterable.

        Args:
            position (int): Desired self._nested_verbs list position

        Returns:
            BxmlVerb: Desired BXML verb
        """
        return self._nested_verbs[position]

    def _generate_xml(self) -> ET.Element:
        """Generates an XML dom

        Returns:
            ET.Element: The XML dom for the verb and its nested verbs
        """
        root = ET.Element(self._tag)
        if self._nested_verbs:
            for verb in self._nested_verbs:
                root.append(verb._to_etree_element())
        dom = ET.ElementTree(root)
        return dom

    def add_verb(self, verb: Verb) -> None:
        """Add a verb to the object's nested_verbs array

        Args:
            verb (BxmlVerb): BXML verb to nest within the parent. Becomes a child xml element.
        """
        self._nested_verbs.append(verb)

    def to_bxml(self) -> str:
        """Return the serialized BXML string

        Returns:
            str: Serialized BXML string
        """
        xml_document = self._generate_xml()
        return re.sub(self.ssml_regex, r"<\1>", ET.tostring(xml_document._root, encoding='UTF-8', method='xml', xml_declaration=True).decode("utf8"))
