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


class AjaxResponse(object):
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
        'result': 'object',
        'target_url': 'str',
        'success': 'bool',
        'error': 'ErrorInfo',
        'un_authorized_request': 'bool',
        'abp': 'bool'
    }

    attribute_map = {
        'result': 'result',
        'target_url': 'targetUrl',
        'success': 'success',
        'error': 'error',
        'un_authorized_request': 'unAuthorizedRequest',
        'abp': '__abp'
    }

    def __init__(self, result=None, target_url=None, success=None, error=None, un_authorized_request=None, abp=None, _configuration=None):  # noqa: E501
        """AjaxResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._result = None
        self._target_url = None
        self._success = None
        self._error = None
        self._un_authorized_request = None
        self._abp = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if target_url is not None:
            self.target_url = target_url
        if success is not None:
            self.success = success
        if error is not None:
            self.error = error
        if un_authorized_request is not None:
            self.un_authorized_request = un_authorized_request
        if abp is not None:
            self.abp = abp

    @property
    def result(self):
        """Gets the result of this AjaxResponse.  # noqa: E501


        :return: The result of this AjaxResponse.  # noqa: E501
        :rtype: object
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this AjaxResponse.


        :param result: The result of this AjaxResponse.  # noqa: E501
        :type: object
        """

        self._result = result

    @property
    def target_url(self):
        """Gets the target_url of this AjaxResponse.  # noqa: E501


        :return: The target_url of this AjaxResponse.  # noqa: E501
        :rtype: str
        """
        return self._target_url

    @target_url.setter
    def target_url(self, target_url):
        """Sets the target_url of this AjaxResponse.


        :param target_url: The target_url of this AjaxResponse.  # noqa: E501
        :type: str
        """

        self._target_url = target_url

    @property
    def success(self):
        """Gets the success of this AjaxResponse.  # noqa: E501


        :return: The success of this AjaxResponse.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this AjaxResponse.


        :param success: The success of this AjaxResponse.  # noqa: E501
        :type: bool
        """

        self._success = success

    @property
    def error(self):
        """Gets the error of this AjaxResponse.  # noqa: E501


        :return: The error of this AjaxResponse.  # noqa: E501
        :rtype: ErrorInfo
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this AjaxResponse.


        :param error: The error of this AjaxResponse.  # noqa: E501
        :type: ErrorInfo
        """

        self._error = error

    @property
    def un_authorized_request(self):
        """Gets the un_authorized_request of this AjaxResponse.  # noqa: E501


        :return: The un_authorized_request of this AjaxResponse.  # noqa: E501
        :rtype: bool
        """
        return self._un_authorized_request

    @un_authorized_request.setter
    def un_authorized_request(self, un_authorized_request):
        """Sets the un_authorized_request of this AjaxResponse.


        :param un_authorized_request: The un_authorized_request of this AjaxResponse.  # noqa: E501
        :type: bool
        """

        self._un_authorized_request = un_authorized_request

    @property
    def abp(self):
        """Gets the abp of this AjaxResponse.  # noqa: E501


        :return: The abp of this AjaxResponse.  # noqa: E501
        :rtype: bool
        """
        return self._abp

    @abp.setter
    def abp(self, abp):
        """Sets the abp of this AjaxResponse.


        :param abp: The abp of this AjaxResponse.  # noqa: E501
        :type: bool
        """

        self._abp = abp

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
        if issubclass(AjaxResponse, dict):
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
        if not isinstance(other, AjaxResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AjaxResponse):
            return True

        return self.to_dict() != other.to_dict()
