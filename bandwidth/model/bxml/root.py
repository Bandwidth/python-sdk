"""
root.py

Defines the base verb class for all BXML roots

@copyright Bandwidth INC
"""
import xml.etree.ElementTree as ET

from bandwidth.model.bxml.verb import BxmlVerb


class BxmlRoot:

    def __init__(self, tag: str, nested_verbs: list[BxmlVerb] = None):
        self.tag = tag
        self._nested_verbs = nested_verbs
        if not self._nested_verbs:
            self._nested_verbs = []

    def __len__(self) -> int:
        return len(self._nested_verbs)
    
    def __getitem__(self, position) -> BxmlVerb:
        return self._nested_verbs[position]
    
    def _generate_xml(self) -> ET.Element:
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
        return ET.tostring(xml_document._root, pretty_print=False, encoding='utf8', method='xml').decode("utf8")

