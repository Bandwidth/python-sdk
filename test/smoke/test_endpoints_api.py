"""
Integration test for Bandwidth's WebRTC Endpoints API
"""
import unittest
import time

from hamcrest import assert_that, has_properties, not_none, instance_of, equal_to

from bandwidth import ApiClient, ApiResponse, Configuration
from bandwidth.api.endpoints_api import EndpointsApi
from bandwidth.models.create_web_rtc_connection_request import CreateWebRtcConnectionRequest
from bandwidth.models.create_endpoint_response import CreateEndpointResponse
from bandwidth.models.endpoint_response import EndpointResponse
from bandwidth.models.list_endpoints_response import ListEndpointsResponse
from bandwidth.models.endpoint_type_enum import EndpointTypeEnum
from bandwidth.models.endpoint_direction_enum import EndpointDirectionEnum
from bandwidth.models.endpoint_status_enum import EndpointStatusEnum
from bandwidth.exceptions import ApiException, UnauthorizedException, ForbiddenException, NotFoundException
from test.utils.env_variables import *


class TestEndpointsApi(unittest.TestCase):
    """EndpointsApi integration Test"""

    @classmethod
    def setUpClass(cls) -> None:
        configuration = Configuration(
            client_id=BW_CLIENT_ID,
            client_secret=BW_CLIENT_SECRET
        )
        api_client = ApiClient(configuration)
        cls.endpoints_api_instance = EndpointsApi(api_client)

        # Unauthorized API Client
        cls.unauthorized_api_client = ApiClient()
        cls.unauthorized_api_instance = EndpointsApi(cls.unauthorized_api_client)

        cls.account_id = BW_ACCOUNT_ID
        cls.endpoint_id_array = []
        cls.TEST_SLEEP = 2

    @classmethod
    def tearDownClass(cls):
        """Clean up endpoints created during tests"""
        for endpoint_id in cls.endpoint_id_array:
            try:
                cls.endpoints_api_instance.delete_endpoint(cls.account_id, endpoint_id)
                time.sleep(1)
            except Exception as e:
                print(f"Failed to cleanup endpoint {endpoint_id}: {e}")

    def test_create_endpoint(self):
        """Test creating a new WebRTC endpoint with all parameters"""
        time.sleep(self.TEST_SLEEP)

        create_request = CreateWebRtcConnectionRequest(
            type=EndpointTypeEnum.WEBRTC,
            direction=EndpointDirectionEnum.BIDIRECTIONAL,
            event_callback_url=BASE_CALLBACK_URL + "/endpoint/callback",
            event_fallback_url=BASE_CALLBACK_URL + "/endpoint/fallback",
            tag="python-sdk-test-endpoint"
        )

        response: ApiResponse = self.endpoints_api_instance.create_endpoint_with_http_info(
            self.account_id,
            create_request
        )

        assert_that(response.status_code, equal_to(201))
        assert_that(response.data, instance_of(CreateEndpointResponse))
        assert_that(response.data.data, has_properties(
            'endpoint_id', instance_of(str),
            'type', EndpointTypeEnum.WEBRTC,
            'status', instance_of(EndpointStatusEnum),
            'token', instance_of(str)
        ))

        # Store endpoint ID for cleanup
        self.endpoint_id_array.append(response.data.data.endpoint_id)

    def test_create_endpoint_minimal(self):
        """Test creating an endpoint with only required parameters"""
        time.sleep(self.TEST_SLEEP)

        create_request = CreateWebRtcConnectionRequest(
            type=EndpointTypeEnum.WEBRTC,
            direction=EndpointDirectionEnum.OUTBOUND
        )

        response: CreateEndpointResponse = self.endpoints_api_instance.create_endpoint(
            self.account_id,
            create_request
        )

        assert_that(response.data, has_properties(
            'endpoint_id', instance_of(str),
            'type', EndpointTypeEnum.WEBRTC,
            'token', not_none()
        ))

        # Store endpoint ID for cleanup
        self.endpoint_id_array.append(response.data.endpoint_id)

    def test_get_endpoint(self):
        """Test retrieving an endpoint by ID"""
        time.sleep(self.TEST_SLEEP)

        # First create an endpoint
        create_request = CreateWebRtcConnectionRequest(
            type=EndpointTypeEnum.WEBRTC,
            direction=EndpointDirectionEnum.INBOUND,
            tag="test-get-endpoint"
        )

        create_response: CreateEndpointResponse = self.endpoints_api_instance.create_endpoint(
            self.account_id,
            create_request
        )

        endpoint_id = create_response.data.endpoint_id
        self.endpoint_id_array.append(endpoint_id)

        time.sleep(self.TEST_SLEEP)

        # Now get the endpoint
        response: ApiResponse = self.endpoints_api_instance.get_endpoint_with_http_info(
            self.account_id,
            endpoint_id
        )

        assert_that(response.status_code, equal_to(200))
        assert_that(response.data, instance_of(EndpointResponse))
        assert_that(response.data.data, has_properties(
            'endpoint_id', endpoint_id,
            'type', EndpointTypeEnum.WEBRTC,
            'tag', "test-get-endpoint"
        ))

    def test_get_endpoint_not_found(self):
        """Test getting a non-existent endpoint returns 404"""
        time.sleep(self.TEST_SLEEP)

        with self.assertRaises(ApiException) as context:
            self.endpoints_api_instance.get_endpoint(
                self.account_id,
                "non-existent-endpoint-id"
            )

        assert_that(context.exception.status, equal_to(404))

    def test_list_endpoints(self):
        """Test listing endpoints"""
        time.sleep(self.TEST_SLEEP)

        # Create a couple of endpoints first
        for i in range(2):
            create_request = CreateWebRtcConnectionRequest(
                type=EndpointTypeEnum.WEBRTC,
                direction=EndpointDirectionEnum.BIDIRECTIONAL,
                tag=f"test-list-endpoint-{i}"
            )
            create_response = self.endpoints_api_instance.create_endpoint(
                self.account_id,
                create_request
            )
            self.endpoint_id_array.append(create_response.data.endpoint_id)
            time.sleep(1)

        time.sleep(self.TEST_SLEEP)

        # List endpoints
        response: ApiResponse = self.endpoints_api_instance.list_endpoints_with_http_info(
            self.account_id,
            limit=10
        )

        assert_that(response.status_code, equal_to(200))
        assert_that(response.data, instance_of(ListEndpointsResponse))
        assert_that(response.data.data, instance_of(list))

    def test_list_endpoints_with_filter(self):
        """Test listing endpoints with type filter"""
        time.sleep(self.TEST_SLEEP)

        response: ListEndpointsResponse = self.endpoints_api_instance.list_endpoints(
            self.account_id,
            type=EndpointTypeEnum.WEBRTC,
            limit=5
        )

        assert_that(response.data, instance_of(list))
        # Verify all returned endpoints are of type WEBRTC
        for endpoint in response.data:
            assert_that(endpoint.type, equal_to(EndpointTypeEnum.WEBRTC))

    def test_delete_endpoint(self):
        """Test deleting an endpoint"""
        time.sleep(self.TEST_SLEEP)

        # Create an endpoint to delete
        create_request = CreateWebRtcConnectionRequest(
            type=EndpointTypeEnum.WEBRTC,
            direction=EndpointDirectionEnum.BIDIRECTIONAL,
            tag="test-delete-endpoint"
        )

        create_response: CreateEndpointResponse = self.endpoints_api_instance.create_endpoint(
            self.account_id,
            create_request
        )
        endpoint_id = create_response.data.endpoint_id

        time.sleep(self.TEST_SLEEP)

        # Delete the endpoint
        response: ApiResponse = self.endpoints_api_instance.delete_endpoint_with_http_info(
            self.account_id,
            endpoint_id
        )

        assert_that(response.status_code, equal_to(204))

        # Verify endpoint is deleted
        time.sleep(self.TEST_SLEEP)
        with self.assertRaises(ApiException) as context:
            self.endpoints_api_instance.get_endpoint(self.account_id, endpoint_id)

        assert_that(context.exception.status, equal_to(404))

    def test_delete_endpoint_not_found(self):
        """Test deleting a non-existent endpoint returns 404"""
        time.sleep(self.TEST_SLEEP)

        with self.assertRaises(ApiException) as context:
            self.endpoints_api_instance.delete_endpoint(
                self.account_id,
                "non-existent-endpoint-id"
            )

        assert_that(context.exception.status, equal_to(404))

    def test_create_endpoint_unauthorized(self):
        """Test creating an endpoint with invalid credentials returns 401"""
        time.sleep(self.TEST_SLEEP)

        create_request = CreateWebRtcConnectionRequest(
            type=EndpointTypeEnum.WEBRTC,
            direction=EndpointDirectionEnum.BIDIRECTIONAL
        )

        with self.assertRaises(ApiException) as context:
            self.unauthorized_api_instance.create_endpoint(
                self.account_id,
                create_request
            )

        assert_that(context.exception.status, equal_to(401))


if __name__ == '__main__':
    unittest.main()
