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
from pydantic import BaseModel, Field, StrictInt, StrictStr
from bandwidth.models.file_format_enum import FileFormatEnum

class ConferenceRecordingAvailableCallback(BaseModel):
    """
    The Conference Recording Available event is sent after a conference recording has been processed. It indicates that the recording is available for download.
    """
    event_type: Optional[StrictStr] = Field(None, alias="eventType", description="The event type, value can be one of the following: answer, bridgeComplete, bridgeTargetComplete, conferenceCreated, conferenceRedirect, conferenceMemberJoin, conferenceMemberExit, conferenceCompleted, conferenceRecordingAvailable, disconnect, dtmf, gather, initiate, machineDetectionComplete, recordingComplete, recordingAvailable, redirect, transcriptionAvailable, transferAnswer, transferComplete, transferDisconnect.")
    event_time: Optional[datetime] = Field(None, alias="eventTime", description="The approximate UTC date and time when the event was generated by the Bandwidth server, in ISO 8601 format. This may not be exactly the time of event execution.")
    conference_id: Optional[StrictStr] = Field(None, alias="conferenceId", description="The unique, Bandwidth-generated ID of the conference that was recorded")
    name: Optional[StrictStr] = Field(None, description="The user-specified name of the conference that was recorded")
    account_id: Optional[StrictStr] = Field(None, alias="accountId", description="The user account associated with the call.")
    recording_id: Optional[StrictStr] = Field(None, alias="recordingId", description="The unique ID of this recording")
    channels: Optional[StrictInt] = Field(None, description="Always `1` for conference recordings; multi-channel recordings are not supported on conferences.")
    start_time: Optional[datetime] = Field(None, alias="startTime", description="Time the call was started, in ISO 8601 format.")
    end_time: Optional[datetime] = Field(None, alias="endTime", description="The time that the recording ended in ISO-8601 format")
    duration: Optional[StrictStr] = Field(None, description="The duration of the recording in ISO-8601 format")
    file_format: Optional[FileFormatEnum] = Field(None, alias="fileFormat")
    media_url: Optional[StrictStr] = Field(None, alias="mediaUrl", description="The URL that can be used to download the recording. Only present if the recording is finished and may be downloaded.")
    tag: Optional[StrictStr] = Field(None, description="(optional) The tag specified on call creation. If no tag was specified or it was previously cleared, this field will not be present.")
    status: Optional[StrictStr] = Field(None, description="The current status of the process. For recording, current possible values are 'processing', 'partial', 'complete', 'deleted', and 'error'. For transcriptions, current possible values are 'none', 'processing', 'available', 'error', 'timeout', 'file-size-too-big', and 'file-size-too-small'. Additional states may be added in the future, so your application must be tolerant of unknown values.")
    additional_properties: Dict[str, Any] = {}
    __properties = ["eventType", "eventTime", "conferenceId", "name", "accountId", "recordingId", "channels", "startTime", "endTime", "duration", "fileFormat", "mediaUrl", "tag", "status"]

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
    def from_json(cls, json_str: str) -> ConferenceRecordingAvailableCallback:
        """Create an instance of ConferenceRecordingAvailableCallback from a JSON string"""
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

        # set to None if media_url (nullable) is None
        # and __fields_set__ contains the field
        if self.media_url is None and "media_url" in self.__fields_set__:
            _dict['mediaUrl'] = None

        # set to None if tag (nullable) is None
        # and __fields_set__ contains the field
        if self.tag is None and "tag" in self.__fields_set__:
            _dict['tag'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ConferenceRecordingAvailableCallback:
        """Create an instance of ConferenceRecordingAvailableCallback from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ConferenceRecordingAvailableCallback.parse_obj(obj)

        _obj = ConferenceRecordingAvailableCallback.parse_obj({
            "event_type": obj.get("eventType"),
            "event_time": obj.get("eventTime"),
            "conference_id": obj.get("conferenceId"),
            "name": obj.get("name"),
            "account_id": obj.get("accountId"),
            "recording_id": obj.get("recordingId"),
            "channels": obj.get("channels"),
            "start_time": obj.get("startTime"),
            "end_time": obj.get("endTime"),
            "duration": obj.get("duration"),
            "file_format": obj.get("fileFormat"),
            "media_url": obj.get("mediaUrl"),
            "tag": obj.get("tag"),
            "status": obj.get("status")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

