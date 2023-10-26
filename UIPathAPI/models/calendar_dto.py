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


class CalendarDto(object):
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
        'time_zone_id': 'str',
        'excluded_dates': 'list[datetime]'
    }

    attribute_map = {
        'time_zone_id': 'TimeZoneId',
        'excluded_dates': 'ExcludedDates'
    }

    def __init__(self, time_zone_id=None, excluded_dates=None, _configuration=None):  # noqa: E501
        """CalendarDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._time_zone_id = None
        self._excluded_dates = None
        self.discriminator = None

        if time_zone_id is not None:
            self.time_zone_id = time_zone_id
        if excluded_dates is not None:
            self.excluded_dates = excluded_dates

    @property
    def time_zone_id(self):
        """Gets the time_zone_id of this CalendarDto.  # noqa: E501


        :return: The time_zone_id of this CalendarDto.  # noqa: E501
        :rtype: str
        """
        return self._time_zone_id

    @time_zone_id.setter
    def time_zone_id(self, time_zone_id):
        """Sets the time_zone_id of this CalendarDto.


        :param time_zone_id: The time_zone_id of this CalendarDto.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                time_zone_id is not None and len(time_zone_id) > 80):
            raise ValueError("Invalid value for `time_zone_id`, length must be less than or equal to `80`")  # noqa: E501

        self._time_zone_id = time_zone_id

    @property
    def excluded_dates(self):
        """Gets the excluded_dates of this CalendarDto.  # noqa: E501


        :return: The excluded_dates of this CalendarDto.  # noqa: E501
        :rtype: list[datetime]
        """
        return self._excluded_dates

    @excluded_dates.setter
    def excluded_dates(self, excluded_dates):
        """Sets the excluded_dates of this CalendarDto.


        :param excluded_dates: The excluded_dates of this CalendarDto.  # noqa: E501
        :type: list[datetime]
        """

        self._excluded_dates = excluded_dates

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
        if issubclass(CalendarDto, dict):
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
        if not isinstance(other, CalendarDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CalendarDto):
            return True

        return self.to_dict() != other.to_dict()
