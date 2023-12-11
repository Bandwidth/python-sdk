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


class RecordingStateEnum(str, Enum):
    """
    The recording state. Possible values:  `paused` to pause an active recording  `recording` to resume a paused recording
    """

    """
    allowed enum values
    """
    PAUSED = 'paused'
    RECORDING = 'recording'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of RecordingStateEnum from a JSON string"""
        return cls(json.loads(json_str))


