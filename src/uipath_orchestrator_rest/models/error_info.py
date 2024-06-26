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


class ErrorInfo(object):
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
        'code': 'int',
        'message': 'str',
        'details': 'str',
        'validation_errors': 'list[ValidationErrorInfo]'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'details': 'details',
        'validation_errors': 'validationErrors'
    }

    def __init__(self, code=None, message=None, details=None, validation_errors=None, _configuration=None):  # noqa: E501
        """ErrorInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._code = None
        self._message = None
        self._details = None
        self._validation_errors = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if details is not None:
            self.details = details
        if validation_errors is not None:
            self.validation_errors = validation_errors

    @property
    def code(self):
        """Gets the code of this ErrorInfo.  # noqa: E501


        :return: The code of this ErrorInfo.  # noqa: E501
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ErrorInfo.


        :param code: The code of this ErrorInfo.  # noqa: E501
        :type: int
        """

        self._code = code

    @property
    def message(self):
        """Gets the message of this ErrorInfo.  # noqa: E501


        :return: The message of this ErrorInfo.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ErrorInfo.


        :param message: The message of this ErrorInfo.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def details(self):
        """Gets the details of this ErrorInfo.  # noqa: E501


        :return: The details of this ErrorInfo.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this ErrorInfo.


        :param details: The details of this ErrorInfo.  # noqa: E501
        :type: str
        """

        self._details = details

    @property
    def validation_errors(self):
        """Gets the validation_errors of this ErrorInfo.  # noqa: E501


        :return: The validation_errors of this ErrorInfo.  # noqa: E501
        :rtype: list[ValidationErrorInfo]
        """
        return self._validation_errors

    @validation_errors.setter
    def validation_errors(self, validation_errors):
        """Sets the validation_errors of this ErrorInfo.


        :param validation_errors: The validation_errors of this ErrorInfo.  # noqa: E501
        :type: list[ValidationErrorInfo]
        """

        self._validation_errors = validation_errors

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
        if issubclass(ErrorInfo, dict):
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
        if not isinstance(other, ErrorInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ErrorInfo):
            return True

        return self.to_dict() != other.to_dict()
