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


class TaskDefintionAssociatedVersionsDto(object):
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
        'version': 'int',
        'creation_date': 'datetime',
        'user_name': 'str'
    }

    attribute_map = {
        'version': 'version',
        'creation_date': 'creationDate',
        'user_name': 'userName'
    }

    def __init__(self, version=None, creation_date=None, user_name=None, _configuration=None):  # noqa: E501
        """TaskDefintionAssociatedVersionsDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._version = None
        self._creation_date = None
        self._user_name = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if creation_date is not None:
            self.creation_date = creation_date
        if user_name is not None:
            self.user_name = user_name

    @property
    def version(self):
        """Gets the version of this TaskDefintionAssociatedVersionsDto.  # noqa: E501


        :return: The version of this TaskDefintionAssociatedVersionsDto.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this TaskDefintionAssociatedVersionsDto.


        :param version: The version of this TaskDefintionAssociatedVersionsDto.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def creation_date(self):
        """Gets the creation_date of this TaskDefintionAssociatedVersionsDto.  # noqa: E501


        :return: The creation_date of this TaskDefintionAssociatedVersionsDto.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this TaskDefintionAssociatedVersionsDto.


        :param creation_date: The creation_date of this TaskDefintionAssociatedVersionsDto.  # noqa: E501
        :type: datetime
        """

        self._creation_date = creation_date

    @property
    def user_name(self):
        """Gets the user_name of this TaskDefintionAssociatedVersionsDto.  # noqa: E501


        :return: The user_name of this TaskDefintionAssociatedVersionsDto.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this TaskDefintionAssociatedVersionsDto.


        :param user_name: The user_name of this TaskDefintionAssociatedVersionsDto.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

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
        if issubclass(TaskDefintionAssociatedVersionsDto, dict):
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
        if not isinstance(other, TaskDefintionAssociatedVersionsDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TaskDefintionAssociatedVersionsDto):
            return True

        return self.to_dict() != other.to_dict()