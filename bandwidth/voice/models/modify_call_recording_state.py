# -*- coding: utf-8 -*-

"""
bandwidth

This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class ModifyCallRecordingState(object):

    """Implementation of the 'ModifyCallRecordingState' model.

    TODO: type model description here.

    Attributes:
        state (State2Enum): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "state": 'state'
    }

    def __init__(self,
                 state=None):
        """Constructor for the ModifyCallRecordingState class"""

        # Initialize members of the class
        self.state = state

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
        state = dictionary.get('state')

        # Return an object of this model
        return cls(state)
