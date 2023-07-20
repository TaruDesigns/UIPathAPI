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


class DirectoryPermissionDto(object):
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
        'directory_group': 'str',
        'organization_units': 'list[UserOrganizationUnitDto]',
        'roles': 'list[LightRoleDto]'
    }

    attribute_map = {
        'directory_group': 'directoryGroup',
        'organization_units': 'organizationUnits',
        'roles': 'roles'
    }

    def __init__(self, directory_group=None, organization_units=None, roles=None, _configuration=None):  # noqa: E501
        """DirectoryPermissionDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._directory_group = None
        self._organization_units = None
        self._roles = None
        self.discriminator = None

        if directory_group is not None:
            self.directory_group = directory_group
        if organization_units is not None:
            self.organization_units = organization_units
        if roles is not None:
            self.roles = roles

    @property
    def directory_group(self):
        """Gets the directory_group of this DirectoryPermissionDto.  # noqa: E501


        :return: The directory_group of this DirectoryPermissionDto.  # noqa: E501
        :rtype: str
        """
        return self._directory_group

    @directory_group.setter
    def directory_group(self, directory_group):
        """Sets the directory_group of this DirectoryPermissionDto.


        :param directory_group: The directory_group of this DirectoryPermissionDto.  # noqa: E501
        :type: str
        """

        self._directory_group = directory_group

    @property
    def organization_units(self):
        """Gets the organization_units of this DirectoryPermissionDto.  # noqa: E501


        :return: The organization_units of this DirectoryPermissionDto.  # noqa: E501
        :rtype: list[UserOrganizationUnitDto]
        """
        return self._organization_units

    @organization_units.setter
    def organization_units(self, organization_units):
        """Sets the organization_units of this DirectoryPermissionDto.


        :param organization_units: The organization_units of this DirectoryPermissionDto.  # noqa: E501
        :type: list[UserOrganizationUnitDto]
        """

        self._organization_units = organization_units

    @property
    def roles(self):
        """Gets the roles of this DirectoryPermissionDto.  # noqa: E501


        :return: The roles of this DirectoryPermissionDto.  # noqa: E501
        :rtype: list[LightRoleDto]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this DirectoryPermissionDto.


        :param roles: The roles of this DirectoryPermissionDto.  # noqa: E501
        :type: list[LightRoleDto]
        """

        self._roles = roles

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
        if issubclass(DirectoryPermissionDto, dict):
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
        if not isinstance(other, DirectoryPermissionDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DirectoryPermissionDto):
            return True

        return self.to_dict() != other.to_dict()