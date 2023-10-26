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


class RaiseProcessAlertRequest(object):
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
        'process_alert': 'ProcessAlertDto'
    }

    attribute_map = {
        'process_alert': 'processAlert'
    }

    def __init__(self, process_alert=None, _configuration=None):  # noqa: E501
        """RaiseProcessAlertRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._process_alert = None
        self.discriminator = None

        self.process_alert = process_alert

    @property
    def process_alert(self):
        """Gets the process_alert of this RaiseProcessAlertRequest.  # noqa: E501


        :return: The process_alert of this RaiseProcessAlertRequest.  # noqa: E501
        :rtype: ProcessAlertDto
        """
        return self._process_alert

    @process_alert.setter
    def process_alert(self, process_alert):
        """Sets the process_alert of this RaiseProcessAlertRequest.


        :param process_alert: The process_alert of this RaiseProcessAlertRequest.  # noqa: E501
        :type: ProcessAlertDto
        """
        if self._configuration.client_side_validation and process_alert is None:
            raise ValueError("Invalid value for `process_alert`, must not be `None`")  # noqa: E501

        self._process_alert = process_alert

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
        if issubclass(RaiseProcessAlertRequest, dict):
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
        if not isinstance(other, RaiseProcessAlertRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RaiseProcessAlertRequest):
            return True

        return self.to_dict() != other.to_dict()
