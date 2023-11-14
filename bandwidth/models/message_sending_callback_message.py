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
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from bandwidth.models.message_direction_enum import MessageDirectionEnum
from bandwidth.models.priority_enum import PriorityEnum

class MessageSendingCallbackMessage(BaseModel):
    """
    Message Sending Callback Message Schema
    """
    id: StrictStr = Field(...)
    owner: StrictStr = Field(...)
    application_id: StrictStr = Field(..., alias="applicationId")
    time: datetime = Field(...)
    segment_count: StrictInt = Field(..., alias="segmentCount")
    direction: MessageDirectionEnum = Field(...)
    to: conlist(StrictStr, unique_items=True) = Field(...)
    var_from: StrictStr = Field(..., alias="from")
    text: StrictStr = Field(...)
    tag: Optional[StrictStr] = None
    media: conlist(StrictStr) = Field(...)
    priority: PriorityEnum = Field(...)
    additional_properties: Dict[str, Any] = {}
    __properties = ["id", "owner", "applicationId", "time", "segmentCount", "direction", "to", "from", "text", "tag", "media", "priority"]

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
    def from_json(cls, json_str: str) -> MessageSendingCallbackMessage:
        """Create an instance of MessageSendingCallbackMessage from a JSON string"""
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

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MessageSendingCallbackMessage:
        """Create an instance of MessageSendingCallbackMessage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MessageSendingCallbackMessage.parse_obj(obj)

        _obj = MessageSendingCallbackMessage.parse_obj({
            "id": obj.get("id"),
            "owner": obj.get("owner"),
            "application_id": obj.get("applicationId"),
            "time": obj.get("time"),
            "segment_count": obj.get("segmentCount"),
            "direction": obj.get("direction"),
            "to": obj.get("to"),
            "var_from": obj.get("from"),
            "text": obj.get("text"),
            "tag": obj.get("tag"),
            "media": obj.get("media"),
            "priority": obj.get("priority")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

