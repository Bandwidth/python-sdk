"""
verb.py

Defines the base verb class for all BXML verbs

@copyright Bandwidth INC
"""
from __future__ import annotations
from typing import Union
import xml.etree.ElementTree as ET


class Verb:
    """Base class for BXML verbs
    """

    def __init__(self, tag: str, content: str = None, nested_verbs: list[Verb] = None):
        """Initialize the verb model

        Args:
            tag (str): Name of the XML element
            content (str, optional): XML element content. Defaults to None.
            nested_verbs (list[BxmlVerb], optional): XML element children. Defaults to None.
        """
        self._tag = tag
        self._content = content
        self._nested_verbs = nested_verbs
        if not self._nested_verbs:
            self._nested_verbs = []

    @property
    def _attributes(self) -> Union[None, dict]:
        return None

    def __len__(self) -> int:
        """Override default len method. Returns length of _nested_verbs array

        Returns:
            int: Length of self._nested_verbs
        """
        return len(self._nested_verbs)

    def __getitem__(self, position) -> Verb:
        """Override default getitem method. Makes the object iterable.

        Args:
            position (int): Desired self._nested_verbs list position

        Returns:
            BxmlVerb: Desired BXML verb
        """
        return self._nested_verbs[position]

    def _set_attributes(self, root: ET.Element):
        """Set XML attributes on an Element

        Args:
            root (ET.Element): XML Element to add attributes to
        """
        if self._attributes is not None:
            for key, value in self._attributes.items():
                if value is not None:
                    root.set(key.strip("_"), value)

    def _to_etree_element(self) -> ET.Element:
        """Generate an ET.Element object from a Verb Object

        Returns:
            ET.Element: ET.Element representation of Verb
        """
        root = ET.Element(self._tag)
        if self._content:
            root.text = self._content
        self._set_attributes(root)
        if self._nested_verbs:
            for verb in self._nested_verbs:
                root.append(verb._to_etree_element())
        return root

    def _generate_xml(self) -> ET.ElementTree:
        """Generates an XML dom

        Returns:
            ET.Element: The XML dom for the verb and its nested verbs
        """
        root = ET.Element(self._tag)
        if self._content:
            root.text = self._content
        self._set_attributes(root)
        if self._nested_verbs:
            for verb in self._nested_verbs:
                root.append(verb._to_etree_element())
        dom = ET.ElementTree(root)
        return dom

    def add_verb(self, verb) -> None:
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
        return ET.tostring(xml_document._root).decode('utf8')
