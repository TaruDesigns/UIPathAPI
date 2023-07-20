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
from UIPathAPI.api.directory_service_api import DirectoryServiceApi  # noqa: E501
from UIPathAPI.rest import ApiException


class TestDirectoryServiceApi(unittest.TestCase):
    """DirectoryServiceApi unit test stubs"""

    def setUp(self):
        self.api = UIPathAPI.api.directory_service_api.DirectoryServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_directory_service_get_directory_permissions(self):
        """Test case for directory_service_get_directory_permissions

        Gets directory permissions  # noqa: E501
        """
        pass

    def test_directory_service_get_domains(self):
        """Test case for directory_service_get_domains

        Gets domains  # noqa: E501
        """
        pass

    def test_directory_service_search_for_users_and_groups(self):
        """Test case for directory_service_search_for_users_and_groups

        Search users and groups  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
