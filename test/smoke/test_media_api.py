"""
Integration test for Bandwidth's Messaging Media API
"""

import uuid
import filecmp
import unittest
import logging

from bandwidth import ApiResponse

import bandwidth
from hamcrest import *
from bandwidth.api import media_api
from bandwidth.models.media import Media
from bandwidth.exceptions import ApiException, NotFoundException
from test.utils.env_variables import *


class TestMedia(unittest.TestCase):
    """Media API integration Test
    """

    def setUp(self) -> None:
        configuration = bandwidth.Configuration(
            username=BW_USERNAME,
            password=BW_PASSWORD
        )
        self.api_client = bandwidth.ApiClient(configuration)
        self.api_instance = media_api.MediaApi(self.api_client)
        self.account_id = BW_ACCOUNT_ID
        self.media_path = "./test/fixtures/"
        self.media_file = "python_cat.jpeg"
        self.media_id = PYTHON_VERSION + "_" + RUNNER_OS + "_" + str(uuid.uuid4()) + "_" + self.media_file
        self.download_file_path = "cat_download.jpeg"
        self.original_file = open(self.media_path + self.media_file, "rb")

    def uploadMedia(self) -> None:
        """Test uploading media
        """
        media_id = self.media_id
        content_type = "image/jpeg"
        cache_control = "no-cache"

        api_response_with_http_info: ApiResponse = self.api_instance.upload_media_with_http_info(
            account_id=self.account_id,
            media_id=media_id,
            body=bytes(self.original_file.read()),
            _content_type=content_type,
            cache_control=cache_control
        )

        logging.debug(api_response_with_http_info)
        assert_that(api_response_with_http_info.status_code, equal_to(204))

        # reopen the media file
        # the client automatically closes any files passed into request bodies
        reopened_file = open(self.media_path + self.media_file, "rb")

        # returns void
        self.api_instance.upload_media(
            account_id=self.account_id,
            media_id=media_id,
            body=bytes(reopened_file.read()),
            _content_type=content_type,
            cache_control=cache_control
        )

    def listMedia(self) -> None:
        """Test listing all media on the account
        """
        api_response_with_http_info = self.api_instance.list_media_with_http_info(
            self.account_id)

        assert_that(api_response_with_http_info.status_code, equal_to(200))

        api_response = self.api_instance.list_media(self.account_id)
        logging.debug("List Media" + str(api_response))

        assert_that(api_response[0], instance_of(Media))
        pass

    def getMedia(self) -> None:
        """Test downloading the media we previously uploaded
        """
        api_response_with_http_info = self.api_instance.get_media_with_http_info(
            self.account_id, self.media_id)

        logging.debug(api_response_with_http_info)
        assert_that(api_response_with_http_info.status_code, equal_to(200))
        assert_that(api_response_with_http_info.headers["Content-Type"], equal_to("image/jpeg"))

        api_response = self.api_instance.get_media(
            self.account_id, self.media_id)

        with open(self.media_path + self.download_file_path, "wb") as download_file:
            download_file.write(api_response)

        assert_that(filecmp.cmp(self.media_path + self.media_file,
                        self.media_path + self.download_file_path), equal_to(True))
        download_file.close()

    def deleteMedia(self) -> None:
        """Test deleting the media that we previously uploaded
        """
        api_response_with_http_info = self.api_instance.delete_media_with_http_info(
            self.account_id, self.media_id)

        logging.debug(api_response_with_http_info)
        assert_that(api_response_with_http_info.status_code, equal_to(204))

        # returns void
        self.api_instance.delete_media(self.account_id, self.media_id)

    def _steps(self):
        call_order = ['uploadMedia', 'listMedia', 'getMedia', 'deleteMedia']
        for name in call_order:
            yield name, getattr(self, name)

    def test_steps(self) -> None:
        """Test each function from _steps.call_order in specified order
        """

        for name, step in self._steps():
            step()

    @unittest.skip("API does not support url encoded characters in path")
    def testGetMediaWithBandwidthId(self) -> None:
        # use a nonexistent mediaId - results in a 404
        media_id = "abcd1234-e5f6-1111-2222-3456ghi7890/image123456.jpg"

        assert_that(calling(self.api_instance.get_media).with_args(
            self.account_id, media_id, _preload_content=False)), raises(NotFoundException)
