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
from UIPathAPI.api.app_tasks_api import AppTasksApi  # noqa: E501
from UIPathAPI.rest import ApiException


class TestAppTasksApi(unittest.TestCase):
    """AppTasksApi unit test stubs"""

    def setUp(self):
        self.api = UIPathAPI.api.app_tasks_api.AppTasksApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_app_tasks_complete_app_task(self):
        """Test case for app_tasks_complete_app_task

        Complete the task by saving app task data and action taken  # noqa: E501
        """
        pass

    def test_app_tasks_create_app_task(self):
        """Test case for app_tasks_create_app_task

        Creates a new App Task.  # noqa: E501
        """
        pass

    def test_app_tasks_get_app_task_by_id(self):
        """Test case for app_tasks_get_app_task_by_id

        Returns dto to render app task  # noqa: E501
        """
        pass

    def test_app_tasks_save_and_reassign_app_tasks(self):
        """Test case for app_tasks_save_and_reassign_app_tasks

        Save changes done by the current user and Reassign Task to another user  # noqa: E501
        """
        pass

    def test_app_tasks_save_app_tasks_data(self):
        """Test case for app_tasks_save_app_tasks_data

        Save task data  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
