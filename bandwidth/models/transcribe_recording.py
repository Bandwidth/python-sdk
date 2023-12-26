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


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from typing_extensions import Annotated
from bandwidth.models.callback_method_enum import CallbackMethodEnum
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class TranscribeRecording(BaseModel):
    """
    TranscribeRecording
    """ # noqa: E501
    callback_url: Optional[StrictStr] = Field(default=None, description="The URL to send the [TranscriptionAvailable](/docs/voice/webhooks/transcriptionAvailable) event to. You should not include sensitive or personally-identifiable information in the callbackUrl field! Always use the proper username and password fields for authorization.", alias="callbackUrl")
    callback_method: Optional[CallbackMethodEnum] = Field(default=None, alias="callbackMethod")
    username: Optional[Annotated[str, Field(strict=True, max_length=1024)]] = Field(default=None, description="Basic auth username.")
    password: Optional[Annotated[str, Field(strict=True, max_length=1024)]] = Field(default=None, description="Basic auth password.")
    tag: Optional[StrictStr] = Field(default=None, description="(optional) The tag specified on call creation. If no tag was specified or it was previously cleared, this field will not be present.")
    callback_timeout: Optional[Union[Annotated[float, Field(le=25, strict=True, ge=1)], Annotated[int, Field(le=25, strict=True, ge=1)]]] = Field(default=15, description="This is the timeout (in seconds) to use when delivering the webhook to `callbackUrl`. Can be any numeric value (including decimals) between 1 and 25.", alias="callbackTimeout")
    detect_language: Optional[StrictBool] = Field(default=False, description="A boolean value to indicate that the recording may not be in English, and the transcription service will need to detect the dominant language the recording is in and transcribe accordingly. Current supported languages are English, French, and Spanish.", alias="detectLanguage")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["callbackUrl", "callbackMethod", "username", "password", "tag", "callbackTimeout", "detectLanguage"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TranscribeRecording from a JSON string"""
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
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "additional_properties",
            },
            exclude_none=True,
        )
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if callback_method (nullable) is None
        # and model_fields_set contains the field
        if self.callback_method is None and "callback_method" in self.model_fields_set:
            _dict['callbackMethod'] = None

        # set to None if username (nullable) is None
        # and model_fields_set contains the field
        if self.username is None and "username" in self.model_fields_set:
            _dict['username'] = None

        # set to None if password (nullable) is None
        # and model_fields_set contains the field
        if self.password is None and "password" in self.model_fields_set:
            _dict['password'] = None

        # set to None if tag (nullable) is None
        # and model_fields_set contains the field
        if self.tag is None and "tag" in self.model_fields_set:
            _dict['tag'] = None

        # set to None if callback_timeout (nullable) is None
        # and model_fields_set contains the field
        if self.callback_timeout is None and "callback_timeout" in self.model_fields_set:
            _dict['callbackTimeout'] = None

        # set to None if detect_language (nullable) is None
        # and model_fields_set contains the field
        if self.detect_language is None and "detect_language" in self.model_fields_set:
            _dict['detectLanguage'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of TranscribeRecording from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "callbackUrl": obj.get("callbackUrl"),
            "callbackMethod": obj.get("callbackMethod"),
            "username": obj.get("username"),
            "password": obj.get("password"),
            "tag": obj.get("tag"),
            "callbackTimeout": obj.get("callbackTimeout") if obj.get("callbackTimeout") is not None else 15,
            "detectLanguage": obj.get("detectLanguage") if obj.get("detectLanguage") is not None else False
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


