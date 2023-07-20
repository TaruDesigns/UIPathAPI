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


class ExecutionSettingsConfiguration(object):
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
        'scope': 'str',
        'configuration': 'list[ExecutionSettingDefinition]'
    }

    attribute_map = {
        'scope': 'Scope',
        'configuration': 'Configuration'
    }

    def __init__(self, scope=None, configuration=None, _configuration=None):  # noqa: E501
        """ExecutionSettingsConfiguration - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._scope = None
        self._configuration = None
        self.discriminator = None

        if scope is not None:
            self.scope = scope
        if configuration is not None:
            self.configuration = configuration

    @property
    def scope(self):
        """Gets the scope of this ExecutionSettingsConfiguration.  # noqa: E501


        :return: The scope of this ExecutionSettingsConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this ExecutionSettingsConfiguration.


        :param scope: The scope of this ExecutionSettingsConfiguration.  # noqa: E501
        :type: str
        """
        allowed_values = ["Global", "Robot"]  # noqa: E501
        if (self._configuration.client_side_validation and
                scope not in allowed_values):
            raise ValueError(
                "Invalid value for `scope` ({0}), must be one of {1}"  # noqa: E501
                .format(scope, allowed_values)
            )

        self._scope = scope

    @property
    def configuration(self):
        """Gets the configuration of this ExecutionSettingsConfiguration.  # noqa: E501


        :return: The configuration of this ExecutionSettingsConfiguration.  # noqa: E501
        :rtype: list[ExecutionSettingDefinition]
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this ExecutionSettingsConfiguration.


        :param configuration: The configuration of this ExecutionSettingsConfiguration.  # noqa: E501
        :type: list[ExecutionSettingDefinition]
        """

        self._configuration = configuration

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
        if issubclass(ExecutionSettingsConfiguration, dict):
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
        if not isinstance(other, ExecutionSettingsConfiguration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExecutionSettingsConfiguration):
            return True

        return self.to_dict() != other.to_dict()
