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


class WebhookSimpleUserDto(object):
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
        'key': 'str',
        'user_name': 'str',
        'domain': 'str',
        'full_name': 'str',
        'email_address': 'str',
        'type': 'str',
        'is_active': 'bool',
        'last_login_time': 'datetime',
        'creation_time': 'datetime',
        'authentication_source': 'str'
    }

    attribute_map = {
        'id': 'Id',
        'key': 'Key',
        'user_name': 'UserName',
        'domain': 'Domain',
        'full_name': 'FullName',
        'email_address': 'EmailAddress',
        'type': 'Type',
        'is_active': 'IsActive',
        'last_login_time': 'LastLoginTime',
        'creation_time': 'CreationTime',
        'authentication_source': 'AuthenticationSource'
    }

    def __init__(self, id=None, key=None, user_name=None, domain=None, full_name=None, email_address=None, type=None, is_active=None, last_login_time=None, creation_time=None, authentication_source=None, _configuration=None):  # noqa: E501
        """WebhookSimpleUserDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._key = None
        self._user_name = None
        self._domain = None
        self._full_name = None
        self._email_address = None
        self._type = None
        self._is_active = None
        self._last_login_time = None
        self._creation_time = None
        self._authentication_source = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if key is not None:
            self.key = key
        if user_name is not None:
            self.user_name = user_name
        if domain is not None:
            self.domain = domain
        if full_name is not None:
            self.full_name = full_name
        if email_address is not None:
            self.email_address = email_address
        if type is not None:
            self.type = type
        if is_active is not None:
            self.is_active = is_active
        if last_login_time is not None:
            self.last_login_time = last_login_time
        if creation_time is not None:
            self.creation_time = creation_time
        if authentication_source is not None:
            self.authentication_source = authentication_source

    @property
    def id(self):
        """Gets the id of this WebhookSimpleUserDto.  # noqa: E501


        :return: The id of this WebhookSimpleUserDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WebhookSimpleUserDto.


        :param id: The id of this WebhookSimpleUserDto.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def key(self):
        """Gets the key of this WebhookSimpleUserDto.  # noqa: E501


        :return: The key of this WebhookSimpleUserDto.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this WebhookSimpleUserDto.


        :param key: The key of this WebhookSimpleUserDto.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def user_name(self):
        """Gets the user_name of this WebhookSimpleUserDto.  # noqa: E501

        The name used to login to Orchestrator.  # noqa: E501

        :return: The user_name of this WebhookSimpleUserDto.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this WebhookSimpleUserDto.

        The name used to login to Orchestrator.  # noqa: E501

        :param user_name: The user_name of this WebhookSimpleUserDto.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def domain(self):
        """Gets the domain of this WebhookSimpleUserDto.  # noqa: E501

        The domain from which the user is imported  # noqa: E501

        :return: The domain of this WebhookSimpleUserDto.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this WebhookSimpleUserDto.

        The domain from which the user is imported  # noqa: E501

        :param domain: The domain of this WebhookSimpleUserDto.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def full_name(self):
        """Gets the full_name of this WebhookSimpleUserDto.  # noqa: E501

        The full name of the person constructed with the format Name Surname.  # noqa: E501

        :return: The full_name of this WebhookSimpleUserDto.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this WebhookSimpleUserDto.

        The full name of the person constructed with the format Name Surname.  # noqa: E501

        :param full_name: The full_name of this WebhookSimpleUserDto.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def email_address(self):
        """Gets the email_address of this WebhookSimpleUserDto.  # noqa: E501

        The e-mail address associated with the user.  # noqa: E501

        :return: The email_address of this WebhookSimpleUserDto.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this WebhookSimpleUserDto.

        The e-mail address associated with the user.  # noqa: E501

        :param email_address: The email_address of this WebhookSimpleUserDto.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

    @property
    def type(self):
        """Gets the type of this WebhookSimpleUserDto.  # noqa: E501

        The user type.  # noqa: E501

        :return: The type of this WebhookSimpleUserDto.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WebhookSimpleUserDto.

        The user type.  # noqa: E501

        :param type: The type of this WebhookSimpleUserDto.  # noqa: E501
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
    def is_active(self):
        """Gets the is_active of this WebhookSimpleUserDto.  # noqa: E501

        States if the user is active or not. An inactive user cannot login to Orchestrator.  # noqa: E501

        :return: The is_active of this WebhookSimpleUserDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this WebhookSimpleUserDto.

        States if the user is active or not. An inactive user cannot login to Orchestrator.  # noqa: E501

        :param is_active: The is_active of this WebhookSimpleUserDto.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    @property
    def last_login_time(self):
        """Gets the last_login_time of this WebhookSimpleUserDto.  # noqa: E501

        The date and time when the user last logged in, or null if the user never logged in.  # noqa: E501

        :return: The last_login_time of this WebhookSimpleUserDto.  # noqa: E501
        :rtype: datetime
        """
        return self._last_login_time

    @last_login_time.setter
    def last_login_time(self, last_login_time):
        """Sets the last_login_time of this WebhookSimpleUserDto.

        The date and time when the user last logged in, or null if the user never logged in.  # noqa: E501

        :param last_login_time: The last_login_time of this WebhookSimpleUserDto.  # noqa: E501
        :type: datetime
        """

        self._last_login_time = last_login_time

    @property
    def creation_time(self):
        """Gets the creation_time of this WebhookSimpleUserDto.  # noqa: E501

        The date and time when the user was created.  # noqa: E501

        :return: The creation_time of this WebhookSimpleUserDto.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this WebhookSimpleUserDto.

        The date and time when the user was created.  # noqa: E501

        :param creation_time: The creation_time of this WebhookSimpleUserDto.  # noqa: E501
        :type: datetime
        """

        self._creation_time = creation_time

    @property
    def authentication_source(self):
        """Gets the authentication_source of this WebhookSimpleUserDto.  # noqa: E501

        The source which authenticated this user.  # noqa: E501

        :return: The authentication_source of this WebhookSimpleUserDto.  # noqa: E501
        :rtype: str
        """
        return self._authentication_source

    @authentication_source.setter
    def authentication_source(self, authentication_source):
        """Sets the authentication_source of this WebhookSimpleUserDto.

        The source which authenticated this user.  # noqa: E501

        :param authentication_source: The authentication_source of this WebhookSimpleUserDto.  # noqa: E501
        :type: str
        """

        self._authentication_source = authentication_source

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
        if issubclass(WebhookSimpleUserDto, dict):
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
        if not isinstance(other, WebhookSimpleUserDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WebhookSimpleUserDto):
            return True

        return self.to_dict() != other.to_dict()
