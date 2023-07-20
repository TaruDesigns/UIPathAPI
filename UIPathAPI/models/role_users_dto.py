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


class RoleUsersDto(object):
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
        'name': 'str',
        'users': 'list[SimpleUserEntityDto]',
        'id': 'int'
    }

    attribute_map = {
        'name': 'Name',
        'users': 'Users',
        'id': 'Id'
    }

    def __init__(self, name=None, users=None, id=None, _configuration=None):  # noqa: E501
        """RoleUsersDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._users = None
        self._id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if users is not None:
            self.users = users
        if id is not None:
            self.id = id

    @property
    def name(self):
        """Gets the name of this RoleUsersDto.  # noqa: E501


        :return: The name of this RoleUsersDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RoleUsersDto.


        :param name: The name of this RoleUsersDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def users(self):
        """Gets the users of this RoleUsersDto.  # noqa: E501


        :return: The users of this RoleUsersDto.  # noqa: E501
        :rtype: list[SimpleUserEntityDto]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this RoleUsersDto.


        :param users: The users of this RoleUsersDto.  # noqa: E501
        :type: list[SimpleUserEntityDto]
        """

        self._users = users

    @property
    def id(self):
        """Gets the id of this RoleUsersDto.  # noqa: E501


        :return: The id of this RoleUsersDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RoleUsersDto.


        :param id: The id of this RoleUsersDto.  # noqa: E501
        :type: int
        """

        self._id = id

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
        if issubclass(RoleUsersDto, dict):
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
        if not isinstance(other, RoleUsersDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RoleUsersDto):
            return True

        return self.to_dict() != other.to_dict()