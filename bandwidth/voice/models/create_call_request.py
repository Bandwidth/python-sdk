# -*- coding: utf-8 -*-

"""
bandwidth

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class CreateCallRequest(object):

    """Implementation of the 'CreateCallRequest' model.

    TODO: type model description here.

    Attributes:
        mfrom (string): Format is E164
        to (string): Format is E164 or SIP URI
        uui (string): When calling a SIP URI, this will be sent as the
            'User-To-User' header within the initial INVITE. It must end with
            an 'encoding' parameter as described in
            https://tools.ietf.org/html/rfc7433. This header cannot exceed 256
            characters, including the encoding parameter.
        call_timeout (float): TODO: type description here.
        callback_timeout (float): TODO: type description here.
        answer_url (string): TODO: type description here.
        answer_fallback_url (string): TODO: type description here.
        username (string): TODO: type description here.
        password (string): TODO: type description here.
        fallback_username (string): TODO: type description here.
        fallback_password (string): TODO: type description here.
        answer_method (AnswerMethodEnum): TODO: type description here.
        answer_fallback_method (AnswerFallbackMethodEnum): TODO: type
            description here.
        disconnect_url (string): TODO: type description here.
        disconnect_method (DisconnectMethodEnum): TODO: type description
            here.
        tag (string): TODO: type description here.
        application_id (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mfrom": 'from',
        "to": 'to',
        "answer_url": 'answerUrl',
        "application_id": 'applicationId',
        "uui": 'uui',
        "call_timeout": 'callTimeout',
        "callback_timeout": 'callbackTimeout',
        "answer_fallback_url": 'answerFallbackUrl',
        "username": 'username',
        "password": 'password',
        "fallback_username": 'fallbackUsername',
        "fallback_password": 'fallbackPassword',
        "answer_method": 'answerMethod',
        "answer_fallback_method": 'answerFallbackMethod',
        "disconnect_url": 'disconnectUrl',
        "disconnect_method": 'disconnectMethod',
        "tag": 'tag'
    }

    def __init__(self,
                 mfrom=None,
                 to=None,
                 answer_url=None,
                 application_id=None,
                 uui=None,
                 call_timeout=None,
                 callback_timeout=None,
                 answer_fallback_url=None,
                 username=None,
                 password=None,
                 fallback_username=None,
                 fallback_password=None,
                 answer_method=None,
                 answer_fallback_method=None,
                 disconnect_url=None,
                 disconnect_method=None,
                 tag=None):
        """Constructor for the CreateCallRequest class"""

        # Initialize members of the class
        self.mfrom = mfrom
        self.to = to
        self.uui = uui
        self.call_timeout = call_timeout
        self.callback_timeout = callback_timeout
        self.answer_url = answer_url
        self.answer_fallback_url = answer_fallback_url
        self.username = username
        self.password = password
        self.fallback_username = fallback_username
        self.fallback_password = fallback_password
        self.answer_method = answer_method
        self.answer_fallback_method = answer_fallback_method
        self.disconnect_url = disconnect_url
        self.disconnect_method = disconnect_method
        self.tag = tag
        self.application_id = application_id

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
        mfrom = dictionary.get('from')
        to = dictionary.get('to')
        answer_url = dictionary.get('answerUrl')
        application_id = dictionary.get('applicationId')
        uui = dictionary.get('uui')
        call_timeout = dictionary.get('callTimeout')
        callback_timeout = dictionary.get('callbackTimeout')
        answer_fallback_url = dictionary.get('answerFallbackUrl')
        username = dictionary.get('username')
        password = dictionary.get('password')
        fallback_username = dictionary.get('fallbackUsername')
        fallback_password = dictionary.get('fallbackPassword')
        answer_method = dictionary.get('answerMethod')
        answer_fallback_method = dictionary.get('answerFallbackMethod')
        disconnect_url = dictionary.get('disconnectUrl')
        disconnect_method = dictionary.get('disconnectMethod')
        tag = dictionary.get('tag')

        # Return an object of this model
        return cls(mfrom,
                   to,
                   answer_url,
                   application_id,
                   uui,
                   call_timeout,
                   callback_timeout,
                   answer_fallback_url,
                   username,
                   password,
                   fallback_username,
                   fallback_password,
                   answer_method,
                   answer_fallback_method,
                   disconnect_url,
                   disconnect_method,
                   tag)