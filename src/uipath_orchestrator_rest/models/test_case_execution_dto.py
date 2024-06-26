# coding: utf-8

"""
    UiPath.WebApi 18.0

    Orchestrator API  # noqa: E501

    OpenAPI spec version: 18.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from uipath_orchestrator_rest.configuration import Configuration


class TestCaseExecutionDto(object):
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
        'job_id': 'int',
        'job_key': 'str',
        'test_set_execution_id': 'int',
        'test_set_execution': 'TestSetExecutionDto',
        'test_case_id': 'int',
        'test_case': 'TestCaseDto',
        'release_version_id': 'int',
        'version_number': 'str',
        'entry_point_path': 'str',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'status': 'str',
        'test_case_assertions': 'list[TestCaseAssertionDto]',
        'test_case_execution_attachments': 'list[TestCaseExecutionAttachmentDto]',
        'data_variation_identifier': 'str',
        'output_arguments': 'str',
        'input_arguments': 'str',
        'info': 'str',
        'host_machine_name': 'str',
        'runtime_type': 'str',
        'robot_name': 'str',
        'has_assertions': 'bool',
        'run_id': 'int',
        'test_case_type': 'str',
        'execution_order': 'int',
        'id': 'int'
    }

    attribute_map = {
        'job_id': 'JobId',
        'job_key': 'JobKey',
        'test_set_execution_id': 'TestSetExecutionId',
        'test_set_execution': 'TestSetExecution',
        'test_case_id': 'TestCaseId',
        'test_case': 'TestCase',
        'release_version_id': 'ReleaseVersionId',
        'version_number': 'VersionNumber',
        'entry_point_path': 'EntryPointPath',
        'start_time': 'StartTime',
        'end_time': 'EndTime',
        'status': 'Status',
        'test_case_assertions': 'TestCaseAssertions',
        'test_case_execution_attachments': 'TestCaseExecutionAttachments',
        'data_variation_identifier': 'DataVariationIdentifier',
        'output_arguments': 'OutputArguments',
        'input_arguments': 'InputArguments',
        'info': 'Info',
        'host_machine_name': 'HostMachineName',
        'runtime_type': 'RuntimeType',
        'robot_name': 'RobotName',
        'has_assertions': 'HasAssertions',
        'run_id': 'RunId',
        'test_case_type': 'TestCaseType',
        'execution_order': 'ExecutionOrder',
        'id': 'Id'
    }

    def __init__(self, job_id=None, job_key=None, test_set_execution_id=None, test_set_execution=None, test_case_id=None, test_case=None, release_version_id=None, version_number=None, entry_point_path=None, start_time=None, end_time=None, status=None, test_case_assertions=None, test_case_execution_attachments=None, data_variation_identifier=None, output_arguments=None, input_arguments=None, info=None, host_machine_name=None, runtime_type=None, robot_name=None, has_assertions=None, run_id=None, test_case_type=None, execution_order=None, id=None, _configuration=None):  # noqa: E501
        """TestCaseExecutionDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._job_id = None
        self._job_key = None
        self._test_set_execution_id = None
        self._test_set_execution = None
        self._test_case_id = None
        self._test_case = None
        self._release_version_id = None
        self._version_number = None
        self._entry_point_path = None
        self._start_time = None
        self._end_time = None
        self._status = None
        self._test_case_assertions = None
        self._test_case_execution_attachments = None
        self._data_variation_identifier = None
        self._output_arguments = None
        self._input_arguments = None
        self._info = None
        self._host_machine_name = None
        self._runtime_type = None
        self._robot_name = None
        self._has_assertions = None
        self._run_id = None
        self._test_case_type = None
        self._execution_order = None
        self._id = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if job_key is not None:
            self.job_key = job_key
        if test_set_execution_id is not None:
            self.test_set_execution_id = test_set_execution_id
        if test_set_execution is not None:
            self.test_set_execution = test_set_execution
        if test_case_id is not None:
            self.test_case_id = test_case_id
        if test_case is not None:
            self.test_case = test_case
        if release_version_id is not None:
            self.release_version_id = release_version_id
        if version_number is not None:
            self.version_number = version_number
        if entry_point_path is not None:
            self.entry_point_path = entry_point_path
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if status is not None:
            self.status = status
        if test_case_assertions is not None:
            self.test_case_assertions = test_case_assertions
        if test_case_execution_attachments is not None:
            self.test_case_execution_attachments = test_case_execution_attachments
        if data_variation_identifier is not None:
            self.data_variation_identifier = data_variation_identifier
        if output_arguments is not None:
            self.output_arguments = output_arguments
        if input_arguments is not None:
            self.input_arguments = input_arguments
        if info is not None:
            self.info = info
        if host_machine_name is not None:
            self.host_machine_name = host_machine_name
        if runtime_type is not None:
            self.runtime_type = runtime_type
        if robot_name is not None:
            self.robot_name = robot_name
        if has_assertions is not None:
            self.has_assertions = has_assertions
        if run_id is not None:
            self.run_id = run_id
        if test_case_type is not None:
            self.test_case_type = test_case_type
        if execution_order is not None:
            self.execution_order = execution_order
        if id is not None:
            self.id = id

    @property
    def job_id(self):
        """Gets the job_id of this TestCaseExecutionDto.  # noqa: E501


        :return: The job_id of this TestCaseExecutionDto.  # noqa: E501
        :rtype: int
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this TestCaseExecutionDto.


        :param job_id: The job_id of this TestCaseExecutionDto.  # noqa: E501
        :type: int
        """

        self._job_id = job_id

    @property
    def job_key(self):
        """Gets the job_key of this TestCaseExecutionDto.  # noqa: E501


        :return: The job_key of this TestCaseExecutionDto.  # noqa: E501
        :rtype: str
        """
        return self._job_key

    @job_key.setter
    def job_key(self, job_key):
        """Sets the job_key of this TestCaseExecutionDto.


        :param job_key: The job_key of this TestCaseExecutionDto.  # noqa: E501
        :type: str
        """

        self._job_key = job_key

    @property
    def test_set_execution_id(self):
        """Gets the test_set_execution_id of this TestCaseExecutionDto.  # noqa: E501


        :return: The test_set_execution_id of this TestCaseExecutionDto.  # noqa: E501
        :rtype: int
        """
        return self._test_set_execution_id

    @test_set_execution_id.setter
    def test_set_execution_id(self, test_set_execution_id):
        """Sets the test_set_execution_id of this TestCaseExecutionDto.


        :param test_set_execution_id: The test_set_execution_id of this TestCaseExecutionDto.  # noqa: E501
        :type: int
        """

        self._test_set_execution_id = test_set_execution_id

    @property
    def test_set_execution(self):
        """Gets the test_set_execution of this TestCaseExecutionDto.  # noqa: E501


        :return: The test_set_execution of this TestCaseExecutionDto.  # noqa: E501
        :rtype: TestSetExecutionDto
        """
        return self._test_set_execution

    @test_set_execution.setter
    def test_set_execution(self, test_set_execution):
        """Sets the test_set_execution of this TestCaseExecutionDto.


        :param test_set_execution: The test_set_execution of this TestCaseExecutionDto.  # noqa: E501
        :type: TestSetExecutionDto
        """

        self._test_set_execution = test_set_execution

    @property
    def test_case_id(self):
        """Gets the test_case_id of this TestCaseExecutionDto.  # noqa: E501


        :return: The test_case_id of this TestCaseExecutionDto.  # noqa: E501
        :rtype: int
        """
        return self._test_case_id

    @test_case_id.setter
    def test_case_id(self, test_case_id):
        """Sets the test_case_id of this TestCaseExecutionDto.


        :param test_case_id: The test_case_id of this TestCaseExecutionDto.  # noqa: E501
        :type: int
        """

        self._test_case_id = test_case_id

    @property
    def test_case(self):
        """Gets the test_case of this TestCaseExecutionDto.  # noqa: E501


        :return: The test_case of this TestCaseExecutionDto.  # noqa: E501
        :rtype: TestCaseDto
        """
        return self._test_case

    @test_case.setter
    def test_case(self, test_case):
        """Sets the test_case of this TestCaseExecutionDto.


        :param test_case: The test_case of this TestCaseExecutionDto.  # noqa: E501
        :type: TestCaseDto
        """

        self._test_case = test_case

    @property
    def release_version_id(self):
        """Gets the release_version_id of this TestCaseExecutionDto.  # noqa: E501


        :return: The release_version_id of this TestCaseExecutionDto.  # noqa: E501
        :rtype: int
        """
        return self._release_version_id

    @release_version_id.setter
    def release_version_id(self, release_version_id):
        """Sets the release_version_id of this TestCaseExecutionDto.


        :param release_version_id: The release_version_id of this TestCaseExecutionDto.  # noqa: E501
        :type: int
        """

        self._release_version_id = release_version_id

    @property
    def version_number(self):
        """Gets the version_number of this TestCaseExecutionDto.  # noqa: E501


        :return: The version_number of this TestCaseExecutionDto.  # noqa: E501
        :rtype: str
        """
        return self._version_number

    @version_number.setter
    def version_number(self, version_number):
        """Sets the version_number of this TestCaseExecutionDto.


        :param version_number: The version_number of this TestCaseExecutionDto.  # noqa: E501
        :type: str
        """

        self._version_number = version_number

    @property
    def entry_point_path(self):
        """Gets the entry_point_path of this TestCaseExecutionDto.  # noqa: E501


        :return: The entry_point_path of this TestCaseExecutionDto.  # noqa: E501
        :rtype: str
        """
        return self._entry_point_path

    @entry_point_path.setter
    def entry_point_path(self, entry_point_path):
        """Sets the entry_point_path of this TestCaseExecutionDto.


        :param entry_point_path: The entry_point_path of this TestCaseExecutionDto.  # noqa: E501
        :type: str
        """

        self._entry_point_path = entry_point_path

    @property
    def start_time(self):
        """Gets the start_time of this TestCaseExecutionDto.  # noqa: E501


        :return: The start_time of this TestCaseExecutionDto.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this TestCaseExecutionDto.


        :param start_time: The start_time of this TestCaseExecutionDto.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this TestCaseExecutionDto.  # noqa: E501


        :return: The end_time of this TestCaseExecutionDto.  # noqa: E501
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this TestCaseExecutionDto.


        :param end_time: The end_time of this TestCaseExecutionDto.  # noqa: E501
        :type: datetime
        """

        self._end_time = end_time

    @property
    def status(self):
        """Gets the status of this TestCaseExecutionDto.  # noqa: E501


        :return: The status of this TestCaseExecutionDto.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TestCaseExecutionDto.


        :param status: The status of this TestCaseExecutionDto.  # noqa: E501
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
    def test_case_assertions(self):
        """Gets the test_case_assertions of this TestCaseExecutionDto.  # noqa: E501


        :return: The test_case_assertions of this TestCaseExecutionDto.  # noqa: E501
        :rtype: list[TestCaseAssertionDto]
        """
        return self._test_case_assertions

    @test_case_assertions.setter
    def test_case_assertions(self, test_case_assertions):
        """Sets the test_case_assertions of this TestCaseExecutionDto.


        :param test_case_assertions: The test_case_assertions of this TestCaseExecutionDto.  # noqa: E501
        :type: list[TestCaseAssertionDto]
        """

        self._test_case_assertions = test_case_assertions

    @property
    def test_case_execution_attachments(self):
        """Gets the test_case_execution_attachments of this TestCaseExecutionDto.  # noqa: E501


        :return: The test_case_execution_attachments of this TestCaseExecutionDto.  # noqa: E501
        :rtype: list[TestCaseExecutionAttachmentDto]
        """
        return self._test_case_execution_attachments

    @test_case_execution_attachments.setter
    def test_case_execution_attachments(self, test_case_execution_attachments):
        """Sets the test_case_execution_attachments of this TestCaseExecutionDto.


        :param test_case_execution_attachments: The test_case_execution_attachments of this TestCaseExecutionDto.  # noqa: E501
        :type: list[TestCaseExecutionAttachmentDto]
        """

        self._test_case_execution_attachments = test_case_execution_attachments

    @property
    def data_variation_identifier(self):
        """Gets the data_variation_identifier of this TestCaseExecutionDto.  # noqa: E501


        :return: The data_variation_identifier of this TestCaseExecutionDto.  # noqa: E501
        :rtype: str
        """
        return self._data_variation_identifier

    @data_variation_identifier.setter
    def data_variation_identifier(self, data_variation_identifier):
        """Sets the data_variation_identifier of this TestCaseExecutionDto.


        :param data_variation_identifier: The data_variation_identifier of this TestCaseExecutionDto.  # noqa: E501
        :type: str
        """

        self._data_variation_identifier = data_variation_identifier

    @property
    def output_arguments(self):
        """Gets the output_arguments of this TestCaseExecutionDto.  # noqa: E501


        :return: The output_arguments of this TestCaseExecutionDto.  # noqa: E501
        :rtype: str
        """
        return self._output_arguments

    @output_arguments.setter
    def output_arguments(self, output_arguments):
        """Sets the output_arguments of this TestCaseExecutionDto.


        :param output_arguments: The output_arguments of this TestCaseExecutionDto.  # noqa: E501
        :type: str
        """

        self._output_arguments = output_arguments

    @property
    def input_arguments(self):
        """Gets the input_arguments of this TestCaseExecutionDto.  # noqa: E501


        :return: The input_arguments of this TestCaseExecutionDto.  # noqa: E501
        :rtype: str
        """
        return self._input_arguments

    @input_arguments.setter
    def input_arguments(self, input_arguments):
        """Sets the input_arguments of this TestCaseExecutionDto.


        :param input_arguments: The input_arguments of this TestCaseExecutionDto.  # noqa: E501
        :type: str
        """

        self._input_arguments = input_arguments

    @property
    def info(self):
        """Gets the info of this TestCaseExecutionDto.  # noqa: E501


        :return: The info of this TestCaseExecutionDto.  # noqa: E501
        :rtype: str
        """
        return self._info

    @info.setter
    def info(self, info):
        """Sets the info of this TestCaseExecutionDto.


        :param info: The info of this TestCaseExecutionDto.  # noqa: E501
        :type: str
        """

        self._info = info

    @property
    def host_machine_name(self):
        """Gets the host_machine_name of this TestCaseExecutionDto.  # noqa: E501


        :return: The host_machine_name of this TestCaseExecutionDto.  # noqa: E501
        :rtype: str
        """
        return self._host_machine_name

    @host_machine_name.setter
    def host_machine_name(self, host_machine_name):
        """Sets the host_machine_name of this TestCaseExecutionDto.


        :param host_machine_name: The host_machine_name of this TestCaseExecutionDto.  # noqa: E501
        :type: str
        """

        self._host_machine_name = host_machine_name

    @property
    def runtime_type(self):
        """Gets the runtime_type of this TestCaseExecutionDto.  # noqa: E501


        :return: The runtime_type of this TestCaseExecutionDto.  # noqa: E501
        :rtype: str
        """
        return self._runtime_type

    @runtime_type.setter
    def runtime_type(self, runtime_type):
        """Sets the runtime_type of this TestCaseExecutionDto.


        :param runtime_type: The runtime_type of this TestCaseExecutionDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["NonProduction", "Attended", "Unattended", "Development", "Studio", "RpaDeveloper", "StudioX", "CitizenDeveloper", "Headless", "StudioPro", "RpaDeveloperPro", "TestAutomation", "AutomationCloud", "Serverless", "AutomationKit", "ServerlessTestAutomation", "AutomationCloudTestAutomation", "AttendedStudioWeb"]  # noqa: E501
        if (self._configuration.client_side_validation and
                runtime_type not in allowed_values):
            raise ValueError(
                "Invalid value for `runtime_type` ({0}), must be one of {1}"  # noqa: E501
                .format(runtime_type, allowed_values)
            )

        self._runtime_type = runtime_type

    @property
    def robot_name(self):
        """Gets the robot_name of this TestCaseExecutionDto.  # noqa: E501


        :return: The robot_name of this TestCaseExecutionDto.  # noqa: E501
        :rtype: str
        """
        return self._robot_name

    @robot_name.setter
    def robot_name(self, robot_name):
        """Sets the robot_name of this TestCaseExecutionDto.


        :param robot_name: The robot_name of this TestCaseExecutionDto.  # noqa: E501
        :type: str
        """

        self._robot_name = robot_name

    @property
    def has_assertions(self):
        """Gets the has_assertions of this TestCaseExecutionDto.  # noqa: E501


        :return: The has_assertions of this TestCaseExecutionDto.  # noqa: E501
        :rtype: bool
        """
        return self._has_assertions

    @has_assertions.setter
    def has_assertions(self, has_assertions):
        """Sets the has_assertions of this TestCaseExecutionDto.


        :param has_assertions: The has_assertions of this TestCaseExecutionDto.  # noqa: E501
        :type: bool
        """

        self._has_assertions = has_assertions

    @property
    def run_id(self):
        """Gets the run_id of this TestCaseExecutionDto.  # noqa: E501


        :return: The run_id of this TestCaseExecutionDto.  # noqa: E501
        :rtype: int
        """
        return self._run_id

    @run_id.setter
    def run_id(self, run_id):
        """Sets the run_id of this TestCaseExecutionDto.


        :param run_id: The run_id of this TestCaseExecutionDto.  # noqa: E501
        :type: int
        """

        self._run_id = run_id

    @property
    def test_case_type(self):
        """Gets the test_case_type of this TestCaseExecutionDto.  # noqa: E501


        :return: The test_case_type of this TestCaseExecutionDto.  # noqa: E501
        :rtype: str
        """
        return self._test_case_type

    @test_case_type.setter
    def test_case_type(self, test_case_type):
        """Sets the test_case_type of this TestCaseExecutionDto.


        :param test_case_type: The test_case_type of this TestCaseExecutionDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["TestCase", "TestDataSetup"]  # noqa: E501
        if (self._configuration.client_side_validation and
                test_case_type not in allowed_values):
            raise ValueError(
                "Invalid value for `test_case_type` ({0}), must be one of {1}"  # noqa: E501
                .format(test_case_type, allowed_values)
            )

        self._test_case_type = test_case_type

    @property
    def execution_order(self):
        """Gets the execution_order of this TestCaseExecutionDto.  # noqa: E501


        :return: The execution_order of this TestCaseExecutionDto.  # noqa: E501
        :rtype: int
        """
        return self._execution_order

    @execution_order.setter
    def execution_order(self, execution_order):
        """Sets the execution_order of this TestCaseExecutionDto.


        :param execution_order: The execution_order of this TestCaseExecutionDto.  # noqa: E501
        :type: int
        """

        self._execution_order = execution_order

    @property
    def id(self):
        """Gets the id of this TestCaseExecutionDto.  # noqa: E501


        :return: The id of this TestCaseExecutionDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TestCaseExecutionDto.


        :param id: The id of this TestCaseExecutionDto.  # noqa: E501
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
        if issubclass(TestCaseExecutionDto, dict):
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
        if not isinstance(other, TestCaseExecutionDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TestCaseExecutionDto):
            return True

        return self.to_dict() != other.to_dict()
