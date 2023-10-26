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


class ConsumptionLicenseStatsModel(object):
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
        'type': 'str',
        'used': 'int',
        'total': 'int',
        'timestamp': 'datetime'
    }

    attribute_map = {
        'type': 'type',
        'used': 'used',
        'total': 'total',
        'timestamp': 'timestamp'
    }

    def __init__(self, type=None, used=None, total=None, timestamp=None, _configuration=None):  # noqa: E501
        """ConsumptionLicenseStatsModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._type = None
        self._used = None
        self._total = None
        self._timestamp = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if used is not None:
            self.used = used
        if total is not None:
            self.total = total
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def type(self):
        """Gets the type of this ConsumptionLicenseStatsModel.  # noqa: E501


        :return: The type of this ConsumptionLicenseStatsModel.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ConsumptionLicenseStatsModel.


        :param type: The type of this ConsumptionLicenseStatsModel.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def used(self):
        """Gets the used of this ConsumptionLicenseStatsModel.  # noqa: E501


        :return: The used of this ConsumptionLicenseStatsModel.  # noqa: E501
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this ConsumptionLicenseStatsModel.


        :param used: The used of this ConsumptionLicenseStatsModel.  # noqa: E501
        :type: int
        """

        self._used = used

    @property
    def total(self):
        """Gets the total of this ConsumptionLicenseStatsModel.  # noqa: E501


        :return: The total of this ConsumptionLicenseStatsModel.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ConsumptionLicenseStatsModel.


        :param total: The total of this ConsumptionLicenseStatsModel.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def timestamp(self):
        """Gets the timestamp of this ConsumptionLicenseStatsModel.  # noqa: E501


        :return: The timestamp of this ConsumptionLicenseStatsModel.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ConsumptionLicenseStatsModel.


        :param timestamp: The timestamp of this ConsumptionLicenseStatsModel.  # noqa: E501
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
        if issubclass(ConsumptionLicenseStatsModel, dict):
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
        if not isinstance(other, ConsumptionLicenseStatsModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConsumptionLicenseStatsModel):
            return True

        return self.to_dict() != other.to_dict()
