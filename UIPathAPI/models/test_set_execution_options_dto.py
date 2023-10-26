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


class TestSetExecutionOptionsDto(object):
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
        'batch_execution_key': 'str',
        'trigger_type': 'str',
        'test_cases': 'list[TestCaseExecutionOptionsDto]',
        'execute_only_specified_test_cases': 'bool',
        'robot_id': 'int',
        'runtime_type': 'str',
        'machine_id': 'int',
        'machine_session_id': 'int',
        'enforce_execution_order': 'bool'
    }

    attribute_map = {
        'batch_execution_key': 'batchExecutionKey',
        'trigger_type': 'triggerType',
        'test_cases': 'testCases',
        'execute_only_specified_test_cases': 'executeOnlySpecifiedTestCases',
        'robot_id': 'robotId',
        'runtime_type': 'runtimeType',
        'machine_id': 'machineId',
        'machine_session_id': 'machineSessionId',
        'enforce_execution_order': 'enforceExecutionOrder'
    }

    def __init__(self, batch_execution_key=None, trigger_type=None, test_cases=None, execute_only_specified_test_cases=None, robot_id=None, runtime_type=None, machine_id=None, machine_session_id=None, enforce_execution_order=None, _configuration=None):  # noqa: E501
        """TestSetExecutionOptionsDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._batch_execution_key = None
        self._trigger_type = None
        self._test_cases = None
        self._execute_only_specified_test_cases = None
        self._robot_id = None
        self._runtime_type = None
        self._machine_id = None
        self._machine_session_id = None
        self._enforce_execution_order = None
        self.discriminator = None

        if batch_execution_key is not None:
            self.batch_execution_key = batch_execution_key
        if trigger_type is not None:
            self.trigger_type = trigger_type
        if test_cases is not None:
            self.test_cases = test_cases
        if execute_only_specified_test_cases is not None:
            self.execute_only_specified_test_cases = execute_only_specified_test_cases
        if robot_id is not None:
            self.robot_id = robot_id
        if runtime_type is not None:
            self.runtime_type = runtime_type
        if machine_id is not None:
            self.machine_id = machine_id
        if machine_session_id is not None:
            self.machine_session_id = machine_session_id
        if enforce_execution_order is not None:
            self.enforce_execution_order = enforce_execution_order

    @property
    def batch_execution_key(self):
        """Gets the batch_execution_key of this TestSetExecutionOptionsDto.  # noqa: E501


        :return: The batch_execution_key of this TestSetExecutionOptionsDto.  # noqa: E501
        :rtype: str
        """
        return self._batch_execution_key

    @batch_execution_key.setter
    def batch_execution_key(self, batch_execution_key):
        """Sets the batch_execution_key of this TestSetExecutionOptionsDto.


        :param batch_execution_key: The batch_execution_key of this TestSetExecutionOptionsDto.  # noqa: E501
        :type: str
        """

        self._batch_execution_key = batch_execution_key

    @property
    def trigger_type(self):
        """Gets the trigger_type of this TestSetExecutionOptionsDto.  # noqa: E501


        :return: The trigger_type of this TestSetExecutionOptionsDto.  # noqa: E501
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        """Sets the trigger_type of this TestSetExecutionOptionsDto.


        :param trigger_type: The trigger_type of this TestSetExecutionOptionsDto.  # noqa: E501
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
    def test_cases(self):
        """Gets the test_cases of this TestSetExecutionOptionsDto.  # noqa: E501


        :return: The test_cases of this TestSetExecutionOptionsDto.  # noqa: E501
        :rtype: list[TestCaseExecutionOptionsDto]
        """
        return self._test_cases

    @test_cases.setter
    def test_cases(self, test_cases):
        """Sets the test_cases of this TestSetExecutionOptionsDto.


        :param test_cases: The test_cases of this TestSetExecutionOptionsDto.  # noqa: E501
        :type: list[TestCaseExecutionOptionsDto]
        """

        self._test_cases = test_cases

    @property
    def execute_only_specified_test_cases(self):
        """Gets the execute_only_specified_test_cases of this TestSetExecutionOptionsDto.  # noqa: E501


        :return: The execute_only_specified_test_cases of this TestSetExecutionOptionsDto.  # noqa: E501
        :rtype: bool
        """
        return self._execute_only_specified_test_cases

    @execute_only_specified_test_cases.setter
    def execute_only_specified_test_cases(self, execute_only_specified_test_cases):
        """Sets the execute_only_specified_test_cases of this TestSetExecutionOptionsDto.


        :param execute_only_specified_test_cases: The execute_only_specified_test_cases of this TestSetExecutionOptionsDto.  # noqa: E501
        :type: bool
        """

        self._execute_only_specified_test_cases = execute_only_specified_test_cases

    @property
    def robot_id(self):
        """Gets the robot_id of this TestSetExecutionOptionsDto.  # noqa: E501


        :return: The robot_id of this TestSetExecutionOptionsDto.  # noqa: E501
        :rtype: int
        """
        return self._robot_id

    @robot_id.setter
    def robot_id(self, robot_id):
        """Sets the robot_id of this TestSetExecutionOptionsDto.


        :param robot_id: The robot_id of this TestSetExecutionOptionsDto.  # noqa: E501
        :type: int
        """

        self._robot_id = robot_id

    @property
    def runtime_type(self):
        """Gets the runtime_type of this TestSetExecutionOptionsDto.  # noqa: E501


        :return: The runtime_type of this TestSetExecutionOptionsDto.  # noqa: E501
        :rtype: str
        """
        return self._runtime_type

    @runtime_type.setter
    def runtime_type(self, runtime_type):
        """Sets the runtime_type of this TestSetExecutionOptionsDto.


        :param runtime_type: The runtime_type of this TestSetExecutionOptionsDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["NonProduction", "Attended", "Unattended", "Development", "Studio", "RpaDeveloper", "StudioX", "CitizenDeveloper", "Headless", "RpaDeveloperPro", "StudioPro", "TestAutomation", "AutomationCloud", "Serverless", "AutomationKit", "ServerlessTestAutomation", "AutomationCloudTestAutomation", "AttendedStudioWeb"]  # noqa: E501
        if (self._configuration.client_side_validation and
                runtime_type not in allowed_values):
            raise ValueError(
                "Invalid value for `runtime_type` ({0}), must be one of {1}"  # noqa: E501
                .format(runtime_type, allowed_values)
            )

        self._runtime_type = runtime_type

    @property
    def machine_id(self):
        """Gets the machine_id of this TestSetExecutionOptionsDto.  # noqa: E501


        :return: The machine_id of this TestSetExecutionOptionsDto.  # noqa: E501
        :rtype: int
        """
        return self._machine_id

    @machine_id.setter
    def machine_id(self, machine_id):
        """Sets the machine_id of this TestSetExecutionOptionsDto.


        :param machine_id: The machine_id of this TestSetExecutionOptionsDto.  # noqa: E501
        :type: int
        """

        self._machine_id = machine_id

    @property
    def machine_session_id(self):
        """Gets the machine_session_id of this TestSetExecutionOptionsDto.  # noqa: E501


        :return: The machine_session_id of this TestSetExecutionOptionsDto.  # noqa: E501
        :rtype: int
        """
        return self._machine_session_id

    @machine_session_id.setter
    def machine_session_id(self, machine_session_id):
        """Sets the machine_session_id of this TestSetExecutionOptionsDto.


        :param machine_session_id: The machine_session_id of this TestSetExecutionOptionsDto.  # noqa: E501
        :type: int
        """

        self._machine_session_id = machine_session_id

    @property
    def enforce_execution_order(self):
        """Gets the enforce_execution_order of this TestSetExecutionOptionsDto.  # noqa: E501


        :return: The enforce_execution_order of this TestSetExecutionOptionsDto.  # noqa: E501
        :rtype: bool
        """
        return self._enforce_execution_order

    @enforce_execution_order.setter
    def enforce_execution_order(self, enforce_execution_order):
        """Sets the enforce_execution_order of this TestSetExecutionOptionsDto.


        :param enforce_execution_order: The enforce_execution_order of this TestSetExecutionOptionsDto.  # noqa: E501
        :type: bool
        """

        self._enforce_execution_order = enforce_execution_order

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
        if issubclass(TestSetExecutionOptionsDto, dict):
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
        if not isinstance(other, TestSetExecutionOptionsDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TestSetExecutionOptionsDto):
            return True

        return self.to_dict() != other.to_dict()
