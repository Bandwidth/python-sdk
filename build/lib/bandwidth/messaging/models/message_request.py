# -*- coding: utf-8 -*-

"""
bandwidth

This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class MessageRequest(object):

    """Implementation of the 'MessageRequest' model.

    TODO: type model description here.

    Attributes:
        application_id (string): TODO: type description here.
        to (list of string): TODO: type description here.
        mfrom (string): TODO: type description here.
        text (string): TODO: type description here.
        media (list of string): TODO: type description here.
        tag (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "application_id": 'applicationId',
        "to": 'to',
        "mfrom": 'from',
        "text": 'text',
        "media": 'media',
        "tag": 'tag'
    }

    def __init__(self,
                 application_id=None,
                 to=None,
                 mfrom=None,
                 text=None,
                 media=None,
                 tag=None):
        """Constructor for the MessageRequest class"""

        # Initialize members of the class
        self.application_id = application_id
        self.to = to
        self.mfrom = mfrom
        self.text = text
        self.media = media
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
        application_id = dictionary.get('applicationId')
        to = dictionary.get('to')
        mfrom = dictionary.get('from')
        text = dictionary.get('text')
        media = dictionary.get('media')
        tag = dictionary.get('tag')

        # Return an object of this model
        return cls(application_id,
                   to,
                   mfrom,
                   text,
                   media,
                   tag)