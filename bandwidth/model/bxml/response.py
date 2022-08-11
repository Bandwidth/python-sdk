"""
response.py

Class that allows user to generate BXML programatically in python

@copyright Bandwidth INC
"""

RESPONSE_TAG = "Response"
XML_HEADER = '<?xml version="1.0" encoding="UTF-8"?>'


class Response:

    def __init__(self):
        """
        Creates the Response class 
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
        Converts the Response class to its XML representation

        :rtype str: The XML representation of the Response class
        """
        xml_string = XML_HEADER
        xml_string += '<' + RESPONSE_TAG + '>'
        for verb in self.verbs:
            xml_string += verb.to_bxml()
        xml_string += '</' + RESPONSE_TAG + '>' 

        return xml_string
