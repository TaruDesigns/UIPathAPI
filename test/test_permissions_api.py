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
from uipath_orchestrator_rest.api.permissions_api import PermissionsApi  # noqa: E501
from uipath_orchestrator_rest.rest import ApiException


class TestPermissionsApi(unittest.TestCase):
    """PermissionsApi unit test stubs"""

    def setUp(self):
        self.api = uipath_orchestrator_rest.api.permissions_api.PermissionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_permissions_get(self):
        """Test case for permissions_get

        Gets permissions.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
