# coding: utf-8

"""
    UiPath.WebApi 17.0

    Orchestrator API  # noqa: E501

    OpenAPI spec version: 17.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from UIPathAPI.configuration import Configuration


class TestSetExecutionDto(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'test_set_id': 'int',
        'organization_unit_id': 'int',
        'test_set': 'TestSetDto',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'status': 'str',
        'trigger_type': 'str',
        'schedule_id': 'int',
        'batch_execution_key': 'str',
        'coverage_status': 'str',
        'run_id': 'int',
        'test_case_executions': 'list[TestCaseExecutionDto]',
        'attachments': 'list[TestSetExecutionAttachmentDto]',
        'enforce_execution_order': 'bool',
        'creation_time': 'datetime',
        'creator_user_id': 'int',
        'id': 'int'
    }

    attribute_map = {
        'name': 'Name',
        'test_set_id': 'TestSetId',
        'organization_unit_id': 'OrganizationUnitId',
        'test_set': 'TestSet',
        'start_time': 'StartTime',
        'end_time': 'EndTime',
        'status': 'Status',
        'trigger_type': 'TriggerType',
        'schedule_id': 'ScheduleId',
        'batch_execution_key': 'BatchExecutionKey',
        'coverage_status': 'CoverageStatus',
        'run_id': 'RunId',
        'test_case_executions': 'TestCaseExecutions',
        'attachments': 'Attachments',
        'enforce_execution_order': 'EnforceExecutionOrder',
        'creation_time': 'CreationTime',
        'creator_user_id': 'CreatorUserId',
        'id': 'Id'
    }

    def __init__(self, name=None, test_set_id=None, organization_unit_id=None, test_set=None, start_time=None, end_time=None, status=None, trigger_type=None, schedule_id=None, batch_execution_key=None, coverage_status=None, run_id=None, test_case_executions=None, attachments=None, enforce_execution_order=None, creation_time=None, creator_user_id=None, id=None, _configuration=None):  # noqa: E501
        """TestSetExecutionDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._test_set_id = None
        self._organization_unit_id = None
        self._test_set = None
        self._start_time = None
        self._end_time = None
        self._status = None
        self._trigger_type = None
        self._schedule_id = None
        self._batch_execution_key = None
        self._coverage_status = None
        self._run_id = None
        self._test_case_executions = None
        self._attachments = None
        self._enforce_execution_order = None
        self._creation_time = None
        self._creator_user_id = None
        self._id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if test_set_id is not None:
            self.test_set_id = test_set_id
        if organization_unit_id is not None:
            self.organization_unit_id = organization_unit_id
        if test_set is not None:
            self.test_set = test_set
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if status is not None:
            self.status = status
        if trigger_type is not None:
            self.trigger_type = trigger_type
        if schedule_id is not None:
            self.schedule_id = schedule_id
        if batch_execution_key is not None:
            self.batch_execution_key = batch_execution_key
        if coverage_status is not None:
            self.coverage_status = coverage_status
        if run_id is not None:
            self.run_id = run_id
        if test_case_executions is not None:
            self.test_case_executions = test_case_executions
        if attachments is not None:
            self.attachments = attachments
        if enforce_execution_order is not None:
            self.enforce_execution_order = enforce_execution_order
        if creation_time is not None:
            self.creation_time = creation_time
        if creator_user_id is not None:
            self.creator_user_id = creator_user_id
        if id is not None:
            self.id = id

    @property
    def name(self):
        """Gets the name of this TestSetExecutionDto.  # noqa: E501


        :return: The name of this TestSetExecutionDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TestSetExecutionDto.


        :param name: The name of this TestSetExecutionDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def test_set_id(self):
        """Gets the test_set_id of this TestSetExecutionDto.  # noqa: E501


        :return: The test_set_id of this TestSetExecutionDto.  # noqa: E501
        :rtype: int
        """
        return self._test_set_id

    @test_set_id.setter
    def test_set_id(self, test_set_id):
        """Sets the test_set_id of this TestSetExecutionDto.


        :param test_set_id: The test_set_id of this TestSetExecutionDto.  # noqa: E501
        :type: int
        """

        self._test_set_id = test_set_id

    @property
    def organization_unit_id(self):
        """Gets the organization_unit_id of this TestSetExecutionDto.  # noqa: E501


        :return: The organization_unit_id of this TestSetExecutionDto.  # noqa: E501
        :rtype: int
        """
        return self._organization_unit_id

    @organization_unit_id.setter
    def organization_unit_id(self, organization_unit_id):
        """Sets the organization_unit_id of this TestSetExecutionDto.


        :param organization_unit_id: The organization_unit_id of this TestSetExecutionDto.  # noqa: E501
        :type: int
        """

        self._organization_unit_id = organization_unit_id

    @property
    def test_set(self):
        """Gets the test_set of this TestSetExecutionDto.  # noqa: E501


        :return: The test_set of this TestSetExecutionDto.  # noqa: E501
        :rtype: TestSetDto
        """
        return self._test_set

    @test_set.setter
    def test_set(self, test_set):
        """Sets the test_set of this TestSetExecutionDto.


        :param test_set: The test_set of this TestSetExecutionDto.  # noqa: E501
        :type: TestSetDto
        """

        self._test_set = test_set

    @property
    def start_time(self):
        """Gets the start_time of this TestSetExecutionDto.  # noqa: E501


        :return: The start_time of this TestSetExecutionDto.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this TestSetExecutionDto.


        :param start_time: The start_time of this TestSetExecutionDto.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this TestSetExecutionDto.  # noqa: E501


        :return: The end_time of this TestSetExecutionDto.  # noqa: E501
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this TestSetExecutionDto.


        :param end_time: The end_time of this TestSetExecutionDto.  # noqa: E501
        :type: datetime
        """

        self._end_time = end_time

    @property
    def status(self):
        """Gets the status of this TestSetExecutionDto.  # noqa: E501


        :return: The status of this TestSetExecutionDto.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TestSetExecutionDto.


        :param status: The status of this TestSetExecutionDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["Pending", "Running", "Cancelling", "Passed", "Failed", "Cancelled"]  # noqa: E501
        if (self._configuration.client_side_validation and
                status not in allowed_values):
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def trigger_type(self):
        """Gets the trigger_type of this TestSetExecutionDto.  # noqa: E501


        :return: The trigger_type of this TestSetExecutionDto.  # noqa: E501
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        """Sets the trigger_type of this TestSetExecutionDto.


        :param trigger_type: The trigger_type of this TestSetExecutionDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["Manual", "Scheduled", "ExternalTool"]  # noqa: E501
        if (self._configuration.client_side_validation and
                trigger_type not in allowed_values):
            raise ValueError(
                "Invalid value for `trigger_type` ({0}), must be one of {1}"  # noqa: E501
                .format(trigger_type, allowed_values)
            )

        self._trigger_type = trigger_type

    @property
    def schedule_id(self):
        """Gets the schedule_id of this TestSetExecutionDto.  # noqa: E501


        :return: The schedule_id of this TestSetExecutionDto.  # noqa: E501
        :rtype: int
        """
        return self._schedule_id

    @schedule_id.setter
    def schedule_id(self, schedule_id):
        """Sets the schedule_id of this TestSetExecutionDto.


        :param schedule_id: The schedule_id of this TestSetExecutionDto.  # noqa: E501
        :type: int
        """

        self._schedule_id = schedule_id

    @property
    def batch_execution_key(self):
        """Gets the batch_execution_key of this TestSetExecutionDto.  # noqa: E501


        :return: The batch_execution_key of this TestSetExecutionDto.  # noqa: E501
        :rtype: str
        """
        return self._batch_execution_key

    @batch_execution_key.setter
    def batch_execution_key(self, batch_execution_key):
        """Sets the batch_execution_key of this TestSetExecutionDto.


        :param batch_execution_key: The batch_execution_key of this TestSetExecutionDto.  # noqa: E501
        :type: str
        """

        self._batch_execution_key = batch_execution_key

    @property
    def coverage_status(self):
        """Gets the coverage_status of this TestSetExecutionDto.  # noqa: E501


        :return: The coverage_status of this TestSetExecutionDto.  # noqa: E501
        :rtype: str
        """
        return self._coverage_status

    @coverage_status.setter
    def coverage_status(self, coverage_status):
        """Sets the coverage_status of this TestSetExecutionDto.


        :param coverage_status: The coverage_status of this TestSetExecutionDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["Disabled", "Pending", "Processing", "Completed"]  # noqa: E501
        if (self._configuration.client_side_validation and
                coverage_status not in allowed_values):
            raise ValueError(
                "Invalid value for `coverage_status` ({0}), must be one of {1}"  # noqa: E501
                .format(coverage_status, allowed_values)
            )

        self._coverage_status = coverage_status

    @property
    def run_id(self):
        """Gets the run_id of this TestSetExecutionDto.  # noqa: E501


        :return: The run_id of this TestSetExecutionDto.  # noqa: E501
        :rtype: int
        """
        return self._run_id

    @run_id.setter
    def run_id(self, run_id):
        """Sets the run_id of this TestSetExecutionDto.


        :param run_id: The run_id of this TestSetExecutionDto.  # noqa: E501
        :type: int
        """

        self._run_id = run_id

    @property
    def test_case_executions(self):
        """Gets the test_case_executions of this TestSetExecutionDto.  # noqa: E501


        :return: The test_case_executions of this TestSetExecutionDto.  # noqa: E501
        :rtype: list[TestCaseExecutionDto]
        """
        return self._test_case_executions

    @test_case_executions.setter
    def test_case_executions(self, test_case_executions):
        """Sets the test_case_executions of this TestSetExecutionDto.


        :param test_case_executions: The test_case_executions of this TestSetExecutionDto.  # noqa: E501
        :type: list[TestCaseExecutionDto]
        """

        self._test_case_executions = test_case_executions

    @property
    def attachments(self):
        """Gets the attachments of this TestSetExecutionDto.  # noqa: E501


        :return: The attachments of this TestSetExecutionDto.  # noqa: E501
        :rtype: list[TestSetExecutionAttachmentDto]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this TestSetExecutionDto.


        :param attachments: The attachments of this TestSetExecutionDto.  # noqa: E501
        :type: list[TestSetExecutionAttachmentDto]
        """

        self._attachments = attachments

    @property
    def enforce_execution_order(self):
        """Gets the enforce_execution_order of this TestSetExecutionDto.  # noqa: E501


        :return: The enforce_execution_order of this TestSetExecutionDto.  # noqa: E501
        :rtype: bool
        """
        return self._enforce_execution_order

    @enforce_execution_order.setter
    def enforce_execution_order(self, enforce_execution_order):
        """Sets the enforce_execution_order of this TestSetExecutionDto.


        :param enforce_execution_order: The enforce_execution_order of this TestSetExecutionDto.  # noqa: E501
        :type: bool
        """

        self._enforce_execution_order = enforce_execution_order

    @property
    def creation_time(self):
        """Gets the creation_time of this TestSetExecutionDto.  # noqa: E501


        :return: The creation_time of this TestSetExecutionDto.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this TestSetExecutionDto.


        :param creation_time: The creation_time of this TestSetExecutionDto.  # noqa: E501
        :type: datetime
        """

        self._creation_time = creation_time

    @property
    def creator_user_id(self):
        """Gets the creator_user_id of this TestSetExecutionDto.  # noqa: E501


        :return: The creator_user_id of this TestSetExecutionDto.  # noqa: E501
        :rtype: int
        """
        return self._creator_user_id

    @creator_user_id.setter
    def creator_user_id(self, creator_user_id):
        """Sets the creator_user_id of this TestSetExecutionDto.


        :param creator_user_id: The creator_user_id of this TestSetExecutionDto.  # noqa: E501
        :type: int
        """

        self._creator_user_id = creator_user_id

    @property
    def id(self):
        """Gets the id of this TestSetExecutionDto.  # noqa: E501


        :return: The id of this TestSetExecutionDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TestSetExecutionDto.


        :param id: The id of this TestSetExecutionDto.  # noqa: E501
        :type: int
        """

        self._id = id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(TestSetExecutionDto, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TestSetExecutionDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TestSetExecutionDto):
            return True

        return self.to_dict() != other.to_dict()
