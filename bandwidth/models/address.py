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

from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class Address(BaseModel):
    """
    Address
    """ # noqa: E501
    name: Annotated[str, Field(min_length=1, strict=True, max_length=500)] = Field(description="The name of the business using the toll-free number.")
    addr1: Annotated[str, Field(min_length=1, strict=True, max_length=500)] = Field(description="The address of the business using the toll-free number.")
    addr2: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=500)]] = Field(default=None, description="The address of the business using the toll-free number.")
    city: Annotated[str, Field(min_length=1, strict=True, max_length=500)] = Field(description="The city of the business using the toll-free number.")
    state: Annotated[str, Field(min_length=1, strict=True, max_length=500)] = Field(description="The state of the business using the toll-free number.")
    zip: Annotated[str, Field(strict=True)] = Field(description="The zip of the business using the toll-free number.")
    url: Annotated[str, Field(min_length=1, strict=True, max_length=500)] = Field(description="The website of the business using the toll-free number.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["name", "addr1", "addr2", "city", "state", "zip", "url"]

    @field_validator('zip')
    def zip_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"[- A-Za-z0-9]{0,500}", value):
            raise ValueError(r"must validate the regular expression /[- A-Za-z0-9]{0,500}/")
        return value

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
        """Create an instance of Address from a JSON string"""
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

        # set to None if addr2 (nullable) is None
        # and model_fields_set contains the field
        if self.addr2 is None and "addr2" in self.model_fields_set:
            _dict['addr2'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Address from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "addr1": obj.get("addr1"),
            "addr2": obj.get("addr2"),
            "city": obj.get("city"),
            "state": obj.get("state"),
            "zip": obj.get("zip"),
            "url": obj.get("url")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


