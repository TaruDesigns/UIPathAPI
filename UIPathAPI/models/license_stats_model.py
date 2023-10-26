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


class LicenseStatsModel(object):
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
        'robot_type': 'str',
        'count': 'int',
        'timestamp': 'datetime'
    }

    attribute_map = {
        'robot_type': 'robotType',
        'count': 'count',
        'timestamp': 'timestamp'
    }

    def __init__(self, robot_type=None, count=None, timestamp=None, _configuration=None):  # noqa: E501
        """LicenseStatsModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._robot_type = None
        self._count = None
        self._timestamp = None
        self.discriminator = None

        if robot_type is not None:
            self.robot_type = robot_type
        if count is not None:
            self.count = count
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def robot_type(self):
        """Gets the robot_type of this LicenseStatsModel.  # noqa: E501


        :return: The robot_type of this LicenseStatsModel.  # noqa: E501
        :rtype: str
        """
        return self._robot_type

    @robot_type.setter
    def robot_type(self, robot_type):
        """Sets the robot_type of this LicenseStatsModel.


        :param robot_type: The robot_type of this LicenseStatsModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["NonProduction", "Attended", "Unattended", "Development", "Studio", "RpaDeveloper", "StudioX", "CitizenDeveloper", "Headless", "RpaDeveloperPro", "StudioPro", "TestAutomation", "AutomationCloud", "Serverless", "AutomationKit", "ServerlessTestAutomation", "AutomationCloudTestAutomation", "AttendedStudioWeb"]  # noqa: E501
        if (self._configuration.client_side_validation and
                robot_type not in allowed_values):
            raise ValueError(
                "Invalid value for `robot_type` ({0}), must be one of {1}"  # noqa: E501
                .format(robot_type, allowed_values)
            )

        self._robot_type = robot_type

    @property
    def count(self):
        """Gets the count of this LicenseStatsModel.  # noqa: E501


        :return: The count of this LicenseStatsModel.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this LicenseStatsModel.


        :param count: The count of this LicenseStatsModel.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def timestamp(self):
        """Gets the timestamp of this LicenseStatsModel.  # noqa: E501


        :return: The timestamp of this LicenseStatsModel.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this LicenseStatsModel.


        :param timestamp: The timestamp of this LicenseStatsModel.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

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
        if issubclass(LicenseStatsModel, dict):
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
        if not isinstance(other, LicenseStatsModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LicenseStatsModel):
            return True

        return self.to_dict() != other.to_dict()
