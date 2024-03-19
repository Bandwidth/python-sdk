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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from bandwidth.models.call_state_enum import CallStateEnum
from bandwidth.models.redirect_method_enum import RedirectMethodEnum
from typing import Optional, Set
from typing_extensions import Self

class UpdateCall(BaseModel):
    """
    UpdateCall
    """ # noqa: E501
    state: Optional[CallStateEnum] = None
    redirect_url: Optional[StrictStr] = Field(default=None, description="The URL to send the [Redirect](/docs/voice/bxml/redirect) event to which will provide new BXML.  Required if `state` is `active`.  Not allowed if `state` is `completed`.", alias="redirectUrl")
    redirect_method: Optional[RedirectMethodEnum] = Field(default=None, alias="redirectMethod")
    username: Optional[Annotated[str, Field(strict=True, max_length=1024)]] = Field(default=None, description="Basic auth username.")
    password: Optional[Annotated[str, Field(strict=True, max_length=1024)]] = Field(default=None, description="Basic auth password.")
    redirect_fallback_url: Optional[StrictStr] = Field(default=None, description="A fallback url which, if provided, will be used to retry the redirect callback delivery in case `redirectUrl` fails to respond.", alias="redirectFallbackUrl")
    redirect_fallback_method: Optional[RedirectMethodEnum] = Field(default=None, alias="redirectFallbackMethod")
    fallback_username: Optional[Annotated[str, Field(strict=True, max_length=1024)]] = Field(default=None, description="Basic auth username.", alias="fallbackUsername")
    fallback_password: Optional[Annotated[str, Field(strict=True, max_length=1024)]] = Field(default=None, description="Basic auth password.", alias="fallbackPassword")
    tag: Optional[Annotated[str, Field(strict=True, max_length=256)]] = Field(default=None, description="A custom string that will be sent with this and all future callbacks unless overwritten by a future `tag` attribute or [`<Tag>`](/docs/voice/bxml/tag) verb, or cleared.  May be cleared by setting `tag=\"\"`.  Max length 256 characters.  Not allowed if `state` is `completed`.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["state", "redirectUrl", "redirectMethod", "username", "password", "redirectFallbackUrl", "redirectFallbackMethod", "fallbackUsername", "fallbackPassword", "tag"]

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
        """Create an instance of UpdateCall from a JSON string"""
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

        # set to None if state (nullable) is None
        # and model_fields_set contains the field
        if self.state is None and "state" in self.model_fields_set:
            _dict['state'] = None

        # set to None if redirect_url (nullable) is None
        # and model_fields_set contains the field
        if self.redirect_url is None and "redirect_url" in self.model_fields_set:
            _dict['redirectUrl'] = None

        # set to None if redirect_method (nullable) is None
        # and model_fields_set contains the field
        if self.redirect_method is None and "redirect_method" in self.model_fields_set:
            _dict['redirectMethod'] = None

        # set to None if username (nullable) is None
        # and model_fields_set contains the field
        if self.username is None and "username" in self.model_fields_set:
            _dict['username'] = None

        # set to None if password (nullable) is None
        # and model_fields_set contains the field
        if self.password is None and "password" in self.model_fields_set:
            _dict['password'] = None

        # set to None if redirect_fallback_url (nullable) is None
        # and model_fields_set contains the field
        if self.redirect_fallback_url is None and "redirect_fallback_url" in self.model_fields_set:
            _dict['redirectFallbackUrl'] = None

        # set to None if redirect_fallback_method (nullable) is None
        # and model_fields_set contains the field
        if self.redirect_fallback_method is None and "redirect_fallback_method" in self.model_fields_set:
            _dict['redirectFallbackMethod'] = None

        # set to None if fallback_username (nullable) is None
        # and model_fields_set contains the field
        if self.fallback_username is None and "fallback_username" in self.model_fields_set:
            _dict['fallbackUsername'] = None

        # set to None if fallback_password (nullable) is None
        # and model_fields_set contains the field
        if self.fallback_password is None and "fallback_password" in self.model_fields_set:
            _dict['fallbackPassword'] = None

        # set to None if tag (nullable) is None
        # and model_fields_set contains the field
        if self.tag is None and "tag" in self.model_fields_set:
            _dict['tag'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdateCall from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "state": obj.get("state"),
            "redirectUrl": obj.get("redirectUrl"),
            "redirectMethod": obj.get("redirectMethod"),
            "username": obj.get("username"),
            "password": obj.get("password"),
            "redirectFallbackUrl": obj.get("redirectFallbackUrl"),
            "redirectFallbackMethod": obj.get("redirectFallbackMethod"),
            "fallbackUsername": obj.get("fallbackUsername"),
            "fallbackPassword": obj.get("fallbackPassword"),
            "tag": obj.get("tag")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


