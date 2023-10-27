# coding: utf-8

"""
    UiPath.WebApi 17.0

    Orchestrator API  # noqa: E501

    OpenAPI spec version: 17.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import UIPathAPI
from UIPathAPI.api.package_feeds_api import PackageFeedsApi  # noqa: E501
from UIPathAPI.rest import ApiException


class TestPackageFeedsApi(unittest.TestCase):
    """PackageFeedsApi unit test stubs"""

    def setUp(self):
        self.api = UIPathAPI.api.package_feeds_api.PackageFeedsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_package_feeds_get_folder_feed(self):
        """Test case for package_feeds_get_folder_feed

        Returns the feed id for a user assigned folder having specific feed  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
