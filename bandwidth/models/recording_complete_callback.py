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
from bandwidth.models.call_direction_enum import CallDirectionEnum
from bandwidth.models.file_format_enum import FileFormatEnum

class RecordingCompleteCallback(BaseModel):
    """
    The Record Complete event is sent after a <Record> verb has executed if the call is still active. The BXML returned by this callback is executed next. When the recording is available for download, a Recording Available event will be sent.
    """
    event_type: Optional[StrictStr] = Field(None, alias="eventType", description="The event type, value can be one of the following: answer, bridgeComplete, bridgeTargetComplete, conferenceCreated, conferenceRedirect, conferenceMemberJoin, conferenceMemberExit, conferenceCompleted, conferenceRecordingAvailable, disconnect, dtmf, gather, initiate, machineDetectionComplete, recordingComplete, recordingAvailable, redirect, transcriptionAvailable, transferAnswer, transferComplete, transferDisconnect.")
    event_time: Optional[datetime] = Field(None, alias="eventTime", description="The approximate UTC date and time when the event was generated by the Bandwidth server, in ISO 8601 format. This may not be exactly the time of event execution.")
    account_id: Optional[StrictStr] = Field(None, alias="accountId", description="The user account associated with the call.")
    application_id: Optional[StrictStr] = Field(None, alias="applicationId", description="The id of the application associated with the call.")
    var_from: Optional[StrictStr] = Field(None, alias="from", description="The provided identifier of the caller: can be a phone number in E.164 format (e.g. +15555555555) or one of Private, Restricted, Unavailable, or Anonymous.")
    to: Optional[StrictStr] = Field(None, description="The phone number that received the call, in E.164 format (e.g. +15555555555).")
    direction: Optional[CallDirectionEnum] = None
    call_id: Optional[StrictStr] = Field(None, alias="callId", description="The call id associated with the event.")
    call_url: Optional[StrictStr] = Field(None, alias="callUrl", description="The URL of the call associated with the event.")
    parent_call_id: Optional[StrictStr] = Field(None, alias="parentCallId", description="(optional) If the event is related to the B leg of a <Transfer>, the call id of the original call leg that executed the <Transfer>. Otherwise, this field will not be present.")
    recording_id: Optional[StrictStr] = Field(None, alias="recordingId", description="The unique ID of this recording")
    media_url: Optional[StrictStr] = Field(None, alias="mediaUrl", description="The URL that can be used to download the recording. Only present if the recording is finished and may be downloaded.")
    enqueued_time: Optional[datetime] = Field(None, alias="enqueuedTime", description="(optional) If call queueing is enabled and this is an outbound call, time the call was queued, in ISO 8601 format.")
    start_time: Optional[datetime] = Field(None, alias="startTime", description="Time the call was started, in ISO 8601 format.")
    answer_time: Optional[datetime] = Field(None, alias="answerTime", description="Time the call was answered, in ISO 8601 format.")
    end_time: Optional[datetime] = Field(None, alias="endTime", description="The time that the recording ended in ISO-8601 format")
    duration: Optional[StrictStr] = Field(None, description="The duration of the recording in ISO-8601 format")
    file_format: Optional[FileFormatEnum] = Field(None, alias="fileFormat")
    channels: Optional[StrictInt] = Field(None, description="Always `1` for conference recordings; multi-channel recordings are not supported on conferences.")
    tag: Optional[StrictStr] = Field(None, description="(optional) The tag specified on call creation. If no tag was specified or it was previously cleared, this field will not be present.")
    transfer_caller_id: Optional[StrictStr] = Field(None, alias="transferCallerId", description="The phone number used as the from field of the B-leg call, in E.164 format (e.g. +15555555555) or one of Restricted, Anonymous, Private, or Unavailable.")
    transfer_to: Optional[StrictStr] = Field(None, alias="transferTo", description="The phone number used as the to field of the B-leg call, in E.164 format (e.g. +15555555555).")
    additional_properties: Dict[str, Any] = {}
    __properties = ["eventType", "eventTime", "accountId", "applicationId", "from", "to", "direction", "callId", "callUrl", "parentCallId", "recordingId", "mediaUrl", "enqueuedTime", "startTime", "answerTime", "endTime", "duration", "fileFormat", "channels", "tag", "transferCallerId", "transferTo"]

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
    def from_json(cls, json_str: str) -> RecordingCompleteCallback:
        """Create an instance of RecordingCompleteCallback from a JSON string"""
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

        # set to None if enqueued_time (nullable) is None
        # and __fields_set__ contains the field
        if self.enqueued_time is None and "enqueued_time" in self.__fields_set__:
            _dict['enqueuedTime'] = None

        # set to None if answer_time (nullable) is None
        # and __fields_set__ contains the field
        if self.answer_time is None and "answer_time" in self.__fields_set__:
            _dict['answerTime'] = None

        # set to None if tag (nullable) is None
        # and __fields_set__ contains the field
        if self.tag is None and "tag" in self.__fields_set__:
            _dict['tag'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RecordingCompleteCallback:
        """Create an instance of RecordingCompleteCallback from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RecordingCompleteCallback.parse_obj(obj)

        _obj = RecordingCompleteCallback.parse_obj({
            "event_type": obj.get("eventType"),
            "event_time": obj.get("eventTime"),
            "account_id": obj.get("accountId"),
            "application_id": obj.get("applicationId"),
            "var_from": obj.get("from"),
            "to": obj.get("to"),
            "direction": obj.get("direction"),
            "call_id": obj.get("callId"),
            "call_url": obj.get("callUrl"),
            "parent_call_id": obj.get("parentCallId"),
            "recording_id": obj.get("recordingId"),
            "media_url": obj.get("mediaUrl"),
            "enqueued_time": obj.get("enqueuedTime"),
            "start_time": obj.get("startTime"),
            "answer_time": obj.get("answerTime"),
            "end_time": obj.get("endTime"),
            "duration": obj.get("duration"),
            "file_format": obj.get("fileFormat"),
            "channels": obj.get("channels"),
            "tag": obj.get("tag"),
            "transfer_caller_id": obj.get("transferCallerId"),
            "transfer_to": obj.get("transferTo")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


