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


class CalendarExistsRequest(object):
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
        'calendar_name': 'str'
    }

    attribute_map = {
        'calendar_name': 'calendarName'
    }

    def __init__(self, calendar_name=None, _configuration=None):  # noqa: E501
        """CalendarExistsRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._calendar_name = None
        self.discriminator = None

        self.calendar_name = calendar_name

    @property
    def calendar_name(self):
        """Gets the calendar_name of this CalendarExistsRequest.  # noqa: E501


        :return: The calendar_name of this CalendarExistsRequest.  # noqa: E501
        :rtype: str
        """
        return self._calendar_name

    @calendar_name.setter
    def calendar_name(self, calendar_name):
        """Sets the calendar_name of this CalendarExistsRequest.


        :param calendar_name: The calendar_name of this CalendarExistsRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and calendar_name is None:
            raise ValueError("Invalid value for `calendar_name`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                calendar_name is not None and len(calendar_name) < 1):
            raise ValueError("Invalid value for `calendar_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._calendar_name = calendar_name

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
        if issubclass(CalendarExistsRequest, dict):
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
        if not isinstance(other, CalendarExistsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CalendarExistsRequest):
            return True

        return self.to_dict() != other.to_dict()
