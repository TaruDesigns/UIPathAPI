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


class SimpleReleaseEventDto(object):
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
        'name': 'str'
    }

    attribute_map = {
        'id': 'Id',
        'key': 'Key',
        'process_key': 'ProcessKey',
        'name': 'Name'
    }

    def __init__(self, id=None, key=None, process_key=None, name=None, _configuration=None):  # noqa: E501
        """SimpleReleaseEventDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._key = None
        self._process_key = None
        self._name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if key is not None:
            self.key = key
        if process_key is not None:
            self.process_key = process_key
        if name is not None:
            self.name = name

    @property
    def id(self):
        """Gets the id of this SimpleReleaseEventDto.  # noqa: E501

        The Id of the process  # noqa: E501

        :return: The id of this SimpleReleaseEventDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SimpleReleaseEventDto.

        The Id of the process  # noqa: E501

        :param id: The id of this SimpleReleaseEventDto.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def key(self):
        """Gets the key of this SimpleReleaseEventDto.  # noqa: E501

        The unique key of the process  # noqa: E501

        :return: The key of this SimpleReleaseEventDto.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this SimpleReleaseEventDto.

        The unique key of the process  # noqa: E501

        :param key: The key of this SimpleReleaseEventDto.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def process_key(self):
        """Gets the process_key of this SimpleReleaseEventDto.  # noqa: E501

        The name of the process  # noqa: E501

        :return: The process_key of this SimpleReleaseEventDto.  # noqa: E501
        :rtype: str
        """
        return self._process_key

    @process_key.setter
    def process_key(self, process_key):
        """Sets the process_key of this SimpleReleaseEventDto.

        The name of the process  # noqa: E501

        :param process_key: The process_key of this SimpleReleaseEventDto.  # noqa: E501
        :type: str
        """

        self._process_key = process_key

    @property
    def name(self):
        """Gets the name of this SimpleReleaseEventDto.  # noqa: E501

        The display name of the process  # noqa: E501

        :return: The name of this SimpleReleaseEventDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SimpleReleaseEventDto.

        The display name of the process  # noqa: E501

        :param name: The name of this SimpleReleaseEventDto.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(SimpleReleaseEventDto, dict):
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
        if not isinstance(other, SimpleReleaseEventDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SimpleReleaseEventDto):
            return True

        return self.to_dict() != other.to_dict()
