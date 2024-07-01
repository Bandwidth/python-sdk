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
from enum import Enum
from typing_extensions import Self


class CallTranscriptionDetectedLanguageEnum(str, Enum):
    """
    The detected language for this transcription.
    """

    """
    allowed enum values
    """
    EN_MINUS_US = 'en-US'
    ES_MINUS_US = 'es-US'
    FR_MINUS_FR = 'fr-FR'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of CallTranscriptionDetectedLanguageEnum from a JSON string"""
        return cls(json.loads(json_str))

