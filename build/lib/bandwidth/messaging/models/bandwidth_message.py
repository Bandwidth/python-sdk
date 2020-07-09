# -*- coding: utf-8 -*-

"""
bandwidth

This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class BandwidthMessage(object):

    """Implementation of the 'BandwidthMessage' model.

    TODO: type model description here.

    Attributes:
        id (string): TODO: type description here.
        owner (string): TODO: type description here.
        application_id (string): TODO: type description here.
        time (string): TODO: type description here.
        segment_count (int): TODO: type description here.
        direction (string): TODO: type description here.
        to (list of string): TODO: type description here.
        mfrom (string): TODO: type description here.
        media (list of string): TODO: type description here.
        text (string): TODO: type description here.
        tag (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "owner": 'owner',
        "application_id": 'applicationId',
        "time": 'time',
        "segment_count": 'segmentCount',
        "direction": 'direction',
        "to": 'to',
        "mfrom": 'from',
        "media": 'media',
        "text": 'text',
        "tag": 'tag'
    }

    def __init__(self,
                 id=None,
                 owner=None,
                 application_id=None,
                 time=None,
                 segment_count=None,
                 direction=None,
                 to=None,
                 mfrom=None,
                 media=None,
                 text=None,
                 tag=None):
        """Constructor for the BandwidthMessage class"""

        # Initialize members of the class
        self.id = id
        self.owner = owner
        self.application_id = application_id
        self.time = time
        self.segment_count = segment_count
        self.direction = direction
        self.to = to
        self.mfrom = mfrom
        self.media = media
        self.text = text
        self.tag = tag

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
        id = dictionary.get('id')
        owner = dictionary.get('owner')
        application_id = dictionary.get('applicationId')
        time = dictionary.get('time')
        segment_count = dictionary.get('segmentCount')
        direction = dictionary.get('direction')
        to = dictionary.get('to')
        mfrom = dictionary.get('from')
        media = dictionary.get('media')
        text = dictionary.get('text')
        tag = dictionary.get('tag')

        # Return an object of this model
        return cls(id,
                   owner,
                   application_id,
                   time,
                   segment_count,
                   direction,
                   to,
                   mfrom,
                   media,
                   text,
                   tag)
