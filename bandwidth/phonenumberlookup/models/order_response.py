# -*- coding: utf-8 -*-

"""
bandwidth

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class OrderResponse(object):

    """Implementation of the 'OrderResponse' model.

    The request has been accepted for processing but not yet finished and in a
    terminal state (COMPLETE, PARTIAL_COMPLETE, or FAILED)

    Attributes:
        request_id (string): TODO: type description here.
        status (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "request_id": 'requestId',
        "status": 'status'
    }

    def __init__(self,
                 request_id=None,
                 status=None):
        """Constructor for the OrderResponse class"""

        # Initialize members of the class
        self.request_id = request_id
        self.status = status

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
        request_id = dictionary.get('requestId')
        status = dictionary.get('status')

        # Return an object of this model
        return cls(request_id,
                   status)