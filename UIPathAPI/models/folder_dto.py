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


class FolderDto(object):
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
        'key': 'str',
        'display_name': 'str',
        'fully_qualified_name': 'str',
        'description': 'str',
        'folder_type': 'str',
        'is_personal': 'bool',
        'provision_type': 'str',
        'permission_model': 'str',
        'parent_id': 'int',
        'parent_key': 'str',
        'feed_type': 'str',
        'id': 'int'
    }

    attribute_map = {
        'key': 'Key',
        'display_name': 'DisplayName',
        'fully_qualified_name': 'FullyQualifiedName',
        'description': 'Description',
        'folder_type': 'FolderType',
        'is_personal': 'IsPersonal',
        'provision_type': 'ProvisionType',
        'permission_model': 'PermissionModel',
        'parent_id': 'ParentId',
        'parent_key': 'ParentKey',
        'feed_type': 'FeedType',
        'id': 'Id'
    }

    def __init__(self, key=None, display_name=None, fully_qualified_name=None, description=None, folder_type=None, is_personal=None, provision_type=None, permission_model=None, parent_id=None, parent_key=None, feed_type=None, id=None, _configuration=None):  # noqa: E501
        """FolderDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._key = None
        self._display_name = None
        self._fully_qualified_name = None
        self._description = None
        self._folder_type = None
        self._is_personal = None
        self._provision_type = None
        self._permission_model = None
        self._parent_id = None
        self._parent_key = None
        self._feed_type = None
        self._id = None
        self.discriminator = None

        if key is not None:
            self.key = key
        self.display_name = display_name
        if fully_qualified_name is not None:
            self.fully_qualified_name = fully_qualified_name
        if description is not None:
            self.description = description
        if folder_type is not None:
            self.folder_type = folder_type
        if is_personal is not None:
            self.is_personal = is_personal
        if provision_type is not None:
            self.provision_type = provision_type
        if permission_model is not None:
            self.permission_model = permission_model
        if parent_id is not None:
            self.parent_id = parent_id
        if parent_key is not None:
            self.parent_key = parent_key
        if feed_type is not None:
            self.feed_type = feed_type
        if id is not None:
            self.id = id

    @property
    def key(self):
        """Gets the key of this FolderDto.  # noqa: E501

        Unique key for the folder  # noqa: E501

        :return: The key of this FolderDto.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this FolderDto.

        Unique key for the folder  # noqa: E501

        :param key: The key of this FolderDto.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def display_name(self):
        """Gets the display_name of this FolderDto.  # noqa: E501

        Display name for the folder.  # noqa: E501

        :return: The display_name of this FolderDto.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this FolderDto.

        Display name for the folder.  # noqa: E501

        :param display_name: The display_name of this FolderDto.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                display_name is not None and len(display_name) > 115):
            raise ValueError("Invalid value for `display_name`, length must be less than or equal to `115`")  # noqa: E501
        if (self._configuration.client_side_validation and
                display_name is not None and len(display_name) < 1):
            raise ValueError("Invalid value for `display_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._display_name = display_name

    @property
    def fully_qualified_name(self):
        """Gets the fully_qualified_name of this FolderDto.  # noqa: E501

        Name of folder prepended by the names of its ancestors.  # noqa: E501

        :return: The fully_qualified_name of this FolderDto.  # noqa: E501
        :rtype: str
        """
        return self._fully_qualified_name

    @fully_qualified_name.setter
    def fully_qualified_name(self, fully_qualified_name):
        """Sets the fully_qualified_name of this FolderDto.

        Name of folder prepended by the names of its ancestors.  # noqa: E501

        :param fully_qualified_name: The fully_qualified_name of this FolderDto.  # noqa: E501
        :type: str
        """

        self._fully_qualified_name = fully_qualified_name

    @property
    def description(self):
        """Gets the description of this FolderDto.  # noqa: E501

        Description of folder  # noqa: E501

        :return: The description of this FolderDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FolderDto.

        Description of folder  # noqa: E501

        :param description: The description of this FolderDto.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                description is not None and len(description) > 500):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `500`")  # noqa: E501

        self._description = description

    @property
    def folder_type(self):
        """Gets the folder_type of this FolderDto.  # noqa: E501

        Folder type  # noqa: E501

        :return: The folder_type of this FolderDto.  # noqa: E501
        :rtype: str
        """
        return self._folder_type

    @folder_type.setter
    def folder_type(self, folder_type):
        """Sets the folder_type of this FolderDto.

        Folder type  # noqa: E501

        :param folder_type: The folder_type of this FolderDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["Standard", "Personal", "Virtual", "Solution"]  # noqa: E501
        if (self._configuration.client_side_validation and
                folder_type not in allowed_values):
            raise ValueError(
                "Invalid value for `folder_type` ({0}), must be one of {1}"  # noqa: E501
                .format(folder_type, allowed_values)
            )

        self._folder_type = folder_type

    @property
    def is_personal(self):
        """Gets the is_personal of this FolderDto.  # noqa: E501

        True if Personal  # noqa: E501

        :return: The is_personal of this FolderDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_personal

    @is_personal.setter
    def is_personal(self, is_personal):
        """Sets the is_personal of this FolderDto.

        True if Personal  # noqa: E501

        :param is_personal: The is_personal of this FolderDto.  # noqa: E501
        :type: bool
        """

        self._is_personal = is_personal

    @property
    def provision_type(self):
        """Gets the provision_type of this FolderDto.  # noqa: E501

        Robot provisioning type  # noqa: E501

        :return: The provision_type of this FolderDto.  # noqa: E501
        :rtype: str
        """
        return self._provision_type

    @provision_type.setter
    def provision_type(self, provision_type):
        """Sets the provision_type of this FolderDto.

        Robot provisioning type  # noqa: E501

        :param provision_type: The provision_type of this FolderDto.  # noqa: E501
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
    def permission_model(self):
        """Gets the permission_model of this FolderDto.  # noqa: E501

        Folder permissions model  # noqa: E501

        :return: The permission_model of this FolderDto.  # noqa: E501
        :rtype: str
        """
        return self._permission_model

    @permission_model.setter
    def permission_model(self, permission_model):
        """Sets the permission_model of this FolderDto.

        Folder permissions model  # noqa: E501

        :param permission_model: The permission_model of this FolderDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["InheritFromTenant", "FineGrained"]  # noqa: E501
        if (self._configuration.client_side_validation and
                permission_model not in allowed_values):
            raise ValueError(
                "Invalid value for `permission_model` ({0}), must be one of {1}"  # noqa: E501
                .format(permission_model, allowed_values)
            )

        self._permission_model = permission_model

    @property
    def parent_id(self):
        """Gets the parent_id of this FolderDto.  # noqa: E501

        Id of parent folder in the folders hierarchy  # noqa: E501

        :return: The parent_id of this FolderDto.  # noqa: E501
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this FolderDto.

        Id of parent folder in the folders hierarchy  # noqa: E501

        :param parent_id: The parent_id of this FolderDto.  # noqa: E501
        :type: int
        """

        self._parent_id = parent_id

    @property
    def parent_key(self):
        """Gets the parent_key of this FolderDto.  # noqa: E501

        Unique key for the parent folder  # noqa: E501

        :return: The parent_key of this FolderDto.  # noqa: E501
        :rtype: str
        """
        return self._parent_key

    @parent_key.setter
    def parent_key(self, parent_key):
        """Sets the parent_key of this FolderDto.

        Unique key for the parent folder  # noqa: E501

        :param parent_key: The parent_key of this FolderDto.  # noqa: E501
        :type: str
        """

        self._parent_key = parent_key

    @property
    def feed_type(self):
        """Gets the feed_type of this FolderDto.  # noqa: E501

        Folder feed type  # noqa: E501

        :return: The feed_type of this FolderDto.  # noqa: E501
        :rtype: str
        """
        return self._feed_type

    @feed_type.setter
    def feed_type(self, feed_type):
        """Sets the feed_type of this FolderDto.

        Folder feed type  # noqa: E501

        :param feed_type: The feed_type of this FolderDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["Undefined", "Processes", "Libraries", "PersonalWorkspace", "FolderHierarchy"]  # noqa: E501
        if (self._configuration.client_side_validation and
                feed_type not in allowed_values):
            raise ValueError(
                "Invalid value for `feed_type` ({0}), must be one of {1}"  # noqa: E501
                .format(feed_type, allowed_values)
            )

        self._feed_type = feed_type

    @property
    def id(self):
        """Gets the id of this FolderDto.  # noqa: E501


        :return: The id of this FolderDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FolderDto.


        :param id: The id of this FolderDto.  # noqa: E501
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
        if issubclass(FolderDto, dict):
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
        if not isinstance(other, FolderDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FolderDto):
            return True

        return self.to_dict() != other.to_dict()
