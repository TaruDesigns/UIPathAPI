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
from UIPathAPI.api.test_case_executions_api import TestCaseExecutionsApi  # noqa: E501
from UIPathAPI.rest import ApiException


class TestTestCaseExecutionsApi(unittest.TestCase):
    """TestCaseExecutionsApi unit test stubs"""

    def setUp(self):
        self.api = UIPathAPI.api.test_case_executions_api.TestCaseExecutionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_test_case_executions_get(self):
        """Test case for test_case_executions_get

        Returns a list of Test Case Executions  # noqa: E501
        """
        pass

    def test_test_case_executions_get_by_id(self):
        """Test case for test_case_executions_get_by_id

        Return a specific Test Case Execution identified by key  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
