# coding: utf-8

"""
    UiPath.WebApi 18.0

    Orchestrator API  # noqa: E501

    OpenAPI spec version: 18.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from uipath_orchestrator_rest.configuration import Configuration


class UpdateSettingsDto(object):
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
        'update_server_source': 'str',
        'update_server_url': 'str',
        'polling_interval': 'int'
    }

    attribute_map = {
        'update_server_source': 'UpdateServerSource',
        'update_server_url': 'UpdateServerUrl',
        'polling_interval': 'PollingInterval'
    }

    def __init__(self, update_server_source=None, update_server_url=None, polling_interval=None, _configuration=None):  # noqa: E501
        """UpdateSettingsDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._update_server_source = None
        self._update_server_url = None
        self._polling_interval = None
        self.discriminator = None

        if update_server_source is not None:
            self.update_server_source = update_server_source
        if update_server_url is not None:
            self.update_server_url = update_server_url
        if polling_interval is not None:
            self.polling_interval = polling_interval

    @property
    def update_server_source(self):
        """Gets the update_server_source of this UpdateSettingsDto.  # noqa: E501


        :return: The update_server_source of this UpdateSettingsDto.  # noqa: E501
        :rtype: str
        """
        return self._update_server_source

    @update_server_source.setter
    def update_server_source(self, update_server_source):
        """Sets the update_server_source of this UpdateSettingsDto.


        :param update_server_source: The update_server_source of this UpdateSettingsDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["Orchestrator"]  # noqa: E501
        if (self._configuration.client_side_validation and
                update_server_source not in allowed_values):
            raise ValueError(
                "Invalid value for `update_server_source` ({0}), must be one of {1}"  # noqa: E501
                .format(update_server_source, allowed_values)
            )

        self._update_server_source = update_server_source

    @property
    def update_server_url(self):
        """Gets the update_server_url of this UpdateSettingsDto.  # noqa: E501


        :return: The update_server_url of this UpdateSettingsDto.  # noqa: E501
        :rtype: str
        """
        return self._update_server_url

    @update_server_url.setter
    def update_server_url(self, update_server_url):
        """Sets the update_server_url of this UpdateSettingsDto.


        :param update_server_url: The update_server_url of this UpdateSettingsDto.  # noqa: E501
        :type: str
        """

        self._update_server_url = update_server_url

    @property
    def polling_interval(self):
        """Gets the polling_interval of this UpdateSettingsDto.  # noqa: E501


        :return: The polling_interval of this UpdateSettingsDto.  # noqa: E501
        :rtype: int
        """
        return self._polling_interval

    @polling_interval.setter
    def polling_interval(self, polling_interval):
        """Sets the polling_interval of this UpdateSettingsDto.


        :param polling_interval: The polling_interval of this UpdateSettingsDto.  # noqa: E501
        :type: int
        """

        self._polling_interval = polling_interval

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
        if issubclass(UpdateSettingsDto, dict):
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
        if not isinstance(other, UpdateSettingsDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateSettingsDto):
            return True

        return self.to_dict() != other.to_dict()
