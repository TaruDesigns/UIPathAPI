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


class UserLoginInfoDto(object):
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
        'surname': 'str',
        'user_name': 'str',
        'email_address': 'str',
        'id': 'int'
    }

    attribute_map = {
        'name': 'name',
        'surname': 'surname',
        'user_name': 'userName',
        'email_address': 'emailAddress',
        'id': 'id'
    }

    def __init__(self, name=None, surname=None, user_name=None, email_address=None, id=None, _configuration=None):  # noqa: E501
        """UserLoginInfoDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._surname = None
        self._user_name = None
        self._email_address = None
        self._id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if surname is not None:
            self.surname = surname
        if user_name is not None:
            self.user_name = user_name
        if email_address is not None:
            self.email_address = email_address
        if id is not None:
            self.id = id

    @property
    def name(self):
        """Gets the name of this UserLoginInfoDto.  # noqa: E501


        :return: The name of this UserLoginInfoDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserLoginInfoDto.


        :param name: The name of this UserLoginInfoDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def surname(self):
        """Gets the surname of this UserLoginInfoDto.  # noqa: E501


        :return: The surname of this UserLoginInfoDto.  # noqa: E501
        :rtype: str
        """
        return self._surname

    @surname.setter
    def surname(self, surname):
        """Sets the surname of this UserLoginInfoDto.


        :param surname: The surname of this UserLoginInfoDto.  # noqa: E501
        :type: str
        """

        self._surname = surname

    @property
    def user_name(self):
        """Gets the user_name of this UserLoginInfoDto.  # noqa: E501


        :return: The user_name of this UserLoginInfoDto.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this UserLoginInfoDto.


        :param user_name: The user_name of this UserLoginInfoDto.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def email_address(self):
        """Gets the email_address of this UserLoginInfoDto.  # noqa: E501


        :return: The email_address of this UserLoginInfoDto.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this UserLoginInfoDto.


        :param email_address: The email_address of this UserLoginInfoDto.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

    @property
    def id(self):
        """Gets the id of this UserLoginInfoDto.  # noqa: E501


        :return: The id of this UserLoginInfoDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserLoginInfoDto.


        :param id: The id of this UserLoginInfoDto.  # noqa: E501
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
        if issubclass(UserLoginInfoDto, dict):
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
        if not isinstance(other, UserLoginInfoDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserLoginInfoDto):
            return True

        return self.to_dict() != other.to_dict()
