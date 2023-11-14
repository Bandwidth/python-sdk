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
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictStr
from bandwidth.models.call_direction_enum import CallDirectionEnum

class CallState(BaseModel):
    """
    CallState
    """
    application_id: Optional[StrictStr] = Field(None, alias="applicationId", description="The application id associated with the call.")
    account_id: Optional[StrictStr] = Field(None, alias="accountId", description="The account id associated with the call.")
    call_id: Optional[StrictStr] = Field(None, alias="callId", description="The programmable voice API call ID.")
    parent_call_id: Optional[StrictStr] = Field(None, alias="parentCallId", description="The A-leg call id, set only if this call is the B-leg of a [`<Transfer>`](/docs/voice/bxml/transfer).")
    to: Optional[StrictStr] = Field(None, description="The phone number that received the call, in E.164 format (e.g. +15555555555), or if the call was to a SIP URI, the SIP URI.")
    var_from: Optional[StrictStr] = Field(None, alias="from", description="The phone number that made the call, in E.164 format (e.g. +15555555555).")
    direction: Optional[CallDirectionEnum] = None
    state: Optional[StrictStr] = Field(None, description="The current state of the call. Current possible values are `queued`, `initiated`, `answered` and `disconnected`. Additional states may be added in the future, so your application must be tolerant of unknown values.")
    stir_shaken: Optional[Dict[str, StrictStr]] = Field(None, alias="stirShaken", description="For inbound calls, the Bandwidth STIR/SHAKEN implementation will verify the information provided in the inbound invite request `Identity` header. The verification status is stored in the call state `stirShaken` property as follows.  | Property          | Description | |:------------------|:------------| | verstat | (optional) The verification status indicating whether the verification was successful or not. Possible values are `TN-Verification-Passed` or `TN-Verification-Failed`. | | attestationIndicator | (optional) The attestation level verified by Bandwidth. Possible values are `A` (full), `B` (partial) or `C` (gateway). | | originatingId | (optional) A unique origination identifier. |  Note that these are common properties but that the `stirShaken` object is free form and can contain other key-value pairs.  More information: [Understanding STIR/SHAKEN](https://www.bandwidth.com/regulations/stir-shaken).")
    identity: Optional[StrictStr] = Field(None, description="The value of the `Identity` header from the inbound invite request. Only present for inbound calls and if the account is configured to forward this header.")
    enqueued_time: Optional[datetime] = Field(None, alias="enqueuedTime", description="The time this call was placed in queue.")
    start_time: Optional[datetime] = Field(None, alias="startTime", description="The time the call was initiated, in ISO 8601 format. `null` if the call is still in your queue.")
    answer_time: Optional[datetime] = Field(None, alias="answerTime", description="Populated once the call has been answered, with the time in ISO 8601 format.")
    end_time: Optional[datetime] = Field(None, alias="endTime", description="Populated once the call has ended, with the time in ISO 8601 format.")
    disconnect_cause: Optional[StrictStr] = Field(None, alias="disconnectCause", description="| Cause | Description | |:------|:------------| | `hangup`| One party hung up the call, a [`<Hangup>`](../../bxml/verbs/hangup.md) verb was executed, or there was no more BXML to execute; it indicates that the call ended normally. | | `busy` | Callee was busy. | | `timeout` | Call wasn't answered before the `callTimeout` was reached. | | `cancel` | Call was cancelled by its originator while it was ringing. | | `rejected` | Call was rejected by the callee. | | `callback-error` | BXML callback couldn't be delivered to your callback server. | | `invalid-bxml` | Invalid BXML was returned in response to a callback. | | `application-error` | An unsupported action was tried on the call, e.g. trying to play a .ogg audio. | | `account-limit` | Account rate limits were reached. | | `node-capacity-exceeded` | System maximum capacity was reached. | | `error` | Some error not described in any of the other causes happened on the call. | | `unknown` | Unknown error happened on the call. |  Note: This list is not exhaustive and other values can appear in the future.")
    error_message: Optional[StrictStr] = Field(None, alias="errorMessage", description="Populated only if the call ended with an error, with text explaining the reason.")
    error_id: Optional[StrictStr] = Field(None, alias="errorId", description="Populated only if the call ended with an error, with a Bandwidth internal id that references the error event.")
    last_update: Optional[datetime] = Field(None, alias="lastUpdate", description="The last time the call had a state update, in ISO 8601 format.")
    additional_properties: Dict[str, Any] = {}
    __properties = ["applicationId", "accountId", "callId", "parentCallId", "to", "from", "direction", "state", "stirShaken", "identity", "enqueuedTime", "startTime", "answerTime", "endTime", "disconnectCause", "errorMessage", "errorId", "lastUpdate"]

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
    def from_json(cls, json_str: str) -> CallState:
        """Create an instance of CallState from a JSON string"""
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

        # set to None if parent_call_id (nullable) is None
        # and __fields_set__ contains the field
        if self.parent_call_id is None and "parent_call_id" in self.__fields_set__:
            _dict['parentCallId'] = None

        # set to None if stir_shaken (nullable) is None
        # and __fields_set__ contains the field
        if self.stir_shaken is None and "stir_shaken" in self.__fields_set__:
            _dict['stirShaken'] = None

        # set to None if identity (nullable) is None
        # and __fields_set__ contains the field
        if self.identity is None and "identity" in self.__fields_set__:
            _dict['identity'] = None

        # set to None if enqueued_time (nullable) is None
        # and __fields_set__ contains the field
        if self.enqueued_time is None and "enqueued_time" in self.__fields_set__:
            _dict['enqueuedTime'] = None

        # set to None if start_time (nullable) is None
        # and __fields_set__ contains the field
        if self.start_time is None and "start_time" in self.__fields_set__:
            _dict['startTime'] = None

        # set to None if answer_time (nullable) is None
        # and __fields_set__ contains the field
        if self.answer_time is None and "answer_time" in self.__fields_set__:
            _dict['answerTime'] = None

        # set to None if end_time (nullable) is None
        # and __fields_set__ contains the field
        if self.end_time is None and "end_time" in self.__fields_set__:
            _dict['endTime'] = None

        # set to None if disconnect_cause (nullable) is None
        # and __fields_set__ contains the field
        if self.disconnect_cause is None and "disconnect_cause" in self.__fields_set__:
            _dict['disconnectCause'] = None

        # set to None if error_message (nullable) is None
        # and __fields_set__ contains the field
        if self.error_message is None and "error_message" in self.__fields_set__:
            _dict['errorMessage'] = None

        # set to None if error_id (nullable) is None
        # and __fields_set__ contains the field
        if self.error_id is None and "error_id" in self.__fields_set__:
            _dict['errorId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CallState:
        """Create an instance of CallState from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CallState.parse_obj(obj)

        _obj = CallState.parse_obj({
            "application_id": obj.get("applicationId"),
            "account_id": obj.get("accountId"),
            "call_id": obj.get("callId"),
            "parent_call_id": obj.get("parentCallId"),
            "to": obj.get("to"),
            "var_from": obj.get("from"),
            "direction": obj.get("direction"),
            "state": obj.get("state"),
            "stir_shaken": obj.get("stirShaken"),
            "identity": obj.get("identity"),
            "enqueued_time": obj.get("enqueuedTime"),
            "start_time": obj.get("startTime"),
            "answer_time": obj.get("answerTime"),
            "end_time": obj.get("endTime"),
            "disconnect_cause": obj.get("disconnectCause"),
            "error_message": obj.get("errorMessage"),
            "error_id": obj.get("errorId"),
            "last_update": obj.get("lastUpdate")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

