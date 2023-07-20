# coding: utf-8

"""
    UiPath.WebApi 16.0

    Orchestrator API  # noqa: E501

    OpenAPI spec version: 16.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from UIPathAPI.configuration import Configuration


class RobotDeleteBulkRequest(object):
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
        'robot_ids': 'list[int]'
    }

    attribute_map = {
        'robot_ids': 'robotIds'
    }

    def __init__(self, robot_ids=None, _configuration=None):  # noqa: E501
        """RobotDeleteBulkRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._robot_ids = None
        self.discriminator = None

        self.robot_ids = robot_ids

    @property
    def robot_ids(self):
        """Gets the robot_ids of this RobotDeleteBulkRequest.  # noqa: E501


        :return: The robot_ids of this RobotDeleteBulkRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._robot_ids

    @robot_ids.setter
    def robot_ids(self, robot_ids):
        """Sets the robot_ids of this RobotDeleteBulkRequest.


        :param robot_ids: The robot_ids of this RobotDeleteBulkRequest.  # noqa: E501
        :type: list[int]
        """
        if self._configuration.client_side_validation and robot_ids is None:
            raise ValueError("Invalid value for `robot_ids`, must not be `None`")  # noqa: E501

        self._robot_ids = robot_ids

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
        if issubclass(RobotDeleteBulkRequest, dict):
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
        if not isinstance(other, RobotDeleteBulkRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RobotDeleteBulkRequest):
            return True

        return self.to_dict() != other.to_dict()
