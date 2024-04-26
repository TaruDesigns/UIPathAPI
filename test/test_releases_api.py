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
from uipath_orchestrator_rest.api.releases_api import ReleasesApi  # noqa: E501
from uipath_orchestrator_rest.rest import ApiException


class TestReleasesApi(unittest.TestCase):
    """ReleasesApi unit test stubs"""

    def setUp(self):
        self.api = uipath_orchestrator_rest.api.releases_api.ReleasesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_releases_delete_by_id(self):
        """Test case for releases_delete_by_id

        Deletes a release.  # noqa: E501
        """
        pass

    def test_releases_delete_by_key(self):
        """Test case for releases_delete_by_key

        """
        pass

    def test_releases_get(self):
        """Test case for releases_get

        Gets multiple releases.  # noqa: E501
        """
        pass

    def test_releases_get_by_id(self):
        """Test case for releases_get_by_id

        Gets a release by id.  # noqa: E501
        """
        pass

    def test_releases_patch_by_id(self):
        """Test case for releases_patch_by_id

        Partially updates a release.  # noqa: E501
        """
        pass

    def test_releases_post(self):
        """Test case for releases_post

        Creates a new release.  # noqa: E501
        """
        pass

    def test_releases_put_by_id(self):
        """Test case for releases_put_by_id

        Edits a release.  # noqa: E501
        """
        pass

    def test_releases_rollback_to_previous_release_version_by_id(self):
        """Test case for releases_rollback_to_previous_release_version_by_id

        Reverts the package versions for the given release to the last version it had before the current one.  # noqa: E501
        """
        pass

    def test_releases_update_by_key(self):
        """Test case for releases_update_by_key

        Updates the package entry point for the given release.  # noqa: E501
        """
        pass

    def test_releases_update_to_latest_package_version_bulk(self):
        """Test case for releases_update_to_latest_package_version_bulk

        Updates the package versions for the given releases to the latest available.  # noqa: E501
        """
        pass

    def test_releases_update_to_latest_package_version_by_id(self):
        """Test case for releases_update_to_latest_package_version_by_id

        Updates the package version for the given release to the latest available.  # noqa: E501
        """
        pass

    def test_releases_update_to_specific_package_version_by_id(self):
        """Test case for releases_update_to_specific_package_version_by_id

        Updates the package version for the given release.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
