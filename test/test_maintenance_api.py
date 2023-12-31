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
from UIPathAPI.api.maintenance_api import MaintenanceApi  # noqa: E501
from UIPathAPI.rest import ApiException


class TestMaintenanceApi(unittest.TestCase):
    """MaintenanceApi unit test stubs"""

    def setUp(self):
        self.api = UIPathAPI.api.maintenance_api.MaintenanceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_maintenance_end(self):
        """Test case for maintenance_end

        Ends a maintenance window  # noqa: E501
        """
        pass

    def test_maintenance_get(self):
        """Test case for maintenance_get

        Gets the host admin logs.  # noqa: E501
        """
        pass

    def test_maintenance_start(self):
        """Test case for maintenance_start

        Starts a maintenance window  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
