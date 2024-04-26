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
from uipath_orchestrator_rest.api.personal_workspaces_api import PersonalWorkspacesApi  # noqa: E501
from uipath_orchestrator_rest.rest import ApiException


class TestPersonalWorkspacesApi(unittest.TestCase):
    """PersonalWorkspacesApi unit test stubs"""

    def setUp(self):
        self.api = uipath_orchestrator_rest.api.personal_workspaces_api.PersonalWorkspacesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_personal_workspaces_convert_to_folder_by_id(self):
        """Test case for personal_workspaces_convert_to_folder_by_id

        Converts a Personal Workspace to a standard Folder.  # noqa: E501
        """
        pass

    def test_personal_workspaces_get(self):
        """Test case for personal_workspaces_get

        Gets Personal Workspaces.  # noqa: E501
        """
        pass

    def test_personal_workspaces_get_personal_workspace(self):
        """Test case for personal_workspaces_get_personal_workspace

        Gets Personal Workspace for current User  # noqa: E501
        """
        pass

    def test_personal_workspaces_start_exploring_by_id(self):
        """Test case for personal_workspaces_start_exploring_by_id

        Assigns the current User to explore a Personal Workspace.  # noqa: E501
        """
        pass

    def test_personal_workspaces_stop_exploring_by_id(self):
        """Test case for personal_workspaces_stop_exploring_by_id

        Unassigns the current User from exploring a Personal Workspace.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
