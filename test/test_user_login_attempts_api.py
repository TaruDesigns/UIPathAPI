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
from UIPathAPI.api.user_login_attempts_api import UserLoginAttemptsApi  # noqa: E501
from UIPathAPI.rest import ApiException


class TestUserLoginAttemptsApi(unittest.TestCase):
    """UserLoginAttemptsApi unit test stubs"""

    def setUp(self):
        self.api = UIPathAPI.api.user_login_attempts_api.UserLoginAttemptsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_user_login_attempts_get_by_id(self):
        """Test case for user_login_attempts_get_by_id

        Gets the user's login attempts  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
