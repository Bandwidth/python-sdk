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
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist

class UpdateConferenceMember(BaseModel):
    """
    UpdateConferenceMember
    """
    mute: Optional[StrictBool] = Field(None, description="Whether or not this member is currently muted. Members who are muted are still able to hear other participants.  Updates this member's mute status. Has no effect if omitted.")
    hold: Optional[StrictBool] = Field(None, description="Whether or not this member is currently on hold. Members who are on hold are not able to hear or speak in the conference.  Updates this member's hold status. Has no effect if omitted.")
    call_ids_to_coach: Optional[conlist(StrictStr)] = Field(None, alias="callIdsToCoach", description="If this member had a value set for `callIdsToCoach` in its [Conference](/docs/voice/bxml/conference) verb or this list was added with a previous PUT request to modify the member, this is that list of calls.  Modifies the calls that this member is coaching. Has no effect if omitted. See the documentation for the [Conference](/docs/voice/bxml/conference) verb for more details about coaching.  Note that this will not add the matching calls to the conference; each call must individually execute a Conference verb to join.")
    additional_properties: Dict[str, Any] = {}
    __properties = ["mute", "hold", "callIdsToCoach"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> UpdateConferenceMember:
        """Create an instance of UpdateConferenceMember from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if call_ids_to_coach (nullable) is None
        # and __fields_set__ contains the field
        if self.call_ids_to_coach is None and "call_ids_to_coach" in self.__fields_set__:
            _dict['callIdsToCoach'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpdateConferenceMember:
        """Create an instance of UpdateConferenceMember from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UpdateConferenceMember.parse_obj(obj)

        _obj = UpdateConferenceMember.parse_obj({
            "mute": obj.get("mute"),
            "hold": obj.get("hold"),
            "call_ids_to_coach": obj.get("callIdsToCoach")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


