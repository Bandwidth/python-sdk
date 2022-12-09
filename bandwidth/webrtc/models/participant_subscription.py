# -*- coding: utf-8 -*-

"""
bandwidth

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class ParticipantSubscription(object):

    """Implementation of the 'ParticipantSubscription' model.

    TODO: type model description here.

    Attributes:
        participant_id (string): Participant the subscriber should be
            subscribed to

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "participant_id": 'participantId'
    }

    def __init__(self,
                 participant_id=None):
        """Constructor for the ParticipantSubscription class"""

        # Initialize members of the class
        self.participant_id = participant_id

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
        participant_id = dictionary.get('participantId')

        # Return an object of this model
        return cls(participant_id)