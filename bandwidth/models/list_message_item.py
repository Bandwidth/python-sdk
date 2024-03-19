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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from bandwidth.models.list_message_direction_enum import ListMessageDirectionEnum
from bandwidth.models.message_status_enum import MessageStatusEnum
from bandwidth.models.message_type_enum import MessageTypeEnum
from typing import Optional, Set
from typing_extensions import Self

class ListMessageItem(BaseModel):
    """
    ListMessageItem
    """ # noqa: E501
    message_id: Optional[StrictStr] = Field(default=None, description="The message id", alias="messageId")
    account_id: Optional[StrictStr] = Field(default=None, description="The account id associated with this message.", alias="accountId")
    source_tn: Optional[StrictStr] = Field(default=None, description="The source phone number of the message.", alias="sourceTn")
    destination_tn: Optional[StrictStr] = Field(default=None, description="The recipient phone number of the message.", alias="destinationTn")
    message_status: Optional[MessageStatusEnum] = Field(default=None, alias="messageStatus")
    message_direction: Optional[ListMessageDirectionEnum] = Field(default=None, alias="messageDirection")
    message_type: Optional[MessageTypeEnum] = Field(default=None, alias="messageType")
    segment_count: Optional[StrictInt] = Field(default=None, description="The number of segments the message was sent as.", alias="segmentCount")
    error_code: Optional[StrictInt] = Field(default=None, description="The numeric error code of the message.", alias="errorCode")
    receive_time: Optional[datetime] = Field(default=None, description="The ISO 8601 datetime of the message.", alias="receiveTime")
    carrier_name: Optional[StrictStr] = Field(default=None, description="The name of the carrier. Not currently supported for MMS coming soon.", alias="carrierName")
    message_size: Optional[StrictInt] = Field(default=None, description="The size of the message including message content and headers.", alias="messageSize")
    message_length: Optional[StrictInt] = Field(default=None, description="The length of the message content.", alias="messageLength")
    attachment_count: Optional[StrictInt] = Field(default=None, description="The number of attachments the message has.", alias="attachmentCount")
    recipient_count: Optional[StrictInt] = Field(default=None, description="The number of recipients the message has.", alias="recipientCount")
    campaign_class: Optional[StrictStr] = Field(default=None, description="The campaign class of the message if it has one.", alias="campaignClass")
    campaign_id: Optional[StrictStr] = Field(default=None, description="The campaign ID of the message if it has one.", alias="campaignId")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["messageId", "accountId", "sourceTn", "destinationTn", "messageStatus", "messageDirection", "messageType", "segmentCount", "errorCode", "receiveTime", "carrierName", "messageSize", "messageLength", "attachmentCount", "recipientCount", "campaignClass", "campaignId"]

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
        """Create an instance of ListMessageItem from a JSON string"""
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

        # set to None if carrier_name (nullable) is None
        # and model_fields_set contains the field
        if self.carrier_name is None and "carrier_name" in self.model_fields_set:
            _dict['carrierName'] = None

        # set to None if message_size (nullable) is None
        # and model_fields_set contains the field
        if self.message_size is None and "message_size" in self.model_fields_set:
            _dict['messageSize'] = None

        # set to None if attachment_count (nullable) is None
        # and model_fields_set contains the field
        if self.attachment_count is None and "attachment_count" in self.model_fields_set:
            _dict['attachmentCount'] = None

        # set to None if recipient_count (nullable) is None
        # and model_fields_set contains the field
        if self.recipient_count is None and "recipient_count" in self.model_fields_set:
            _dict['recipientCount'] = None

        # set to None if campaign_class (nullable) is None
        # and model_fields_set contains the field
        if self.campaign_class is None and "campaign_class" in self.model_fields_set:
            _dict['campaignClass'] = None

        # set to None if campaign_id (nullable) is None
        # and model_fields_set contains the field
        if self.campaign_id is None and "campaign_id" in self.model_fields_set:
            _dict['campaignId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ListMessageItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "messageId": obj.get("messageId"),
            "accountId": obj.get("accountId"),
            "sourceTn": obj.get("sourceTn"),
            "destinationTn": obj.get("destinationTn"),
            "messageStatus": obj.get("messageStatus"),
            "messageDirection": obj.get("messageDirection"),
            "messageType": obj.get("messageType"),
            "segmentCount": obj.get("segmentCount"),
            "errorCode": obj.get("errorCode"),
            "receiveTime": obj.get("receiveTime"),
            "carrierName": obj.get("carrierName"),
            "messageSize": obj.get("messageSize"),
            "messageLength": obj.get("messageLength"),
            "attachmentCount": obj.get("attachmentCount"),
            "recipientCount": obj.get("recipientCount"),
            "campaignClass": obj.get("campaignClass"),
            "campaignId": obj.get("campaignId")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


