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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ConferenceMemberExitCallback(BaseModel):
    """
    The Conference Member Exit event is fired whenever a caller exits a conference that specified a callbackUrl. The response may be either empty or a BXML document. Only the following verbs are valid for conferences: PlayAudio, SpeakSentence, StartRecording, StopRecording, PauseRecording, ResumeRecording. Audio verbs will be heard by all members of the conference. Recordings capture audio from all members who are not muted or on hold, as well as any audio verbs that are played into the conference.
    """ # noqa: E501
    event_type: Optional[StrictStr] = Field(default=None, description="The event type, value can be one of the following: answer, bridgeComplete, bridgeTargetComplete, conferenceCreated, conferenceRedirect, conferenceMemberJoin, conferenceMemberExit, conferenceCompleted, conferenceRecordingAvailable, disconnect, dtmf, gather, initiate, machineDetectionComplete, recordingComplete, recordingAvailable, redirect, transcriptionAvailable, transferAnswer, transferComplete, transferDisconnect.", alias="eventType")
    event_time: Optional[datetime] = Field(default=None, description="The approximate UTC date and time when the event was generated by the Bandwidth server, in ISO 8601 format. This may not be exactly the time of event execution.", alias="eventTime")
    conference_id: Optional[StrictStr] = Field(default=None, description="The unique, Bandwidth-generated ID of the conference that was recorded", alias="conferenceId")
    name: Optional[StrictStr] = Field(default=None, description="The user-specified name of the conference that was recorded")
    var_from: Optional[StrictStr] = Field(default=None, description="The provided identifier of the caller. Must be a phone number in E.164 format (e.g. +15555555555).", alias="from")
    to: Optional[StrictStr] = Field(default=None, description="The phone number that received the call, in E.164 format (e.g. +15555555555).")
    call_id: Optional[StrictStr] = Field(default=None, description="The call id associated with the event.", alias="callId")
    tag: Optional[StrictStr] = Field(default=None, description="(optional) The tag specified on call creation. If no tag was specified or it was previously cleared, this field will not be present.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["eventType", "eventTime", "conferenceId", "name", "from", "to", "callId", "tag"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ConferenceMemberExitCallback from a JSON string"""
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
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if tag (nullable) is None
        # and model_fields_set contains the field
        if self.tag is None and "tag" in self.model_fields_set:
            _dict['tag'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConferenceMemberExitCallback from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "eventType": obj.get("eventType"),
            "eventTime": obj.get("eventTime"),
            "conferenceId": obj.get("conferenceId"),
            "name": obj.get("name"),
            "from": obj.get("from"),
            "to": obj.get("to"),
            "callId": obj.get("callId"),
            "tag": obj.get("tag")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


