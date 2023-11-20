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


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictStr, constr
from bandwidth.models.conference_state_enum import ConferenceStateEnum
from bandwidth.models.redirect_method_enum import RedirectMethodEnum

class UpdateConference(BaseModel):
    """
    UpdateConference
    """
    status: Optional[ConferenceStateEnum] = None
    redirect_url: Optional[StrictStr] = Field(None, alias="redirectUrl", description="The URL to send the [conferenceRedirect](/docs/voice/webhooks/conferenceRedirect) event which will provide new BXML. Not allowed if `state` is `completed`, but required if `state` is `active`.")
    redirect_method: Optional[RedirectMethodEnum] = Field(None, alias="redirectMethod")
    username: Optional[constr(strict=True, max_length=1024)] = Field(None, description="Basic auth username.")
    password: Optional[constr(strict=True, max_length=1024)] = Field(None, description="Basic auth password.")
    redirect_fallback_url: Optional[StrictStr] = Field(None, alias="redirectFallbackUrl", description="A fallback url which, if provided, will be used to retry the `conferenceRedirect` webhook delivery in case `redirectUrl` fails to respond.  Not allowed if `state` is `completed`.")
    redirect_fallback_method: Optional[RedirectMethodEnum] = Field(None, alias="redirectFallbackMethod")
    fallback_username: Optional[constr(strict=True, max_length=1024)] = Field(None, alias="fallbackUsername", description="Basic auth username.")
    fallback_password: Optional[constr(strict=True, max_length=1024)] = Field(None, alias="fallbackPassword", description="Basic auth password.")
    additional_properties: Dict[str, Any] = {}
    __properties = ["status", "redirectUrl", "redirectMethod", "username", "password", "redirectFallbackUrl", "redirectFallbackMethod", "fallbackUsername", "fallbackPassword"]

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
    def from_json(cls, json_str: str) -> UpdateConference:
        """Create an instance of UpdateConference from a JSON string"""
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

        # set to None if status (nullable) is None
        # and __fields_set__ contains the field
        if self.status is None and "status" in self.__fields_set__:
            _dict['status'] = None

        # set to None if redirect_url (nullable) is None
        # and __fields_set__ contains the field
        if self.redirect_url is None and "redirect_url" in self.__fields_set__:
            _dict['redirectUrl'] = None

        # set to None if redirect_method (nullable) is None
        # and __fields_set__ contains the field
        if self.redirect_method is None and "redirect_method" in self.__fields_set__:
            _dict['redirectMethod'] = None

        # set to None if username (nullable) is None
        # and __fields_set__ contains the field
        if self.username is None and "username" in self.__fields_set__:
            _dict['username'] = None

        # set to None if password (nullable) is None
        # and __fields_set__ contains the field
        if self.password is None and "password" in self.__fields_set__:
            _dict['password'] = None

        # set to None if redirect_fallback_url (nullable) is None
        # and __fields_set__ contains the field
        if self.redirect_fallback_url is None and "redirect_fallback_url" in self.__fields_set__:
            _dict['redirectFallbackUrl'] = None

        # set to None if redirect_fallback_method (nullable) is None
        # and __fields_set__ contains the field
        if self.redirect_fallback_method is None and "redirect_fallback_method" in self.__fields_set__:
            _dict['redirectFallbackMethod'] = None

        # set to None if fallback_username (nullable) is None
        # and __fields_set__ contains the field
        if self.fallback_username is None and "fallback_username" in self.__fields_set__:
            _dict['fallbackUsername'] = None

        # set to None if fallback_password (nullable) is None
        # and __fields_set__ contains the field
        if self.fallback_password is None and "fallback_password" in self.__fields_set__:
            _dict['fallbackPassword'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpdateConference:
        """Create an instance of UpdateConference from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UpdateConference.parse_obj(obj)

        _obj = UpdateConference.parse_obj({
            "status": obj.get("status"),
            "redirect_url": obj.get("redirectUrl"),
            "redirect_method": obj.get("redirectMethod"),
            "username": obj.get("username"),
            "password": obj.get("password"),
            "redirect_fallback_url": obj.get("redirectFallbackUrl"),
            "redirect_fallback_method": obj.get("redirectFallbackMethod"),
            "fallback_username": obj.get("fallbackUsername"),
            "fallback_password": obj.get("fallbackPassword")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


