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


class ResourceOverwriteDto(object):
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
        'properties2': 'list[NameValueDto]',
        'resource_type': 'str',
        'resource_key': 'str',
        'entity_id': 'str',
        'properties': 'dict(str, object)',
        'entity_display_name': 'str',
        'entity_folder_id': 'int'
    }

    attribute_map = {
        'properties2': 'properties2',
        'resource_type': 'resourceType',
        'resource_key': 'resourceKey',
        'entity_id': 'entityId',
        'properties': 'properties',
        'entity_display_name': 'entityDisplayName',
        'entity_folder_id': 'entityFolderId'
    }

    def __init__(self, properties2=None, resource_type=None, resource_key=None, entity_id=None, properties=None, entity_display_name=None, entity_folder_id=None, _configuration=None):  # noqa: E501
        """ResourceOverwriteDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._properties2 = None
        self._resource_type = None
        self._resource_key = None
        self._entity_id = None
        self._properties = None
        self._entity_display_name = None
        self._entity_folder_id = None
        self.discriminator = None

        if properties2 is not None:
            self.properties2 = properties2
        self.resource_type = resource_type
        self.resource_key = resource_key
        if entity_id is not None:
            self.entity_id = entity_id
        if properties is not None:
            self.properties = properties
        if entity_display_name is not None:
            self.entity_display_name = entity_display_name
        if entity_folder_id is not None:
            self.entity_folder_id = entity_folder_id

    @property
    def properties2(self):
        """Gets the properties2 of this ResourceOverwriteDto.  # noqa: E501


        :return: The properties2 of this ResourceOverwriteDto.  # noqa: E501
        :rtype: list[NameValueDto]
        """
        return self._properties2

    @properties2.setter
    def properties2(self, properties2):
        """Sets the properties2 of this ResourceOverwriteDto.


        :param properties2: The properties2 of this ResourceOverwriteDto.  # noqa: E501
        :type: list[NameValueDto]
        """

        self._properties2 = properties2

    @property
    def resource_type(self):
        """Gets the resource_type of this ResourceOverwriteDto.  # noqa: E501

        The type of the resource to be overwritten  # noqa: E501

        :return: The resource_type of this ResourceOverwriteDto.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ResourceOverwriteDto.

        The type of the resource to be overwritten  # noqa: E501

        :param resource_type: The resource_type of this ResourceOverwriteDto.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and resource_type is None:
            raise ValueError("Invalid value for `resource_type`, must not be `None`")  # noqa: E501
        allowed_values = ["Unknown", "Queue", "Asset", "Bucket", "Process", "TaskCatalog", "Entity", "Connection", "TimeTrigger", "EventTrigger", "QueueTrigger", "AppsTrigger", "Property"]  # noqa: E501
        if (self._configuration.client_side_validation and
                resource_type not in allowed_values):
            raise ValueError(
                "Invalid value for `resource_type` ({0}), must be one of {1}"  # noqa: E501
                .format(resource_type, allowed_values)
            )

        self._resource_type = resource_type

    @property
    def resource_key(self):
        """Gets the resource_key of this ResourceOverwriteDto.  # noqa: E501

        The key of the resource to be overwritten  # noqa: E501

        :return: The resource_key of this ResourceOverwriteDto.  # noqa: E501
        :rtype: str
        """
        return self._resource_key

    @resource_key.setter
    def resource_key(self, resource_key):
        """Sets the resource_key of this ResourceOverwriteDto.

        The key of the resource to be overwritten  # noqa: E501

        :param resource_key: The resource_key of this ResourceOverwriteDto.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and resource_key is None:
            raise ValueError("Invalid value for `resource_key`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                resource_key is not None and len(resource_key) < 1):
            raise ValueError("Invalid value for `resource_key`, length must be greater than or equal to `1`")  # noqa: E501

        self._resource_key = resource_key

    @property
    def entity_id(self):
        """Gets the entity_id of this ResourceOverwriteDto.  # noqa: E501

        The id of the entity that overwrites the resource (e.g. ConnectionId)  # noqa: E501

        :return: The entity_id of this ResourceOverwriteDto.  # noqa: E501
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this ResourceOverwriteDto.

        The id of the entity that overwrites the resource (e.g. ConnectionId)  # noqa: E501

        :param entity_id: The entity_id of this ResourceOverwriteDto.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                entity_id is not None and len(entity_id) > 50):
            raise ValueError("Invalid value for `entity_id`, length must be less than or equal to `50`")  # noqa: E501

        self._entity_id = entity_id

    @property
    def properties(self):
        """Gets the properties of this ResourceOverwriteDto.  # noqa: E501

        Custom property overwrites  # noqa: E501

        :return: The properties of this ResourceOverwriteDto.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this ResourceOverwriteDto.

        Custom property overwrites  # noqa: E501

        :param properties: The properties of this ResourceOverwriteDto.  # noqa: E501
        :type: dict(str, object)
        """

        self._properties = properties

    @property
    def entity_display_name(self):
        """Gets the entity_display_name of this ResourceOverwriteDto.  # noqa: E501

        The name of the entity that overwrites the resource (e.g. ConnectionName)  # noqa: E501

        :return: The entity_display_name of this ResourceOverwriteDto.  # noqa: E501
        :rtype: str
        """
        return self._entity_display_name

    @entity_display_name.setter
    def entity_display_name(self, entity_display_name):
        """Sets the entity_display_name of this ResourceOverwriteDto.

        The name of the entity that overwrites the resource (e.g. ConnectionName)  # noqa: E501

        :param entity_display_name: The entity_display_name of this ResourceOverwriteDto.  # noqa: E501
        :type: str
        """

        self._entity_display_name = entity_display_name

    @property
    def entity_folder_id(self):
        """Gets the entity_folder_id of this ResourceOverwriteDto.  # noqa: E501


        :return: The entity_folder_id of this ResourceOverwriteDto.  # noqa: E501
        :rtype: int
        """
        return self._entity_folder_id

    @entity_folder_id.setter
    def entity_folder_id(self, entity_folder_id):
        """Sets the entity_folder_id of this ResourceOverwriteDto.


        :param entity_folder_id: The entity_folder_id of this ResourceOverwriteDto.  # noqa: E501
        :type: int
        """

        self._entity_folder_id = entity_folder_id

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
        if issubclass(ResourceOverwriteDto, dict):
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
        if not isinstance(other, ResourceOverwriteDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResourceOverwriteDto):
            return True

        return self.to_dict() != other.to_dict()