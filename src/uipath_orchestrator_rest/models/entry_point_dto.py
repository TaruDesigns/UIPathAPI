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


class EntryPointDto(object):
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
        'unique_id': 'str',
        'path': 'str',
        'input_arguments': 'str',
        'output_arguments': 'str',
        'data_variation': 'EntryPointDataVariationDto',
        'id': 'int'
    }

    attribute_map = {
        'unique_id': 'UniqueId',
        'path': 'Path',
        'input_arguments': 'InputArguments',
        'output_arguments': 'OutputArguments',
        'data_variation': 'DataVariation',
        'id': 'Id'
    }

    def __init__(self, unique_id=None, path=None, input_arguments=None, output_arguments=None, data_variation=None, id=None, _configuration=None):  # noqa: E501
        """EntryPointDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._unique_id = None
        self._path = None
        self._input_arguments = None
        self._output_arguments = None
        self._data_variation = None
        self._id = None
        self.discriminator = None

        if unique_id is not None:
            self.unique_id = unique_id
        if path is not None:
            self.path = path
        if input_arguments is not None:
            self.input_arguments = input_arguments
        if output_arguments is not None:
            self.output_arguments = output_arguments
        if data_variation is not None:
            self.data_variation = data_variation
        if id is not None:
            self.id = id

    @property
    def unique_id(self):
        """Gets the unique_id of this EntryPointDto.  # noqa: E501


        :return: The unique_id of this EntryPointDto.  # noqa: E501
        :rtype: str
        """
        return self._unique_id

    @unique_id.setter
    def unique_id(self, unique_id):
        """Sets the unique_id of this EntryPointDto.


        :param unique_id: The unique_id of this EntryPointDto.  # noqa: E501
        :type: str
        """

        self._unique_id = unique_id

    @property
    def path(self):
        """Gets the path of this EntryPointDto.  # noqa: E501


        :return: The path of this EntryPointDto.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this EntryPointDto.


        :param path: The path of this EntryPointDto.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def input_arguments(self):
        """Gets the input_arguments of this EntryPointDto.  # noqa: E501


        :return: The input_arguments of this EntryPointDto.  # noqa: E501
        :rtype: str
        """
        return self._input_arguments

    @input_arguments.setter
    def input_arguments(self, input_arguments):
        """Sets the input_arguments of this EntryPointDto.


        :param input_arguments: The input_arguments of this EntryPointDto.  # noqa: E501
        :type: str
        """

        self._input_arguments = input_arguments

    @property
    def output_arguments(self):
        """Gets the output_arguments of this EntryPointDto.  # noqa: E501


        :return: The output_arguments of this EntryPointDto.  # noqa: E501
        :rtype: str
        """
        return self._output_arguments

    @output_arguments.setter
    def output_arguments(self, output_arguments):
        """Sets the output_arguments of this EntryPointDto.


        :param output_arguments: The output_arguments of this EntryPointDto.  # noqa: E501
        :type: str
        """

        self._output_arguments = output_arguments

    @property
    def data_variation(self):
        """Gets the data_variation of this EntryPointDto.  # noqa: E501


        :return: The data_variation of this EntryPointDto.  # noqa: E501
        :rtype: EntryPointDataVariationDto
        """
        return self._data_variation

    @data_variation.setter
    def data_variation(self, data_variation):
        """Sets the data_variation of this EntryPointDto.


        :param data_variation: The data_variation of this EntryPointDto.  # noqa: E501
        :type: EntryPointDataVariationDto
        """

        self._data_variation = data_variation

    @property
    def id(self):
        """Gets the id of this EntryPointDto.  # noqa: E501


        :return: The id of this EntryPointDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EntryPointDto.


        :param id: The id of this EntryPointDto.  # noqa: E501
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
        if issubclass(EntryPointDto, dict):
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
        if not isinstance(other, EntryPointDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EntryPointDto):
            return True

        return self.to_dict() != other.to_dict()