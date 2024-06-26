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
from uipath_orchestrator_rest.api.test_data_queue_actions_api import TestDataQueueActionsApi  # noqa: E501
from uipath_orchestrator_rest.rest import ApiException


class TestTestDataQueueActionsApi(unittest.TestCase):
    """TestDataQueueActionsApi unit test stubs"""

    def setUp(self):
        self.api = uipath_orchestrator_rest.api.test_data_queue_actions_api.TestDataQueueActionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_test_data_queue_actions_add_item(self):
        """Test case for test_data_queue_actions_add_item

        Add a new test data queue item  # noqa: E501
        """
        pass

    def test_test_data_queue_actions_bulk_add_items(self):
        """Test case for test_data_queue_actions_bulk_add_items

        Bulk adds an array of data queue items  # noqa: E501
        """
        pass

    def test_test_data_queue_actions_delete_all_items(self):
        """Test case for test_data_queue_actions_delete_all_items

        Delete all items from a test data queue  # noqa: E501
        """
        pass

    def test_test_data_queue_actions_delete_items(self):
        """Test case for test_data_queue_actions_delete_items

        Delete specific test data queue items  # noqa: E501
        """
        pass

    def test_test_data_queue_actions_get_next_item(self):
        """Test case for test_data_queue_actions_get_next_item

        Get the next unconsumed test data queue item  # noqa: E501
        """
        pass

    def test_test_data_queue_actions_set_all_items_consumed(self):
        """Test case for test_data_queue_actions_set_all_items_consumed

        Set the IsConsumed flag for all items from a test data queue  # noqa: E501
        """
        pass

    def test_test_data_queue_actions_set_items_consumed(self):
        """Test case for test_data_queue_actions_set_items_consumed

        Set the IsConsumed flag for specific test data queue items  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
