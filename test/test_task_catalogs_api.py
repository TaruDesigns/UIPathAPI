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
from UIPathAPI.api.task_catalogs_api import TaskCatalogsApi  # noqa: E501
from UIPathAPI.rest import ApiException


class TestTaskCatalogsApi(unittest.TestCase):
    """TaskCatalogsApi unit test stubs"""

    def setUp(self):
        self.api = UIPathAPI.api.task_catalogs_api.TaskCatalogsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_task_catalogs_create_task_catalog(self):
        """Test case for task_catalogs_create_task_catalog

        Creates a new Task Catalog.  # noqa: E501
        """
        pass

    def test_task_catalogs_delete_by_id(self):
        """Test case for task_catalogs_delete_by_id

        Deletes Task Catalog.  # noqa: E501
        """
        pass

    def test_task_catalogs_get(self):
        """Test case for task_catalogs_get

        Gets Task Catalog objects with the given OData queries.  # noqa: E501
        """
        pass

    def test_task_catalogs_get_by_id(self):
        """Test case for task_catalogs_get_by_id

        Gets a Task Catalog item by Id.  # noqa: E501
        """
        pass

    def test_task_catalogs_get_folders_for_task_catalog_by_id(self):
        """Test case for task_catalogs_get_folders_for_task_catalog_by_id

        Get all accessible folders where the task catalog is shared, and the total count of folders where it is shared (including unaccessible folders).  # noqa: E501
        """
        pass

    def test_task_catalogs_get_task_catalog_extended_details_by_taskcatalogid(self):
        """Test case for task_catalogs_get_task_catalog_extended_details_by_taskcatalogid

        Validates task catalog deletion request.  # noqa: E501
        """
        pass

    def test_task_catalogs_get_task_catalogs_from_folders_with_permissions(self):
        """Test case for task_catalogs_get_task_catalogs_from_folders_with_permissions

        Gets Task Catalogs across folders having given permission with the given OData queries .  # noqa: E501
        """
        pass

    def test_task_catalogs_share_to_folders(self):
        """Test case for task_catalogs_share_to_folders

        Makes the task catalogs visible in the specified folders.  # noqa: E501
        """
        pass

    def test_task_catalogs_update_task_catalog_by_id(self):
        """Test case for task_catalogs_update_task_catalog_by_id

        Updates Task Catalog.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()