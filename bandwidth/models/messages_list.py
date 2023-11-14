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
from pydantic import BaseModel, Field, StrictInt, conlist
from bandwidth.models.list_message_item import ListMessageItem
from bandwidth.models.page_info import PageInfo

class MessagesList(BaseModel):
    """
    MessagesList
    """
    total_count: Optional[StrictInt] = Field(None, alias="totalCount", description="The total number of messages matched by the search. When the request has limitTotalCount set to true this value is limited to 10,000.")
    page_info: Optional[PageInfo] = Field(None, alias="pageInfo")
    messages: Optional[conlist(ListMessageItem)] = None
    additional_properties: Dict[str, Any] = {}
    __properties = ["totalCount", "pageInfo", "messages"]

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
    def from_json(cls, json_str: str) -> MessagesList:
        """Create an instance of MessagesList from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of page_info
        if self.page_info:
            _dict['pageInfo'] = self.page_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in messages (list)
        _items = []
        if self.messages:
            for _item in self.messages:
                if _item:
                    _items.append(_item.to_dict())
            _dict['messages'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MessagesList:
        """Create an instance of MessagesList from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MessagesList.parse_obj(obj)

        _obj = MessagesList.parse_obj({
            "total_count": obj.get("totalCount"),
            "page_info": PageInfo.from_dict(obj.get("pageInfo")) if obj.get("pageInfo") is not None else None,
            "messages": [ListMessageItem.from_dict(_item) for _item in obj.get("messages")] if obj.get("messages") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

