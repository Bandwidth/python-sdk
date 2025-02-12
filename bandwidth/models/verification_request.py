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
from bandwidth.models.address import Address
from bandwidth.models.contact import Contact
from bandwidth.models.opt_in_workflow import OptInWorkflow
from typing import Optional, Set
from typing_extensions import Self

class VerificationRequest(BaseModel):
    """
    VerificationRequest
    """ # noqa: E501
    business_address: Address = Field(alias="businessAddress")
    business_contact: Contact = Field(alias="businessContact")
    message_volume: Annotated[int, Field(le=10000000, strict=True, ge=10)] = Field(description="Estimated monthly volume of messages from the toll-free number.", alias="messageVolume")
    phone_numbers: Annotated[List[Annotated[str, Field(min_length=12, strict=True, max_length=12)]], Field(min_length=1, max_length=10)] = Field(alias="phoneNumbers")
    use_case: Annotated[str, Field(min_length=0, strict=True, max_length=500)] = Field(description="The category of the use case.", alias="useCase")
    use_case_summary: Annotated[str, Field(min_length=1, strict=True, max_length=500)] = Field(description="A general idea of the use case and customer.", alias="useCaseSummary")
    production_message_content: Annotated[str, Field(min_length=1, strict=True, max_length=500)] = Field(description="Example of message content.", alias="productionMessageContent")
    opt_in_workflow: OptInWorkflow = Field(alias="optInWorkflow")
    additional_information: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=500)]] = Field(default=None, description="Any additional information.", alias="additionalInformation")
    isv_reseller: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=500)]] = Field(default=None, description="ISV name.", alias="isvReseller")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["businessAddress", "businessContact", "messageVolume", "phoneNumbers", "useCase", "useCaseSummary", "productionMessageContent", "optInWorkflow", "additionalInformation", "isvReseller"]

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
        """Create an instance of VerificationRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of business_address
        if self.business_address:
            _dict['businessAddress'] = self.business_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of business_contact
        if self.business_contact:
            _dict['businessContact'] = self.business_contact.to_dict()
        # override the default output from pydantic by calling `to_dict()` of opt_in_workflow
        if self.opt_in_workflow:
            _dict['optInWorkflow'] = self.opt_in_workflow.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if additional_information (nullable) is None
        # and model_fields_set contains the field
        if self.additional_information is None and "additional_information" in self.model_fields_set:
            _dict['additionalInformation'] = None

        # set to None if isv_reseller (nullable) is None
        # and model_fields_set contains the field
        if self.isv_reseller is None and "isv_reseller" in self.model_fields_set:
            _dict['isvReseller'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VerificationRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "businessAddress": Address.from_dict(obj["businessAddress"]) if obj.get("businessAddress") is not None else None,
            "businessContact": Contact.from_dict(obj["businessContact"]) if obj.get("businessContact") is not None else None,
            "messageVolume": obj.get("messageVolume"),
            "phoneNumbers": obj.get("phoneNumbers"),
            "useCase": obj.get("useCase"),
            "useCaseSummary": obj.get("useCaseSummary"),
            "productionMessageContent": obj.get("productionMessageContent"),
            "optInWorkflow": OptInWorkflow.from_dict(obj["optInWorkflow"]) if obj.get("optInWorkflow") is not None else None,
            "additionalInformation": obj.get("additionalInformation"),
            "isvReseller": obj.get("isvReseller")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


