# coding: utf-8

"""
    Bandwidth

    Bandwidth's Communication APIs

    The version of the OpenAPI document: 1.0.0
    Contact: letstalk@bandwidth.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from enum import Enum



try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


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
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ListMessageDirectionEnum from a JSON string"""
        return cls(json.loads(json_str))


