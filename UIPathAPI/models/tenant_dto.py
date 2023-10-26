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


class TenantDto(object):
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
        'key': 'str',
        'display_name': 'str',
        'admin_email_address': 'str',
        'admin_name': 'str',
        'admin_surname': 'str',
        'admin_user_key': 'str',
        'admin_password': 'str',
        'last_login_time': 'datetime',
        'is_active': 'bool',
        'accepted_domains_list': 'list[str]',
        'has_connection_string': 'bool',
        'connection_string': 'str',
        'license': 'TenantLicenseDto',
        'organization_name': 'str',
        'id': 'int'
    }

    attribute_map = {
        'name': 'Name',
        'key': 'Key',
        'display_name': 'DisplayName',
        'admin_email_address': 'AdminEmailAddress',
        'admin_name': 'AdminName',
        'admin_surname': 'AdminSurname',
        'admin_user_key': 'AdminUserKey',
        'admin_password': 'AdminPassword',
        'last_login_time': 'LastLoginTime',
        'is_active': 'IsActive',
        'accepted_domains_list': 'AcceptedDomainsList',
        'has_connection_string': 'HasConnectionString',
        'connection_string': 'ConnectionString',
        'license': 'License',
        'organization_name': 'OrganizationName',
        'id': 'Id'
    }

    def __init__(self, name=None, key=None, display_name=None, admin_email_address=None, admin_name=None, admin_surname=None, admin_user_key=None, admin_password=None, last_login_time=None, is_active=None, accepted_domains_list=None, has_connection_string=None, connection_string=None, license=None, organization_name=None, id=None, _configuration=None):  # noqa: E501
        """TenantDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._key = None
        self._display_name = None
        self._admin_email_address = None
        self._admin_name = None
        self._admin_surname = None
        self._admin_user_key = None
        self._admin_password = None
        self._last_login_time = None
        self._is_active = None
        self._accepted_domains_list = None
        self._has_connection_string = None
        self._connection_string = None
        self._license = None
        self._organization_name = None
        self._id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if key is not None:
            self.key = key
        if display_name is not None:
            self.display_name = display_name
        if admin_email_address is not None:
            self.admin_email_address = admin_email_address
        if admin_name is not None:
            self.admin_name = admin_name
        if admin_surname is not None:
            self.admin_surname = admin_surname
        if admin_user_key is not None:
            self.admin_user_key = admin_user_key
        if admin_password is not None:
            self.admin_password = admin_password
        if last_login_time is not None:
            self.last_login_time = last_login_time
        if is_active is not None:
            self.is_active = is_active
        if accepted_domains_list is not None:
            self.accepted_domains_list = accepted_domains_list
        if has_connection_string is not None:
            self.has_connection_string = has_connection_string
        if connection_string is not None:
            self.connection_string = connection_string
        if license is not None:
            self.license = license
        if organization_name is not None:
            self.organization_name = organization_name
        if id is not None:
            self.id = id

    @property
    def name(self):
        """Gets the name of this TenantDto.  # noqa: E501

        Name of the tenant.  # noqa: E501

        :return: The name of this TenantDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TenantDto.

        Name of the tenant.  # noqa: E501

        :param name: The name of this TenantDto.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                name is not None and len(name) > 64):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `64`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and len(name) < 0):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and not re.search(r'^[\\p{L}][\\p{L}0-9-_]+$', name)):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[\\p{L}][\\p{L}0-9-_]+$/`")  # noqa: E501

        self._name = name

    @property
    def key(self):
        """Gets the key of this TenantDto.  # noqa: E501

        Unique Key of the tenant.  # noqa: E501

        :return: The key of this TenantDto.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this TenantDto.

        Unique Key of the tenant.  # noqa: E501

        :param key: The key of this TenantDto.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def display_name(self):
        """Gets the display_name of this TenantDto.  # noqa: E501

        Display name of the the tenant  # noqa: E501

        :return: The display_name of this TenantDto.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this TenantDto.

        Display name of the the tenant  # noqa: E501

        :param display_name: The display_name of this TenantDto.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                display_name is not None and len(display_name) > 128):
            raise ValueError("Invalid value for `display_name`, length must be less than or equal to `128`")  # noqa: E501
        if (self._configuration.client_side_validation and
                display_name is not None and len(display_name) < 0):
            raise ValueError("Invalid value for `display_name`, length must be greater than or equal to `0`")  # noqa: E501

        self._display_name = display_name

    @property
    def admin_email_address(self):
        """Gets the admin_email_address of this TenantDto.  # noqa: E501

        Default tenant's admin user account email address.  # noqa: E501

        :return: The admin_email_address of this TenantDto.  # noqa: E501
        :rtype: str
        """
        return self._admin_email_address

    @admin_email_address.setter
    def admin_email_address(self, admin_email_address):
        """Sets the admin_email_address of this TenantDto.

        Default tenant's admin user account email address.  # noqa: E501

        :param admin_email_address: The admin_email_address of this TenantDto.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                admin_email_address is not None and len(admin_email_address) > 256):
            raise ValueError("Invalid value for `admin_email_address`, length must be less than or equal to `256`")  # noqa: E501
        if (self._configuration.client_side_validation and
                admin_email_address is not None and len(admin_email_address) < 0):
            raise ValueError("Invalid value for `admin_email_address`, length must be greater than or equal to `0`")  # noqa: E501

        self._admin_email_address = admin_email_address

    @property
    def admin_name(self):
        """Gets the admin_name of this TenantDto.  # noqa: E501

        Default tenant's admin user account name.  # noqa: E501

        :return: The admin_name of this TenantDto.  # noqa: E501
        :rtype: str
        """
        return self._admin_name

    @admin_name.setter
    def admin_name(self, admin_name):
        """Sets the admin_name of this TenantDto.

        Default tenant's admin user account name.  # noqa: E501

        :param admin_name: The admin_name of this TenantDto.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                admin_name is not None and len(admin_name) > 32):
            raise ValueError("Invalid value for `admin_name`, length must be less than or equal to `32`")  # noqa: E501
        if (self._configuration.client_side_validation and
                admin_name is not None and len(admin_name) < 0):
            raise ValueError("Invalid value for `admin_name`, length must be greater than or equal to `0`")  # noqa: E501

        self._admin_name = admin_name

    @property
    def admin_surname(self):
        """Gets the admin_surname of this TenantDto.  # noqa: E501

        Default tenant's admin user account surname.  # noqa: E501

        :return: The admin_surname of this TenantDto.  # noqa: E501
        :rtype: str
        """
        return self._admin_surname

    @admin_surname.setter
    def admin_surname(self, admin_surname):
        """Sets the admin_surname of this TenantDto.

        Default tenant's admin user account surname.  # noqa: E501

        :param admin_surname: The admin_surname of this TenantDto.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                admin_surname is not None and len(admin_surname) > 32):
            raise ValueError("Invalid value for `admin_surname`, length must be less than or equal to `32`")  # noqa: E501
        if (self._configuration.client_side_validation and
                admin_surname is not None and len(admin_surname) < 0):
            raise ValueError("Invalid value for `admin_surname`, length must be greater than or equal to `0`")  # noqa: E501

        self._admin_surname = admin_surname

    @property
    def admin_user_key(self):
        """Gets the admin_user_key of this TenantDto.  # noqa: E501

        Default tenant's admin user account key.  # noqa: E501

        :return: The admin_user_key of this TenantDto.  # noqa: E501
        :rtype: str
        """
        return self._admin_user_key

    @admin_user_key.setter
    def admin_user_key(self, admin_user_key):
        """Sets the admin_user_key of this TenantDto.

        Default tenant's admin user account key.  # noqa: E501

        :param admin_user_key: The admin_user_key of this TenantDto.  # noqa: E501
        :type: str
        """

        self._admin_user_key = admin_user_key

    @property
    def admin_password(self):
        """Gets the admin_password of this TenantDto.  # noqa: E501

        Default tenant's admin user account password. Only valid for create/update operations.  # noqa: E501

        :return: The admin_password of this TenantDto.  # noqa: E501
        :rtype: str
        """
        return self._admin_password

    @admin_password.setter
    def admin_password(self, admin_password):
        """Sets the admin_password of this TenantDto.

        Default tenant's admin user account password. Only valid for create/update operations.  # noqa: E501

        :param admin_password: The admin_password of this TenantDto.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                admin_password is not None and len(admin_password) > 32):
            raise ValueError("Invalid value for `admin_password`, length must be less than or equal to `32`")  # noqa: E501
        if (self._configuration.client_side_validation and
                admin_password is not None and len(admin_password) < 0):
            raise ValueError("Invalid value for `admin_password`, length must be greater than or equal to `0`")  # noqa: E501

        self._admin_password = admin_password

    @property
    def last_login_time(self):
        """Gets the last_login_time of this TenantDto.  # noqa: E501

        The last time a user logged in this tenant.  # noqa: E501

        :return: The last_login_time of this TenantDto.  # noqa: E501
        :rtype: datetime
        """
        return self._last_login_time

    @last_login_time.setter
    def last_login_time(self, last_login_time):
        """Sets the last_login_time of this TenantDto.

        The last time a user logged in this tenant.  # noqa: E501

        :param last_login_time: The last_login_time of this TenantDto.  # noqa: E501
        :type: datetime
        """

        self._last_login_time = last_login_time

    @property
    def is_active(self):
        """Gets the is_active of this TenantDto.  # noqa: E501

        Specifies if the tenant is active or not.  # noqa: E501

        :return: The is_active of this TenantDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this TenantDto.

        Specifies if the tenant is active or not.  # noqa: E501

        :param is_active: The is_active of this TenantDto.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    @property
    def accepted_domains_list(self):
        """Gets the accepted_domains_list of this TenantDto.  # noqa: E501

        DEPRECATED. Accepted DNS list.  # noqa: E501

        :return: The accepted_domains_list of this TenantDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._accepted_domains_list

    @accepted_domains_list.setter
    def accepted_domains_list(self, accepted_domains_list):
        """Sets the accepted_domains_list of this TenantDto.

        DEPRECATED. Accepted DNS list.  # noqa: E501

        :param accepted_domains_list: The accepted_domains_list of this TenantDto.  # noqa: E501
        :type: list[str]
        """

        self._accepted_domains_list = accepted_domains_list

    @property
    def has_connection_string(self):
        """Gets the has_connection_string of this TenantDto.  # noqa: E501

        DEPRECATED. Specifies if the the tenant has a connection string defined  # noqa: E501

        :return: The has_connection_string of this TenantDto.  # noqa: E501
        :rtype: bool
        """
        return self._has_connection_string

    @has_connection_string.setter
    def has_connection_string(self, has_connection_string):
        """Sets the has_connection_string of this TenantDto.

        DEPRECATED. Specifies if the the tenant has a connection string defined  # noqa: E501

        :param has_connection_string: The has_connection_string of this TenantDto.  # noqa: E501
        :type: bool
        """

        self._has_connection_string = has_connection_string

    @property
    def connection_string(self):
        """Gets the connection_string of this TenantDto.  # noqa: E501

        DEPRECATED. DB connection string  # noqa: E501

        :return: The connection_string of this TenantDto.  # noqa: E501
        :rtype: str
        """
        return self._connection_string

    @connection_string.setter
    def connection_string(self, connection_string):
        """Sets the connection_string of this TenantDto.

        DEPRECATED. DB connection string  # noqa: E501

        :param connection_string: The connection_string of this TenantDto.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                connection_string is not None and len(connection_string) > 1024):
            raise ValueError("Invalid value for `connection_string`, length must be less than or equal to `1024`")  # noqa: E501
        if (self._configuration.client_side_validation and
                connection_string is not None and len(connection_string) < 0):
            raise ValueError("Invalid value for `connection_string`, length must be greater than or equal to `0`")  # noqa: E501

        self._connection_string = connection_string

    @property
    def license(self):
        """Gets the license of this TenantDto.  # noqa: E501


        :return: The license of this TenantDto.  # noqa: E501
        :rtype: TenantLicenseDto
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this TenantDto.


        :param license: The license of this TenantDto.  # noqa: E501
        :type: TenantLicenseDto
        """

        self._license = license

    @property
    def organization_name(self):
        """Gets the organization_name of this TenantDto.  # noqa: E501

        Organization Name of the tenant.  # noqa: E501

        :return: The organization_name of this TenantDto.  # noqa: E501
        :rtype: str
        """
        return self._organization_name

    @organization_name.setter
    def organization_name(self, organization_name):
        """Sets the organization_name of this TenantDto.

        Organization Name of the tenant.  # noqa: E501

        :param organization_name: The organization_name of this TenantDto.  # noqa: E501
        :type: str
        """

        self._organization_name = organization_name

    @property
    def id(self):
        """Gets the id of this TenantDto.  # noqa: E501


        :return: The id of this TenantDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TenantDto.


        :param id: The id of this TenantDto.  # noqa: E501
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
        if issubclass(TenantDto, dict):
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
        if not isinstance(other, TenantDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TenantDto):
            return True

        return self.to_dict() != other.to_dict()
