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
from UIPathAPI.api.settings_api import SettingsApi  # noqa: E501
from UIPathAPI.rest import ApiException


class TestSettingsApi(unittest.TestCase):
    """SettingsApi unit test stubs"""

    def setUp(self):
        self.api = UIPathAPI.api.settings_api.SettingsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_settings_activate_license_offline(self):
        """Test case for settings_activate_license_offline

        Uploads a new offline license activation.  The content of the license is sent as a file embedded in the HTTP request.  # noqa: E501
        """
        pass

    def test_settings_activate_license_online(self):
        """Test case for settings_activate_license_online

        Activate the license for a specific tenant  # noqa: E501
        """
        pass

    def test_settings_deactivate_license_online(self):
        """Test case for settings_deactivate_license_online

        Deactivate the license for a specific tenant  # noqa: E501
        """
        pass

    def test_settings_delete_bulk(self):
        """Test case for settings_delete_bulk

        Deletes values for the specified settings in the Tenant scope.  # noqa: E501
        """
        pass

    def test_settings_delete_license(self):
        """Test case for settings_delete_license

        Removes the license  # noqa: E501
        """
        pass

    def test_settings_get(self):
        """Test case for settings_get

        Gets the settings.  # noqa: E501
        """
        pass

    def test_settings_get_activity_settings(self):
        """Test case for settings_get_activity_settings

        Returns Orchestrator settings used by activities  # noqa: E501
        """
        pass

    def test_settings_get_authentication_settings(self):
        """Test case for settings_get_authentication_settings

        Gets the authentication settings  # noqa: E501
        """
        pass

    def test_settings_get_by_id(self):
        """Test case for settings_get_by_id

        Gets a settings value based on its key.  # noqa: E501
        """
        pass

    def test_settings_get_calendar(self):
        """Test case for settings_get_calendar

        Gets custom calendar, with excluded dates in UTC, for current tenant  # noqa: E501
        """
        pass

    def test_settings_get_connection_string(self):
        """Test case for settings_get_connection_string

        Gets the connection string  # noqa: E501
        """
        pass

    def test_settings_get_deactivate_license_offline(self):
        """Test case for settings_get_deactivate_license_offline

        Deactivate the license offline for a specific tenant  # noqa: E501
        """
        pass

    def test_settings_get_execution_settings_configuration_by_scope(self):
        """Test case for settings_get_execution_settings_configuration_by_scope

        Gets the execution settings configuration (display name, value type, etc.).  If scope is 0 (Global), the default values will be the initial ones. If scope is 1 (Robot), then  the default values will be the actual values set globally.  e.g., Resolution width  Assume it was set globally to 720.  Then within the config returned by this function, the default value for this setting will be:  - 0 for scope = 0 and  - 720 for scope = 1.  # noqa: E501
        """
        pass

    def test_settings_get_languages(self):
        """Test case for settings_get_languages

        Gets supported languages  # noqa: E501
        """
        pass

    def test_settings_get_license(self):
        """Test case for settings_get_license

        Retrieves the current license information.  # noqa: E501
        """
        pass

    def test_settings_get_license_offline(self):
        """Test case for settings_get_license_offline

        Create the offline activation request for a specific tenant  # noqa: E501
        """
        pass

    def test_settings_get_secure_store_configuration_by_storetypename(self):
        """Test case for settings_get_secure_store_configuration_by_storetypename

        Gets the configuration format for a Secure store  # noqa: E501
        """
        pass

    def test_settings_get_timezones(self):
        """Test case for settings_get_timezones

        Gets timezones.  # noqa: E501
        """
        pass

    def test_settings_get_update_settings(self):
        """Test case for settings_get_update_settings

        Gets the update settings  # noqa: E501
        """
        pass

    def test_settings_get_web_settings(self):
        """Test case for settings_get_web_settings

        Returns a collection of key value pairs representing settings used by Orchestrator web client.  # noqa: E501
        """
        pass

    def test_settings_put_by_id(self):
        """Test case for settings_put_by_id

        Edits a setting.  # noqa: E501
        """
        pass

    def test_settings_set_calendar(self):
        """Test case for settings_set_calendar

        Sets custom calendar, with excluded dates in UTC, for current tenant  # noqa: E501
        """
        pass

    def test_settings_update_bulk(self):
        """Test case for settings_update_bulk

        Updates the current settings.  # noqa: E501
        """
        pass

    def test_settings_update_license_online(self):
        """Test case for settings_update_license_online

        Update the license for a specific tenant  # noqa: E501
        """
        pass

    def test_settings_update_user_setting(self):
        """Test case for settings_update_user_setting

        Edits a user setting.  # noqa: E501
        """
        pass

    def test_settings_upload_license(self):
        """Test case for settings_upload_license

        Uploads a new license file that was previously generated with Regutil. The content of the license is sent as a file embedded in the HTTP request.  # noqa: E501
        """
        pass

    def test_settings_verify_smtp_setting(self):
        """Test case for settings_verify_smtp_setting

        Verify whether the given SMTP settings are correct or not by sending an email to a recipient.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
