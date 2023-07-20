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


class SettingsUpdateBulkRequest(object):
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
        'settings': 'list[SettingsDto]'
    }

    attribute_map = {
        'settings': 'settings'
    }

    def __init__(self, settings=None, _configuration=None):  # noqa: E501
        """SettingsUpdateBulkRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._settings = None
        self.discriminator = None

        if settings is not None:
            self.settings = settings

    @property
    def settings(self):
        """Gets the settings of this SettingsUpdateBulkRequest.  # noqa: E501


        :return: The settings of this SettingsUpdateBulkRequest.  # noqa: E501
        :rtype: list[SettingsDto]
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this SettingsUpdateBulkRequest.


        :param settings: The settings of this SettingsUpdateBulkRequest.  # noqa: E501
        :type: list[SettingsDto]
        """

        self._settings = settings

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
        if issubclass(SettingsUpdateBulkRequest, dict):
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
        if not isinstance(other, SettingsUpdateBulkRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SettingsUpdateBulkRequest):
            return True

        return self.to_dict() != other.to_dict()