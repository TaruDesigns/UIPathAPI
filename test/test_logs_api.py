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
from uipath_orchestrator_rest.api.logs_api import LogsApi  # noqa: E501
from uipath_orchestrator_rest.rest import ApiException


class TestLogsApi(unittest.TestCase):
    """LogsApi unit test stubs"""

    def setUp(self):
        self.api = uipath_orchestrator_rest.api.logs_api.LogsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_logs_post(self):
        """Test case for logs_post

        Inserts a log entry with a specified message in JSON format.  # noqa: E501
        """
        pass

    def test_logs_submit_logs(self):
        """Test case for logs_submit_logs

        Inserts a collection of log entries, each in a specific JSON format.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
