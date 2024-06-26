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


class ReexecuteTestCasesOptionsDto(object):
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
        'test_case_executions': 'list[TestCaseExecutionArgumentsDto]',
        'robot_id': 'int',
        'machine_id': 'int',
        'machine_session_id': 'int',
        'runtime_type': 'str',
        'enforce_execution_order': 'bool'
    }

    attribute_map = {
        'test_case_executions': 'testCaseExecutions',
        'robot_id': 'robotId',
        'machine_id': 'machineId',
        'machine_session_id': 'machineSessionId',
        'runtime_type': 'runtimeType',
        'enforce_execution_order': 'enforceExecutionOrder'
    }

    def __init__(self, test_case_executions=None, robot_id=None, machine_id=None, machine_session_id=None, runtime_type=None, enforce_execution_order=None, _configuration=None):  # noqa: E501
        """ReexecuteTestCasesOptionsDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._test_case_executions = None
        self._robot_id = None
        self._machine_id = None
        self._machine_session_id = None
        self._runtime_type = None
        self._enforce_execution_order = None
        self.discriminator = None

        self.test_case_executions = test_case_executions
        if robot_id is not None:
            self.robot_id = robot_id
        if machine_id is not None:
            self.machine_id = machine_id
        if machine_session_id is not None:
            self.machine_session_id = machine_session_id
        if runtime_type is not None:
            self.runtime_type = runtime_type
        if enforce_execution_order is not None:
            self.enforce_execution_order = enforce_execution_order

    @property
    def test_case_executions(self):
        """Gets the test_case_executions of this ReexecuteTestCasesOptionsDto.  # noqa: E501


        :return: The test_case_executions of this ReexecuteTestCasesOptionsDto.  # noqa: E501
        :rtype: list[TestCaseExecutionArgumentsDto]
        """
        return self._test_case_executions

    @test_case_executions.setter
    def test_case_executions(self, test_case_executions):
        """Sets the test_case_executions of this ReexecuteTestCasesOptionsDto.


        :param test_case_executions: The test_case_executions of this ReexecuteTestCasesOptionsDto.  # noqa: E501
        :type: list[TestCaseExecutionArgumentsDto]
        """
        if self._configuration.client_side_validation and test_case_executions is None:
            raise ValueError("Invalid value for `test_case_executions`, must not be `None`")  # noqa: E501

        self._test_case_executions = test_case_executions

    @property
    def robot_id(self):
        """Gets the robot_id of this ReexecuteTestCasesOptionsDto.  # noqa: E501


        :return: The robot_id of this ReexecuteTestCasesOptionsDto.  # noqa: E501
        :rtype: int
        """
        return self._robot_id

    @robot_id.setter
    def robot_id(self, robot_id):
        """Sets the robot_id of this ReexecuteTestCasesOptionsDto.


        :param robot_id: The robot_id of this ReexecuteTestCasesOptionsDto.  # noqa: E501
        :type: int
        """

        self._robot_id = robot_id

    @property
    def machine_id(self):
        """Gets the machine_id of this ReexecuteTestCasesOptionsDto.  # noqa: E501


        :return: The machine_id of this ReexecuteTestCasesOptionsDto.  # noqa: E501
        :rtype: int
        """
        return self._machine_id

    @machine_id.setter
    def machine_id(self, machine_id):
        """Sets the machine_id of this ReexecuteTestCasesOptionsDto.


        :param machine_id: The machine_id of this ReexecuteTestCasesOptionsDto.  # noqa: E501
        :type: int
        """

        self._machine_id = machine_id

    @property
    def machine_session_id(self):
        """Gets the machine_session_id of this ReexecuteTestCasesOptionsDto.  # noqa: E501


        :return: The machine_session_id of this ReexecuteTestCasesOptionsDto.  # noqa: E501
        :rtype: int
        """
        return self._machine_session_id

    @machine_session_id.setter
    def machine_session_id(self, machine_session_id):
        """Sets the machine_session_id of this ReexecuteTestCasesOptionsDto.


        :param machine_session_id: The machine_session_id of this ReexecuteTestCasesOptionsDto.  # noqa: E501
        :type: int
        """

        self._machine_session_id = machine_session_id

    @property
    def runtime_type(self):
        """Gets the runtime_type of this ReexecuteTestCasesOptionsDto.  # noqa: E501


        :return: The runtime_type of this ReexecuteTestCasesOptionsDto.  # noqa: E501
        :rtype: str
        """
        return self._runtime_type

    @runtime_type.setter
    def runtime_type(self, runtime_type):
        """Sets the runtime_type of this ReexecuteTestCasesOptionsDto.


        :param runtime_type: The runtime_type of this ReexecuteTestCasesOptionsDto.  # noqa: E501
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
    def enforce_execution_order(self):
        """Gets the enforce_execution_order of this ReexecuteTestCasesOptionsDto.  # noqa: E501


        :return: The enforce_execution_order of this ReexecuteTestCasesOptionsDto.  # noqa: E501
        :rtype: bool
        """
        return self._enforce_execution_order

    @enforce_execution_order.setter
    def enforce_execution_order(self, enforce_execution_order):
        """Sets the enforce_execution_order of this ReexecuteTestCasesOptionsDto.


        :param enforce_execution_order: The enforce_execution_order of this ReexecuteTestCasesOptionsDto.  # noqa: E501
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
        if issubclass(ReexecuteTestCasesOptionsDto, dict):
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
        if not isinstance(other, ReexecuteTestCasesOptionsDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReexecuteTestCasesOptionsDto):
            return True

        return self.to_dict() != other.to_dict()
