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
from uipath_orchestrator_rest.api.test_data_queue_items_api import TestDataQueueItemsApi  # noqa: E501
from uipath_orchestrator_rest.rest import ApiException


class TestTestDataQueueItemsApi(unittest.TestCase):
    """TestDataQueueItemsApi unit test stubs"""

    def setUp(self):
        self.api = uipath_orchestrator_rest.api.test_data_queue_items_api.TestDataQueueItemsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_test_data_queue_items_get(self):
        """Test case for test_data_queue_items_get

        Return a list of test data queue items  # noqa: E501
        """
        pass

    def test_test_data_queue_items_get_by_id(self):
        """Test case for test_data_queue_items_get_by_id

        Return a specific test data queue item identified by key  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
