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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from bandwidth.models.lookup_result import LookupResult
from bandwidth.models.lookup_status_enum import LookupStatusEnum
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class LookupStatus(BaseModel):
    """
    If requestId exists, the result for that request is returned. See the Examples for details on the various responses that you can receive. Generally, if you see a Response Code of 0 in a result for a TN, information will be available for it.  Any other Response Code will indicate no information was available for the TN.
    """ # noqa: E501
    request_id: Optional[StrictStr] = Field(default=None, description="The requestId.", alias="requestId")
    status: Optional[LookupStatusEnum] = None
    result: Optional[List[LookupResult]] = Field(default=None, description="The carrier information results for the specified telephone number.")
    failed_telephone_numbers: Optional[List[StrictStr]] = Field(default=None, description="The telephone numbers whose lookup failed.", alias="failedTelephoneNumbers")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["requestId", "status", "result", "failedTelephoneNumbers"]

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
        """Create an instance of LookupStatus from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in result (list)
        _items = []
        if self.result:
            for _item in self.result:
                if _item:
                    _items.append(_item.to_dict())
            _dict['result'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of LookupStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "requestId": obj.get("requestId"),
            "status": obj.get("status"),
            "result": [LookupResult.from_dict(_item) for _item in obj.get("result")] if obj.get("result") is not None else None,
            "failedTelephoneNumbers": obj.get("failedTelephoneNumbers")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


