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
from UIPathAPI.api.environments_api import EnvironmentsApi  # noqa: E501
from UIPathAPI.rest import ApiException


class TestEnvironmentsApi(unittest.TestCase):
    """EnvironmentsApi unit test stubs"""

    def setUp(self):
        self.api = UIPathAPI.api.environments_api.EnvironmentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_environments_add_robot_by_id(self):
        """Test case for environments_add_robot_by_id

        Associates a robot with the given environment.  # noqa: E501
        """
        pass

    def test_environments_delete_by_id(self):
        """Test case for environments_delete_by_id

        Deletes an environment.  # noqa: E501
        """
        pass

    def test_environments_get(self):
        """Test case for environments_get

        Gets Environments.  # noqa: E501
        """
        pass

    def test_environments_get_by_id(self):
        """Test case for environments_get_by_id

        Gets a single environment.  # noqa: E501
        """
        pass

    def test_environments_get_robot_ids_for_environment_by_key(self):
        """Test case for environments_get_robot_ids_for_environment_by_key

        Returns a collection of all the ids of the robots associated to an environment based on environment Id.  # noqa: E501
        """
        pass

    def test_environments_get_robots_for_environment_by_key(self):
        """Test case for environments_get_robots_for_environment_by_key

        Returns a collection of all robots and, if no other sorting is provided, will place first those belonging to the environment. Allows odata query options.  # noqa: E501
        """
        pass

    def test_environments_post(self):
        """Test case for environments_post

        Post new environment  # noqa: E501
        """
        pass

    def test_environments_put_by_id(self):
        """Test case for environments_put_by_id

        Updates an environment.  # noqa: E501
        """
        pass

    def test_environments_remove_robot_by_id(self):
        """Test case for environments_remove_robot_by_id

        Dissociates a robot from the given environment.  # noqa: E501
        """
        pass

    def test_environments_set_robots_by_id(self):
        """Test case for environments_set_robots_by_id

        Associates a group of robots with and dissociates another group of robots from the given environment.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
