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


class ExecutionSettingDefinition(object):
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
        'key': 'str',
        'display_name': 'str',
        'value_type': 'str',
        'default_value': 'str',
        'possible_values': 'list[str]'
    }

    attribute_map = {
        'key': 'Key',
        'display_name': 'DisplayName',
        'value_type': 'ValueType',
        'default_value': 'DefaultValue',
        'possible_values': 'PossibleValues'
    }

    def __init__(self, key=None, display_name=None, value_type=None, default_value=None, possible_values=None, _configuration=None):  # noqa: E501
        """ExecutionSettingDefinition - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._key = None
        self._display_name = None
        self._value_type = None
        self._default_value = None
        self._possible_values = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if display_name is not None:
            self.display_name = display_name
        if value_type is not None:
            self.value_type = value_type
        if default_value is not None:
            self.default_value = default_value
        if possible_values is not None:
            self.possible_values = possible_values

    @property
    def key(self):
        """Gets the key of this ExecutionSettingDefinition.  # noqa: E501


        :return: The key of this ExecutionSettingDefinition.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ExecutionSettingDefinition.


        :param key: The key of this ExecutionSettingDefinition.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def display_name(self):
        """Gets the display_name of this ExecutionSettingDefinition.  # noqa: E501


        :return: The display_name of this ExecutionSettingDefinition.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ExecutionSettingDefinition.


        :param display_name: The display_name of this ExecutionSettingDefinition.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def value_type(self):
        """Gets the value_type of this ExecutionSettingDefinition.  # noqa: E501


        :return: The value_type of this ExecutionSettingDefinition.  # noqa: E501
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """Sets the value_type of this ExecutionSettingDefinition.


        :param value_type: The value_type of this ExecutionSettingDefinition.  # noqa: E501
        :type: str
        """

        self._value_type = value_type

    @property
    def default_value(self):
        """Gets the default_value of this ExecutionSettingDefinition.  # noqa: E501


        :return: The default_value of this ExecutionSettingDefinition.  # noqa: E501
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this ExecutionSettingDefinition.


        :param default_value: The default_value of this ExecutionSettingDefinition.  # noqa: E501
        :type: str
        """

        self._default_value = default_value

    @property
    def possible_values(self):
        """Gets the possible_values of this ExecutionSettingDefinition.  # noqa: E501


        :return: The possible_values of this ExecutionSettingDefinition.  # noqa: E501
        :rtype: list[str]
        """
        return self._possible_values

    @possible_values.setter
    def possible_values(self, possible_values):
        """Sets the possible_values of this ExecutionSettingDefinition.


        :param possible_values: The possible_values of this ExecutionSettingDefinition.  # noqa: E501
        :type: list[str]
        """

        self._possible_values = possible_values

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
        if issubclass(ExecutionSettingDefinition, dict):
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
        if not isinstance(other, ExecutionSettingDefinition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExecutionSettingDefinition):
            return True

        return self.to_dict() != other.to_dict()
