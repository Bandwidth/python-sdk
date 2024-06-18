"""
nestable_verb.py

Defines the base nestable_verb class for all BXML verbs that can have nested verbs

@copyright Bandwidth INC
"""
from __future__ import annotations
import re
from typing import Union
import xml.etree.ElementTree as ET

from .verb import Verb


class NestableVerb(Verb):
    """Base class for nestable BXML verbs
    """
    ssml_regex = r"&lt;([a-zA-Z//].*?)&gt;"

    def __init__(self, tag: str, content: str = None, nested_verbs: list[Verb] = None):
        """Initialize the verb model

        Args:
            tag (str): Name of the XML element
            content (str, optional): XML element content. Defaults to None.
            nested_verbs (list[Verb], optional): XML element children. Defaults to None.
        """
        self._tag = tag
        self._content = content
        self._nested_verbs = nested_verbs
        if not self._nested_verbs:
            self._nested_verbs = []

    def _to_etree_element(self) -> ET.Element:
        """Generate an ET.Element object from a NestableVerb Object

        Returns:
            ET.Element: ET.Element representation of NestableVerb
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
            verb (Verb): BXML verb to nest within the parent. Becomes a child xml element.
        """
        self._nested_verbs.append(verb)
