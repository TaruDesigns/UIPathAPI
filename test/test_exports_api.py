# coding: utf-8

"""
    UiPath.WebApi 18.0

    Orchestrator API  # noqa: E501

    OpenAPI spec version: 18.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import uipath_orchestrator_rest
from uipath_orchestrator_rest.api.exports_api import ExportsApi  # noqa: E501
from uipath_orchestrator_rest.rest import ApiException


class TestExportsApi(unittest.TestCase):
    """ExportsApi unit test stubs"""

    def setUp(self):
        self.api = uipath_orchestrator_rest.api.exports_api.ExportsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_exports_get_by_id(self):
        """Test case for exports_get_by_id

        """
        pass

    def test_exports_get_download_link_by_id(self):
        """Test case for exports_get_download_link_by_id

        """
        pass


if __name__ == '__main__':
    unittest.main()
