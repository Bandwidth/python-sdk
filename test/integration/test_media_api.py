"""
Integration test for Bandwidth's Multi-Factor Authentication API
"""

import os
import filecmp
import unittest

from rich import inspect

import bandwidth
from bandwidth.api import media_api
from bandwidth.model.media import Media

class TestMedia(unittest.TestCase):
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
        self.download_file_path = "cat_download.jpeg"

        self.original_file = open(self.media_path + self.media_id, "rb")
    
    def tearDown(self) -> None:
        self.original_file.close()

    def testUploadMedia(self):
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

        # returns void
        self.api_instance.upload_media(
            account_id=self.account_id,
            media_id=media_id,
            body=self.original_file,
            content_type=content_type,
            cache_control=cache_control,
            _return_http_data_only=False
        )

    def testGetMedia(self):
        api_response_with_http_info = self.api_instance.get_media(
            self.account_id, self.media_id, _return_http_data_only=False)
        
        self.assertEqual(api_response_with_http_info[1], 200)
        
        api_response = self.api_instance.get_media(
            self.account_id, self.media_id, _preload_content=False)
        
        download_file = open(self.media_path + self.download_file_path, "wb")
        download_file.write(api_response.data)

        self.assertTrue(filecmp.cmp(self.media_path + self.media_id, self.media_path + self.download_file_path))
        download_file.close()
    
    def testListMedia(self):
        api_response_with_http_info = self.api_instance.list_media(
            self.account_id, _return_http_data_only=False)
        
        self.assertEqual(api_response_with_http_info[1], 200)

        api_response = self.api_instance.list_media(self.account_id)
        
        self.assertIs(type(api_response[0]), Media)

    def testDeleteMedia(self):
        api_response_with_http_info = self.api_instance.delete_media(
            self.account_id, self.media_id, _return_http_data_only=False)
        
        self.assertEqual(api_response_with_http_info[1], 204)
        pass

    def testGetMediaWithBandwidthId(self): 
        media_id = "c0e41604-9a21-4b68-9289-f47c98856e87/1/image000000.jpg"

        api_response = self.api_instance.get_media(
            self.account_id, media_id, _preload_content=False)
        
        inspect(api_response)
