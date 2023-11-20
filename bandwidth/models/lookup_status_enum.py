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





class LookupStatusEnum(str, Enum):
    """
    The status of the request (IN_PROGRESS, COMPLETE, PARTIAL_COMPLETE, or FAILED).
    """

    """
    allowed enum values
    """
    IN_PROGRESS = 'IN_PROGRESS'
    COMPLETE = 'COMPLETE'
    PARTIAL_COMPLETE = 'PARTIAL_COMPLETE'
    FAILED = 'FAILED'

    @classmethod
    def from_json(cls, json_str: str) -> LookupStatusEnum:
        """Create an instance of LookupStatusEnum from a JSON string"""
        return LookupStatusEnum(json.loads(json_str))


