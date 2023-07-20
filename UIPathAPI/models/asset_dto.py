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


class AssetDto(object):
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
        'name': 'str',
        'can_be_deleted': 'bool',
        'value_scope': 'str',
        'value_type': 'str',
        'value': 'str',
        'string_value': 'str',
        'bool_value': 'bool',
        'int_value': 'int',
        'credential_username': 'str',
        'credential_password': 'str',
        'external_name': 'str',
        'credential_store_id': 'int',
        'key_value_list': 'list[CustomKeyValuePair]',
        'has_default_value': 'bool',
        'description': 'str',
        'robot_values': 'list[AssetRobotValueDto]',
        'user_values': 'list[AssetUserValueDto]',
        'tags': 'list[TagDto]',
        'folders_count': 'int',
        'last_modification_time': 'datetime',
        'last_modifier_user_id': 'int',
        'creation_time': 'datetime',
        'creator_user_id': 'int',
        'id': 'int'
    }

    attribute_map = {
        'key': 'Key',
        'name': 'Name',
        'can_be_deleted': 'CanBeDeleted',
        'value_scope': 'ValueScope',
        'value_type': 'ValueType',
        'value': 'Value',
        'string_value': 'StringValue',
        'bool_value': 'BoolValue',
        'int_value': 'IntValue',
        'credential_username': 'CredentialUsername',
        'credential_password': 'CredentialPassword',
        'external_name': 'ExternalName',
        'credential_store_id': 'CredentialStoreId',
        'key_value_list': 'KeyValueList',
        'has_default_value': 'HasDefaultValue',
        'description': 'Description',
        'robot_values': 'RobotValues',
        'user_values': 'UserValues',
        'tags': 'Tags',
        'folders_count': 'FoldersCount',
        'last_modification_time': 'LastModificationTime',
        'last_modifier_user_id': 'LastModifierUserId',
        'creation_time': 'CreationTime',
        'creator_user_id': 'CreatorUserId',
        'id': 'Id'
    }

    def __init__(self, key=None, name=None, can_be_deleted=None, value_scope=None, value_type=None, value=None, string_value=None, bool_value=None, int_value=None, credential_username=None, credential_password=None, external_name=None, credential_store_id=None, key_value_list=None, has_default_value=None, description=None, robot_values=None, user_values=None, tags=None, folders_count=None, last_modification_time=None, last_modifier_user_id=None, creation_time=None, creator_user_id=None, id=None, _configuration=None):  # noqa: E501
        """AssetDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._key = None
        self._name = None
        self._can_be_deleted = None
        self._value_scope = None
        self._value_type = None
        self._value = None
        self._string_value = None
        self._bool_value = None
        self._int_value = None
        self._credential_username = None
        self._credential_password = None
        self._external_name = None
        self._credential_store_id = None
        self._key_value_list = None
        self._has_default_value = None
        self._description = None
        self._robot_values = None
        self._user_values = None
        self._tags = None
        self._folders_count = None
        self._last_modification_time = None
        self._last_modifier_user_id = None
        self._creation_time = None
        self._creator_user_id = None
        self._id = None
        self.discriminator = None

        if key is not None:
            self.key = key
        self.name = name
        if can_be_deleted is not None:
            self.can_be_deleted = can_be_deleted
        self.value_scope = value_scope
        if value_type is not None:
            self.value_type = value_type
        if value is not None:
            self.value = value
        if string_value is not None:
            self.string_value = string_value
        if bool_value is not None:
            self.bool_value = bool_value
        if int_value is not None:
            self.int_value = int_value
        if credential_username is not None:
            self.credential_username = credential_username
        if credential_password is not None:
            self.credential_password = credential_password
        if external_name is not None:
            self.external_name = external_name
        if credential_store_id is not None:
            self.credential_store_id = credential_store_id
        if key_value_list is not None:
            self.key_value_list = key_value_list
        if has_default_value is not None:
            self.has_default_value = has_default_value
        if description is not None:
            self.description = description
        if robot_values is not None:
            self.robot_values = robot_values
        if user_values is not None:
            self.user_values = user_values
        if tags is not None:
            self.tags = tags
        if folders_count is not None:
            self.folders_count = folders_count
        if last_modification_time is not None:
            self.last_modification_time = last_modification_time
        if last_modifier_user_id is not None:
            self.last_modifier_user_id = last_modifier_user_id
        if creation_time is not None:
            self.creation_time = creation_time
        if creator_user_id is not None:
            self.creator_user_id = creator_user_id
        if id is not None:
            self.id = id

    @property
    def key(self):
        """Gets the key of this AssetDto.  # noqa: E501

        An unique identifier  # noqa: E501

        :return: The key of this AssetDto.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this AssetDto.

        An unique identifier  # noqa: E501

        :param key: The key of this AssetDto.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def name(self):
        """Gets the name of this AssetDto.  # noqa: E501

        A custom name for the asset.  # noqa: E501

        :return: The name of this AssetDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AssetDto.

        A custom name for the asset.  # noqa: E501

        :param name: The name of this AssetDto.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and len(name) > 256):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `256`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def can_be_deleted(self):
        """Gets the can_be_deleted of this AssetDto.  # noqa: E501

        States if an assets can be deleted. The default value of this property is true.  # noqa: E501

        :return: The can_be_deleted of this AssetDto.  # noqa: E501
        :rtype: bool
        """
        return self._can_be_deleted

    @can_be_deleted.setter
    def can_be_deleted(self, can_be_deleted):
        """Sets the can_be_deleted of this AssetDto.

        States if an assets can be deleted. The default value of this property is true.  # noqa: E501

        :param can_be_deleted: The can_be_deleted of this AssetDto.  # noqa: E501
        :type: bool
        """

        self._can_be_deleted = can_be_deleted

    @property
    def value_scope(self):
        """Gets the value_scope of this AssetDto.  # noqa: E501

        Defines the scope of the asset.  # noqa: E501

        :return: The value_scope of this AssetDto.  # noqa: E501
        :rtype: str
        """
        return self._value_scope

    @value_scope.setter
    def value_scope(self, value_scope):
        """Sets the value_scope of this AssetDto.

        Defines the scope of the asset.  # noqa: E501

        :param value_scope: The value_scope of this AssetDto.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and value_scope is None:
            raise ValueError("Invalid value for `value_scope`, must not be `None`")  # noqa: E501
        allowed_values = ["Global", "PerRobot"]  # noqa: E501
        if (self._configuration.client_side_validation and
                value_scope not in allowed_values):
            raise ValueError(
                "Invalid value for `value_scope` ({0}), must be one of {1}"  # noqa: E501
                .format(value_scope, allowed_values)
            )

        self._value_scope = value_scope

    @property
    def value_type(self):
        """Gets the value_type of this AssetDto.  # noqa: E501

        Defines the type of value stored by the asset.  # noqa: E501

        :return: The value_type of this AssetDto.  # noqa: E501
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """Sets the value_type of this AssetDto.

        Defines the type of value stored by the asset.  # noqa: E501

        :param value_type: The value_type of this AssetDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["DBConnectionString", "HttpConnectionString", "Text", "Bool", "Integer", "Credential", "WindowsCredential", "KeyValueList"]  # noqa: E501
        if (self._configuration.client_side_validation and
                value_type not in allowed_values):
            raise ValueError(
                "Invalid value for `value_type` ({0}), must be one of {1}"  # noqa: E501
                .format(value_type, allowed_values)
            )

        self._value_type = value_type

    @property
    def value(self):
        """Gets the value of this AssetDto.  # noqa: E501

        The textual representation of the asset value, irrespective of value type.  # noqa: E501

        :return: The value of this AssetDto.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this AssetDto.

        The textual representation of the asset value, irrespective of value type.  # noqa: E501

        :param value: The value of this AssetDto.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def string_value(self):
        """Gets the string_value of this AssetDto.  # noqa: E501

        The value of the asset when the value type is Text. Empty when the value type is not Text.  # noqa: E501

        :return: The string_value of this AssetDto.  # noqa: E501
        :rtype: str
        """
        return self._string_value

    @string_value.setter
    def string_value(self, string_value):
        """Sets the string_value of this AssetDto.

        The value of the asset when the value type is Text. Empty when the value type is not Text.  # noqa: E501

        :param string_value: The string_value of this AssetDto.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                string_value is not None and len(string_value) > 1000000):
            raise ValueError("Invalid value for `string_value`, length must be less than or equal to `1000000`")  # noqa: E501

        self._string_value = string_value

    @property
    def bool_value(self):
        """Gets the bool_value of this AssetDto.  # noqa: E501

        The value of the asset when the value type is Bool. False when the value type is not Bool.  # noqa: E501

        :return: The bool_value of this AssetDto.  # noqa: E501
        :rtype: bool
        """
        return self._bool_value

    @bool_value.setter
    def bool_value(self, bool_value):
        """Sets the bool_value of this AssetDto.

        The value of the asset when the value type is Bool. False when the value type is not Bool.  # noqa: E501

        :param bool_value: The bool_value of this AssetDto.  # noqa: E501
        :type: bool
        """

        self._bool_value = bool_value

    @property
    def int_value(self):
        """Gets the int_value of this AssetDto.  # noqa: E501

        The value of the asset when the value type is Integer. 0 when the value type is not Integer.  # noqa: E501

        :return: The int_value of this AssetDto.  # noqa: E501
        :rtype: int
        """
        return self._int_value

    @int_value.setter
    def int_value(self, int_value):
        """Sets the int_value of this AssetDto.

        The value of the asset when the value type is Integer. 0 when the value type is not Integer.  # noqa: E501

        :param int_value: The int_value of this AssetDto.  # noqa: E501
        :type: int
        """

        self._int_value = int_value

    @property
    def credential_username(self):
        """Gets the credential_username of this AssetDto.  # noqa: E501

        The user name when the value type is Credential. Empty when the value type is not Credential.  # noqa: E501

        :return: The credential_username of this AssetDto.  # noqa: E501
        :rtype: str
        """
        return self._credential_username

    @credential_username.setter
    def credential_username(self, credential_username):
        """Sets the credential_username of this AssetDto.

        The user name when the value type is Credential. Empty when the value type is not Credential.  # noqa: E501

        :param credential_username: The credential_username of this AssetDto.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                credential_username is not None and len(credential_username) > 512):
            raise ValueError("Invalid value for `credential_username`, length must be less than or equal to `512`")  # noqa: E501

        self._credential_username = credential_username

    @property
    def credential_password(self):
        """Gets the credential_password of this AssetDto.  # noqa: E501

        The password when the value type is Credential. Empty when the value type is not Credential.  # noqa: E501

        :return: The credential_password of this AssetDto.  # noqa: E501
        :rtype: str
        """
        return self._credential_password

    @credential_password.setter
    def credential_password(self, credential_password):
        """Sets the credential_password of this AssetDto.

        The password when the value type is Credential. Empty when the value type is not Credential.  # noqa: E501

        :param credential_password: The credential_password of this AssetDto.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                credential_password is not None and len(credential_password) > 25000):
            raise ValueError("Invalid value for `credential_password`, length must be less than or equal to `25000`")  # noqa: E501

        self._credential_password = credential_password

    @property
    def external_name(self):
        """Gets the external_name of this AssetDto.  # noqa: E501

        Contains the value of the key in the external store used to store the credentials.  # noqa: E501

        :return: The external_name of this AssetDto.  # noqa: E501
        :rtype: str
        """
        return self._external_name

    @external_name.setter
    def external_name(self, external_name):
        """Sets the external_name of this AssetDto.

        Contains the value of the key in the external store used to store the credentials.  # noqa: E501

        :param external_name: The external_name of this AssetDto.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                external_name is not None and len(external_name) > 450):
            raise ValueError("Invalid value for `external_name`, length must be less than or equal to `450`")  # noqa: E501
        if (self._configuration.client_side_validation and
                external_name is not None and len(external_name) < 0):
            raise ValueError("Invalid value for `external_name`, length must be greater than or equal to `0`")  # noqa: E501

        self._external_name = external_name

    @property
    def credential_store_id(self):
        """Gets the credential_store_id of this AssetDto.  # noqa: E501

        The Credential Store used to store the credentials.  # noqa: E501

        :return: The credential_store_id of this AssetDto.  # noqa: E501
        :rtype: int
        """
        return self._credential_store_id

    @credential_store_id.setter
    def credential_store_id(self, credential_store_id):
        """Sets the credential_store_id of this AssetDto.

        The Credential Store used to store the credentials.  # noqa: E501

        :param credential_store_id: The credential_store_id of this AssetDto.  # noqa: E501
        :type: int
        """

        self._credential_store_id = credential_store_id

    @property
    def key_value_list(self):
        """Gets the key_value_list of this AssetDto.  # noqa: E501

        A collection of key value pairs when the type is KeyValueList. Empty when the value type is not KeyValueList.  # noqa: E501

        :return: The key_value_list of this AssetDto.  # noqa: E501
        :rtype: list[CustomKeyValuePair]
        """
        return self._key_value_list

    @key_value_list.setter
    def key_value_list(self, key_value_list):
        """Sets the key_value_list of this AssetDto.

        A collection of key value pairs when the type is KeyValueList. Empty when the value type is not KeyValueList.  # noqa: E501

        :param key_value_list: The key_value_list of this AssetDto.  # noqa: E501
        :type: list[CustomKeyValuePair]
        """

        self._key_value_list = key_value_list

    @property
    def has_default_value(self):
        """Gets the has_default_value of this AssetDto.  # noqa: E501

        The asset has a default value set. This value will be null when set from legacy components that don't support  the PerRobot assets with default value feature.  # noqa: E501

        :return: The has_default_value of this AssetDto.  # noqa: E501
        :rtype: bool
        """
        return self._has_default_value

    @has_default_value.setter
    def has_default_value(self, has_default_value):
        """Sets the has_default_value of this AssetDto.

        The asset has a default value set. This value will be null when set from legacy components that don't support  the PerRobot assets with default value feature.  # noqa: E501

        :param has_default_value: The has_default_value of this AssetDto.  # noqa: E501
        :type: bool
        """

        self._has_default_value = has_default_value

    @property
    def description(self):
        """Gets the description of this AssetDto.  # noqa: E501

        The description of the asset.  # noqa: E501

        :return: The description of this AssetDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AssetDto.

        The description of the asset.  # noqa: E501

        :param description: The description of this AssetDto.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                description is not None and len(description) > 250):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `250`")  # noqa: E501

        self._description = description

    @property
    def robot_values(self):
        """Gets the robot_values of this AssetDto.  # noqa: E501

        The collection of asset values per robot. Empty if the asset type is Global or PerUser.  # noqa: E501

        :return: The robot_values of this AssetDto.  # noqa: E501
        :rtype: list[AssetRobotValueDto]
        """
        return self._robot_values

    @robot_values.setter
    def robot_values(self, robot_values):
        """Sets the robot_values of this AssetDto.

        The collection of asset values per robot. Empty if the asset type is Global or PerUser.  # noqa: E501

        :param robot_values: The robot_values of this AssetDto.  # noqa: E501
        :type: list[AssetRobotValueDto]
        """

        self._robot_values = robot_values

    @property
    def user_values(self):
        """Gets the user_values of this AssetDto.  # noqa: E501

        The collection of asset values per user. Empty if the asset type is Global or PerRobot.  # noqa: E501

        :return: The user_values of this AssetDto.  # noqa: E501
        :rtype: list[AssetUserValueDto]
        """
        return self._user_values

    @user_values.setter
    def user_values(self, user_values):
        """Sets the user_values of this AssetDto.

        The collection of asset values per user. Empty if the asset type is Global or PerRobot.  # noqa: E501

        :param user_values: The user_values of this AssetDto.  # noqa: E501
        :type: list[AssetUserValueDto]
        """

        self._user_values = user_values

    @property
    def tags(self):
        """Gets the tags of this AssetDto.  # noqa: E501


        :return: The tags of this AssetDto.  # noqa: E501
        :rtype: list[TagDto]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this AssetDto.


        :param tags: The tags of this AssetDto.  # noqa: E501
        :type: list[TagDto]
        """

        self._tags = tags

    @property
    def folders_count(self):
        """Gets the folders_count of this AssetDto.  # noqa: E501

        Number of folders where the asset is shared.  # noqa: E501

        :return: The folders_count of this AssetDto.  # noqa: E501
        :rtype: int
        """
        return self._folders_count

    @folders_count.setter
    def folders_count(self, folders_count):
        """Sets the folders_count of this AssetDto.

        Number of folders where the asset is shared.  # noqa: E501

        :param folders_count: The folders_count of this AssetDto.  # noqa: E501
        :type: int
        """

        self._folders_count = folders_count

    @property
    def last_modification_time(self):
        """Gets the last_modification_time of this AssetDto.  # noqa: E501


        :return: The last_modification_time of this AssetDto.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modification_time

    @last_modification_time.setter
    def last_modification_time(self, last_modification_time):
        """Sets the last_modification_time of this AssetDto.


        :param last_modification_time: The last_modification_time of this AssetDto.  # noqa: E501
        :type: datetime
        """

        self._last_modification_time = last_modification_time

    @property
    def last_modifier_user_id(self):
        """Gets the last_modifier_user_id of this AssetDto.  # noqa: E501


        :return: The last_modifier_user_id of this AssetDto.  # noqa: E501
        :rtype: int
        """
        return self._last_modifier_user_id

    @last_modifier_user_id.setter
    def last_modifier_user_id(self, last_modifier_user_id):
        """Sets the last_modifier_user_id of this AssetDto.


        :param last_modifier_user_id: The last_modifier_user_id of this AssetDto.  # noqa: E501
        :type: int
        """

        self._last_modifier_user_id = last_modifier_user_id

    @property
    def creation_time(self):
        """Gets the creation_time of this AssetDto.  # noqa: E501


        :return: The creation_time of this AssetDto.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this AssetDto.


        :param creation_time: The creation_time of this AssetDto.  # noqa: E501
        :type: datetime
        """

        self._creation_time = creation_time

    @property
    def creator_user_id(self):
        """Gets the creator_user_id of this AssetDto.  # noqa: E501


        :return: The creator_user_id of this AssetDto.  # noqa: E501
        :rtype: int
        """
        return self._creator_user_id

    @creator_user_id.setter
    def creator_user_id(self, creator_user_id):
        """Sets the creator_user_id of this AssetDto.


        :param creator_user_id: The creator_user_id of this AssetDto.  # noqa: E501
        :type: int
        """

        self._creator_user_id = creator_user_id

    @property
    def id(self):
        """Gets the id of this AssetDto.  # noqa: E501


        :return: The id of this AssetDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AssetDto.


        :param id: The id of this AssetDto.  # noqa: E501
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
        if issubclass(AssetDto, dict):
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
        if not isinstance(other, AssetDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AssetDto):
            return True

        return self.to_dict() != other.to_dict()
