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
from UIPathAPI.api.licenses_runtime_api import LicensesRuntimeApi  # noqa: E501
from UIPathAPI.rest import ApiException


class TestLicensesRuntimeApi(unittest.TestCase):
    """LicensesRuntimeApi unit test stubs"""

    def setUp(self):
        self.api = UIPathAPI.api.licenses_runtime_api.LicensesRuntimeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_licenses_runtime_get_licenses_runtime_by_robottype(self):
        """Test case for licenses_runtime_get_licenses_runtime_by_robottype

        Gets runtime licenses.  # noqa: E501
        """
        pass

    def test_licenses_runtime_toggle_enabled_by_key(self):
        """Test case for licenses_runtime_toggle_enabled_by_key

        Toggles machine licensing on/off.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
