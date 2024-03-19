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
from bandwidth.models.call_direction_enum import CallDirectionEnum
from bandwidth.models.file_format_enum import FileFormatEnum
from bandwidth.models.transcription import Transcription
from typing import Optional, Set
from typing_extensions import Self

class TranscriptionAvailableCallback(BaseModel):
    """
    The Transcription Available event is sent when the recording transcription is available to be downloaded.
    """ # noqa: E501
    event_type: Optional[StrictStr] = Field(default=None, description="The event type, value can be one of the following: answer, bridgeComplete, bridgeTargetComplete, conferenceCreated, conferenceRedirect, conferenceMemberJoin, conferenceMemberExit, conferenceCompleted, conferenceRecordingAvailable, disconnect, dtmf, gather, initiate, machineDetectionComplete, recordingComplete, recordingAvailable, redirect, transcriptionAvailable, transferAnswer, transferComplete, transferDisconnect.", alias="eventType")
    event_time: Optional[datetime] = Field(default=None, description="The approximate UTC date and time when the event was generated by the Bandwidth server, in ISO 8601 format. This may not be exactly the time of event execution.", alias="eventTime")
    account_id: Optional[StrictStr] = Field(default=None, description="The user account associated with the call.", alias="accountId")
    application_id: Optional[StrictStr] = Field(default=None, description="The id of the application associated with the call.", alias="applicationId")
    var_from: Optional[StrictStr] = Field(default=None, description="The provided identifier of the caller: can be a phone number in E.164 format (e.g. +15555555555) or one of Private, Restricted, Unavailable, or Anonymous.", alias="from")
    to: Optional[StrictStr] = Field(default=None, description="The phone number that received the call, in E.164 format (e.g. +15555555555).")
    direction: Optional[CallDirectionEnum] = None
    call_id: Optional[StrictStr] = Field(default=None, description="The call id associated with the event.", alias="callId")
    call_url: Optional[StrictStr] = Field(default=None, description="The URL of the call associated with the event.", alias="callUrl")
    media_url: Optional[StrictStr] = Field(default=None, description="The URL that can be used to download the recording. Only present if the recording is finished and may be downloaded.", alias="mediaUrl")
    parent_call_id: Optional[StrictStr] = Field(default=None, description="(optional) If the event is related to the B leg of a <Transfer>, the call id of the original call leg that executed the <Transfer>. Otherwise, this field will not be present.", alias="parentCallId")
    recording_id: Optional[StrictStr] = Field(default=None, description="The unique ID of this recording", alias="recordingId")
    enqueued_time: Optional[datetime] = Field(default=None, description="(optional) If call queueing is enabled and this is an outbound call, time the call was queued, in ISO 8601 format.", alias="enqueuedTime")
    start_time: Optional[datetime] = Field(default=None, description="Time the call was started, in ISO 8601 format.", alias="startTime")
    end_time: Optional[datetime] = Field(default=None, description="The time that the recording ended in ISO-8601 format", alias="endTime")
    duration: Optional[StrictStr] = Field(default=None, description="The duration of the recording in ISO-8601 format")
    file_format: Optional[FileFormatEnum] = Field(default=None, alias="fileFormat")
    tag: Optional[StrictStr] = Field(default=None, description="(optional) The tag specified on call creation. If no tag was specified or it was previously cleared, this field will not be present.")
    transcription: Optional[Transcription] = None
    transfer_caller_id: Optional[StrictStr] = Field(default=None, description="The phone number used as the from field of the B-leg call, in E.164 format (e.g. +15555555555) or one of Restricted, Anonymous, Private, or Unavailable.", alias="transferCallerId")
    transfer_to: Optional[StrictStr] = Field(default=None, description="The phone number used as the to field of the B-leg call, in E.164 format (e.g. +15555555555).", alias="transferTo")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["eventType", "eventTime", "accountId", "applicationId", "from", "to", "direction", "callId", "callUrl", "mediaUrl", "parentCallId", "recordingId", "enqueuedTime", "startTime", "endTime", "duration", "fileFormat", "tag", "transcription", "transferCallerId", "transferTo"]

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
        """Create an instance of TranscriptionAvailableCallback from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of transcription
        if self.transcription:
            _dict['transcription'] = self.transcription.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if media_url (nullable) is None
        # and model_fields_set contains the field
        if self.media_url is None and "media_url" in self.model_fields_set:
            _dict['mediaUrl'] = None

        # set to None if enqueued_time (nullable) is None
        # and model_fields_set contains the field
        if self.enqueued_time is None and "enqueued_time" in self.model_fields_set:
            _dict['enqueuedTime'] = None

        # set to None if tag (nullable) is None
        # and model_fields_set contains the field
        if self.tag is None and "tag" in self.model_fields_set:
            _dict['tag'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TranscriptionAvailableCallback from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "eventType": obj.get("eventType"),
            "eventTime": obj.get("eventTime"),
            "accountId": obj.get("accountId"),
            "applicationId": obj.get("applicationId"),
            "from": obj.get("from"),
            "to": obj.get("to"),
            "direction": obj.get("direction"),
            "callId": obj.get("callId"),
            "callUrl": obj.get("callUrl"),
            "mediaUrl": obj.get("mediaUrl"),
            "parentCallId": obj.get("parentCallId"),
            "recordingId": obj.get("recordingId"),
            "enqueuedTime": obj.get("enqueuedTime"),
            "startTime": obj.get("startTime"),
            "endTime": obj.get("endTime"),
            "duration": obj.get("duration"),
            "fileFormat": obj.get("fileFormat"),
            "tag": obj.get("tag"),
            "transcription": Transcription.from_dict(obj["transcription"]) if obj.get("transcription") is not None else None,
            "transferCallerId": obj.get("transferCallerId"),
            "transferTo": obj.get("transferTo")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


