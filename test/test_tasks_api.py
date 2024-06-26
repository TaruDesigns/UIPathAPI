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
from uipath_orchestrator_rest.api.tasks_api import TasksApi  # noqa: E501
from uipath_orchestrator_rest.rest import ApiException


class TestTasksApi(unittest.TestCase):
    """TasksApi unit test stubs"""

    def setUp(self):
        self.api = uipath_orchestrator_rest.api.tasks_api.TasksApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_tasks_assign_tasks(self):
        """Test case for tasks_assign_tasks

        Assigns the tasks to given users.  # noqa: E501
        """
        pass

    def test_tasks_delete_tasks(self):
        """Test case for tasks_delete_tasks

        Deletes the tasks.  # noqa: E501
        """
        pass

    def test_tasks_edit_task_metadata(self):
        """Test case for tasks_edit_task_metadata

        Edits the metadata of a task  # noqa: E501
        """
        pass

    def test_tasks_get(self):
        """Test case for tasks_get

        Gets Task objects from classic folders with the given OData queries.  # noqa: E501
        """
        pass

    def test_tasks_get_by_id(self):
        """Test case for tasks_get_by_id

        Gets a Task with the given primary key.  # noqa: E501
        """
        pass

    def test_tasks_get_task_permissions(self):
        """Test case for tasks_get_task_permissions

        Gets all the tasks related permissions for the logged in user on the folder in session  # noqa: E501
        """
        pass

    def test_tasks_get_task_users_by_organizationunitid(self):
        """Test case for tasks_get_task_users_by_organizationunitid

        Gets users in given Organization Unit, who have Tasks.View and Tasks.Edit permissions  # noqa: E501
        """
        pass

    def test_tasks_get_tasks_across_folders(self):
        """Test case for tasks_get_tasks_across_folders

        Gets Task objects across folders (including Modern folders) with the given OData queries.  # noqa: E501
        """
        pass

    def test_tasks_get_tasks_across_folders_for_admin(self):
        """Test case for tasks_get_tasks_across_folders_for_admin

        Gets Task objects across folders (including Modern folders) where the current user has task admin permissions, with the given OData query options  # noqa: E501
        """
        pass

    def test_tasks_reassign_tasks(self):
        """Test case for tasks_reassign_tasks

        Reassigns the tasks to given users.  # noqa: E501
        """
        pass

    def test_tasks_unassign_tasks(self):
        """Test case for tasks_unassign_tasks

        Unassigns the tasks from the users.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
