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


class TestCaseDto(object):
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
        'enabled': 'bool',
        'definition_id': 'int',
        'definition': 'TestCaseDefinitionDto',
        'release_id': 'int',
        'version_number': 'str',
        'test_set_id': 'int',
        'test_set': 'TestSetDto',
        'last_modification_time': 'datetime',
        'last_modifier_user_id': 'int',
        'creation_time': 'datetime',
        'creator_user_id': 'int',
        'id': 'int'
    }

    attribute_map = {
        'enabled': 'Enabled',
        'definition_id': 'DefinitionId',
        'definition': 'Definition',
        'release_id': 'ReleaseId',
        'version_number': 'VersionNumber',
        'test_set_id': 'TestSetId',
        'test_set': 'TestSet',
        'last_modification_time': 'LastModificationTime',
        'last_modifier_user_id': 'LastModifierUserId',
        'creation_time': 'CreationTime',
        'creator_user_id': 'CreatorUserId',
        'id': 'Id'
    }

    def __init__(self, enabled=None, definition_id=None, definition=None, release_id=None, version_number=None, test_set_id=None, test_set=None, last_modification_time=None, last_modifier_user_id=None, creation_time=None, creator_user_id=None, id=None, _configuration=None):  # noqa: E501
        """TestCaseDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._enabled = None
        self._definition_id = None
        self._definition = None
        self._release_id = None
        self._version_number = None
        self._test_set_id = None
        self._test_set = None
        self._last_modification_time = None
        self._last_modifier_user_id = None
        self._creation_time = None
        self._creator_user_id = None
        self._id = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        self.definition_id = definition_id
        if definition is not None:
            self.definition = definition
        self.release_id = release_id
        self.version_number = version_number
        if test_set_id is not None:
            self.test_set_id = test_set_id
        if test_set is not None:
            self.test_set = test_set
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
    def enabled(self):
        """Gets the enabled of this TestCaseDto.  # noqa: E501


        :return: The enabled of this TestCaseDto.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this TestCaseDto.


        :param enabled: The enabled of this TestCaseDto.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def definition_id(self):
        """Gets the definition_id of this TestCaseDto.  # noqa: E501


        :return: The definition_id of this TestCaseDto.  # noqa: E501
        :rtype: int
        """
        return self._definition_id

    @definition_id.setter
    def definition_id(self, definition_id):
        """Sets the definition_id of this TestCaseDto.


        :param definition_id: The definition_id of this TestCaseDto.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and definition_id is None:
            raise ValueError("Invalid value for `definition_id`, must not be `None`")  # noqa: E501

        self._definition_id = definition_id

    @property
    def definition(self):
        """Gets the definition of this TestCaseDto.  # noqa: E501


        :return: The definition of this TestCaseDto.  # noqa: E501
        :rtype: TestCaseDefinitionDto
        """
        return self._definition

    @definition.setter
    def definition(self, definition):
        """Sets the definition of this TestCaseDto.


        :param definition: The definition of this TestCaseDto.  # noqa: E501
        :type: TestCaseDefinitionDto
        """

        self._definition = definition

    @property
    def release_id(self):
        """Gets the release_id of this TestCaseDto.  # noqa: E501


        :return: The release_id of this TestCaseDto.  # noqa: E501
        :rtype: int
        """
        return self._release_id

    @release_id.setter
    def release_id(self, release_id):
        """Sets the release_id of this TestCaseDto.


        :param release_id: The release_id of this TestCaseDto.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and release_id is None:
            raise ValueError("Invalid value for `release_id`, must not be `None`")  # noqa: E501

        self._release_id = release_id

    @property
    def version_number(self):
        """Gets the version_number of this TestCaseDto.  # noqa: E501


        :return: The version_number of this TestCaseDto.  # noqa: E501
        :rtype: str
        """
        return self._version_number

    @version_number.setter
    def version_number(self, version_number):
        """Sets the version_number of this TestCaseDto.


        :param version_number: The version_number of this TestCaseDto.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and version_number is None:
            raise ValueError("Invalid value for `version_number`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                version_number is not None and len(version_number) < 1):
            raise ValueError("Invalid value for `version_number`, length must be greater than or equal to `1`")  # noqa: E501

        self._version_number = version_number

    @property
    def test_set_id(self):
        """Gets the test_set_id of this TestCaseDto.  # noqa: E501


        :return: The test_set_id of this TestCaseDto.  # noqa: E501
        :rtype: int
        """
        return self._test_set_id

    @test_set_id.setter
    def test_set_id(self, test_set_id):
        """Sets the test_set_id of this TestCaseDto.


        :param test_set_id: The test_set_id of this TestCaseDto.  # noqa: E501
        :type: int
        """

        self._test_set_id = test_set_id

    @property
    def test_set(self):
        """Gets the test_set of this TestCaseDto.  # noqa: E501


        :return: The test_set of this TestCaseDto.  # noqa: E501
        :rtype: TestSetDto
        """
        return self._test_set

    @test_set.setter
    def test_set(self, test_set):
        """Sets the test_set of this TestCaseDto.


        :param test_set: The test_set of this TestCaseDto.  # noqa: E501
        :type: TestSetDto
        """

        self._test_set = test_set

    @property
    def last_modification_time(self):
        """Gets the last_modification_time of this TestCaseDto.  # noqa: E501


        :return: The last_modification_time of this TestCaseDto.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modification_time

    @last_modification_time.setter
    def last_modification_time(self, last_modification_time):
        """Sets the last_modification_time of this TestCaseDto.


        :param last_modification_time: The last_modification_time of this TestCaseDto.  # noqa: E501
        :type: datetime
        """

        self._last_modification_time = last_modification_time

    @property
    def last_modifier_user_id(self):
        """Gets the last_modifier_user_id of this TestCaseDto.  # noqa: E501


        :return: The last_modifier_user_id of this TestCaseDto.  # noqa: E501
        :rtype: int
        """
        return self._last_modifier_user_id

    @last_modifier_user_id.setter
    def last_modifier_user_id(self, last_modifier_user_id):
        """Sets the last_modifier_user_id of this TestCaseDto.


        :param last_modifier_user_id: The last_modifier_user_id of this TestCaseDto.  # noqa: E501
        :type: int
        """

        self._last_modifier_user_id = last_modifier_user_id

    @property
    def creation_time(self):
        """Gets the creation_time of this TestCaseDto.  # noqa: E501


        :return: The creation_time of this TestCaseDto.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this TestCaseDto.


        :param creation_time: The creation_time of this TestCaseDto.  # noqa: E501
        :type: datetime
        """

        self._creation_time = creation_time

    @property
    def creator_user_id(self):
        """Gets the creator_user_id of this TestCaseDto.  # noqa: E501


        :return: The creator_user_id of this TestCaseDto.  # noqa: E501
        :rtype: int
        """
        return self._creator_user_id

    @creator_user_id.setter
    def creator_user_id(self, creator_user_id):
        """Sets the creator_user_id of this TestCaseDto.


        :param creator_user_id: The creator_user_id of this TestCaseDto.  # noqa: E501
        :type: int
        """

        self._creator_user_id = creator_user_id

    @property
    def id(self):
        """Gets the id of this TestCaseDto.  # noqa: E501


        :return: The id of this TestCaseDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TestCaseDto.


        :param id: The id of this TestCaseDto.  # noqa: E501
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
        if issubclass(TestCaseDto, dict):
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
        if not isinstance(other, TestCaseDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TestCaseDto):
            return True

        return self.to_dict() != other.to_dict()
