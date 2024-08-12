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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from bandwidth.models.call_direction_enum import CallDirectionEnum
from bandwidth.models.file_format_enum import FileFormatEnum
from bandwidth.models.recording_transcription_metadata import RecordingTranscriptionMetadata
from typing import Optional, Set
from typing_extensions import Self

class CallRecordingMetadata(BaseModel):
    """
    CallRecordingMetadata
    """ # noqa: E501
    application_id: Optional[StrictStr] = Field(default=None, description="The id of the application associated with the call.", alias="applicationId")
    account_id: Optional[StrictStr] = Field(default=None, description="The user account associated with the call.", alias="accountId")
    call_id: Optional[StrictStr] = Field(default=None, description="The call id associated with the event.", alias="callId")
    parent_call_id: Optional[StrictStr] = Field(default=None, description="(optional) If the event is related to the B leg of a <Transfer>, the call id of the original call leg that executed the <Transfer>. Otherwise, this field will not be present.", alias="parentCallId")
    recording_id: Optional[StrictStr] = Field(default=None, description="The unique ID of this recording", alias="recordingId")
    to: Optional[StrictStr] = Field(default=None, description="The phone number that received the call, in E.164 format (e.g. +15555555555).")
    var_from: Optional[StrictStr] = Field(default=None, description="The provided identifier of the caller. Must be a phone number in E.164 format (e.g. +15555555555).", alias="from")
    transfer_caller_id: Optional[StrictStr] = Field(default=None, description="The phone number used as the from field of the B-leg call, in E.164 format (e.g. +15555555555).", alias="transferCallerId")
    transfer_to: Optional[StrictStr] = Field(default=None, description="The phone number used as the to field of the B-leg call, in E.164 format (e.g. +15555555555).", alias="transferTo")
    duration: Optional[StrictStr] = Field(default=None, description="The duration of the recording in ISO-8601 format")
    direction: Optional[CallDirectionEnum] = None
    channels: Optional[StrictInt] = Field(default=None, description="Always `1` for conference recordings; multi-channel recordings are not supported on conferences.")
    start_time: Optional[datetime] = Field(default=None, description="Time the call was started, in ISO 8601 format.", alias="startTime")
    end_time: Optional[datetime] = Field(default=None, description="The time that the recording ended in ISO-8601 format", alias="endTime")
    file_format: Optional[FileFormatEnum] = Field(default=None, alias="fileFormat")
    status: Optional[StrictStr] = Field(default=None, description="The current status of the process. For recording, current possible values are 'processing', 'partial', 'complete', 'deleted', and 'error'. For transcriptions, current possible values are 'none', 'processing', 'available', 'error', 'timeout', 'file-size-too-big', and 'file-size-too-small'. Additional states may be added in the future, so your application must be tolerant of unknown values.")
    media_url: Optional[StrictStr] = Field(default=None, description="The URL that can be used to download the recording. Only present if the recording is finished and may be downloaded.", alias="mediaUrl")
    transcription: Optional[RecordingTranscriptionMetadata] = None
    recording_name: Optional[StrictStr] = Field(default=None, description="A name to identify this recording.", alias="recordingName")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["applicationId", "accountId", "callId", "parentCallId", "recordingId", "to", "from", "transferCallerId", "transferTo", "duration", "direction", "channels", "startTime", "endTime", "fileFormat", "status", "mediaUrl", "transcription", "recordingName"]

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
        """Create an instance of CallRecordingMetadata from a JSON string"""
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

        # set to None if transcription (nullable) is None
        # and model_fields_set contains the field
        if self.transcription is None and "transcription" in self.model_fields_set:
            _dict['transcription'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CallRecordingMetadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "applicationId": obj.get("applicationId"),
            "accountId": obj.get("accountId"),
            "callId": obj.get("callId"),
            "parentCallId": obj.get("parentCallId"),
            "recordingId": obj.get("recordingId"),
            "to": obj.get("to"),
            "from": obj.get("from"),
            "transferCallerId": obj.get("transferCallerId"),
            "transferTo": obj.get("transferTo"),
            "duration": obj.get("duration"),
            "direction": obj.get("direction"),
            "channels": obj.get("channels"),
            "startTime": obj.get("startTime"),
            "endTime": obj.get("endTime"),
            "fileFormat": obj.get("fileFormat"),
            "status": obj.get("status"),
            "mediaUrl": obj.get("mediaUrl"),
            "transcription": RecordingTranscriptionMetadata.from_dict(obj["transcription"]) if obj.get("transcription") is not None else None,
            "recordingName": obj.get("recordingName")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


