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


class UserPermissionsCollection(object):
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
        'user_id': 'int',
        'permissions': 'list[str]'
    }

    attribute_map = {
        'user_id': 'UserId',
        'permissions': 'Permissions'
    }

    def __init__(self, user_id=None, permissions=None, _configuration=None):  # noqa: E501
        """UserPermissionsCollection - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._user_id = None
        self._permissions = None
        self.discriminator = None

        if user_id is not None:
            self.user_id = user_id
        if permissions is not None:
            self.permissions = permissions

    @property
    def user_id(self):
        """Gets the user_id of this UserPermissionsCollection.  # noqa: E501

        The Id of the user associated with the permissions.  # noqa: E501

        :return: The user_id of this UserPermissionsCollection.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this UserPermissionsCollection.

        The Id of the user associated with the permissions.  # noqa: E501

        :param user_id: The user_id of this UserPermissionsCollection.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def permissions(self):
        """Gets the permissions of this UserPermissionsCollection.  # noqa: E501

        The collection of names of the permissions the user is associated with.  # noqa: E501

        :return: The permissions of this UserPermissionsCollection.  # noqa: E501
        :rtype: list[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this UserPermissionsCollection.

        The collection of names of the permissions the user is associated with.  # noqa: E501

        :param permissions: The permissions of this UserPermissionsCollection.  # noqa: E501
        :type: list[str]
        """

        self._permissions = permissions

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
        if issubclass(UserPermissionsCollection, dict):
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
        if not isinstance(other, UserPermissionsCollection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserPermissionsCollection):
            return True

        return self.to_dict() != other.to_dict()
