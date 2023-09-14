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





class MachineDetectionModeEnum(str, Enum):
    """
    The machine detection mode. If set to 'async', the detection result will be sent in a 'machineDetectionComplete' callback. If set to 'sync', the 'answer' callback will wait for the machine detection to complete and will include its result.
    """

    """
    allowed enum values
    """
    SYNC = 'sync'
    ASYNC = 'async'

    @classmethod
    def from_json(cls, json_str: str) -> MachineDetectionModeEnum:
        """Create an instance of MachineDetectionModeEnum from a JSON string"""
        return MachineDetectionModeEnum(json.loads(json_str))


