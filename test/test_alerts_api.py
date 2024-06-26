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
from uipath_orchestrator_rest.api.alerts_api import AlertsApi  # noqa: E501
from uipath_orchestrator_rest.rest import ApiException


class TestAlertsApi(unittest.TestCase):
    """AlertsApi unit test stubs"""

    def setUp(self):
        self.api = uipath_orchestrator_rest.api.alerts_api.AlertsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_alerts_get(self):
        """Test case for alerts_get

        Gets alerts.  # noqa: E501
        """
        pass

    def test_alerts_get_unread_count(self):
        """Test case for alerts_get_unread_count

        Returns the total number of alerts, per tenant, that haven't been read by the current user.  # noqa: E501
        """
        pass

    def test_alerts_mark_as_read(self):
        """Test case for alerts_mark_as_read

        Marks alerts as read and returns the remaining number of unread notifications.  # noqa: E501
        """
        pass

    def test_alerts_raise_process_alert(self):
        """Test case for alerts_raise_process_alert

        Creates a Process Alert  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
