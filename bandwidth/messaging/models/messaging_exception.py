# -*- coding: utf-8 -*-

"""
bandwidth

This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class MessagingException(object):

    """Implementation of the 'MessagingException' model.

    TODO: type model description here.

    Attributes:
        mtype (string): TODO: type description here.
        description (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mtype": 'type',
        "description": 'description'
    }

    def __init__(self,
                 mtype=None,
                 description=None):
        """Constructor for the MessagingException class"""

        # Initialize members of the class
        self.mtype = mtype
        self.description = description

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
        mtype = dictionary.get('type')
        description = dictionary.get('description')

        # Return an object of this model
        return cls(mtype,
                   description)
