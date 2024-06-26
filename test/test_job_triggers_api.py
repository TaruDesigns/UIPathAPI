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
from uipath_orchestrator_rest.api.job_triggers_api import JobTriggersApi  # noqa: E501
from uipath_orchestrator_rest.rest import ApiException


class TestJobTriggersApi(unittest.TestCase):
    """JobTriggersApi unit test stubs"""

    def setUp(self):
        self.api = uipath_orchestrator_rest.api.job_triggers_api.JobTriggersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_job_triggers_deliver_payload_by_inboxid(self):
        """Test case for job_triggers_deliver_payload_by_inboxid

        Deliver payload for trigger inboxId.  # noqa: E501
        """
        pass

    def test_job_triggers_get(self):
        """Test case for job_triggers_get

        Gets JobTriggers.  # noqa: E501
        """
        pass

    def test_job_triggers_get_payload_by_inboxid(self):
        """Test case for job_triggers_get_payload_by_inboxid

        Get payload for trigger inboxId.  # noqa: E501
        """
        pass

    def test_job_triggers_get_with_wait_events_by_jobid(self):
        """Test case for job_triggers_get_with_wait_events_by_jobid

        Gets Trigger option for a job instance along with wait event details    .  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
