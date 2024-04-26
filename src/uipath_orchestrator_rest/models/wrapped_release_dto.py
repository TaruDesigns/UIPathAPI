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


class WrappedReleaseDto(object):
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
        'process_key': 'str',
        'process_version': 'str',
        'process_type': 'str',
        'entry_point_id': 'str',
        'name': 'str',
        'description': 'str',
        'is_latest_version': 'bool',
        'tags': 'list[TagDto]',
        'environment_id': 'int',
        'environment': 'WrappedEnvironmentDto',
        'input_arguments': 'object'
    }

    attribute_map = {
        'id': 'Id',
        'key': 'Key',
        'process_key': 'ProcessKey',
        'process_version': 'ProcessVersion',
        'process_type': 'ProcessType',
        'entry_point_id': 'EntryPointId',
        'name': 'Name',
        'description': 'Description',
        'is_latest_version': 'IsLatestVersion',
        'tags': 'Tags',
        'environment_id': 'EnvironmentId',
        'environment': 'Environment',
        'input_arguments': 'InputArguments'
    }

    def __init__(self, id=None, key=None, process_key=None, process_version=None, process_type=None, entry_point_id=None, name=None, description=None, is_latest_version=None, tags=None, environment_id=None, environment=None, input_arguments=None, _configuration=None):  # noqa: E501
        """WrappedReleaseDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._key = None
        self._process_key = None
        self._process_version = None
        self._process_type = None
        self._entry_point_id = None
        self._name = None
        self._description = None
        self._is_latest_version = None
        self._tags = None
        self._environment_id = None
        self._environment = None
        self._input_arguments = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if key is not None:
            self.key = key
        if process_key is not None:
            self.process_key = process_key
        if process_version is not None:
            self.process_version = process_version
        if process_type is not None:
            self.process_type = process_type
        if entry_point_id is not None:
            self.entry_point_id = entry_point_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if is_latest_version is not None:
            self.is_latest_version = is_latest_version
        if tags is not None:
            self.tags = tags
        if environment_id is not None:
            self.environment_id = environment_id
        if environment is not None:
            self.environment = environment
        if input_arguments is not None:
            self.input_arguments = input_arguments

    @property
    def id(self):
        """Gets the id of this WrappedReleaseDto.  # noqa: E501


        :return: The id of this WrappedReleaseDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WrappedReleaseDto.


        :param id: The id of this WrappedReleaseDto.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def key(self):
        """Gets the key of this WrappedReleaseDto.  # noqa: E501


        :return: The key of this WrappedReleaseDto.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this WrappedReleaseDto.


        :param key: The key of this WrappedReleaseDto.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def process_key(self):
        """Gets the process_key of this WrappedReleaseDto.  # noqa: E501


        :return: The process_key of this WrappedReleaseDto.  # noqa: E501
        :rtype: str
        """
        return self._process_key

    @process_key.setter
    def process_key(self, process_key):
        """Sets the process_key of this WrappedReleaseDto.


        :param process_key: The process_key of this WrappedReleaseDto.  # noqa: E501
        :type: str
        """

        self._process_key = process_key

    @property
    def process_version(self):
        """Gets the process_version of this WrappedReleaseDto.  # noqa: E501


        :return: The process_version of this WrappedReleaseDto.  # noqa: E501
        :rtype: str
        """
        return self._process_version

    @process_version.setter
    def process_version(self, process_version):
        """Sets the process_version of this WrappedReleaseDto.


        :param process_version: The process_version of this WrappedReleaseDto.  # noqa: E501
        :type: str
        """

        self._process_version = process_version

    @property
    def process_type(self):
        """Gets the process_type of this WrappedReleaseDto.  # noqa: E501


        :return: The process_type of this WrappedReleaseDto.  # noqa: E501
        :rtype: str
        """
        return self._process_type

    @process_type.setter
    def process_type(self, process_type):
        """Sets the process_type of this WrappedReleaseDto.


        :param process_type: The process_type of this WrappedReleaseDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["Undefined", "Process", "TestAutomationProcess"]  # noqa: E501
        if (self._configuration.client_side_validation and
                process_type not in allowed_values):
            raise ValueError(
                "Invalid value for `process_type` ({0}), must be one of {1}"  # noqa: E501
                .format(process_type, allowed_values)
            )

        self._process_type = process_type

    @property
    def entry_point_id(self):
        """Gets the entry_point_id of this WrappedReleaseDto.  # noqa: E501


        :return: The entry_point_id of this WrappedReleaseDto.  # noqa: E501
        :rtype: str
        """
        return self._entry_point_id

    @entry_point_id.setter
    def entry_point_id(self, entry_point_id):
        """Sets the entry_point_id of this WrappedReleaseDto.


        :param entry_point_id: The entry_point_id of this WrappedReleaseDto.  # noqa: E501
        :type: str
        """

        self._entry_point_id = entry_point_id

    @property
    def name(self):
        """Gets the name of this WrappedReleaseDto.  # noqa: E501


        :return: The name of this WrappedReleaseDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WrappedReleaseDto.


        :param name: The name of this WrappedReleaseDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this WrappedReleaseDto.  # noqa: E501


        :return: The description of this WrappedReleaseDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WrappedReleaseDto.


        :param description: The description of this WrappedReleaseDto.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def is_latest_version(self):
        """Gets the is_latest_version of this WrappedReleaseDto.  # noqa: E501


        :return: The is_latest_version of this WrappedReleaseDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_latest_version

    @is_latest_version.setter
    def is_latest_version(self, is_latest_version):
        """Sets the is_latest_version of this WrappedReleaseDto.


        :param is_latest_version: The is_latest_version of this WrappedReleaseDto.  # noqa: E501
        :type: bool
        """

        self._is_latest_version = is_latest_version

    @property
    def tags(self):
        """Gets the tags of this WrappedReleaseDto.  # noqa: E501


        :return: The tags of this WrappedReleaseDto.  # noqa: E501
        :rtype: list[TagDto]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this WrappedReleaseDto.


        :param tags: The tags of this WrappedReleaseDto.  # noqa: E501
        :type: list[TagDto]
        """

        self._tags = tags

    @property
    def environment_id(self):
        """Gets the environment_id of this WrappedReleaseDto.  # noqa: E501


        :return: The environment_id of this WrappedReleaseDto.  # noqa: E501
        :rtype: int
        """
        return self._environment_id

    @environment_id.setter
    def environment_id(self, environment_id):
        """Sets the environment_id of this WrappedReleaseDto.


        :param environment_id: The environment_id of this WrappedReleaseDto.  # noqa: E501
        :type: int
        """

        self._environment_id = environment_id

    @property
    def environment(self):
        """Gets the environment of this WrappedReleaseDto.  # noqa: E501


        :return: The environment of this WrappedReleaseDto.  # noqa: E501
        :rtype: WrappedEnvironmentDto
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this WrappedReleaseDto.


        :param environment: The environment of this WrappedReleaseDto.  # noqa: E501
        :type: WrappedEnvironmentDto
        """

        self._environment = environment

    @property
    def input_arguments(self):
        """Gets the input_arguments of this WrappedReleaseDto.  # noqa: E501


        :return: The input_arguments of this WrappedReleaseDto.  # noqa: E501
        :rtype: object
        """
        return self._input_arguments

    @input_arguments.setter
    def input_arguments(self, input_arguments):
        """Sets the input_arguments of this WrappedReleaseDto.


        :param input_arguments: The input_arguments of this WrappedReleaseDto.  # noqa: E501
        :type: object
        """

        self._input_arguments = input_arguments

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
        if issubclass(WrappedReleaseDto, dict):
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
        if not isinstance(other, WrappedReleaseDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WrappedReleaseDto):
            return True

        return self.to_dict() != other.to_dict()