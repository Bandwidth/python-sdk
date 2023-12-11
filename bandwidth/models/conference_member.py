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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ConferenceMember(BaseModel):
    """
    ConferenceMember
    """ # noqa: E501
    call_id: Optional[StrictStr] = Field(default=None, description="The call id associated with the event.", alias="callId")
    conference_id: Optional[StrictStr] = Field(default=None, description="The unique, Bandwidth-generated ID of the conference that was recorded", alias="conferenceId")
    member_url: Optional[StrictStr] = Field(default=None, description="A URL that may be used to retrieve information about or update the state of this conference member. This is the URL of this member's [Get Conference Member](/apis/voice/#operation/getConferenceMember) endpoint and [Modify Conference Member](/apis/voice/#operation/updateConferenceMember) endpoint.", alias="memberUrl")
    mute: Optional[StrictBool] = Field(default=None, description="Whether or not this member is currently muted. Members who are muted are still able to hear other participants.  If used in a PUT request, updates this member's mute status. Has no effect if omitted.")
    hold: Optional[StrictBool] = Field(default=None, description="Whether or not this member is currently on hold. Members who are on hold are not able to hear or speak in the conference.  If used in a PUT request, updates this member's hold status. Has no effect if omitted.")
    call_ids_to_coach: Optional[List[StrictStr]] = Field(default=None, description="If this member had a value set for `callIdsToCoach` in its [Conference](/docs/voice/bxml/conference) verb or this list was added with a previous PUT request to modify the member, this is that list of calls.  If present in a PUT request, modifies the calls that this member is coaching. Has no effect if omitted. See the documentation for the [Conference](/docs/voice/bxml/conference) verb for more details about coaching. Note that this will not add the matching calls to the conference; each call must individually execute a Conference verb to join.", alias="callIdsToCoach")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["callId", "conferenceId", "memberUrl", "mute", "hold", "callIdsToCoach"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ConferenceMember from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "additional_properties",
            },
            exclude_none=True,
        )
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if call_ids_to_coach (nullable) is None
        # and model_fields_set contains the field
        if self.call_ids_to_coach is None and "call_ids_to_coach" in self.model_fields_set:
            _dict['callIdsToCoach'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ConferenceMember from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "callId": obj.get("callId"),
            "conferenceId": obj.get("conferenceId"),
            "memberUrl": obj.get("memberUrl"),
            "mute": obj.get("mute"),
            "hold": obj.get("hold"),
            "callIdsToCoach": obj.get("callIdsToCoach")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


