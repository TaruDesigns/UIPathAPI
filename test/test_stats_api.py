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
from UIPathAPI.api.stats_api import StatsApi  # noqa: E501
from UIPathAPI.rest import ApiException


class TestStatsApi(unittest.TestCase):
    """StatsApi unit test stubs"""

    def setUp(self):
        self.api = UIPathAPI.api.stats_api.StatsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_stats_get_consumption_license_stats(self):
        """Test case for stats_get_consumption_license_stats

        Gets the consumption licensing usage statistics  # noqa: E501
        """
        pass

    def test_stats_get_count_stats(self):
        """Test case for stats_get_count_stats

        Gets the total number of various entities registered in Orchestrator  # noqa: E501
        """
        pass

    def test_stats_get_jobs_stats(self):
        """Test case for stats_get_jobs_stats

        Gets the total number of jobs aggregated by Job State  # noqa: E501
        """
        pass

    def test_stats_get_license_stats(self):
        """Test case for stats_get_license_stats

        Gets the licensing usage statistics  # noqa: E501
        """
        pass

    def test_stats_get_sessions_stats(self):
        """Test case for stats_get_sessions_stats

        Gets the total number of robots aggregated by Robot State  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
