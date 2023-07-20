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


class TestSetDto(object):
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
        'description': 'str',
        'source_type': 'str',
        'organization_unit_id': 'int',
        'environment_id': 'int',
        'environment': 'TestEnvironmentDto',
        'test_case_count': 'int',
        'robot_id': 'int',
        'enable_coverage': 'bool',
        'packages': 'list[TestSetPackageDto]',
        'test_cases': 'list[TestCaseDto]',
        'input_arguments': 'list[TestSetInputArgumentDto]',
        'is_deleted': 'bool',
        'deleter_user_id': 'int',
        'deletion_time': 'datetime',
        'last_modification_time': 'datetime',
        'last_modifier_user_id': 'int',
        'creation_time': 'datetime',
        'creator_user_id': 'int',
        'id': 'int'
    }

    attribute_map = {
        'key': 'Key',
        'name': 'Name',
        'description': 'Description',
        'source_type': 'SourceType',
        'organization_unit_id': 'OrganizationUnitId',
        'environment_id': 'EnvironmentId',
        'environment': 'Environment',
        'test_case_count': 'TestCaseCount',
        'robot_id': 'RobotId',
        'enable_coverage': 'EnableCoverage',
        'packages': 'Packages',
        'test_cases': 'TestCases',
        'input_arguments': 'InputArguments',
        'is_deleted': 'IsDeleted',
        'deleter_user_id': 'DeleterUserId',
        'deletion_time': 'DeletionTime',
        'last_modification_time': 'LastModificationTime',
        'last_modifier_user_id': 'LastModifierUserId',
        'creation_time': 'CreationTime',
        'creator_user_id': 'CreatorUserId',
        'id': 'Id'
    }

    def __init__(self, key=None, name=None, description=None, source_type=None, organization_unit_id=None, environment_id=None, environment=None, test_case_count=None, robot_id=None, enable_coverage=None, packages=None, test_cases=None, input_arguments=None, is_deleted=None, deleter_user_id=None, deletion_time=None, last_modification_time=None, last_modifier_user_id=None, creation_time=None, creator_user_id=None, id=None, _configuration=None):  # noqa: E501
        """TestSetDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._key = None
        self._name = None
        self._description = None
        self._source_type = None
        self._organization_unit_id = None
        self._environment_id = None
        self._environment = None
        self._test_case_count = None
        self._robot_id = None
        self._enable_coverage = None
        self._packages = None
        self._test_cases = None
        self._input_arguments = None
        self._is_deleted = None
        self._deleter_user_id = None
        self._deletion_time = None
        self._last_modification_time = None
        self._last_modifier_user_id = None
        self._creation_time = None
        self._creator_user_id = None
        self._id = None
        self.discriminator = None

        if key is not None:
            self.key = key
        self.name = name
        if description is not None:
            self.description = description
        if source_type is not None:
            self.source_type = source_type
        if organization_unit_id is not None:
            self.organization_unit_id = organization_unit_id
        if environment_id is not None:
            self.environment_id = environment_id
        if environment is not None:
            self.environment = environment
        if test_case_count is not None:
            self.test_case_count = test_case_count
        if robot_id is not None:
            self.robot_id = robot_id
        if enable_coverage is not None:
            self.enable_coverage = enable_coverage
        self.packages = packages
        self.test_cases = test_cases
        if input_arguments is not None:
            self.input_arguments = input_arguments
        if is_deleted is not None:
            self.is_deleted = is_deleted
        if deleter_user_id is not None:
            self.deleter_user_id = deleter_user_id
        if deletion_time is not None:
            self.deletion_time = deletion_time
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
        """Gets the key of this TestSetDto.  # noqa: E501


        :return: The key of this TestSetDto.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this TestSetDto.


        :param key: The key of this TestSetDto.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def name(self):
        """Gets the name of this TestSetDto.  # noqa: E501


        :return: The name of this TestSetDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TestSetDto.


        :param name: The name of this TestSetDto.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this TestSetDto.  # noqa: E501


        :return: The description of this TestSetDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TestSetDto.


        :param description: The description of this TestSetDto.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def source_type(self):
        """Gets the source_type of this TestSetDto.  # noqa: E501


        :return: The source_type of this TestSetDto.  # noqa: E501
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this TestSetDto.


        :param source_type: The source_type of this TestSetDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["User", "ExternalTool", "Transient"]  # noqa: E501
        if (self._configuration.client_side_validation and
                source_type not in allowed_values):
            raise ValueError(
                "Invalid value for `source_type` ({0}), must be one of {1}"  # noqa: E501
                .format(source_type, allowed_values)
            )

        self._source_type = source_type

    @property
    def organization_unit_id(self):
        """Gets the organization_unit_id of this TestSetDto.  # noqa: E501


        :return: The organization_unit_id of this TestSetDto.  # noqa: E501
        :rtype: int
        """
        return self._organization_unit_id

    @organization_unit_id.setter
    def organization_unit_id(self, organization_unit_id):
        """Sets the organization_unit_id of this TestSetDto.


        :param organization_unit_id: The organization_unit_id of this TestSetDto.  # noqa: E501
        :type: int
        """

        self._organization_unit_id = organization_unit_id

    @property
    def environment_id(self):
        """Gets the environment_id of this TestSetDto.  # noqa: E501


        :return: The environment_id of this TestSetDto.  # noqa: E501
        :rtype: int
        """
        return self._environment_id

    @environment_id.setter
    def environment_id(self, environment_id):
        """Sets the environment_id of this TestSetDto.


        :param environment_id: The environment_id of this TestSetDto.  # noqa: E501
        :type: int
        """

        self._environment_id = environment_id

    @property
    def environment(self):
        """Gets the environment of this TestSetDto.  # noqa: E501


        :return: The environment of this TestSetDto.  # noqa: E501
        :rtype: TestEnvironmentDto
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this TestSetDto.


        :param environment: The environment of this TestSetDto.  # noqa: E501
        :type: TestEnvironmentDto
        """

        self._environment = environment

    @property
    def test_case_count(self):
        """Gets the test_case_count of this TestSetDto.  # noqa: E501


        :return: The test_case_count of this TestSetDto.  # noqa: E501
        :rtype: int
        """
        return self._test_case_count

    @test_case_count.setter
    def test_case_count(self, test_case_count):
        """Sets the test_case_count of this TestSetDto.


        :param test_case_count: The test_case_count of this TestSetDto.  # noqa: E501
        :type: int
        """

        self._test_case_count = test_case_count

    @property
    def robot_id(self):
        """Gets the robot_id of this TestSetDto.  # noqa: E501


        :return: The robot_id of this TestSetDto.  # noqa: E501
        :rtype: int
        """
        return self._robot_id

    @robot_id.setter
    def robot_id(self, robot_id):
        """Sets the robot_id of this TestSetDto.


        :param robot_id: The robot_id of this TestSetDto.  # noqa: E501
        :type: int
        """

        self._robot_id = robot_id

    @property
    def enable_coverage(self):
        """Gets the enable_coverage of this TestSetDto.  # noqa: E501


        :return: The enable_coverage of this TestSetDto.  # noqa: E501
        :rtype: bool
        """
        return self._enable_coverage

    @enable_coverage.setter
    def enable_coverage(self, enable_coverage):
        """Sets the enable_coverage of this TestSetDto.


        :param enable_coverage: The enable_coverage of this TestSetDto.  # noqa: E501
        :type: bool
        """

        self._enable_coverage = enable_coverage

    @property
    def packages(self):
        """Gets the packages of this TestSetDto.  # noqa: E501


        :return: The packages of this TestSetDto.  # noqa: E501
        :rtype: list[TestSetPackageDto]
        """
        return self._packages

    @packages.setter
    def packages(self, packages):
        """Sets the packages of this TestSetDto.


        :param packages: The packages of this TestSetDto.  # noqa: E501
        :type: list[TestSetPackageDto]
        """
        if self._configuration.client_side_validation and packages is None:
            raise ValueError("Invalid value for `packages`, must not be `None`")  # noqa: E501

        self._packages = packages

    @property
    def test_cases(self):
        """Gets the test_cases of this TestSetDto.  # noqa: E501


        :return: The test_cases of this TestSetDto.  # noqa: E501
        :rtype: list[TestCaseDto]
        """
        return self._test_cases

    @test_cases.setter
    def test_cases(self, test_cases):
        """Sets the test_cases of this TestSetDto.


        :param test_cases: The test_cases of this TestSetDto.  # noqa: E501
        :type: list[TestCaseDto]
        """
        if self._configuration.client_side_validation and test_cases is None:
            raise ValueError("Invalid value for `test_cases`, must not be `None`")  # noqa: E501

        self._test_cases = test_cases

    @property
    def input_arguments(self):
        """Gets the input_arguments of this TestSetDto.  # noqa: E501


        :return: The input_arguments of this TestSetDto.  # noqa: E501
        :rtype: list[TestSetInputArgumentDto]
        """
        return self._input_arguments

    @input_arguments.setter
    def input_arguments(self, input_arguments):
        """Sets the input_arguments of this TestSetDto.


        :param input_arguments: The input_arguments of this TestSetDto.  # noqa: E501
        :type: list[TestSetInputArgumentDto]
        """

        self._input_arguments = input_arguments

    @property
    def is_deleted(self):
        """Gets the is_deleted of this TestSetDto.  # noqa: E501


        :return: The is_deleted of this TestSetDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        """Sets the is_deleted of this TestSetDto.


        :param is_deleted: The is_deleted of this TestSetDto.  # noqa: E501
        :type: bool
        """

        self._is_deleted = is_deleted

    @property
    def deleter_user_id(self):
        """Gets the deleter_user_id of this TestSetDto.  # noqa: E501


        :return: The deleter_user_id of this TestSetDto.  # noqa: E501
        :rtype: int
        """
        return self._deleter_user_id

    @deleter_user_id.setter
    def deleter_user_id(self, deleter_user_id):
        """Sets the deleter_user_id of this TestSetDto.


        :param deleter_user_id: The deleter_user_id of this TestSetDto.  # noqa: E501
        :type: int
        """

        self._deleter_user_id = deleter_user_id

    @property
    def deletion_time(self):
        """Gets the deletion_time of this TestSetDto.  # noqa: E501


        :return: The deletion_time of this TestSetDto.  # noqa: E501
        :rtype: datetime
        """
        return self._deletion_time

    @deletion_time.setter
    def deletion_time(self, deletion_time):
        """Sets the deletion_time of this TestSetDto.


        :param deletion_time: The deletion_time of this TestSetDto.  # noqa: E501
        :type: datetime
        """

        self._deletion_time = deletion_time

    @property
    def last_modification_time(self):
        """Gets the last_modification_time of this TestSetDto.  # noqa: E501


        :return: The last_modification_time of this TestSetDto.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modification_time

    @last_modification_time.setter
    def last_modification_time(self, last_modification_time):
        """Sets the last_modification_time of this TestSetDto.


        :param last_modification_time: The last_modification_time of this TestSetDto.  # noqa: E501
        :type: datetime
        """

        self._last_modification_time = last_modification_time

    @property
    def last_modifier_user_id(self):
        """Gets the last_modifier_user_id of this TestSetDto.  # noqa: E501


        :return: The last_modifier_user_id of this TestSetDto.  # noqa: E501
        :rtype: int
        """
        return self._last_modifier_user_id

    @last_modifier_user_id.setter
    def last_modifier_user_id(self, last_modifier_user_id):
        """Sets the last_modifier_user_id of this TestSetDto.


        :param last_modifier_user_id: The last_modifier_user_id of this TestSetDto.  # noqa: E501
        :type: int
        """

        self._last_modifier_user_id = last_modifier_user_id

    @property
    def creation_time(self):
        """Gets the creation_time of this TestSetDto.  # noqa: E501


        :return: The creation_time of this TestSetDto.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this TestSetDto.


        :param creation_time: The creation_time of this TestSetDto.  # noqa: E501
        :type: datetime
        """

        self._creation_time = creation_time

    @property
    def creator_user_id(self):
        """Gets the creator_user_id of this TestSetDto.  # noqa: E501


        :return: The creator_user_id of this TestSetDto.  # noqa: E501
        :rtype: int
        """
        return self._creator_user_id

    @creator_user_id.setter
    def creator_user_id(self, creator_user_id):
        """Sets the creator_user_id of this TestSetDto.


        :param creator_user_id: The creator_user_id of this TestSetDto.  # noqa: E501
        :type: int
        """

        self._creator_user_id = creator_user_id

    @property
    def id(self):
        """Gets the id of this TestSetDto.  # noqa: E501


        :return: The id of this TestSetDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TestSetDto.


        :param id: The id of this TestSetDto.  # noqa: E501
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
        if issubclass(TestSetDto, dict):
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
        if not isinstance(other, TestSetDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TestSetDto):
            return True

        return self.to_dict() != other.to_dict()
