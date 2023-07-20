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


class HostSetTenantLicenseRequest(object):
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
        'license': 'HostLicensePerTenantDto'
    }

    attribute_map = {
        'license': 'license'
    }

    def __init__(self, license=None, _configuration=None):  # noqa: E501
        """HostSetTenantLicenseRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._license = None
        self.discriminator = None

        self.license = license

    @property
    def license(self):
        """Gets the license of this HostSetTenantLicenseRequest.  # noqa: E501


        :return: The license of this HostSetTenantLicenseRequest.  # noqa: E501
        :rtype: HostLicensePerTenantDto
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this HostSetTenantLicenseRequest.


        :param license: The license of this HostSetTenantLicenseRequest.  # noqa: E501
        :type: HostLicensePerTenantDto
        """
        if self._configuration.client_side_validation and license is None:
            raise ValueError("Invalid value for `license`, must not be `None`")  # noqa: E501

        self._license = license

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
        if issubclass(HostSetTenantLicenseRequest, dict):
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
        if not isinstance(other, HostSetTenantLicenseRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HostSetTenantLicenseRequest):
            return True

        return self.to_dict() != other.to_dict()
