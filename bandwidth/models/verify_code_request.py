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


from typing import Any, Dict, Optional, Union
from pydantic import BaseModel, Field, StrictStr, confloat, conint, constr, validator

class VerifyCodeRequest(BaseModel):
    """
    VerifyCodeRequest
    """
    to: constr(strict=True) = Field(..., description="The phone number to send the mfa code to.")
    scope: Optional[StrictStr] = Field(None, description="An optional field to denote what scope or action the mfa code is addressing.  If not supplied, defaults to \"2FA\".")
    expiration_time_in_minutes: Union[confloat(le=15, ge=1, strict=True), conint(le=15, ge=1, strict=True)] = Field(..., alias="expirationTimeInMinutes", description="The time period, in minutes, to validate the mfa code.  By setting this to 3 minutes, it will mean any code generated within the last 3 minutes are still valid.  The valid range for expiration time is between 0 and 15 minutes, exclusively and inclusively, respectively.")
    code: constr(strict=True, max_length=8, min_length=4) = Field(..., description="The generated mfa code to check if valid.")
    additional_properties: Dict[str, Any] = {}
    __properties = ["to", "scope", "expirationTimeInMinutes", "code"]

    @validator('to')
    def to_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^\+[1-9]\d{1,14}$", value):
            raise ValueError(r"must validate the regular expression /^\+[1-9]\d{1,14}$/")
        return value

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
    def from_json(cls, json_str: str) -> VerifyCodeRequest:
        """Create an instance of VerifyCodeRequest from a JSON string"""
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
    def from_dict(cls, obj: dict) -> VerifyCodeRequest:
        """Create an instance of VerifyCodeRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return VerifyCodeRequest.parse_obj(obj)

        _obj = VerifyCodeRequest.parse_obj({
            "to": obj.get("to"),
            "scope": obj.get("scope"),
            "expiration_time_in_minutes": obj.get("expirationTimeInMinutes"),
            "code": obj.get("code")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


