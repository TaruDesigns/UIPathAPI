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


class MachineRobotDto(object):
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
        'machine_id': 'int',
        'machine_name': 'str',
        'robot_id': 'int',
        'robot_user_name': 'str'
    }

    attribute_map = {
        'machine_id': 'MachineId',
        'machine_name': 'MachineName',
        'robot_id': 'RobotId',
        'robot_user_name': 'RobotUserName'
    }

    def __init__(self, machine_id=None, machine_name=None, robot_id=None, robot_user_name=None, _configuration=None):  # noqa: E501
        """MachineRobotDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._machine_id = None
        self._machine_name = None
        self._robot_id = None
        self._robot_user_name = None
        self.discriminator = None

        if machine_id is not None:
            self.machine_id = machine_id
        if machine_name is not None:
            self.machine_name = machine_name
        if robot_id is not None:
            self.robot_id = robot_id
        if robot_user_name is not None:
            self.robot_user_name = robot_user_name

    @property
    def machine_id(self):
        """Gets the machine_id of this MachineRobotDto.  # noqa: E501

        The Id of the Machine.  # noqa: E501

        :return: The machine_id of this MachineRobotDto.  # noqa: E501
        :rtype: int
        """
        return self._machine_id

    @machine_id.setter
    def machine_id(self, machine_id):
        """Sets the machine_id of this MachineRobotDto.

        The Id of the Machine.  # noqa: E501

        :param machine_id: The machine_id of this MachineRobotDto.  # noqa: E501
        :type: int
        """

        self._machine_id = machine_id

    @property
    def machine_name(self):
        """Gets the machine_name of this MachineRobotDto.  # noqa: E501

        The name of the Machine.  # noqa: E501

        :return: The machine_name of this MachineRobotDto.  # noqa: E501
        :rtype: str
        """
        return self._machine_name

    @machine_name.setter
    def machine_name(self, machine_name):
        """Sets the machine_name of this MachineRobotDto.

        The name of the Machine.  # noqa: E501

        :param machine_name: The machine_name of this MachineRobotDto.  # noqa: E501
        :type: str
        """

        self._machine_name = machine_name

    @property
    def robot_id(self):
        """Gets the robot_id of this MachineRobotDto.  # noqa: E501

        The Id of the Robot.  # noqa: E501

        :return: The robot_id of this MachineRobotDto.  # noqa: E501
        :rtype: int
        """
        return self._robot_id

    @robot_id.setter
    def robot_id(self, robot_id):
        """Sets the robot_id of this MachineRobotDto.

        The Id of the Robot.  # noqa: E501

        :param robot_id: The robot_id of this MachineRobotDto.  # noqa: E501
        :type: int
        """

        self._robot_id = robot_id

    @property
    def robot_user_name(self):
        """Gets the robot_user_name of this MachineRobotDto.  # noqa: E501

        The robot user name.  # noqa: E501

        :return: The robot_user_name of this MachineRobotDto.  # noqa: E501
        :rtype: str
        """
        return self._robot_user_name

    @robot_user_name.setter
    def robot_user_name(self, robot_user_name):
        """Sets the robot_user_name of this MachineRobotDto.

        The robot user name.  # noqa: E501

        :param robot_user_name: The robot_user_name of this MachineRobotDto.  # noqa: E501
        :type: str
        """

        self._robot_user_name = robot_user_name

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
        if issubclass(MachineRobotDto, dict):
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
        if not isinstance(other, MachineRobotDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MachineRobotDto):
            return True

        return self.to_dict() != other.to_dict()
