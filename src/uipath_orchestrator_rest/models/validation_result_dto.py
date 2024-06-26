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


class ValidationResultDto(object):
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
        'is_valid': 'bool',
        'errors': 'list[str]',
        'error_codes': 'list[str]'
    }

    attribute_map = {
        'is_valid': 'IsValid',
        'errors': 'Errors',
        'error_codes': 'ErrorCodes'
    }

    def __init__(self, is_valid=None, errors=None, error_codes=None, _configuration=None):  # noqa: E501
        """ValidationResultDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._is_valid = None
        self._errors = None
        self._error_codes = None
        self.discriminator = None

        if is_valid is not None:
            self.is_valid = is_valid
        if errors is not None:
            self.errors = errors
        if error_codes is not None:
            self.error_codes = error_codes

    @property
    def is_valid(self):
        """Gets the is_valid of this ValidationResultDto.  # noqa: E501


        :return: The is_valid of this ValidationResultDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_valid

    @is_valid.setter
    def is_valid(self, is_valid):
        """Sets the is_valid of this ValidationResultDto.


        :param is_valid: The is_valid of this ValidationResultDto.  # noqa: E501
        :type: bool
        """

        self._is_valid = is_valid

    @property
    def errors(self):
        """Gets the errors of this ValidationResultDto.  # noqa: E501


        :return: The errors of this ValidationResultDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this ValidationResultDto.


        :param errors: The errors of this ValidationResultDto.  # noqa: E501
        :type: list[str]
        """

        self._errors = errors

    @property
    def error_codes(self):
        """Gets the error_codes of this ValidationResultDto.  # noqa: E501


        :return: The error_codes of this ValidationResultDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._error_codes

    @error_codes.setter
    def error_codes(self, error_codes):
        """Sets the error_codes of this ValidationResultDto.


        :param error_codes: The error_codes of this ValidationResultDto.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["RobotNotAssignedToFolder", "RobotNotFound", "RobotNoCredentials", "RobotBusy", "RobotConcurrencyLimit", "RobotNoMatchingUsernames", "TemplateNoRuntime", "TemplateNoHostsAvailable", "TemplateNoLicense", "TemplateFullCapacity", "TemplateNotAssignedToFolder", "TemplateMaintenanceMode", "DynamicJobAccountCredentialsInvalid", "DynamicJobForegroundAutomationTypeInvalid", "DynamicJobBackgroundAutomationTypeInvalid", "DynamicJobWindowsTargetFrameworkInvalid", "DynamicJobCrossPlatformTargetFrameworkInvalid", "DynamicJobConnectedMachinesInvalid", "DynamicJobConnectedMachinesUserCredentialsInvalid", "DynamicJobConnectedMachinesCrossPlatformRobotVersionInvalid", "DynamicJobConnectedMachinesWindowsRobotVersionInvalid"]  # noqa: E501
        if (self._configuration.client_side_validation and
                not set(error_codes).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `error_codes` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(error_codes) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._error_codes = error_codes

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
        if issubclass(ValidationResultDto, dict):
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
        if not isinstance(other, ValidationResultDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ValidationResultDto):
            return True

        return self.to_dict() != other.to_dict()
