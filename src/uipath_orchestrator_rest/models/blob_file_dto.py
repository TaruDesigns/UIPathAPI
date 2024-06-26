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


class BlobFileDto(object):
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
        'full_path': 'str',
        'content_type': 'str',
        'size': 'int',
        'is_directory': 'bool',
        'id': 'str'
    }

    attribute_map = {
        'full_path': 'FullPath',
        'content_type': 'ContentType',
        'size': 'Size',
        'is_directory': 'IsDirectory',
        'id': 'Id'
    }

    def __init__(self, full_path=None, content_type=None, size=None, is_directory=None, id=None, _configuration=None):  # noqa: E501
        """BlobFileDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._full_path = None
        self._content_type = None
        self._size = None
        self._is_directory = None
        self._id = None
        self.discriminator = None

        if full_path is not None:
            self.full_path = full_path
        if content_type is not None:
            self.content_type = content_type
        if size is not None:
            self.size = size
        if is_directory is not None:
            self.is_directory = is_directory
        if id is not None:
            self.id = id

    @property
    def full_path(self):
        """Gets the full_path of this BlobFileDto.  # noqa: E501


        :return: The full_path of this BlobFileDto.  # noqa: E501
        :rtype: str
        """
        return self._full_path

    @full_path.setter
    def full_path(self, full_path):
        """Sets the full_path of this BlobFileDto.


        :param full_path: The full_path of this BlobFileDto.  # noqa: E501
        :type: str
        """

        self._full_path = full_path

    @property
    def content_type(self):
        """Gets the content_type of this BlobFileDto.  # noqa: E501


        :return: The content_type of this BlobFileDto.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this BlobFileDto.


        :param content_type: The content_type of this BlobFileDto.  # noqa: E501
        :type: str
        """

        self._content_type = content_type

    @property
    def size(self):
        """Gets the size of this BlobFileDto.  # noqa: E501


        :return: The size of this BlobFileDto.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this BlobFileDto.


        :param size: The size of this BlobFileDto.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def is_directory(self):
        """Gets the is_directory of this BlobFileDto.  # noqa: E501


        :return: The is_directory of this BlobFileDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_directory

    @is_directory.setter
    def is_directory(self, is_directory):
        """Sets the is_directory of this BlobFileDto.


        :param is_directory: The is_directory of this BlobFileDto.  # noqa: E501
        :type: bool
        """

        self._is_directory = is_directory

    @property
    def id(self):
        """Gets the id of this BlobFileDto.  # noqa: E501


        :return: The id of this BlobFileDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BlobFileDto.


        :param id: The id of this BlobFileDto.  # noqa: E501
        :type: str
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
        if issubclass(BlobFileDto, dict):
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
        if not isinstance(other, BlobFileDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BlobFileDto):
            return True

        return self.to_dict() != other.to_dict()
