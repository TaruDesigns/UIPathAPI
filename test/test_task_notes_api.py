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
from uipath_orchestrator_rest.api.task_notes_api import TaskNotesApi  # noqa: E501
from uipath_orchestrator_rest.rest import ApiException


class TestTaskNotesApi(unittest.TestCase):
    """TaskNotesApi unit test stubs"""

    def setUp(self):
        self.api = uipath_orchestrator_rest.api.task_notes_api.TaskNotesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_task_notes_create_task_note(self):
        """Test case for task_notes_create_task_note

        Adds a task note.  # noqa: E501
        """
        pass

    def test_task_notes_get_by_task_id(self):
        """Test case for task_notes_get_by_task_id

        Gets Task Notes for a Task  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
