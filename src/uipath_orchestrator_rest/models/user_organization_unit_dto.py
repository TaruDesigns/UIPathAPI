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


class UserOrganizationUnitDto(object):
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
        'user_name': 'str',
        'organization_unit_id': 'int',
        'organization_unit_name': 'str',
        'id': 'int'
    }

    attribute_map = {
        'user_id': 'userId',
        'user_name': 'userName',
        'organization_unit_id': 'organizationUnitId',
        'organization_unit_name': 'organizationUnitName',
        'id': 'id'
    }

    def __init__(self, user_id=None, user_name=None, organization_unit_id=None, organization_unit_name=None, id=None, _configuration=None):  # noqa: E501
        """UserOrganizationUnitDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._user_id = None
        self._user_name = None
        self._organization_unit_id = None
        self._organization_unit_name = None
        self._id = None
        self.discriminator = None

        if user_id is not None:
            self.user_id = user_id
        if user_name is not None:
            self.user_name = user_name
        if organization_unit_id is not None:
            self.organization_unit_id = organization_unit_id
        if organization_unit_name is not None:
            self.organization_unit_name = organization_unit_name
        if id is not None:
            self.id = id

    @property
    def user_id(self):
        """Gets the user_id of this UserOrganizationUnitDto.  # noqa: E501

        The Id of the user  # noqa: E501

        :return: The user_id of this UserOrganizationUnitDto.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this UserOrganizationUnitDto.

        The Id of the user  # noqa: E501

        :param user_id: The user_id of this UserOrganizationUnitDto.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def user_name(self):
        """Gets the user_name of this UserOrganizationUnitDto.  # noqa: E501

        The name of the user  # noqa: E501

        :return: The user_name of this UserOrganizationUnitDto.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this UserOrganizationUnitDto.

        The name of the user  # noqa: E501

        :param user_name: The user_name of this UserOrganizationUnitDto.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def organization_unit_id(self):
        """Gets the organization_unit_id of this UserOrganizationUnitDto.  # noqa: E501

        The Id of the organization unit  # noqa: E501

        :return: The organization_unit_id of this UserOrganizationUnitDto.  # noqa: E501
        :rtype: int
        """
        return self._organization_unit_id

    @organization_unit_id.setter
    def organization_unit_id(self, organization_unit_id):
        """Sets the organization_unit_id of this UserOrganizationUnitDto.

        The Id of the organization unit  # noqa: E501

        :param organization_unit_id: The organization_unit_id of this UserOrganizationUnitDto.  # noqa: E501
        :type: int
        """

        self._organization_unit_id = organization_unit_id

    @property
    def organization_unit_name(self):
        """Gets the organization_unit_name of this UserOrganizationUnitDto.  # noqa: E501

        The name of the organization unit.  # noqa: E501

        :return: The organization_unit_name of this UserOrganizationUnitDto.  # noqa: E501
        :rtype: str
        """
        return self._organization_unit_name

    @organization_unit_name.setter
    def organization_unit_name(self, organization_unit_name):
        """Sets the organization_unit_name of this UserOrganizationUnitDto.

        The name of the organization unit.  # noqa: E501

        :param organization_unit_name: The organization_unit_name of this UserOrganizationUnitDto.  # noqa: E501
        :type: str
        """

        self._organization_unit_name = organization_unit_name

    @property
    def id(self):
        """Gets the id of this UserOrganizationUnitDto.  # noqa: E501


        :return: The id of this UserOrganizationUnitDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserOrganizationUnitDto.


        :param id: The id of this UserOrganizationUnitDto.  # noqa: E501
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
        if issubclass(UserOrganizationUnitDto, dict):
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
        if not isinstance(other, UserOrganizationUnitDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserOrganizationUnitDto):
            return True

        return self.to_dict() != other.to_dict()