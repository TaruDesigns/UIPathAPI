# coding: utf-8

"""
    UiPath.WebApi 17.0

    Orchestrator API  # noqa: E501

    OpenAPI spec version: 17.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from UIPathAPI.configuration import Configuration


class FolderNavigationContextDto(object):
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
        'id': 'int',
        'display_name': 'str',
        'is_selectable': 'bool',
        'is_personal': 'bool',
        'provision_type': 'str',
        'ancestors': 'list[SimpleFolderDto]',
        'children_page': 'list[ExtendedFolderDto]',
        'children_count': 'int'
    }

    attribute_map = {
        'id': 'Id',
        'display_name': 'DisplayName',
        'is_selectable': 'IsSelectable',
        'is_personal': 'IsPersonal',
        'provision_type': 'ProvisionType',
        'ancestors': 'Ancestors',
        'children_page': 'ChildrenPage',
        'children_count': 'ChildrenCount'
    }

    def __init__(self, id=None, display_name=None, is_selectable=None, is_personal=None, provision_type=None, ancestors=None, children_page=None, children_count=None, _configuration=None):  # noqa: E501
        """FolderNavigationContextDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._display_name = None
        self._is_selectable = None
        self._is_personal = None
        self._provision_type = None
        self._ancestors = None
        self._children_page = None
        self._children_count = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if display_name is not None:
            self.display_name = display_name
        if is_selectable is not None:
            self.is_selectable = is_selectable
        if is_personal is not None:
            self.is_personal = is_personal
        if provision_type is not None:
            self.provision_type = provision_type
        if ancestors is not None:
            self.ancestors = ancestors
        if children_page is not None:
            self.children_page = children_page
        if children_count is not None:
            self.children_count = children_count

    @property
    def id(self):
        """Gets the id of this FolderNavigationContextDto.  # noqa: E501


        :return: The id of this FolderNavigationContextDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FolderNavigationContextDto.


        :param id: The id of this FolderNavigationContextDto.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def display_name(self):
        """Gets the display_name of this FolderNavigationContextDto.  # noqa: E501


        :return: The display_name of this FolderNavigationContextDto.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this FolderNavigationContextDto.


        :param display_name: The display_name of this FolderNavigationContextDto.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def is_selectable(self):
        """Gets the is_selectable of this FolderNavigationContextDto.  # noqa: E501


        :return: The is_selectable of this FolderNavigationContextDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_selectable

    @is_selectable.setter
    def is_selectable(self, is_selectable):
        """Sets the is_selectable of this FolderNavigationContextDto.


        :param is_selectable: The is_selectable of this FolderNavigationContextDto.  # noqa: E501
        :type: bool
        """

        self._is_selectable = is_selectable

    @property
    def is_personal(self):
        """Gets the is_personal of this FolderNavigationContextDto.  # noqa: E501


        :return: The is_personal of this FolderNavigationContextDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_personal

    @is_personal.setter
    def is_personal(self, is_personal):
        """Sets the is_personal of this FolderNavigationContextDto.


        :param is_personal: The is_personal of this FolderNavigationContextDto.  # noqa: E501
        :type: bool
        """

        self._is_personal = is_personal

    @property
    def provision_type(self):
        """Gets the provision_type of this FolderNavigationContextDto.  # noqa: E501


        :return: The provision_type of this FolderNavigationContextDto.  # noqa: E501
        :rtype: str
        """
        return self._provision_type

    @provision_type.setter
    def provision_type(self, provision_type):
        """Sets the provision_type of this FolderNavigationContextDto.


        :param provision_type: The provision_type of this FolderNavigationContextDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["Manual", "Automatic"]  # noqa: E501
        if (self._configuration.client_side_validation and
                provision_type not in allowed_values):
            raise ValueError(
                "Invalid value for `provision_type` ({0}), must be one of {1}"  # noqa: E501
                .format(provision_type, allowed_values)
            )

        self._provision_type = provision_type

    @property
    def ancestors(self):
        """Gets the ancestors of this FolderNavigationContextDto.  # noqa: E501


        :return: The ancestors of this FolderNavigationContextDto.  # noqa: E501
        :rtype: list[SimpleFolderDto]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """Sets the ancestors of this FolderNavigationContextDto.


        :param ancestors: The ancestors of this FolderNavigationContextDto.  # noqa: E501
        :type: list[SimpleFolderDto]
        """

        self._ancestors = ancestors

    @property
    def children_page(self):
        """Gets the children_page of this FolderNavigationContextDto.  # noqa: E501


        :return: The children_page of this FolderNavigationContextDto.  # noqa: E501
        :rtype: list[ExtendedFolderDto]
        """
        return self._children_page

    @children_page.setter
    def children_page(self, children_page):
        """Sets the children_page of this FolderNavigationContextDto.


        :param children_page: The children_page of this FolderNavigationContextDto.  # noqa: E501
        :type: list[ExtendedFolderDto]
        """

        self._children_page = children_page

    @property
    def children_count(self):
        """Gets the children_count of this FolderNavigationContextDto.  # noqa: E501


        :return: The children_count of this FolderNavigationContextDto.  # noqa: E501
        :rtype: int
        """
        return self._children_count

    @children_count.setter
    def children_count(self, children_count):
        """Sets the children_count of this FolderNavigationContextDto.


        :param children_count: The children_count of this FolderNavigationContextDto.  # noqa: E501
        :type: int
        """

        self._children_count = children_count

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
        if issubclass(FolderNavigationContextDto, dict):
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
        if not isinstance(other, FolderNavigationContextDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FolderNavigationContextDto):
            return True

        return self.to_dict() != other.to_dict()
