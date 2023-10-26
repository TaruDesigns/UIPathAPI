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


class ExecutionMediaDto(object):
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
        'storage_location': 'str',
        'name': 'str',
        'job_id': 'int',
        'release_name': 'str',
        'id': 'int'
    }

    attribute_map = {
        'storage_location': 'StorageLocation',
        'name': 'Name',
        'job_id': 'JobId',
        'release_name': 'ReleaseName',
        'id': 'Id'
    }

    def __init__(self, storage_location=None, name=None, job_id=None, release_name=None, id=None, _configuration=None):  # noqa: E501
        """ExecutionMediaDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._storage_location = None
        self._name = None
        self._job_id = None
        self._release_name = None
        self._id = None
        self.discriminator = None

        if storage_location is not None:
            self.storage_location = storage_location
        if name is not None:
            self.name = name
        if job_id is not None:
            self.job_id = job_id
        if release_name is not None:
            self.release_name = release_name
        if id is not None:
            self.id = id

    @property
    def storage_location(self):
        """Gets the storage_location of this ExecutionMediaDto.  # noqa: E501


        :return: The storage_location of this ExecutionMediaDto.  # noqa: E501
        :rtype: str
        """
        return self._storage_location

    @storage_location.setter
    def storage_location(self, storage_location):
        """Sets the storage_location of this ExecutionMediaDto.


        :param storage_location: The storage_location of this ExecutionMediaDto.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                storage_location is not None and len(storage_location) > 255):
            raise ValueError("Invalid value for `storage_location`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                storage_location is not None and len(storage_location) < 0):
            raise ValueError("Invalid value for `storage_location`, length must be greater than or equal to `0`")  # noqa: E501

        self._storage_location = storage_location

    @property
    def name(self):
        """Gets the name of this ExecutionMediaDto.  # noqa: E501


        :return: The name of this ExecutionMediaDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ExecutionMediaDto.


        :param name: The name of this ExecutionMediaDto.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and len(name) < 0):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501

        self._name = name

    @property
    def job_id(self):
        """Gets the job_id of this ExecutionMediaDto.  # noqa: E501


        :return: The job_id of this ExecutionMediaDto.  # noqa: E501
        :rtype: int
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ExecutionMediaDto.


        :param job_id: The job_id of this ExecutionMediaDto.  # noqa: E501
        :type: int
        """

        self._job_id = job_id

    @property
    def release_name(self):
        """Gets the release_name of this ExecutionMediaDto.  # noqa: E501


        :return: The release_name of this ExecutionMediaDto.  # noqa: E501
        :rtype: str
        """
        return self._release_name

    @release_name.setter
    def release_name(self, release_name):
        """Sets the release_name of this ExecutionMediaDto.


        :param release_name: The release_name of this ExecutionMediaDto.  # noqa: E501
        :type: str
        """

        self._release_name = release_name

    @property
    def id(self):
        """Gets the id of this ExecutionMediaDto.  # noqa: E501


        :return: The id of this ExecutionMediaDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ExecutionMediaDto.


        :param id: The id of this ExecutionMediaDto.  # noqa: E501
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
        if issubclass(ExecutionMediaDto, dict):
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
        if not isinstance(other, ExecutionMediaDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExecutionMediaDto):
            return True

        return self.to_dict() != other.to_dict()
