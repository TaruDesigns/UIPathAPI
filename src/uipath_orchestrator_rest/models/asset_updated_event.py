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


class AssetUpdatedEvent(object):
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
        'name': 'str',
        'description': 'str',
        'key': 'str',
        'asset_type': 'str',
        'asset_scope': 'str',
        'tags': 'list[TagDto]',
        'folder_keys': 'list[str]',
        'event_time': 'datetime',
        'event_source': 'object'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'key': 'key',
        'asset_type': 'assetType',
        'asset_scope': 'assetScope',
        'tags': 'tags',
        'folder_keys': 'folderKeys',
        'event_time': 'eventTime',
        'event_source': 'eventSource'
    }

    def __init__(self, name=None, description=None, key=None, asset_type=None, asset_scope=None, tags=None, folder_keys=None, event_time=None, event_source=None, _configuration=None):  # noqa: E501
        """AssetUpdatedEvent - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._description = None
        self._key = None
        self._asset_type = None
        self._asset_scope = None
        self._tags = None
        self._folder_keys = None
        self._event_time = None
        self._event_source = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if key is not None:
            self.key = key
        if asset_type is not None:
            self.asset_type = asset_type
        if asset_scope is not None:
            self.asset_scope = asset_scope
        if tags is not None:
            self.tags = tags
        if folder_keys is not None:
            self.folder_keys = folder_keys
        if event_time is not None:
            self.event_time = event_time
        if event_source is not None:
            self.event_source = event_source

    @property
    def name(self):
        """Gets the name of this AssetUpdatedEvent.  # noqa: E501


        :return: The name of this AssetUpdatedEvent.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AssetUpdatedEvent.


        :param name: The name of this AssetUpdatedEvent.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this AssetUpdatedEvent.  # noqa: E501


        :return: The description of this AssetUpdatedEvent.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AssetUpdatedEvent.


        :param description: The description of this AssetUpdatedEvent.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def key(self):
        """Gets the key of this AssetUpdatedEvent.  # noqa: E501


        :return: The key of this AssetUpdatedEvent.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this AssetUpdatedEvent.


        :param key: The key of this AssetUpdatedEvent.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def asset_type(self):
        """Gets the asset_type of this AssetUpdatedEvent.  # noqa: E501

        Defines what type of value is stored by an asset.  # noqa: E501

        :return: The asset_type of this AssetUpdatedEvent.  # noqa: E501
        :rtype: str
        """
        return self._asset_type

    @asset_type.setter
    def asset_type(self, asset_type):
        """Sets the asset_type of this AssetUpdatedEvent.

        Defines what type of value is stored by an asset.  # noqa: E501

        :param asset_type: The asset_type of this AssetUpdatedEvent.  # noqa: E501
        :type: str
        """
        allowed_values = ["DBConnectionString", "HttpConnectionString", "Text", "Bool", "Integer", "Credential", "WindowsCredential", "KeyValueList"]  # noqa: E501
        if (self._configuration.client_side_validation and
                asset_type not in allowed_values):
            raise ValueError(
                "Invalid value for `asset_type` ({0}), must be one of {1}"  # noqa: E501
                .format(asset_type, allowed_values)
            )

        self._asset_type = asset_type

    @property
    def asset_scope(self):
        """Gets the asset_scope of this AssetUpdatedEvent.  # noqa: E501

        Defines the visibility level of an asset.  # noqa: E501

        :return: The asset_scope of this AssetUpdatedEvent.  # noqa: E501
        :rtype: str
        """
        return self._asset_scope

    @asset_scope.setter
    def asset_scope(self, asset_scope):
        """Sets the asset_scope of this AssetUpdatedEvent.

        Defines the visibility level of an asset.  # noqa: E501

        :param asset_scope: The asset_scope of this AssetUpdatedEvent.  # noqa: E501
        :type: str
        """
        allowed_values = ["Global", "PerRobot"]  # noqa: E501
        if (self._configuration.client_side_validation and
                asset_scope not in allowed_values):
            raise ValueError(
                "Invalid value for `asset_scope` ({0}), must be one of {1}"  # noqa: E501
                .format(asset_scope, allowed_values)
            )

        self._asset_scope = asset_scope

    @property
    def tags(self):
        """Gets the tags of this AssetUpdatedEvent.  # noqa: E501


        :return: The tags of this AssetUpdatedEvent.  # noqa: E501
        :rtype: list[TagDto]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this AssetUpdatedEvent.


        :param tags: The tags of this AssetUpdatedEvent.  # noqa: E501
        :type: list[TagDto]
        """

        self._tags = tags

    @property
    def folder_keys(self):
        """Gets the folder_keys of this AssetUpdatedEvent.  # noqa: E501


        :return: The folder_keys of this AssetUpdatedEvent.  # noqa: E501
        :rtype: list[str]
        """
        return self._folder_keys

    @folder_keys.setter
    def folder_keys(self, folder_keys):
        """Sets the folder_keys of this AssetUpdatedEvent.


        :param folder_keys: The folder_keys of this AssetUpdatedEvent.  # noqa: E501
        :type: list[str]
        """

        self._folder_keys = folder_keys

    @property
    def event_time(self):
        """Gets the event_time of this AssetUpdatedEvent.  # noqa: E501


        :return: The event_time of this AssetUpdatedEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._event_time

    @event_time.setter
    def event_time(self, event_time):
        """Sets the event_time of this AssetUpdatedEvent.


        :param event_time: The event_time of this AssetUpdatedEvent.  # noqa: E501
        :type: datetime
        """

        self._event_time = event_time

    @property
    def event_source(self):
        """Gets the event_source of this AssetUpdatedEvent.  # noqa: E501


        :return: The event_source of this AssetUpdatedEvent.  # noqa: E501
        :rtype: object
        """
        return self._event_source

    @event_source.setter
    def event_source(self, event_source):
        """Sets the event_source of this AssetUpdatedEvent.


        :param event_source: The event_source of this AssetUpdatedEvent.  # noqa: E501
        :type: object
        """

        self._event_source = event_source

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
        if issubclass(AssetUpdatedEvent, dict):
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
        if not isinstance(other, AssetUpdatedEvent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AssetUpdatedEvent):
            return True

        return self.to_dict() != other.to_dict()
