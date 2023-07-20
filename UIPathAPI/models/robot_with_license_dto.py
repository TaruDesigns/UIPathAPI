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


class RobotWithLicenseDto(object):
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
        'license': 'RobotLicenseDto',
        'user': 'UserDto',
        'license_key': 'str',
        'machine_name': 'str',
        'machine_id': 'int',
        'name': 'str',
        'username': 'str',
        'external_name': 'str',
        'description': 'str',
        'type': 'str',
        'hosting_type': 'str',
        'provision_type': 'str',
        'password': 'str',
        'credential_store_id': 'int',
        'user_id': 'int',
        'enabled': 'bool',
        'credential_type': 'str',
        'environments': 'list[EnvironmentDto]',
        'robot_environments': 'str',
        'execution_settings': 'dict(str, object)',
        'is_external_licensed': 'bool',
        'limit_concurrent_execution': 'bool',
        'last_modification_time': 'datetime',
        'last_modifier_user_id': 'int',
        'creation_time': 'datetime',
        'creator_user_id': 'int',
        'id': 'int'
    }

    attribute_map = {
        'license': 'License',
        'user': 'User',
        'license_key': 'LicenseKey',
        'machine_name': 'MachineName',
        'machine_id': 'MachineId',
        'name': 'Name',
        'username': 'Username',
        'external_name': 'ExternalName',
        'description': 'Description',
        'type': 'Type',
        'hosting_type': 'HostingType',
        'provision_type': 'ProvisionType',
        'password': 'Password',
        'credential_store_id': 'CredentialStoreId',
        'user_id': 'UserId',
        'enabled': 'Enabled',
        'credential_type': 'CredentialType',
        'environments': 'Environments',
        'robot_environments': 'RobotEnvironments',
        'execution_settings': 'ExecutionSettings',
        'is_external_licensed': 'IsExternalLicensed',
        'limit_concurrent_execution': 'LimitConcurrentExecution',
        'last_modification_time': 'LastModificationTime',
        'last_modifier_user_id': 'LastModifierUserId',
        'creation_time': 'CreationTime',
        'creator_user_id': 'CreatorUserId',
        'id': 'Id'
    }

    def __init__(self, license=None, user=None, license_key=None, machine_name=None, machine_id=None, name=None, username=None, external_name=None, description=None, type=None, hosting_type=None, provision_type=None, password=None, credential_store_id=None, user_id=None, enabled=None, credential_type=None, environments=None, robot_environments=None, execution_settings=None, is_external_licensed=None, limit_concurrent_execution=None, last_modification_time=None, last_modifier_user_id=None, creation_time=None, creator_user_id=None, id=None, _configuration=None):  # noqa: E501
        """RobotWithLicenseDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._license = None
        self._user = None
        self._license_key = None
        self._machine_name = None
        self._machine_id = None
        self._name = None
        self._username = None
        self._external_name = None
        self._description = None
        self._type = None
        self._hosting_type = None
        self._provision_type = None
        self._password = None
        self._credential_store_id = None
        self._user_id = None
        self._enabled = None
        self._credential_type = None
        self._environments = None
        self._robot_environments = None
        self._execution_settings = None
        self._is_external_licensed = None
        self._limit_concurrent_execution = None
        self._last_modification_time = None
        self._last_modifier_user_id = None
        self._creation_time = None
        self._creator_user_id = None
        self._id = None
        self.discriminator = None

        if license is not None:
            self.license = license
        if user is not None:
            self.user = user
        if license_key is not None:
            self.license_key = license_key
        if machine_name is not None:
            self.machine_name = machine_name
        if machine_id is not None:
            self.machine_id = machine_id
        self.name = name
        if username is not None:
            self.username = username
        if external_name is not None:
            self.external_name = external_name
        if description is not None:
            self.description = description
        self.type = type
        self.hosting_type = hosting_type
        if provision_type is not None:
            self.provision_type = provision_type
        if password is not None:
            self.password = password
        if credential_store_id is not None:
            self.credential_store_id = credential_store_id
        if user_id is not None:
            self.user_id = user_id
        if enabled is not None:
            self.enabled = enabled
        if credential_type is not None:
            self.credential_type = credential_type
        if environments is not None:
            self.environments = environments
        if robot_environments is not None:
            self.robot_environments = robot_environments
        if execution_settings is not None:
            self.execution_settings = execution_settings
        if is_external_licensed is not None:
            self.is_external_licensed = is_external_licensed
        if limit_concurrent_execution is not None:
            self.limit_concurrent_execution = limit_concurrent_execution
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
    def license(self):
        """Gets the license of this RobotWithLicenseDto.  # noqa: E501


        :return: The license of this RobotWithLicenseDto.  # noqa: E501
        :rtype: RobotLicenseDto
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this RobotWithLicenseDto.


        :param license: The license of this RobotWithLicenseDto.  # noqa: E501
        :type: RobotLicenseDto
        """

        self._license = license

    @property
    def user(self):
        """Gets the user of this RobotWithLicenseDto.  # noqa: E501


        :return: The user of this RobotWithLicenseDto.  # noqa: E501
        :rtype: UserDto
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this RobotWithLicenseDto.


        :param user: The user of this RobotWithLicenseDto.  # noqa: E501
        :type: UserDto
        """

        self._user = user

    @property
    def license_key(self):
        """Gets the license_key of this RobotWithLicenseDto.  # noqa: E501

        The key is automatically generated from the server for the Robot machine.  <para />For the robot to work, the same key must exist on both the robot and Orchestrator.  <para />All robots on a machine must have the same license key in order to register correctly.  # noqa: E501

        :return: The license_key of this RobotWithLicenseDto.  # noqa: E501
        :rtype: str
        """
        return self._license_key

    @license_key.setter
    def license_key(self, license_key):
        """Sets the license_key of this RobotWithLicenseDto.

        The key is automatically generated from the server for the Robot machine.  <para />For the robot to work, the same key must exist on both the robot and Orchestrator.  <para />All robots on a machine must have the same license key in order to register correctly.  # noqa: E501

        :param license_key: The license_key of this RobotWithLicenseDto.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                license_key is not None and len(license_key) > 255):
            raise ValueError("Invalid value for `license_key`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                license_key is not None and len(license_key) < 0):
            raise ValueError("Invalid value for `license_key`, length must be greater than or equal to `0`")  # noqa: E501

        self._license_key = license_key

    @property
    def machine_name(self):
        """Gets the machine_name of this RobotWithLicenseDto.  # noqa: E501

        The name of the machine a Robot is hosted on.  # noqa: E501

        :return: The machine_name of this RobotWithLicenseDto.  # noqa: E501
        :rtype: str
        """
        return self._machine_name

    @machine_name.setter
    def machine_name(self, machine_name):
        """Sets the machine_name of this RobotWithLicenseDto.

        The name of the machine a Robot is hosted on.  # noqa: E501

        :param machine_name: The machine_name of this RobotWithLicenseDto.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                machine_name is not None and len(machine_name) > 450):
            raise ValueError("Invalid value for `machine_name`, length must be less than or equal to `450`")  # noqa: E501
        if (self._configuration.client_side_validation and
                machine_name is not None and len(machine_name) < 0):
            raise ValueError("Invalid value for `machine_name`, length must be greater than or equal to `0`")  # noqa: E501

        self._machine_name = machine_name

    @property
    def machine_id(self):
        """Gets the machine_id of this RobotWithLicenseDto.  # noqa: E501

        The Id of the machine a Robot is hosted on  # noqa: E501

        :return: The machine_id of this RobotWithLicenseDto.  # noqa: E501
        :rtype: int
        """
        return self._machine_id

    @machine_id.setter
    def machine_id(self, machine_id):
        """Sets the machine_id of this RobotWithLicenseDto.

        The Id of the machine a Robot is hosted on  # noqa: E501

        :param machine_id: The machine_id of this RobotWithLicenseDto.  # noqa: E501
        :type: int
        """

        self._machine_id = machine_id

    @property
    def name(self):
        """Gets the name of this RobotWithLicenseDto.  # noqa: E501

        A custom name for the robot.  # noqa: E501

        :return: The name of this RobotWithLicenseDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RobotWithLicenseDto.

        A custom name for the robot.  # noqa: E501

        :param name: The name of this RobotWithLicenseDto.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and len(name) > 19):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `19`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and len(name) < 0):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501

        self._name = name

    @property
    def username(self):
        """Gets the username of this RobotWithLicenseDto.  # noqa: E501

        The machine username. If the user is under a domain, you are required to also specify it in a DOMAIN\\username format.  <para />Note: You must use short domain names, such as desktop\\administrator and NOT desktop.local/administrator.  # noqa: E501

        :return: The username of this RobotWithLicenseDto.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this RobotWithLicenseDto.

        The machine username. If the user is under a domain, you are required to also specify it in a DOMAIN\\username format.  <para />Note: You must use short domain names, such as desktop\\administrator and NOT desktop.local/administrator.  # noqa: E501

        :param username: The username of this RobotWithLicenseDto.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                username is not None and len(username) > 100):
            raise ValueError("Invalid value for `username`, length must be less than or equal to `100`")  # noqa: E501
        if (self._configuration.client_side_validation and
                username is not None and len(username) < 0):
            raise ValueError("Invalid value for `username`, length must be greater than or equal to `0`")  # noqa: E501

        self._username = username

    @property
    def external_name(self):
        """Gets the external_name of this RobotWithLicenseDto.  # noqa: E501

        Contains the value of the key in the external store used to store the password.  # noqa: E501

        :return: The external_name of this RobotWithLicenseDto.  # noqa: E501
        :rtype: str
        """
        return self._external_name

    @external_name.setter
    def external_name(self, external_name):
        """Sets the external_name of this RobotWithLicenseDto.

        Contains the value of the key in the external store used to store the password.  # noqa: E501

        :param external_name: The external_name of this RobotWithLicenseDto.  # noqa: E501
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
    def description(self):
        """Gets the description of this RobotWithLicenseDto.  # noqa: E501

        Used to add additional information about a robot in order to better identify it.  # noqa: E501

        :return: The description of this RobotWithLicenseDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RobotWithLicenseDto.

        Used to add additional information about a robot in order to better identify it.  # noqa: E501

        :param description: The description of this RobotWithLicenseDto.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                description is not None and len(description) > 500):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `500`")  # noqa: E501
        if (self._configuration.client_side_validation and
                description is not None and len(description) < 0):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def type(self):
        """Gets the type of this RobotWithLicenseDto.  # noqa: E501

        The Robot type.  # noqa: E501

        :return: The type of this RobotWithLicenseDto.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RobotWithLicenseDto.

        The Robot type.  # noqa: E501

        :param type: The type of this RobotWithLicenseDto.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["NonProduction", "Attended", "Unattended", "Development", "Studio", "RpaDeveloper", "StudioX", "CitizenDeveloper", "Headless", "RpaDeveloperPro", "StudioPro", "TestAutomation", "AutomationCloud", "Serverless", "AutomationKit", "ServerlessTestAutomation", "AutomationCloudTestAutomation", "AttendedStudioWeb"]  # noqa: E501
        if (self._configuration.client_side_validation and
                type not in allowed_values):
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def hosting_type(self):
        """Gets the hosting_type of this RobotWithLicenseDto.  # noqa: E501

        The Robot hosting type (Standard / Floating).  # noqa: E501

        :return: The hosting_type of this RobotWithLicenseDto.  # noqa: E501
        :rtype: str
        """
        return self._hosting_type

    @hosting_type.setter
    def hosting_type(self, hosting_type):
        """Sets the hosting_type of this RobotWithLicenseDto.

        The Robot hosting type (Standard / Floating).  # noqa: E501

        :param hosting_type: The hosting_type of this RobotWithLicenseDto.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and hosting_type is None:
            raise ValueError("Invalid value for `hosting_type`, must not be `None`")  # noqa: E501
        allowed_values = ["Standard", "Floating"]  # noqa: E501
        if (self._configuration.client_side_validation and
                hosting_type not in allowed_values):
            raise ValueError(
                "Invalid value for `hosting_type` ({0}), must be one of {1}"  # noqa: E501
                .format(hosting_type, allowed_values)
            )

        self._hosting_type = hosting_type

    @property
    def provision_type(self):
        """Gets the provision_type of this RobotWithLicenseDto.  # noqa: E501

        The Robot provision type.  # noqa: E501

        :return: The provision_type of this RobotWithLicenseDto.  # noqa: E501
        :rtype: str
        """
        return self._provision_type

    @provision_type.setter
    def provision_type(self, provision_type):
        """Sets the provision_type of this RobotWithLicenseDto.

        The Robot provision type.  # noqa: E501

        :param provision_type: The provision_type of this RobotWithLicenseDto.  # noqa: E501
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
    def password(self):
        """Gets the password of this RobotWithLicenseDto.  # noqa: E501

        The Windows password associated with the machine username.  # noqa: E501

        :return: The password of this RobotWithLicenseDto.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this RobotWithLicenseDto.

        The Windows password associated with the machine username.  # noqa: E501

        :param password: The password of this RobotWithLicenseDto.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                password is not None and len(password) > 100):
            raise ValueError("Invalid value for `password`, length must be less than or equal to `100`")  # noqa: E501
        if (self._configuration.client_side_validation and
                password is not None and len(password) < 0):
            raise ValueError("Invalid value for `password`, length must be greater than or equal to `0`")  # noqa: E501

        self._password = password

    @property
    def credential_store_id(self):
        """Gets the credential_store_id of this RobotWithLicenseDto.  # noqa: E501

        The Credential Store used to store the password.  # noqa: E501

        :return: The credential_store_id of this RobotWithLicenseDto.  # noqa: E501
        :rtype: int
        """
        return self._credential_store_id

    @credential_store_id.setter
    def credential_store_id(self, credential_store_id):
        """Sets the credential_store_id of this RobotWithLicenseDto.

        The Credential Store used to store the password.  # noqa: E501

        :param credential_store_id: The credential_store_id of this RobotWithLicenseDto.  # noqa: E501
        :type: int
        """

        self._credential_store_id = credential_store_id

    @property
    def user_id(self):
        """Gets the user_id of this RobotWithLicenseDto.  # noqa: E501

        The associated user's Id.  # noqa: E501

        :return: The user_id of this RobotWithLicenseDto.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this RobotWithLicenseDto.

        The associated user's Id.  # noqa: E501

        :param user_id: The user_id of this RobotWithLicenseDto.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def enabled(self):
        """Gets the enabled of this RobotWithLicenseDto.  # noqa: E501

        Specificies the state of the Robot (enabled/disabled) - a disabled robot cannot connect to Orchestrator  # noqa: E501

        :return: The enabled of this RobotWithLicenseDto.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this RobotWithLicenseDto.

        Specificies the state of the Robot (enabled/disabled) - a disabled robot cannot connect to Orchestrator  # noqa: E501

        :param enabled: The enabled of this RobotWithLicenseDto.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def credential_type(self):
        """Gets the credential_type of this RobotWithLicenseDto.  # noqa: E501

        The robot credentials type (Default/ SmartCard)  # noqa: E501

        :return: The credential_type of this RobotWithLicenseDto.  # noqa: E501
        :rtype: str
        """
        return self._credential_type

    @credential_type.setter
    def credential_type(self, credential_type):
        """Sets the credential_type of this RobotWithLicenseDto.

        The robot credentials type (Default/ SmartCard)  # noqa: E501

        :param credential_type: The credential_type of this RobotWithLicenseDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["Default", "SmartCard", "NCipher", "SafeNet", "NoCredential"]  # noqa: E501
        if (self._configuration.client_side_validation and
                credential_type not in allowed_values):
            raise ValueError(
                "Invalid value for `credential_type` ({0}), must be one of {1}"  # noqa: E501
                .format(credential_type, allowed_values)
            )

        self._credential_type = credential_type

    @property
    def environments(self):
        """Gets the environments of this RobotWithLicenseDto.  # noqa: E501

        The collection of environments the robot is part of.  # noqa: E501

        :return: The environments of this RobotWithLicenseDto.  # noqa: E501
        :rtype: list[EnvironmentDto]
        """
        return self._environments

    @environments.setter
    def environments(self, environments):
        """Sets the environments of this RobotWithLicenseDto.

        The collection of environments the robot is part of.  # noqa: E501

        :param environments: The environments of this RobotWithLicenseDto.  # noqa: E501
        :type: list[EnvironmentDto]
        """

        self._environments = environments

    @property
    def robot_environments(self):
        """Gets the robot_environments of this RobotWithLicenseDto.  # noqa: E501

        The comma separated textual representation of environment names the robot is part of.  # noqa: E501

        :return: The robot_environments of this RobotWithLicenseDto.  # noqa: E501
        :rtype: str
        """
        return self._robot_environments

    @robot_environments.setter
    def robot_environments(self, robot_environments):
        """Sets the robot_environments of this RobotWithLicenseDto.

        The comma separated textual representation of environment names the robot is part of.  # noqa: E501

        :param robot_environments: The robot_environments of this RobotWithLicenseDto.  # noqa: E501
        :type: str
        """

        self._robot_environments = robot_environments

    @property
    def execution_settings(self):
        """Gets the execution_settings of this RobotWithLicenseDto.  # noqa: E501

        A collection of key value pairs containing execution settings for this robot.  # noqa: E501

        :return: The execution_settings of this RobotWithLicenseDto.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._execution_settings

    @execution_settings.setter
    def execution_settings(self, execution_settings):
        """Sets the execution_settings of this RobotWithLicenseDto.

        A collection of key value pairs containing execution settings for this robot.  # noqa: E501

        :param execution_settings: The execution_settings of this RobotWithLicenseDto.  # noqa: E501
        :type: dict(str, object)
        """

        self._execution_settings = execution_settings

    @property
    def is_external_licensed(self):
        """Gets the is_external_licensed of this RobotWithLicenseDto.  # noqa: E501

        Flag to indicate if the robot uses an external license  # noqa: E501

        :return: The is_external_licensed of this RobotWithLicenseDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_external_licensed

    @is_external_licensed.setter
    def is_external_licensed(self, is_external_licensed):
        """Sets the is_external_licensed of this RobotWithLicenseDto.

        Flag to indicate if the robot uses an external license  # noqa: E501

        :param is_external_licensed: The is_external_licensed of this RobotWithLicenseDto.  # noqa: E501
        :type: bool
        """

        self._is_external_licensed = is_external_licensed

    @property
    def limit_concurrent_execution(self):
        """Gets the limit_concurrent_execution of this RobotWithLicenseDto.  # noqa: E501

        Specifies if the robot can be used concurrently on multiple machines  # noqa: E501

        :return: The limit_concurrent_execution of this RobotWithLicenseDto.  # noqa: E501
        :rtype: bool
        """
        return self._limit_concurrent_execution

    @limit_concurrent_execution.setter
    def limit_concurrent_execution(self, limit_concurrent_execution):
        """Sets the limit_concurrent_execution of this RobotWithLicenseDto.

        Specifies if the robot can be used concurrently on multiple machines  # noqa: E501

        :param limit_concurrent_execution: The limit_concurrent_execution of this RobotWithLicenseDto.  # noqa: E501
        :type: bool
        """

        self._limit_concurrent_execution = limit_concurrent_execution

    @property
    def last_modification_time(self):
        """Gets the last_modification_time of this RobotWithLicenseDto.  # noqa: E501


        :return: The last_modification_time of this RobotWithLicenseDto.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modification_time

    @last_modification_time.setter
    def last_modification_time(self, last_modification_time):
        """Sets the last_modification_time of this RobotWithLicenseDto.


        :param last_modification_time: The last_modification_time of this RobotWithLicenseDto.  # noqa: E501
        :type: datetime
        """

        self._last_modification_time = last_modification_time

    @property
    def last_modifier_user_id(self):
        """Gets the last_modifier_user_id of this RobotWithLicenseDto.  # noqa: E501


        :return: The last_modifier_user_id of this RobotWithLicenseDto.  # noqa: E501
        :rtype: int
        """
        return self._last_modifier_user_id

    @last_modifier_user_id.setter
    def last_modifier_user_id(self, last_modifier_user_id):
        """Sets the last_modifier_user_id of this RobotWithLicenseDto.


        :param last_modifier_user_id: The last_modifier_user_id of this RobotWithLicenseDto.  # noqa: E501
        :type: int
        """

        self._last_modifier_user_id = last_modifier_user_id

    @property
    def creation_time(self):
        """Gets the creation_time of this RobotWithLicenseDto.  # noqa: E501


        :return: The creation_time of this RobotWithLicenseDto.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this RobotWithLicenseDto.


        :param creation_time: The creation_time of this RobotWithLicenseDto.  # noqa: E501
        :type: datetime
        """

        self._creation_time = creation_time

    @property
    def creator_user_id(self):
        """Gets the creator_user_id of this RobotWithLicenseDto.  # noqa: E501


        :return: The creator_user_id of this RobotWithLicenseDto.  # noqa: E501
        :rtype: int
        """
        return self._creator_user_id

    @creator_user_id.setter
    def creator_user_id(self, creator_user_id):
        """Sets the creator_user_id of this RobotWithLicenseDto.


        :param creator_user_id: The creator_user_id of this RobotWithLicenseDto.  # noqa: E501
        :type: int
        """

        self._creator_user_id = creator_user_id

    @property
    def id(self):
        """Gets the id of this RobotWithLicenseDto.  # noqa: E501


        :return: The id of this RobotWithLicenseDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RobotWithLicenseDto.


        :param id: The id of this RobotWithLicenseDto.  # noqa: E501
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
        if issubclass(RobotWithLicenseDto, dict):
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
        if not isinstance(other, RobotWithLicenseDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RobotWithLicenseDto):
            return True

        return self.to_dict() != other.to_dict()
