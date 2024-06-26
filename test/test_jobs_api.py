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
from uipath_orchestrator_rest.api.jobs_api import JobsApi  # noqa: E501
from uipath_orchestrator_rest.rest import ApiException


class TestJobsApi(unittest.TestCase):
    """JobsApi unit test stubs"""

    def setUp(self):
        self.api = uipath_orchestrator_rest.api.jobs_api.JobsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_jobs_export(self):
        """Test case for jobs_export

        Requests a CSV export of filtered items.  # noqa: E501
        """
        pass

    def test_jobs_get(self):
        """Test case for jobs_get

        Gets Jobs.  # noqa: E501
        """
        pass

    def test_jobs_get_by_id(self):
        """Test case for jobs_get_by_id

        Gets a single job.  # noqa: E501
        """
        pass

    def test_jobs_restart_job(self):
        """Test case for jobs_restart_job

        Restarts the specified job.  # noqa: E501
        """
        pass

    def test_jobs_resume_job(self):
        """Test case for jobs_resume_job

        Resumes the specified job.  # noqa: E501
        """
        pass

    def test_jobs_start_jobs(self):
        """Test case for jobs_start_jobs

        Adds a new job and sets it in Pending state for each robot based on the input parameters and notifies the respective robots about the pending job.  # noqa: E501
        """
        pass

    def test_jobs_stop_job_by_id(self):
        """Test case for jobs_stop_job_by_id

        Cancels or terminates the specified job.  # noqa: E501
        """
        pass

    def test_jobs_stop_jobs(self):
        """Test case for jobs_stop_jobs

        Cancels or terminates the specified jobs.  # noqa: E501
        """
        pass

    def test_jobs_validate_dynamic_job(self):
        """Test case for jobs_validate_dynamic_job

        Validates the input which would start a job.  # noqa: E501
        """
        pass

    def test_jobs_validate_existing_job_by_id(self):
        """Test case for jobs_validate_existing_job_by_id

        Validates an existing job.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
