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
from UIPathAPI.api.execution_media_api import ExecutionMediaApi  # noqa: E501
from UIPathAPI.rest import ApiException


class TestExecutionMediaApi(unittest.TestCase):
    """ExecutionMediaApi unit test stubs"""

    def setUp(self):
        self.api = UIPathAPI.api.execution_media_api.ExecutionMediaApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_execution_media_delete_media_by_job_id(self):
        """Test case for execution_media_delete_media_by_job_id

        Deletes the execution media for the given job key.  # noqa: E501
        """
        pass

    def test_execution_media_download_media_by_job_id(self):
        """Test case for execution_media_download_media_by_job_id

        Downloads execution media by job id  # noqa: E501
        """
        pass

    def test_execution_media_get(self):
        """Test case for execution_media_get

        """
        pass

    def test_execution_media_get_by_id(self):
        """Test case for execution_media_get_by_id

        Get by id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
