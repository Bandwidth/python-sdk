# -*- coding: utf-8 -*-

"""
bandwidth

This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""
from bandwidth.webrtc.models.subscriptions import Subscriptions


class Participant(object):

    """Implementation of the 'Participant' model.

    A participant object

    Attributes:
        id (string): Unique id of the participant
        callback_url (string): Full callback url to use for notifications
            about this participant
        publish_permissions (list of PublishPermissionEnum): Defines if this
            participant can publish audio or video
        sessions (list of string): List of session ids this participant is
            associated with  Capped to one
        subscriptions (Subscriptions): TODO: type description here.
        tag (string): User defined tag to associate with the participant
        device_api_version (DeviceApiVersionEnum): Optional field to define
            the device api version of this participant

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "callback_url": 'callbackUrl',
        "publish_permissions": 'publishPermissions',
        "sessions": 'sessions',
        "subscriptions": 'subscriptions',
        "tag": 'tag',
        "device_api_version": 'deviceApiVersion'
    }

    def __init__(self,
                 id=None,
                 callback_url=None,
                 publish_permissions=None,
                 sessions=None,
                 subscriptions=None,
                 tag=None,
                 device_api_version='V2'):
        """Constructor for the Participant class"""

        # Initialize members of the class
        self.id = id
        self.callback_url = callback_url
        self.publish_permissions = publish_permissions
        self.sessions = sessions
        self.subscriptions = subscriptions
        self.tag = tag
        self.device_api_version = device_api_version

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
        callback_url = dictionary.get('callbackUrl')
        publish_permissions = dictionary.get('publishPermissions')
        sessions = dictionary.get('sessions')
        subscriptions = Subscriptions.from_dictionary(dictionary.get('subscriptions')) if dictionary.get('subscriptions') else None
        tag = dictionary.get('tag')
        device_api_version = dictionary.get("deviceApiVersion") if dictionary.get("deviceApiVersion") else 'V2'

        # Return an object of this model
        return cls(id,
                   callback_url,
                   publish_permissions,
                   sessions,
                   subscriptions,
                   tag,
                   device_api_version)
