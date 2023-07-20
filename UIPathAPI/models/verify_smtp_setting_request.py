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


class VerifySmtpSettingRequest(object):
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
        'send_to': 'str',
        'smtp_setting_model': 'SmtpSettingModel'
    }

    attribute_map = {
        'send_to': 'sendTo',
        'smtp_setting_model': 'smtpSettingModel'
    }

    def __init__(self, send_to=None, smtp_setting_model=None, _configuration=None):  # noqa: E501
        """VerifySmtpSettingRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._send_to = None
        self._smtp_setting_model = None
        self.discriminator = None

        self.send_to = send_to
        if smtp_setting_model is not None:
            self.smtp_setting_model = smtp_setting_model

    @property
    def send_to(self):
        """Gets the send_to of this VerifySmtpSettingRequest.  # noqa: E501


        :return: The send_to of this VerifySmtpSettingRequest.  # noqa: E501
        :rtype: str
        """
        return self._send_to

    @send_to.setter
    def send_to(self, send_to):
        """Sets the send_to of this VerifySmtpSettingRequest.


        :param send_to: The send_to of this VerifySmtpSettingRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and send_to is None:
            raise ValueError("Invalid value for `send_to`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                send_to is not None and len(send_to) < 1):
            raise ValueError("Invalid value for `send_to`, length must be greater than or equal to `1`")  # noqa: E501

        self._send_to = send_to

    @property
    def smtp_setting_model(self):
        """Gets the smtp_setting_model of this VerifySmtpSettingRequest.  # noqa: E501


        :return: The smtp_setting_model of this VerifySmtpSettingRequest.  # noqa: E501
        :rtype: SmtpSettingModel
        """
        return self._smtp_setting_model

    @smtp_setting_model.setter
    def smtp_setting_model(self, smtp_setting_model):
        """Sets the smtp_setting_model of this VerifySmtpSettingRequest.


        :param smtp_setting_model: The smtp_setting_model of this VerifySmtpSettingRequest.  # noqa: E501
        :type: SmtpSettingModel
        """

        self._smtp_setting_model = smtp_setting_model

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
        if issubclass(VerifySmtpSettingRequest, dict):
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
        if not isinstance(other, VerifySmtpSettingRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VerifySmtpSettingRequest):
            return True

        return self.to_dict() != other.to_dict()
