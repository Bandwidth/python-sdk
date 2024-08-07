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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from bandwidth.models.callback_method_enum import CallbackMethodEnum
from bandwidth.models.machine_detection_mode_enum import MachineDetectionModeEnum
from typing import Optional, Set
from typing_extensions import Self

class MachineDetectionConfiguration(BaseModel):
    """
    The machine detection request used to perform <a href='/docs/voice/guides/machineDetection'>machine detection</a> on the call. Currently, there is an issue where decimal values are not getting processed correctly. Please use whole number values. We are working to resolve this issue. Please contact Bandwidth Support if you need more information.
    """ # noqa: E501
    mode: Optional[MachineDetectionModeEnum] = MachineDetectionModeEnum.ASYNC
    detection_timeout: Optional[Union[StrictFloat, StrictInt]] = Field(default=15, description="The timeout used for the whole operation, in seconds. If no result is determined in this period, a callback with a `timeout` result is sent.", alias="detectionTimeout")
    silence_timeout: Optional[Union[StrictFloat, StrictInt]] = Field(default=10, description="If no speech is detected in this period, a callback with a 'silence' result is sent.", alias="silenceTimeout")
    speech_threshold: Optional[Union[StrictFloat, StrictInt]] = Field(default=10, description="When speech has ended and a result couldn't be determined based on the audio content itself, this value is used to determine if the speaker is a machine based on the speech duration. If the length of the speech detected is greater than or equal to this threshold, the result will be 'answering-machine'. If the length of speech detected is below this threshold, the result will be 'human'.", alias="speechThreshold")
    speech_end_threshold: Optional[Union[StrictFloat, StrictInt]] = Field(default=5, description="Amount of silence (in seconds) before assuming the callee has finished speaking.", alias="speechEndThreshold")
    machine_speech_end_threshold: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="When an answering machine is detected, the amount of silence (in seconds) before assuming the message has finished playing.  If not provided it will default to the speechEndThreshold value.", alias="machineSpeechEndThreshold")
    delay_result: Optional[StrictBool] = Field(default=False, description="If set to 'true' and if an answering machine is detected, the 'answering-machine' callback will be delayed until the machine is done speaking, or an end of message tone is detected, or until the 'detectionTimeout' is exceeded. If false, the 'answering-machine' result is sent immediately.", alias="delayResult")
    callback_url: Optional[Annotated[str, Field(strict=True, max_length=2048)]] = Field(default=None, description="The URL to send the 'machineDetectionComplete' webhook when the detection is completed. Only for 'async' mode.", alias="callbackUrl")
    callback_method: Optional[CallbackMethodEnum] = Field(default=CallbackMethodEnum.POST, alias="callbackMethod")
    username: Optional[Annotated[str, Field(strict=True, max_length=1024)]] = Field(default=None, description="Basic auth username.")
    password: Optional[Annotated[str, Field(strict=True, max_length=1024)]] = Field(default=None, description="Basic auth password.")
    fallback_url: Optional[Annotated[str, Field(strict=True, max_length=2048)]] = Field(default=None, description="A fallback URL which, if provided, will be used to retry the machine detection complete webhook delivery in case `callbackUrl` fails to respond", alias="fallbackUrl")
    fallback_method: Optional[CallbackMethodEnum] = Field(default=CallbackMethodEnum.POST, alias="fallbackMethod")
    fallback_username: Optional[Annotated[str, Field(strict=True, max_length=1024)]] = Field(default=None, description="Basic auth username.", alias="fallbackUsername")
    fallback_password: Optional[Annotated[str, Field(strict=True, max_length=1024)]] = Field(default=None, description="Basic auth password.", alias="fallbackPassword")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["mode", "detectionTimeout", "silenceTimeout", "speechThreshold", "speechEndThreshold", "machineSpeechEndThreshold", "delayResult", "callbackUrl", "callbackMethod", "username", "password", "fallbackUrl", "fallbackMethod", "fallbackUsername", "fallbackPassword"]

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
        """Create an instance of MachineDetectionConfiguration from a JSON string"""
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

        # set to None if detection_timeout (nullable) is None
        # and model_fields_set contains the field
        if self.detection_timeout is None and "detection_timeout" in self.model_fields_set:
            _dict['detectionTimeout'] = None

        # set to None if silence_timeout (nullable) is None
        # and model_fields_set contains the field
        if self.silence_timeout is None and "silence_timeout" in self.model_fields_set:
            _dict['silenceTimeout'] = None

        # set to None if speech_threshold (nullable) is None
        # and model_fields_set contains the field
        if self.speech_threshold is None and "speech_threshold" in self.model_fields_set:
            _dict['speechThreshold'] = None

        # set to None if speech_end_threshold (nullable) is None
        # and model_fields_set contains the field
        if self.speech_end_threshold is None and "speech_end_threshold" in self.model_fields_set:
            _dict['speechEndThreshold'] = None

        # set to None if machine_speech_end_threshold (nullable) is None
        # and model_fields_set contains the field
        if self.machine_speech_end_threshold is None and "machine_speech_end_threshold" in self.model_fields_set:
            _dict['machineSpeechEndThreshold'] = None

        # set to None if delay_result (nullable) is None
        # and model_fields_set contains the field
        if self.delay_result is None and "delay_result" in self.model_fields_set:
            _dict['delayResult'] = None

        # set to None if callback_url (nullable) is None
        # and model_fields_set contains the field
        if self.callback_url is None and "callback_url" in self.model_fields_set:
            _dict['callbackUrl'] = None

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

        # set to None if fallback_url (nullable) is None
        # and model_fields_set contains the field
        if self.fallback_url is None and "fallback_url" in self.model_fields_set:
            _dict['fallbackUrl'] = None

        # set to None if fallback_method (nullable) is None
        # and model_fields_set contains the field
        if self.fallback_method is None and "fallback_method" in self.model_fields_set:
            _dict['fallbackMethod'] = None

        # set to None if fallback_username (nullable) is None
        # and model_fields_set contains the field
        if self.fallback_username is None and "fallback_username" in self.model_fields_set:
            _dict['fallbackUsername'] = None

        # set to None if fallback_password (nullable) is None
        # and model_fields_set contains the field
        if self.fallback_password is None and "fallback_password" in self.model_fields_set:
            _dict['fallbackPassword'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MachineDetectionConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "mode": obj.get("mode") if obj.get("mode") is not None else MachineDetectionModeEnum.ASYNC,
            "detectionTimeout": obj.get("detectionTimeout") if obj.get("detectionTimeout") is not None else 15,
            "silenceTimeout": obj.get("silenceTimeout") if obj.get("silenceTimeout") is not None else 10,
            "speechThreshold": obj.get("speechThreshold") if obj.get("speechThreshold") is not None else 10,
            "speechEndThreshold": obj.get("speechEndThreshold") if obj.get("speechEndThreshold") is not None else 5,
            "machineSpeechEndThreshold": obj.get("machineSpeechEndThreshold"),
            "delayResult": obj.get("delayResult") if obj.get("delayResult") is not None else False,
            "callbackUrl": obj.get("callbackUrl"),
            "callbackMethod": obj.get("callbackMethod") if obj.get("callbackMethod") is not None else CallbackMethodEnum.POST,
            "username": obj.get("username"),
            "password": obj.get("password"),
            "fallbackUrl": obj.get("fallbackUrl"),
            "fallbackMethod": obj.get("fallbackMethod") if obj.get("fallbackMethod") is not None else CallbackMethodEnum.POST,
            "fallbackUsername": obj.get("fallbackUsername"),
            "fallbackPassword": obj.get("fallbackPassword")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


