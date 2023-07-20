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


class SimpleMachineDto(object):
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
        'name': 'str',
        'service_user_name': 'str',
        'type': 'str',
        'scope': 'str'
    }

    attribute_map = {
        'id': 'Id',
        'key': 'Key',
        'name': 'Name',
        'service_user_name': 'ServiceUserName',
        'type': 'Type',
        'scope': 'Scope'
    }

    def __init__(self, id=None, key=None, name=None, service_user_name=None, type=None, scope=None, _configuration=None):  # noqa: E501
        """SimpleMachineDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._key = None
        self._name = None
        self._service_user_name = None
        self._type = None
        self._scope = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if key is not None:
            self.key = key
        if name is not None:
            self.name = name
        if service_user_name is not None:
            self.service_user_name = service_user_name
        if type is not None:
            self.type = type
        if scope is not None:
            self.scope = scope

    @property
    def id(self):
        """Gets the id of this SimpleMachineDto.  # noqa: E501


        :return: The id of this SimpleMachineDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SimpleMachineDto.


        :param id: The id of this SimpleMachineDto.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def key(self):
        """Gets the key of this SimpleMachineDto.  # noqa: E501


        :return: The key of this SimpleMachineDto.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this SimpleMachineDto.


        :param key: The key of this SimpleMachineDto.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def name(self):
        """Gets the name of this SimpleMachineDto.  # noqa: E501


        :return: The name of this SimpleMachineDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SimpleMachineDto.


        :param name: The name of this SimpleMachineDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def service_user_name(self):
        """Gets the service_user_name of this SimpleMachineDto.  # noqa: E501


        :return: The service_user_name of this SimpleMachineDto.  # noqa: E501
        :rtype: str
        """
        return self._service_user_name

    @service_user_name.setter
    def service_user_name(self, service_user_name):
        """Sets the service_user_name of this SimpleMachineDto.


        :param service_user_name: The service_user_name of this SimpleMachineDto.  # noqa: E501
        :type: str
        """

        self._service_user_name = service_user_name

    @property
    def type(self):
        """Gets the type of this SimpleMachineDto.  # noqa: E501


        :return: The type of this SimpleMachineDto.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SimpleMachineDto.


        :param type: The type of this SimpleMachineDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["Standard", "Template"]  # noqa: E501
        if (self._configuration.client_side_validation and
                type not in allowed_values):
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def scope(self):
        """Gets the scope of this SimpleMachineDto.  # noqa: E501


        :return: The scope of this SimpleMachineDto.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this SimpleMachineDto.


        :param scope: The scope of this SimpleMachineDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["Default", "Shared", "PersonalWorkspace", "Cloud", "Serverless"]  # noqa: E501
        if (self._configuration.client_side_validation and
                scope not in allowed_values):
            raise ValueError(
                "Invalid value for `scope` ({0}), must be one of {1}"  # noqa: E501
                .format(scope, allowed_values)
            )

        self._scope = scope

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
        if issubclass(SimpleMachineDto, dict):
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
        if not isinstance(other, SimpleMachineDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SimpleMachineDto):
            return True

        return self.to_dict() != other.to_dict()
