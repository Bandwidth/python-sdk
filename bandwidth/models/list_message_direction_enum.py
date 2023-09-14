# coding: utf-8

"""
    Bandwidth

    Bandwidth's Communication APIs

    The version of the OpenAPI document: 1.0.0
    Contact: letstalk@bandwidth.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class ListMessageDirectionEnum(str, Enum):
    """
    The direction of the message. One of INBOUND OUTBOUND.
    """

    """
    allowed enum values
    """
    INBOUND = 'INBOUND'
    OUTBOUND = 'OUTBOUND'

    @classmethod
    def from_json(cls, json_str: str) -> ListMessageDirectionEnum:
        """Create an instance of ListMessageDirectionEnum from a JSON string"""
        return ListMessageDirectionEnum(json.loads(json_str))


