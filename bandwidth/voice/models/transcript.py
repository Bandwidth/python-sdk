# -*- coding: utf-8 -*-

"""
bandwidth

This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class Transcript(object):

    """Implementation of the 'Transcript' model.

    TODO: type model description here.

    Attributes:
        text (string): TODO: type description here.
        confidence (float): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "text": 'text',
        "confidence": 'confidence'
    }

    def __init__(self,
                 text=None,
                 confidence=None):
        """Constructor for the Transcript class"""

        # Initialize members of the class
        self.text = text
        self.confidence = confidence

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        text = dictionary.get('text')
        confidence = dictionary.get('confidence')

        # Return an object of this model
        return cls(text,
                   confidence)