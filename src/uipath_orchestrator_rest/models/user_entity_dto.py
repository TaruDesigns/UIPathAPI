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


class UserEntityDto(object):
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
        'full_name': 'str',
        'authentication_source': 'str',
        'user_name': 'str',
        'is_inherited': 'bool',
        'assigned_to_folder_ids': 'list[int]',
        'may_have_attended': 'bool',
        'may_have_unattended': 'bool',
        'type': 'str',
        'source': 'str',
        'id': 'int'
    }

    attribute_map = {
        'full_name': 'FullName',
        'authentication_source': 'AuthenticationSource',
        'user_name': 'UserName',
        'is_inherited': 'IsInherited',
        'assigned_to_folder_ids': 'AssignedToFolderIds',
        'may_have_attended': 'MayHaveAttended',
        'may_have_unattended': 'MayHaveUnattended',
        'type': 'Type',
        'source': 'Source',
        'id': 'Id'
    }

    def __init__(self, full_name=None, authentication_source=None, user_name=None, is_inherited=None, assigned_to_folder_ids=None, may_have_attended=None, may_have_unattended=None, type=None, source=None, id=None, _configuration=None):  # noqa: E501
        """UserEntityDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._full_name = None
        self._authentication_source = None
        self._user_name = None
        self._is_inherited = None
        self._assigned_to_folder_ids = None
        self._may_have_attended = None
        self._may_have_unattended = None
        self._type = None
        self._source = None
        self._id = None
        self.discriminator = None

        if full_name is not None:
            self.full_name = full_name
        if authentication_source is not None:
            self.authentication_source = authentication_source
        if user_name is not None:
            self.user_name = user_name
        if is_inherited is not None:
            self.is_inherited = is_inherited
        if assigned_to_folder_ids is not None:
            self.assigned_to_folder_ids = assigned_to_folder_ids
        if may_have_attended is not None:
            self.may_have_attended = may_have_attended
        if may_have_unattended is not None:
            self.may_have_unattended = may_have_unattended
        if type is not None:
            self.type = type
        if source is not None:
            self.source = source
        if id is not None:
            self.id = id

    @property
    def full_name(self):
        """Gets the full_name of this UserEntityDto.  # noqa: E501


        :return: The full_name of this UserEntityDto.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this UserEntityDto.


        :param full_name: The full_name of this UserEntityDto.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def authentication_source(self):
        """Gets the authentication_source of this UserEntityDto.  # noqa: E501


        :return: The authentication_source of this UserEntityDto.  # noqa: E501
        :rtype: str
        """
        return self._authentication_source

    @authentication_source.setter
    def authentication_source(self, authentication_source):
        """Sets the authentication_source of this UserEntityDto.


        :param authentication_source: The authentication_source of this UserEntityDto.  # noqa: E501
        :type: str
        """

        self._authentication_source = authentication_source

    @property
    def user_name(self):
        """Gets the user_name of this UserEntityDto.  # noqa: E501


        :return: The user_name of this UserEntityDto.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this UserEntityDto.


        :param user_name: The user_name of this UserEntityDto.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def is_inherited(self):
        """Gets the is_inherited of this UserEntityDto.  # noqa: E501


        :return: The is_inherited of this UserEntityDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_inherited

    @is_inherited.setter
    def is_inherited(self, is_inherited):
        """Sets the is_inherited of this UserEntityDto.


        :param is_inherited: The is_inherited of this UserEntityDto.  # noqa: E501
        :type: bool
        """

        self._is_inherited = is_inherited

    @property
    def assigned_to_folder_ids(self):
        """Gets the assigned_to_folder_ids of this UserEntityDto.  # noqa: E501


        :return: The assigned_to_folder_ids of this UserEntityDto.  # noqa: E501
        :rtype: list[int]
        """
        return self._assigned_to_folder_ids

    @assigned_to_folder_ids.setter
    def assigned_to_folder_ids(self, assigned_to_folder_ids):
        """Sets the assigned_to_folder_ids of this UserEntityDto.


        :param assigned_to_folder_ids: The assigned_to_folder_ids of this UserEntityDto.  # noqa: E501
        :type: list[int]
        """

        self._assigned_to_folder_ids = assigned_to_folder_ids

    @property
    def may_have_attended(self):
        """Gets the may_have_attended of this UserEntityDto.  # noqa: E501


        :return: The may_have_attended of this UserEntityDto.  # noqa: E501
        :rtype: bool
        """
        return self._may_have_attended

    @may_have_attended.setter
    def may_have_attended(self, may_have_attended):
        """Sets the may_have_attended of this UserEntityDto.


        :param may_have_attended: The may_have_attended of this UserEntityDto.  # noqa: E501
        :type: bool
        """

        self._may_have_attended = may_have_attended

    @property
    def may_have_unattended(self):
        """Gets the may_have_unattended of this UserEntityDto.  # noqa: E501


        :return: The may_have_unattended of this UserEntityDto.  # noqa: E501
        :rtype: bool
        """
        return self._may_have_unattended

    @may_have_unattended.setter
    def may_have_unattended(self, may_have_unattended):
        """Sets the may_have_unattended of this UserEntityDto.


        :param may_have_unattended: The may_have_unattended of this UserEntityDto.  # noqa: E501
        :type: bool
        """

        self._may_have_unattended = may_have_unattended

    @property
    def type(self):
        """Gets the type of this UserEntityDto.  # noqa: E501


        :return: The type of this UserEntityDto.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UserEntityDto.


        :param type: The type of this UserEntityDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["User", "Robot", "DirectoryUser", "DirectoryGroup", "DirectoryRobot", "DirectoryExternalApplication"]  # noqa: E501
        if (self._configuration.client_side_validation and
                type not in allowed_values):
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def source(self):
        """Gets the source of this UserEntityDto.  # noqa: E501


        :return: The source of this UserEntityDto.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this UserEntityDto.


        :param source: The source of this UserEntityDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["Orchestrator", "Portal", "All"]  # noqa: E501
        if (self._configuration.client_side_validation and
                source not in allowed_values):
            raise ValueError(
                "Invalid value for `source` ({0}), must be one of {1}"  # noqa: E501
                .format(source, allowed_values)
            )

        self._source = source

    @property
    def id(self):
        """Gets the id of this UserEntityDto.  # noqa: E501


        :return: The id of this UserEntityDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserEntityDto.


        :param id: The id of this UserEntityDto.  # noqa: E501
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
        if issubclass(UserEntityDto, dict):
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
        if not isinstance(other, UserEntityDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserEntityDto):
            return True

        return self.to_dict() != other.to_dict()