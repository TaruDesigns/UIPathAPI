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


class ProcessSetEnabledRequest(object):
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
        'enabled': 'bool',
        'multistatus_enabled': 'bool',
        'schedule_ids': 'list[int]'
    }

    attribute_map = {
        'enabled': 'enabled',
        'multistatus_enabled': 'multistatusEnabled',
        'schedule_ids': 'scheduleIds'
    }

    def __init__(self, enabled=None, multistatus_enabled=None, schedule_ids=None, _configuration=None):  # noqa: E501
        """ProcessSetEnabledRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._enabled = None
        self._multistatus_enabled = None
        self._schedule_ids = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if multistatus_enabled is not None:
            self.multistatus_enabled = multistatus_enabled
        if schedule_ids is not None:
            self.schedule_ids = schedule_ids

    @property
    def enabled(self):
        """Gets the enabled of this ProcessSetEnabledRequest.  # noqa: E501


        :return: The enabled of this ProcessSetEnabledRequest.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ProcessSetEnabledRequest.


        :param enabled: The enabled of this ProcessSetEnabledRequest.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def multistatus_enabled(self):
        """Gets the multistatus_enabled of this ProcessSetEnabledRequest.  # noqa: E501


        :return: The multistatus_enabled of this ProcessSetEnabledRequest.  # noqa: E501
        :rtype: bool
        """
        return self._multistatus_enabled

    @multistatus_enabled.setter
    def multistatus_enabled(self, multistatus_enabled):
        """Sets the multistatus_enabled of this ProcessSetEnabledRequest.


        :param multistatus_enabled: The multistatus_enabled of this ProcessSetEnabledRequest.  # noqa: E501
        :type: bool
        """

        self._multistatus_enabled = multistatus_enabled

    @property
    def schedule_ids(self):
        """Gets the schedule_ids of this ProcessSetEnabledRequest.  # noqa: E501


        :return: The schedule_ids of this ProcessSetEnabledRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._schedule_ids

    @schedule_ids.setter
    def schedule_ids(self, schedule_ids):
        """Sets the schedule_ids of this ProcessSetEnabledRequest.


        :param schedule_ids: The schedule_ids of this ProcessSetEnabledRequest.  # noqa: E501
        :type: list[int]
        """

        self._schedule_ids = schedule_ids

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
        if issubclass(ProcessSetEnabledRequest, dict):
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
        if not isinstance(other, ProcessSetEnabledRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProcessSetEnabledRequest):
            return True

        return self.to_dict() != other.to_dict()
