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


class ResponseDictionaryDto(object):
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
        'keys': 'list[str]',
        'values': 'list[str]'
    }

    attribute_map = {
        'keys': 'Keys',
        'values': 'Values'
    }

    def __init__(self, keys=None, values=None, _configuration=None):  # noqa: E501
        """ResponseDictionaryDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._keys = None
        self._values = None
        self.discriminator = None

        if keys is not None:
            self.keys = keys
        if values is not None:
            self.values = values

    @property
    def keys(self):
        """Gets the keys of this ResponseDictionaryDto.  # noqa: E501


        :return: The keys of this ResponseDictionaryDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._keys

    @keys.setter
    def keys(self, keys):
        """Sets the keys of this ResponseDictionaryDto.


        :param keys: The keys of this ResponseDictionaryDto.  # noqa: E501
        :type: list[str]
        """

        self._keys = keys

    @property
    def values(self):
        """Gets the values of this ResponseDictionaryDto.  # noqa: E501


        :return: The values of this ResponseDictionaryDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this ResponseDictionaryDto.


        :param values: The values of this ResponseDictionaryDto.  # noqa: E501
        :type: list[str]
        """

        self._values = values

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
        if issubclass(ResponseDictionaryDto, dict):
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
        if not isinstance(other, ResponseDictionaryDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResponseDictionaryDto):
            return True

        return self.to_dict() != other.to_dict()
