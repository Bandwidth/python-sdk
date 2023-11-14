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
from pydantic import BaseModel, Field, StrictStr, conlist
from bandwidth.models.field_error import FieldError

class CreateMessageRequestError(BaseModel):
    """
    CreateMessageRequestError
    """
    type: StrictStr = Field(...)
    description: StrictStr = Field(...)
    field_errors: Optional[conlist(FieldError)] = Field(None, alias="fieldErrors")
    additional_properties: Dict[str, Any] = {}
    __properties = ["type", "description", "fieldErrors"]

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
    def from_json(cls, json_str: str) -> CreateMessageRequestError:
        """Create an instance of CreateMessageRequestError from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in field_errors (list)
        _items = []
        if self.field_errors:
            for _item in self.field_errors:
                if _item:
                    _items.append(_item.to_dict())
            _dict['fieldErrors'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateMessageRequestError:
        """Create an instance of CreateMessageRequestError from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateMessageRequestError.parse_obj(obj)

        _obj = CreateMessageRequestError.parse_obj({
            "type": obj.get("type"),
            "description": obj.get("description"),
            "field_errors": [FieldError.from_dict(_item) for _item in obj.get("fieldErrors")] if obj.get("fieldErrors") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

