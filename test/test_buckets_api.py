# coding: utf-8

"""
    UiPath.WebApi 16.0

    Orchestrator API  # noqa: E501

    OpenAPI spec version: 16.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import UIPathAPI
from UIPathAPI.api.buckets_api import BucketsApi  # noqa: E501
from UIPathAPI.rest import ApiException


class TestBucketsApi(unittest.TestCase):
    """BucketsApi unit test stubs"""

    def setUp(self):
        self.api = UIPathAPI.api.buckets_api.BucketsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_buckets_delete_by_id(self):
        """Test case for buckets_delete_by_id

        Delete a bucket  # noqa: E501
        """
        pass

    def test_buckets_delete_file_by_key(self):
        """Test case for buckets_delete_file_by_key

        Deletes a file.  # noqa: E501
        """
        pass

    def test_buckets_get(self):
        """Test case for buckets_get

        Gets Buckets.  # noqa: E501
        """
        pass

    def test_buckets_get_buckets_across_folders(self):
        """Test case for buckets_get_buckets_across_folders

        Get the buckets from all the folders in which the current user has the Buckets.View permission, except the one specified.  # noqa: E501
        """
        pass

    def test_buckets_get_by_id(self):
        """Test case for buckets_get_by_id

        Gets a single Bucket.  # noqa: E501
        """
        pass

    def test_buckets_get_directories_by_key(self):
        """Test case for buckets_get_directories_by_key

        Gets the child directories in a directory.  # noqa: E501
        """
        pass

    def test_buckets_get_file_by_key(self):
        """Test case for buckets_get_file_by_key

        Gets a file metadata.  # noqa: E501
        """
        pass

    def test_buckets_get_files_by_key(self):
        """Test case for buckets_get_files_by_key

        Gets the files in a directory.  Optionally returns all files in all child directories (recursive).  # noqa: E501
        """
        pass

    def test_buckets_get_folders_for_bucket_by_id(self):
        """Test case for buckets_get_folders_for_bucket_by_id

        Get all accessible folders where the bucket is shared, and the total count of folders where it is shared (including unaccessible folders).  # noqa: E501
        """
        pass

    def test_buckets_get_read_uri_by_key(self):
        """Test case for buckets_get_read_uri_by_key

        Gets a direct download URL for BlobFile.  # noqa: E501
        """
        pass

    def test_buckets_get_write_uri_by_key(self):
        """Test case for buckets_get_write_uri_by_key

        Gets a direct upload URL for BlobFile.  # noqa: E501
        """
        pass

    def test_buckets_post(self):
        """Test case for buckets_post

        Creates an Bucket  # noqa: E501
        """
        pass

    def test_buckets_put_by_id(self):
        """Test case for buckets_put_by_id

        Updates a bucket.  # noqa: E501
        """
        pass

    def test_buckets_share_to_folders(self):
        """Test case for buckets_share_to_folders

        Adds the buckets to the folders specified in 'ToAddFolderIds'. Removes the buckets from the folders specified in 'ToRemoveFolderIds'.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
