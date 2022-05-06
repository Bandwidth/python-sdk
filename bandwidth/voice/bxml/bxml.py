"""
bxml.py

Class that allows user to generate BXML programatically in python
BXML is the parent element

@copyright Bandwidth INC
"""

BXML_TAG = "Bxml"
XML_HEADER = '<?xml version="1.0" encoding="UTF-8"?>'


class Bxml:

    def __init__(self):
        """
        Creates the Bxml class 
        """
        self.verbs = []

    def add_verb(self, verb):
        """
        Adds the Verb to the already existing verbs

        :param Verb verb: The Verb to add
        """
        self.verbs.append(verb)

    def to_bxml(self):
        """
        Converts the Bxml class to its XML representation

        :rtype str: The XML representation of the Bxml class
        """
        xml_string = XML_HEADER
        xml_string += '<' + BXML_TAG + '>'
        for verb in self.verbs:
            xml_string += verb.to_bxml()
        xml_string += '</' + BXML_TAG + '>' 

        return xml_string
