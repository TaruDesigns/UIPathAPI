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


class ValidateProcessScheduleRequest(object):
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
        'process_schedule': 'ProcessScheduleDto'
    }

    attribute_map = {
        'process_schedule': 'processSchedule'
    }

    def __init__(self, process_schedule=None, _configuration=None):  # noqa: E501
        """ValidateProcessScheduleRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._process_schedule = None
        self.discriminator = None

        self.process_schedule = process_schedule

    @property
    def process_schedule(self):
        """Gets the process_schedule of this ValidateProcessScheduleRequest.  # noqa: E501


        :return: The process_schedule of this ValidateProcessScheduleRequest.  # noqa: E501
        :rtype: ProcessScheduleDto
        """
        return self._process_schedule

    @process_schedule.setter
    def process_schedule(self, process_schedule):
        """Sets the process_schedule of this ValidateProcessScheduleRequest.


        :param process_schedule: The process_schedule of this ValidateProcessScheduleRequest.  # noqa: E501
        :type: ProcessScheduleDto
        """
        if self._configuration.client_side_validation and process_schedule is None:
            raise ValueError("Invalid value for `process_schedule`, must not be `None`")  # noqa: E501

        self._process_schedule = process_schedule

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
        if issubclass(ValidateProcessScheduleRequest, dict):
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
        if not isinstance(other, ValidateProcessScheduleRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ValidateProcessScheduleRequest):
            return True

        return self.to_dict() != other.to_dict()
