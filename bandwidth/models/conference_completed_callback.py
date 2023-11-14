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
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictStr

class ConferenceCompletedCallback(BaseModel):
    """
    The Conference Completed event is fired when the last member leaves the conference. The response to this event may not contain BXML.
    """
    event_type: Optional[StrictStr] = Field(None, alias="eventType", description="The event type, value can be one of the following: answer, bridgeComplete, bridgeTargetComplete, conferenceCreated, conferenceRedirect, conferenceMemberJoin, conferenceMemberExit, conferenceCompleted, conferenceRecordingAvailable, disconnect, dtmf, gather, initiate, machineDetectionComplete, recordingComplete, recordingAvailable, redirect, transcriptionAvailable, transferAnswer, transferComplete, transferDisconnect.")
    event_time: Optional[datetime] = Field(None, alias="eventTime", description="The approximate UTC date and time when the event was generated by the Bandwidth server, in ISO 8601 format. This may not be exactly the time of event execution.")
    conference_id: Optional[StrictStr] = Field(None, alias="conferenceId", description="The unique, Bandwidth-generated ID of the conference that was recorded")
    name: Optional[StrictStr] = Field(None, description="The user-specified name of the conference that was recorded")
    tag: Optional[StrictStr] = Field(None, description="(optional) The tag specified on call creation. If no tag was specified or it was previously cleared, this field will not be present.")
    additional_properties: Dict[str, Any] = {}
    __properties = ["eventType", "eventTime", "conferenceId", "name", "tag"]

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
    def from_json(cls, json_str: str) -> ConferenceCompletedCallback:
        """Create an instance of ConferenceCompletedCallback from a JSON string"""
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

        # set to None if tag (nullable) is None
        # and __fields_set__ contains the field
        if self.tag is None and "tag" in self.__fields_set__:
            _dict['tag'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ConferenceCompletedCallback:
        """Create an instance of ConferenceCompletedCallback from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ConferenceCompletedCallback.parse_obj(obj)

        _obj = ConferenceCompletedCallback.parse_obj({
            "event_type": obj.get("eventType"),
            "event_time": obj.get("eventTime"),
            "conference_id": obj.get("conferenceId"),
            "name": obj.get("name"),
            "tag": obj.get("tag")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

