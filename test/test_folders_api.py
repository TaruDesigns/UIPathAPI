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
from uipath_orchestrator_rest.api.folders_api import FoldersApi  # noqa: E501
from uipath_orchestrator_rest.rest import ApiException


class TestFoldersApi(unittest.TestCase):
    """FoldersApi unit test stubs"""

    def setUp(self):
        self.api = uipath_orchestrator_rest.api.folders_api.FoldersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_folders_assign_domain_user(self):
        """Test case for folders_assign_domain_user

        Assigns a directory user or group to a set of folders with an optional set of roles per folder.  # noqa: E501
        """
        pass

    def test_folders_assign_machines(self):
        """Test case for folders_assign_machines

        Assigns one or more machines to a set of folders.  # noqa: E501
        """
        pass

    def test_folders_assign_users(self):
        """Test case for folders_assign_users

        Assigns one or more users to a set of folders with an optional set of roles per folder.  # noqa: E501
        """
        pass

    def test_folders_delete_by_id(self):
        """Test case for folders_delete_by_id

        Deletes a folder. Succeeds only if no entities or user associations  exist in this folder or any of its descendants.  # noqa: E501
        """
        pass

    def test_folders_delete_by_key(self):
        """Test case for folders_delete_by_key

        Deletes a folder. Succeeds only if no entities or user associations  exist in this folder or any of its descendants.  # noqa: E501
        """
        pass

    def test_folders_get(self):
        """Test case for folders_get

        Gets folders.  # noqa: E501
        """
        pass

    def test_folders_get_all_roles_for_user_by_username_and_skip_and_take(self):
        """Test case for folders_get_all_roles_for_user_by_username_and_skip_and_take

        Returns a page of the user-folder assignments for the input user, including the roles for each folder.  The response also includes the folders assigned to the directory groups of the user.  The distinction between the folders assigned directly to the user and the ones assigned to one of his groups  can be made via the User field of the response.  LIMITATION: If URI parameters contain special characters (eg. \\, /), use instead api/FoldersNavigation/GetAllRolesForUser endpoint.  # noqa: E501
        """
        pass

    def test_folders_get_by_id(self):
        """Test case for folders_get_by_id

        Gets a single folder, based on its Id.  # noqa: E501
        """
        pass

    def test_folders_get_by_key_by_identifier(self):
        """Test case for folders_get_by_key_by_identifier

        Gets a single folder, based on its Key.  # noqa: E501
        """
        pass

    def test_folders_get_machines_for_folder_by_key(self):
        """Test case for folders_get_machines_for_folder_by_key

        Returns the machines assigned to a folder.  # noqa: E501
        """
        pass

    def test_folders_get_move_folder_machines_changes(self):
        """Test case for folders_get_move_folder_machines_changes

        Gets the machine changes when moving a folder  # noqa: E501
        """
        pass

    def test_folders_get_subfolders_with_assigned_machine(self):
        """Test case for folders_get_subfolders_with_assigned_machine

        Gets direct machine assignments for all subfolders of the specific folder  # noqa: E501
        """
        pass

    def test_folders_get_users_for_folder_by_key_and_includeinherited(self):
        """Test case for folders_get_users_for_folder_by_key_and_includeinherited

        Returns the users who have access to a folder and optionally the fine-grained roles each one  has on that folder.  # noqa: E501
        """
        pass

    def test_folders_move_folder_by_folderid(self):
        """Test case for folders_move_folder_by_folderid

        Move a folder.  # noqa: E501
        """
        pass

    def test_folders_patch_name_description(self):
        """Test case for folders_patch_name_description

        Edits a folder.  # noqa: E501
        """
        pass

    def test_folders_post(self):
        """Test case for folders_post

        Creates a new folder.  # noqa: E501
        """
        pass

    def test_folders_put_by_id(self):
        """Test case for folders_put_by_id

        Edits a folder.  # noqa: E501
        """
        pass

    def test_folders_remove_machines_from_folder_by_id(self):
        """Test case for folders_remove_machines_from_folder_by_id

        Remove user assignment from a folder.  # noqa: E501
        """
        pass

    def test_folders_remove_user_from_folder_by_id(self):
        """Test case for folders_remove_user_from_folder_by_id

        Remove user assignment from a folder.  # noqa: E501
        """
        pass

    def test_folders_toggle_folder_machine_inherit(self):
        """Test case for folders_toggle_folder_machine_inherit

        Toggle machine propagation for a folder to all subfolders.  # noqa: E501
        """
        pass

    def test_folders_update_machines_to_folder_associations(self):
        """Test case for folders_update_machines_to_folder_associations

        Add and remove machine associations to a folder  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
