# coding: utf-8

"""
    Bandwidth

    Bandwidth's Communication APIs

    The version of the OpenAPI document: 1.0.0
    Contact: letstalk@bandwidth.com
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class StreamingModeEnum(str, Enum):
    """
    The Mode to use when streaming audio over the WebSocket. unidirectional or bidirectional.
    """

    """
    allowed enum values
    """
    UNIDIRECTIONAL = 'unidirectional'
    BIDIRECTIONAL = 'bidirectional'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of StreamingModeEnum from a JSON string"""
        return cls(json.loads(json_str))
