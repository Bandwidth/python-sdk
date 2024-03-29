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
from bandwidth.models.call_state_enum import CallStateEnum
from bandwidth.models.redirect_method_enum import RedirectMethodEnum

class UpdateCall(BaseModel):
    """
    UpdateCall
    """
    state: Optional[CallStateEnum] = None
    redirect_url: Optional[StrictStr] = Field(None, alias="redirectUrl", description="The URL to send the [Redirect](/docs/voice/bxml/redirect) event to which will provide new BXML.  Required if `state` is `active`.  Not allowed if `state` is `completed`.")
    redirect_method: Optional[RedirectMethodEnum] = Field(None, alias="redirectMethod")
    username: Optional[constr(strict=True, max_length=1024)] = Field(None, description="Basic auth username.")
    password: Optional[constr(strict=True, max_length=1024)] = Field(None, description="Basic auth password.")
    redirect_fallback_url: Optional[StrictStr] = Field(None, alias="redirectFallbackUrl", description="A fallback url which, if provided, will be used to retry the redirect callback delivery in case `redirectUrl` fails to respond.")
    redirect_fallback_method: Optional[RedirectMethodEnum] = Field(None, alias="redirectFallbackMethod")
    fallback_username: Optional[constr(strict=True, max_length=1024)] = Field(None, alias="fallbackUsername", description="Basic auth username.")
    fallback_password: Optional[constr(strict=True, max_length=1024)] = Field(None, alias="fallbackPassword", description="Basic auth password.")
    tag: Optional[constr(strict=True, max_length=256)] = Field(None, description="A custom string that will be sent with this and all future callbacks unless overwritten by a future `tag` attribute or [`<Tag>`](/docs/voice/bxml/tag) verb, or cleared.  May be cleared by setting `tag=\"\"`.  Max length 256 characters.  Not allowed if `state` is `completed`.")
    additional_properties: Dict[str, Any] = {}
    __properties = ["state", "redirectUrl", "redirectMethod", "username", "password", "redirectFallbackUrl", "redirectFallbackMethod", "fallbackUsername", "fallbackPassword", "tag"]

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
    def from_json(cls, json_str: str) -> UpdateCall:
        """Create an instance of UpdateCall from a JSON string"""
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

        # set to None if state (nullable) is None
        # and __fields_set__ contains the field
        if self.state is None and "state" in self.__fields_set__:
            _dict['state'] = None

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

        # set to None if tag (nullable) is None
        # and __fields_set__ contains the field
        if self.tag is None and "tag" in self.__fields_set__:
            _dict['tag'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpdateCall:
        """Create an instance of UpdateCall from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UpdateCall.parse_obj(obj)

        _obj = UpdateCall.parse_obj({
            "state": obj.get("state"),
            "redirect_url": obj.get("redirectUrl"),
            "redirect_method": obj.get("redirectMethod"),
            "username": obj.get("username"),
            "password": obj.get("password"),
            "redirect_fallback_url": obj.get("redirectFallbackUrl"),
            "redirect_fallback_method": obj.get("redirectFallbackMethod"),
            "fallback_username": obj.get("fallbackUsername"),
            "fallback_password": obj.get("fallbackPassword"),
            "tag": obj.get("tag")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


