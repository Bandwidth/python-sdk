"""
Integration test for Bandwidth's Multi-Factor Authentication API
"""

import os
import unittest

import bandwidth
from bandwidth.api import media_api


class TestMultiFactorAuthentication(unittest.TestCase):
    """Media API integration Test
    """

    def setUp(self):
        configuration = bandwidth.Configuration(
            username=os.environ['BW_USERNAME'],
            password=os.environ['BW_PASSWORD']
        )
        api_client = bandwidth.ApiClient(configuration)
        self.api_instance = media_api.MediaApi(api_client)
        self.account_id = os.environ['BW_ACCOUNT_ID']
        self.media_path = "./test/fixtures/"
        self.media_id = "python_cat.jpeg"

    def testUploadMedia(self):
        media_id = self.media_id
        content_type = "image/jpeg"
        cache_control = "no-cache"
        image_file = open(self.media_path + self.media_id, "rb")

        api_response = self.api_instance.upload_media(
            account_id=self.account_id,
            media_id=media_id,
            body=image_file,
            content_type=content_type,
            cache_control=cache_control
        )

    def testDownloadMedia(self):
        api_response = self.api_instance.get_media(
            self.account_id, self.media_id, _preload_content=False)
        
        downloadFile = open(self.media_path + "new_file_download.jpeg", "wb")
        downloadFile.write(api_response.data)
        downloadFile.close()
