"""
verb.py

Defines the base verb class for all BXML verbs

@copyright Bandwidth INC
"""
from __future__ import annotations
import xml.etree.ElementTree as ET


class BxmlVerb:

    def __init__(self, tag: str, content: str = None, attributes: dict = None, nested_verbs: list[BxmlVerb] = None):
        self._tag = tag
        self._content = content
        self._attributes = attributes
        self._nested_verbs = nested_verbs
        if not self._nested_verbs:
            self._nested_verbs = []

    def __len__(self) -> int:
        return len(self._nested_verbs)
    
    def __getitem__(self, position) -> BxmlVerb:
        return self._nested_verbs[position]
    
    def _to_etree_element(self) -> ET.Element:
        root = ET.Element(self._tag)
        if self._content:
            root.text = self._content
        if self._attributes:
            for key, value in self._attributes:
                if value:
                    root.set(key, value)
        if self._nested_verbs:
            for verb in self._nested_verbs:
                root.append(verb._to_etree_element())
        return root

    def _generate_xml(self) -> ET.ElementTree:
        root = ET.Element(self.tag)
        if self._nested_verbs:
            for verb in self._nested_verbs:
                root.append(verb._to_etree_element())
        dom = ET.ElementTree(root)
        return dom

    def add_verb(self, verb) -> None:
        self._nested_verbs.append(verb)

    def to_bxml(self) -> str:
        xml_document = self._generate_xml()
        return ET.tostring(xml_document._root)
