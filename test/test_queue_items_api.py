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
from uipath_orchestrator_rest.api.queue_items_api import QueueItemsApi  # noqa: E501
from uipath_orchestrator_rest.rest import ApiException


class TestQueueItemsApi(unittest.TestCase):
    """QueueItemsApi unit test stubs"""

    def setUp(self):
        self.api = uipath_orchestrator_rest.api.queue_items_api.QueueItemsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_queue_items_delete_bulk(self):
        """Test case for queue_items_delete_bulk

        Sets the given queue items' status to Deleted.  # noqa: E501
        """
        pass

    def test_queue_items_delete_by_id(self):
        """Test case for queue_items_delete_by_id

        Deletes a queue item by Id.  # noqa: E501
        """
        pass

    def test_queue_items_get(self):
        """Test case for queue_items_get

        Gets a collection of queue items.  # noqa: E501
        """
        pass

    def test_queue_items_get_by_id(self):
        """Test case for queue_items_get_by_id

        Gets a queue item by Id.  # noqa: E501
        """
        pass

    def test_queue_items_get_item_last_retry_by_id(self):
        """Test case for queue_items_get_item_last_retry_by_id

        Returns the last retry of a queue item.  # noqa: E501
        """
        pass

    def test_queue_items_get_item_processing_history_by_id(self):
        """Test case for queue_items_get_item_processing_history_by_id

        Returns data about the processing history of the given queue item. Allows odata query options.  # noqa: E501
        """
        pass

    def test_queue_items_get_reviewers(self):
        """Test case for queue_items_get_reviewers

        Returns a collection of users having the permission for Queue Items review. Allows odata query options.  # noqa: E501
        """
        pass

    def test_queue_items_put_by_id(self):
        """Test case for queue_items_put_by_id

        Updates the QueueItem properties with the new values provided.  # noqa: E501
        """
        pass

    def test_queue_items_set_item_review_status(self):
        """Test case for queue_items_set_item_review_status

        Updates the review status of the specified queue items to an indicated state.  # noqa: E501
        """
        pass

    def test_queue_items_set_item_reviewer(self):
        """Test case for queue_items_set_item_reviewer

        Sets the reviewer for multiple queue items  # noqa: E501
        """
        pass

    def test_queue_items_set_transaction_progress_by_id(self):
        """Test case for queue_items_set_transaction_progress_by_id

        Updates the progress field of a queue item with the status 'In Progress'.  # noqa: E501
        """
        pass

    def test_queue_items_unset_item_reviewer(self):
        """Test case for queue_items_unset_item_reviewer

        Unsets the reviewer for multiple queue items  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
