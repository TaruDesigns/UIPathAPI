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


class ExtendedCalendarDto(object):
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
        'time_zone_id': 'str',
        'excluded_dates': 'list[datetime]',
        'key': 'str',
        'id': 'int'
    }

    attribute_map = {
        'name': 'Name',
        'time_zone_id': 'TimeZoneId',
        'excluded_dates': 'ExcludedDates',
        'key': 'Key',
        'id': 'Id'
    }

    def __init__(self, name=None, time_zone_id=None, excluded_dates=None, key=None, id=None, _configuration=None):  # noqa: E501
        """ExtendedCalendarDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._time_zone_id = None
        self._excluded_dates = None
        self._key = None
        self._id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if time_zone_id is not None:
            self.time_zone_id = time_zone_id
        if excluded_dates is not None:
            self.excluded_dates = excluded_dates
        if key is not None:
            self.key = key
        if id is not None:
            self.id = id

    @property
    def name(self):
        """Gets the name of this ExtendedCalendarDto.  # noqa: E501


        :return: The name of this ExtendedCalendarDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ExtendedCalendarDto.


        :param name: The name of this ExtendedCalendarDto.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                name is not None and len(name) > 150):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `150`")  # noqa: E501

        self._name = name

    @property
    def time_zone_id(self):
        """Gets the time_zone_id of this ExtendedCalendarDto.  # noqa: E501


        :return: The time_zone_id of this ExtendedCalendarDto.  # noqa: E501
        :rtype: str
        """
        return self._time_zone_id

    @time_zone_id.setter
    def time_zone_id(self, time_zone_id):
        """Sets the time_zone_id of this ExtendedCalendarDto.


        :param time_zone_id: The time_zone_id of this ExtendedCalendarDto.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                time_zone_id is not None and len(time_zone_id) > 80):
            raise ValueError("Invalid value for `time_zone_id`, length must be less than or equal to `80`")  # noqa: E501

        self._time_zone_id = time_zone_id

    @property
    def excluded_dates(self):
        """Gets the excluded_dates of this ExtendedCalendarDto.  # noqa: E501


        :return: The excluded_dates of this ExtendedCalendarDto.  # noqa: E501
        :rtype: list[datetime]
        """
        return self._excluded_dates

    @excluded_dates.setter
    def excluded_dates(self, excluded_dates):
        """Sets the excluded_dates of this ExtendedCalendarDto.


        :param excluded_dates: The excluded_dates of this ExtendedCalendarDto.  # noqa: E501
        :type: list[datetime]
        """

        self._excluded_dates = excluded_dates

    @property
    def key(self):
        """Gets the key of this ExtendedCalendarDto.  # noqa: E501


        :return: The key of this ExtendedCalendarDto.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ExtendedCalendarDto.


        :param key: The key of this ExtendedCalendarDto.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def id(self):
        """Gets the id of this ExtendedCalendarDto.  # noqa: E501


        :return: The id of this ExtendedCalendarDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ExtendedCalendarDto.


        :param id: The id of this ExtendedCalendarDto.  # noqa: E501
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
        if issubclass(ExtendedCalendarDto, dict):
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
        if not isinstance(other, ExtendedCalendarDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExtendedCalendarDto):
            return True

        return self.to_dict() != other.to_dict()
