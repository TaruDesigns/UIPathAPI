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


class LicenseResultDto(object):
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
        'is_success': 'bool',
        'error_code': 'str',
        'error_message': 'str'
    }

    attribute_map = {
        'is_success': 'isSuccess',
        'error_code': 'errorCode',
        'error_message': 'errorMessage'
    }

    def __init__(self, is_success=None, error_code=None, error_message=None, _configuration=None):  # noqa: E501
        """LicenseResultDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._is_success = None
        self._error_code = None
        self._error_message = None
        self.discriminator = None

        if is_success is not None:
            self.is_success = is_success
        if error_code is not None:
            self.error_code = error_code
        if error_message is not None:
            self.error_message = error_message

    @property
    def is_success(self):
        """Gets the is_success of this LicenseResultDto.  # noqa: E501


        :return: The is_success of this LicenseResultDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        """Sets the is_success of this LicenseResultDto.


        :param is_success: The is_success of this LicenseResultDto.  # noqa: E501
        :type: bool
        """

        self._is_success = is_success

    @property
    def error_code(self):
        """Gets the error_code of this LicenseResultDto.  # noqa: E501


        :return: The error_code of this LicenseResultDto.  # noqa: E501
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this LicenseResultDto.


        :param error_code: The error_code of this LicenseResultDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["NoLicense", "LicenseExpired", "LicenseUnregistered", "NoAvailableLicenses", "NotEnoughAvailableSlots", "NotEnoughRuntimeLicenses", "LicenseIsAlreadyInUse", "InvalidRequest", "SlotsExceedLicenseLimit", "RuntimeDisabled", "ExternalNotSupported", "UsageExceedsLicenseLimit", "LicenseNotCompatible"]  # noqa: E501
        if (self._configuration.client_side_validation and
                error_code not in allowed_values):
            raise ValueError(
                "Invalid value for `error_code` ({0}), must be one of {1}"  # noqa: E501
                .format(error_code, allowed_values)
            )

        self._error_code = error_code

    @property
    def error_message(self):
        """Gets the error_message of this LicenseResultDto.  # noqa: E501


        :return: The error_message of this LicenseResultDto.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this LicenseResultDto.


        :param error_message: The error_message of this LicenseResultDto.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

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
        if issubclass(LicenseResultDto, dict):
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
        if not isinstance(other, LicenseResultDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LicenseResultDto):
            return True

        return self.to_dict() != other.to_dict()
