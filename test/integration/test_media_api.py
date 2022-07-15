"""
Integration test for Bandwidth's Media API
"""

import os
import filecmp
import unittest

import bandwidth
from bandwidth.api import media_api
from bandwidth.model.media import Media
from bandwidth.exceptions import ApiException, NotFoundException


class TestMedia(unittest.TestCase):
    """Media API integration Test
    """

    def setUp(self) -> None:
        configuration = bandwidth.Configuration(
            username=os.environ['BW_USERNAME'],
            password=os.environ['BW_PASSWORD']
        )
        api_client = bandwidth.ApiClient(configuration)
        self.api_instance = media_api.MediaApi(api_client)
        self.account_id = os.environ['BW_ACCOUNT_ID']
        self.media_path = "./test/fixtures/"
        self.media_id = "python_cat.jpeg"
        self.download_file_path = "cat_download.jpeg"

        self.original_file = open(self.media_path + self.media_id, "rb")

    def step1(self) -> None:
        """Test uploading media
        """
        media_id = self.media_id
        content_type = "image/jpeg"
        cache_control = "no-cache"

        api_response_with_http_info = self.api_instance.upload_media(
            account_id=self.account_id,
            media_id=media_id,
            body=self.original_file,
            content_type=content_type,
            cache_control=cache_control,
            _return_http_data_only=False
        )

        self.assertEqual(api_response_with_http_info[1], 204)

        # reopen the media file
        # the client automatically closes any files passed into request bodies
        reopened_file = open(self.media_path + self.media_id, "rb")
        # returns void
        self.api_instance.upload_media(
            account_id=self.account_id,
            media_id=media_id,
            body=reopened_file,
            content_type=content_type,
            cache_control=cache_control,
            _return_http_data_only=False
        )

    def step2(self) -> None:
        """Test listing all media on the account
        """
        api_response_with_http_info = self.api_instance.list_media(
            self.account_id, _return_http_data_only=False)

        self.assertEqual(api_response_with_http_info[1], 200)

        api_response = self.api_instance.list_media(self.account_id)

        self.assertIs(type(api_response[0]), Media)
        pass

    def step3(self) -> None:
        """Test downloading the media we uploaded in step 1
        """
        api_response_with_http_info = self.api_instance.get_media(
            self.account_id, self.media_id, _return_http_data_only=False)

        self.assertEqual(api_response_with_http_info[1], 200)

        api_response = self.api_instance.get_media(
            self.account_id, self.media_id, _preload_content=False)

        download_file = open(self.media_path + self.download_file_path, "wb")
        download_file.write(api_response.data)

        self.assertTrue(filecmp.cmp(self.media_path + self.media_id,
                        self.media_path + self.download_file_path))
        download_file.close()

    def step4(self) -> None:
        """Test deleting the media that was uploaded in step 1
        """
        api_response_with_http_info = self.api_instance.delete_media(
            self.account_id, self.media_id, _return_http_data_only=False)

        self.assertEqual(api_response_with_http_info[1], 204)

    def _steps(self) -> None:
        for name in dir(self):  # dir() result is implicitly sorted
            if name.startswith("step"):
                yield name, getattr(self, name)

    def test_steps(self) -> None:
        """Test each step{x} function in numerical order
        """
        for name, step in self._steps():
            try:
                step()
            except ApiException as e:
                self.fail("{} failed ({}: {})".format(step, type(e), e))

    @unittest.skip("API does not support url encoded characters in path")
    def testGetMediaWithBandwidthId(self) -> None:
        # use a nonexistent mediaId - results in a 404
        media_id = "abcd1234-e5f6-1111-2222-3456ghi7890/image123456.jpg"

        with self.assertRaises(NotFoundException) as context:
            api_response = self.api_instance.get_media(
                self.account_id,
                media_id,
                _preload_content=False
            )

        self.assertEqual(context.exception.status, 404)
