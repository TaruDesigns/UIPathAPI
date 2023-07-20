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


class FolderAssignmentsDto(object):
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
        'folder': 'SimpleFolderDto',
        'roles': 'list[RoleUsersDto]'
    }

    attribute_map = {
        'folder': 'Folder',
        'roles': 'Roles'
    }

    def __init__(self, folder=None, roles=None, _configuration=None):  # noqa: E501
        """FolderAssignmentsDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._folder = None
        self._roles = None
        self.discriminator = None

        if folder is not None:
            self.folder = folder
        if roles is not None:
            self.roles = roles

    @property
    def folder(self):
        """Gets the folder of this FolderAssignmentsDto.  # noqa: E501


        :return: The folder of this FolderAssignmentsDto.  # noqa: E501
        :rtype: SimpleFolderDto
        """
        return self._folder

    @folder.setter
    def folder(self, folder):
        """Sets the folder of this FolderAssignmentsDto.


        :param folder: The folder of this FolderAssignmentsDto.  # noqa: E501
        :type: SimpleFolderDto
        """

        self._folder = folder

    @property
    def roles(self):
        """Gets the roles of this FolderAssignmentsDto.  # noqa: E501


        :return: The roles of this FolderAssignmentsDto.  # noqa: E501
        :rtype: list[RoleUsersDto]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this FolderAssignmentsDto.


        :param roles: The roles of this FolderAssignmentsDto.  # noqa: E501
        :type: list[RoleUsersDto]
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
        if issubclass(FolderAssignmentsDto, dict):
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
        if not isinstance(other, FolderAssignmentsDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FolderAssignmentsDto):
            return True

        return self.to_dict() != other.to_dict()