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


class ReleaseVersionDto(object):
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
        'release_id': 'int',
        'version_number': 'str',
        'creation_time': 'datetime',
        'release_name': 'str',
        'id': 'int'
    }

    attribute_map = {
        'release_id': 'ReleaseId',
        'version_number': 'VersionNumber',
        'creation_time': 'CreationTime',
        'release_name': 'ReleaseName',
        'id': 'Id'
    }

    def __init__(self, release_id=None, version_number=None, creation_time=None, release_name=None, id=None, _configuration=None):  # noqa: E501
        """ReleaseVersionDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._release_id = None
        self._version_number = None
        self._creation_time = None
        self._release_name = None
        self._id = None
        self.discriminator = None

        self.release_id = release_id
        self.version_number = version_number
        if creation_time is not None:
            self.creation_time = creation_time
        if release_name is not None:
            self.release_name = release_name
        if id is not None:
            self.id = id

    @property
    def release_id(self):
        """Gets the release_id of this ReleaseVersionDto.  # noqa: E501

        The Id of the parent release.  # noqa: E501

        :return: The release_id of this ReleaseVersionDto.  # noqa: E501
        :rtype: int
        """
        return self._release_id

    @release_id.setter
    def release_id(self, release_id):
        """Sets the release_id of this ReleaseVersionDto.

        The Id of the parent release.  # noqa: E501

        :param release_id: The release_id of this ReleaseVersionDto.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and release_id is None:
            raise ValueError("Invalid value for `release_id`, must not be `None`")  # noqa: E501

        self._release_id = release_id

    @property
    def version_number(self):
        """Gets the version_number of this ReleaseVersionDto.  # noqa: E501

        The version of process associated with the release.  # noqa: E501

        :return: The version_number of this ReleaseVersionDto.  # noqa: E501
        :rtype: str
        """
        return self._version_number

    @version_number.setter
    def version_number(self, version_number):
        """Sets the version_number of this ReleaseVersionDto.

        The version of process associated with the release.  # noqa: E501

        :param version_number: The version_number of this ReleaseVersionDto.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and version_number is None:
            raise ValueError("Invalid value for `version_number`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                version_number is not None and len(version_number) > 50):
            raise ValueError("Invalid value for `version_number`, length must be less than or equal to `50`")  # noqa: E501
        if (self._configuration.client_side_validation and
                version_number is not None and len(version_number) < 1):
            raise ValueError("Invalid value for `version_number`, length must be greater than or equal to `1`")  # noqa: E501

        self._version_number = version_number

    @property
    def creation_time(self):
        """Gets the creation_time of this ReleaseVersionDto.  # noqa: E501

        The date and time when the version was associated with the release.  # noqa: E501

        :return: The creation_time of this ReleaseVersionDto.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this ReleaseVersionDto.

        The date and time when the version was associated with the release.  # noqa: E501

        :param creation_time: The creation_time of this ReleaseVersionDto.  # noqa: E501
        :type: datetime
        """

        self._creation_time = creation_time

    @property
    def release_name(self):
        """Gets the release_name of this ReleaseVersionDto.  # noqa: E501

        The name of the process associated with the release.  # noqa: E501

        :return: The release_name of this ReleaseVersionDto.  # noqa: E501
        :rtype: str
        """
        return self._release_name

    @release_name.setter
    def release_name(self, release_name):
        """Sets the release_name of this ReleaseVersionDto.

        The name of the process associated with the release.  # noqa: E501

        :param release_name: The release_name of this ReleaseVersionDto.  # noqa: E501
        :type: str
        """

        self._release_name = release_name

    @property
    def id(self):
        """Gets the id of this ReleaseVersionDto.  # noqa: E501


        :return: The id of this ReleaseVersionDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ReleaseVersionDto.


        :param id: The id of this ReleaseVersionDto.  # noqa: E501
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
        if issubclass(ReleaseVersionDto, dict):
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
        if not isinstance(other, ReleaseVersionDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReleaseVersionDto):
            return True

        return self.to_dict() != other.to_dict()
