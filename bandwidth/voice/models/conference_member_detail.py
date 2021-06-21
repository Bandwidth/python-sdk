# -*- coding: utf-8 -*-

"""
bandwidth

This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class ConferenceMemberDetail(object):

    """Implementation of the 'ConferenceMemberDetail' model.

    TODO: type model description here.

    Attributes:
        call_id (string): TODO: type description here.
        conference_id (string): TODO: type description here.
        member_url (string): TODO: type description here.
        mute (bool): TODO: type description here.
        hold (bool): TODO: type description here.
        call_ids_to_coach (list of string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "call_id": 'callId',
        "conference_id": 'conferenceId',
        "member_url": 'memberUrl',
        "mute": 'mute',
        "hold": 'hold',
        "call_ids_to_coach": 'callIdsToCoach'
    }

    def __init__(self,
                 call_id=None,
                 conference_id=None,
                 member_url=None,
                 mute=None,
                 hold=None,
                 call_ids_to_coach=None):
        """Constructor for the ConferenceMemberDetail class"""

        # Initialize members of the class
        self.call_id = call_id
        self.conference_id = conference_id
        self.member_url = member_url
        self.mute = mute
        self.hold = hold
        self.call_ids_to_coach = call_ids_to_coach

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
        call_id = dictionary.get('callId')
        conference_id = dictionary.get('conferenceId')
        member_url = dictionary.get('memberUrl')
        mute = dictionary.get('mute')
        hold = dictionary.get('hold')
        call_ids_to_coach = dictionary.get('callIdsToCoach')

        # Return an object of this model
        return cls(call_id,
                   conference_id,
                   member_url,
                   mute,
                   hold,
                   call_ids_to_coach)
