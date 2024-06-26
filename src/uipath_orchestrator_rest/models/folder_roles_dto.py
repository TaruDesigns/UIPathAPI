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


class FolderRolesDto(object):
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
        'folder_id': 'int',
        'role_ids': 'list[int]'
    }

    attribute_map = {
        'folder_id': 'FolderId',
        'role_ids': 'RoleIds'
    }

    def __init__(self, folder_id=None, role_ids=None, _configuration=None):  # noqa: E501
        """FolderRolesDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._folder_id = None
        self._role_ids = None
        self.discriminator = None

        if folder_id is not None:
            self.folder_id = folder_id
        if role_ids is not None:
            self.role_ids = role_ids

    @property
    def folder_id(self):
        """Gets the folder_id of this FolderRolesDto.  # noqa: E501


        :return: The folder_id of this FolderRolesDto.  # noqa: E501
        :rtype: int
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        """Sets the folder_id of this FolderRolesDto.


        :param folder_id: The folder_id of this FolderRolesDto.  # noqa: E501
        :type: int
        """

        self._folder_id = folder_id

    @property
    def role_ids(self):
        """Gets the role_ids of this FolderRolesDto.  # noqa: E501


        :return: The role_ids of this FolderRolesDto.  # noqa: E501
        :rtype: list[int]
        """
        return self._role_ids

    @role_ids.setter
    def role_ids(self, role_ids):
        """Sets the role_ids of this FolderRolesDto.


        :param role_ids: The role_ids of this FolderRolesDto.  # noqa: E501
        :type: list[int]
        """

        self._role_ids = role_ids

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
        if issubclass(FolderRolesDto, dict):
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
        if not isinstance(other, FolderRolesDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FolderRolesDto):
            return True

        return self.to_dict() != other.to_dict()
