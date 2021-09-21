"""
test_api.py

Integration tests for API requests

@copyright Bandwidth INC
"""
import os
import pytest
from datetime import datetime
from bandwidth.bandwidth_client import BandwidthClient
from bandwidth.messaging.exceptions.messaging_exception import MessagingException
from bandwidth.exceptions.api_exception import APIException
from bandwidth.messaging.models.message_request import MessageRequest
from bandwidth.voice.models.create_call_request import CreateCallRequest
from bandwidth.voice.models.machine_detection_request import MachineDetectionRequest
from bandwidth.multifactorauth.models.two_factor_code_request_schema import TwoFactorCodeRequestSchema
from bandwidth.multifactorauth.models.two_factor_verify_request_schema import TwoFactorVerifyRequestSchema
from bandwidth.phonenumberlookup.models.order_request import OrderRequest
from bandwidth.configuration import Environment

try:
    BW_USERNAME = os.environ["BW_USERNAME"]
    BW_PASSWORD = os.environ["BW_PASSWORD"]
    BW_ACCOUNT_ID = os.environ["BW_ACCOUNT_ID"]
    BW_VOICE_APPLICATION_ID = os.environ["BW_VOICE_APPLICATION_ID"]
    BW_MESSAGING_APPLICATION_ID = os.environ["BW_MESSAGING_APPLICATION_ID"]
    BASE_CALLBACK_URL = os.environ["BASE_CALLBACK_URL"]
    BW_NUMBER = os.environ["BW_NUMBER"]
    USER_NUMBER = os.environ["USER_NUMBER"]
except KeyError as e:
    raise Exception("Environmental variables not found")


@pytest.fixture()
def messaging_client():
    bandwidth_client = BandwidthClient(
        messaging_basic_auth_user_name=BW_USERNAME,
        messaging_basic_auth_password=BW_PASSWORD,
    )
    messaging_client = bandwidth_client.messaging_client.client
    return messaging_client


@pytest.fixture()
def voice_client():
    bandwidth_client = BandwidthClient(
        voice_basic_auth_user_name=BW_USERNAME,
        voice_basic_auth_password=BW_PASSWORD,
    )
    voice_client = bandwidth_client.voice_client.client
    return voice_client


@pytest.fixture()
def mfa_client():
    bandwidth_client = BandwidthClient(
        multi_factor_auth_basic_auth_user_name=BW_USERNAME,
        multi_factor_auth_basic_auth_password=BW_PASSWORD,
    )
    mfa_client = bandwidth_client.multi_factor_auth_client.mfa
    return mfa_client


@pytest.fixture()
def tn_lookup_client():
    bandwidth_client = BandwidthClient(
        phone_number_lookup_basic_auth_user_name=BW_USERNAME,
        phone_number_lookup_basic_auth_password=BW_PASSWORD,
    )
    tn_lookup_client = bandwidth_client.phone_number_lookup_client.client
    return tn_lookup_client


class TestApi:
    """
    Class that holds basic monitoring tests for the Python SDK. Makes requests to cover JSON call and response,
    error handling, and binary string uploads and downloads
    """
    def test_create_successful_message(self, messaging_client):
        """Create valid request to send an SMS using the Messaging API.

        Args:
            messaging_client: Contains the basic auth credentials needed to authenticate.

        """
        message_body = MessageRequest()
        message_body.application_id = BW_MESSAGING_APPLICATION_ID
        message_body.to = [USER_NUMBER]
        message_body.mfrom = BW_NUMBER
        message_body.text = "Python Monitoring"
        response = messaging_client.create_message(BW_ACCOUNT_ID, message_body)
        body = response.body
        assert (response.status_code == 202)
        assert len(body.id) == 29    # asserts `messageId` returned and matches expected length (29)
        assert body.owner == body.mfrom == BW_NUMBER    # asserts `owner` matches `mfrom` number and `BW_NUMBER`
        assert body.application_id == BW_MESSAGING_APPLICATION_ID
        assert datetime.fromisoformat(body.time.replace('Z', '+00:00'))    # asserts the date string is valid ISO
        assert type(body.segment_count) is int
        assert body.to == [USER_NUMBER]
        assert body.media == message_body.media
        assert body.text == message_body.text
        assert body.tag == message_body.tag
        assert body.priority == message_body.priority

    def test_create_failed_message(self, messaging_client):
        """Create invalid request to send an SMS using the Messaging API.

        Args:
            messaging_client: Contains the basic auth credentials needed to authenticate.

        """
        with pytest.raises(MessagingException):    # asserts that a messaging exception is raised
            message_body = MessageRequest()
            message_body.application_id = BW_MESSAGING_APPLICATION_ID
            message_body.to = ["+1invalid"]
            message_body.mfrom = BW_NUMBER
            message_body.text = "Python Monitoring"
            response = messaging_client.create_message(BW_ACCOUNT_ID, message_body)
            body = response.body
            assert response.status_code == 400
            assert type(body.type) == "request-validation"
            assert type(body.description) is str

    def test_media_successful_upload_download(self, messaging_client):
        """Upload a binary string and then download it and confirm both files match

        Args:
            messaging_client: Contains the basic auth credentials needed to authenticate.

        """
        media_file_name = 'python_monitoring'
        media_file = b'12345'
        messaging_client.upload_media(BW_ACCOUNT_ID, media_file_name, media_file)
        response = messaging_client.get_media(BW_ACCOUNT_ID, media_file_name)
        downloaded_media = response.body
        assert response.status_code == 200    # assert successful status
        assert downloaded_media == media_file    # assert the binary strings match

    def test_media_failed_download(self, messaging_client):
        """Attempt to download media that doesnt exist and validate a 404 is reutrned from the API

        Args:
            messaging_client: Contains the basic auth credentials needed to authenticate.

        """
        with pytest.raises(MessagingException):  # asserts that a messaging exception is raised
            media_file_name = 'invalid_python_monitoring'
            response = messaging_client.get_media(BW_ACCOUNT_ID, media_file_name)
            body = response.body
            assert response.status_code == 404    # assert status code
            assert body.type == "object-not-found"
            assert type(body.description) is str
