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
from uipath_orchestrator_rest.api.test_set_executions_api import TestSetExecutionsApi  # noqa: E501
from uipath_orchestrator_rest.rest import ApiException


class TestTestSetExecutionsApi(unittest.TestCase):
    """TestSetExecutionsApi unit test stubs"""

    def setUp(self):
        self.api = uipath_orchestrator_rest.api.test_set_executions_api.TestSetExecutionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_test_set_executions_get(self):
        """Test case for test_set_executions_get

        Returns a list of Test Set Executions cross-folder when no current folder is sent by header.  It will return Test Set Executions from folder where current user has TestSetExecutionsView.  If there is none, will return forbidden.  # noqa: E501
        """
        pass

    def test_test_set_executions_get_by_id(self):
        """Test case for test_set_executions_get_by_id

        Return a specific Test Set Execution identified by key  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
