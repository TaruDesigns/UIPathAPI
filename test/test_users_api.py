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
from UIPathAPI.api.users_api import UsersApi  # noqa: E501
from UIPathAPI.rest import ApiException


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = UIPathAPI.api.users_api.UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_users_assign_roles_by_id(self):
        """Test case for users_assign_roles_by_id

        """
        pass

    def test_users_change_culture(self):
        """Test case for users_change_culture

        Changes the culture for the current user  # noqa: E501
        """
        pass

    def test_users_change_user_culture_by_id(self):
        """Test case for users_change_user_culture_by_id

        Changes the culture for the specified user  # noqa: E501
        """
        pass

    def test_users_delete_by_id(self):
        """Test case for users_delete_by_id

        Deletes a user.  # noqa: E501
        """
        pass

    def test_users_get(self):
        """Test case for users_get

        Gets users.  # noqa: E501
        """
        pass

    def test_users_get_by_id(self):
        """Test case for users_get_by_id

        Gets a user based on its id.  # noqa: E501
        """
        pass

    def test_users_get_current_permissions(self):
        """Test case for users_get_current_permissions

        Returns a user permission collection containing data about the current user and all the permissions it has.  # noqa: E501
        """
        pass

    def test_users_get_current_user(self):
        """Test case for users_get_current_user

        Returns details about the user currently logged into Orchestrator.  # noqa: E501
        """
        pass

    def test_users_patch_by_id(self):
        """Test case for users_patch_by_id

        Partially updates a user.  Cannot update roles or organization units via this endpoint.  # noqa: E501
        """
        pass

    def test_users_post(self):
        """Test case for users_post

        Creates a new user.  # noqa: E501
        """
        pass

    def test_users_put_by_id(self):
        """Test case for users_put_by_id

        Edits a user.  # noqa: E501
        """
        pass

    def test_users_set_active_by_id(self):
        """Test case for users_set_active_by_id

        Activate or deactivate a user  # noqa: E501
        """
        pass

    def test_users_toggle_organization_unit_by_id(self):
        """Test case for users_toggle_organization_unit_by_id

        Associates/dissociates the given user with/from an organization unit based on toggle parameter.  # noqa: E501
        """
        pass

    def test_users_toggle_role_by_id(self):
        """Test case for users_toggle_role_by_id

        Associates/dissociates the given user with/from a role based on toggle parameter.  # noqa: E501
        """
        pass

    def test_users_validate_by_userids(self):
        """Test case for users_validate_by_userids

        Validates if the robots for the given users are busy  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
