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


class QueueCreatedEvent(object):
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
        'key': 'str',
        'name': 'str',
        'description': 'str',
        'tags': 'list[TagDto]',
        'folder_keys': 'list[str]',
        'event_time': 'datetime',
        'event_source': 'object'
    }

    attribute_map = {
        'key': 'key',
        'name': 'name',
        'description': 'description',
        'tags': 'tags',
        'folder_keys': 'folderKeys',
        'event_time': 'eventTime',
        'event_source': 'eventSource'
    }

    def __init__(self, key=None, name=None, description=None, tags=None, folder_keys=None, event_time=None, event_source=None, _configuration=None):  # noqa: E501
        """QueueCreatedEvent - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._key = None
        self._name = None
        self._description = None
        self._tags = None
        self._folder_keys = None
        self._event_time = None
        self._event_source = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        if folder_keys is not None:
            self.folder_keys = folder_keys
        if event_time is not None:
            self.event_time = event_time
        if event_source is not None:
            self.event_source = event_source

    @property
    def key(self):
        """Gets the key of this QueueCreatedEvent.  # noqa: E501


        :return: The key of this QueueCreatedEvent.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this QueueCreatedEvent.


        :param key: The key of this QueueCreatedEvent.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def name(self):
        """Gets the name of this QueueCreatedEvent.  # noqa: E501


        :return: The name of this QueueCreatedEvent.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this QueueCreatedEvent.


        :param name: The name of this QueueCreatedEvent.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this QueueCreatedEvent.  # noqa: E501


        :return: The description of this QueueCreatedEvent.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this QueueCreatedEvent.


        :param description: The description of this QueueCreatedEvent.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this QueueCreatedEvent.  # noqa: E501


        :return: The tags of this QueueCreatedEvent.  # noqa: E501
        :rtype: list[TagDto]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this QueueCreatedEvent.


        :param tags: The tags of this QueueCreatedEvent.  # noqa: E501
        :type: list[TagDto]
        """

        self._tags = tags

    @property
    def folder_keys(self):
        """Gets the folder_keys of this QueueCreatedEvent.  # noqa: E501


        :return: The folder_keys of this QueueCreatedEvent.  # noqa: E501
        :rtype: list[str]
        """
        return self._folder_keys

    @folder_keys.setter
    def folder_keys(self, folder_keys):
        """Sets the folder_keys of this QueueCreatedEvent.


        :param folder_keys: The folder_keys of this QueueCreatedEvent.  # noqa: E501
        :type: list[str]
        """

        self._folder_keys = folder_keys

    @property
    def event_time(self):
        """Gets the event_time of this QueueCreatedEvent.  # noqa: E501


        :return: The event_time of this QueueCreatedEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._event_time

    @event_time.setter
    def event_time(self, event_time):
        """Sets the event_time of this QueueCreatedEvent.


        :param event_time: The event_time of this QueueCreatedEvent.  # noqa: E501
        :type: datetime
        """

        self._event_time = event_time

    @property
    def event_source(self):
        """Gets the event_source of this QueueCreatedEvent.  # noqa: E501


        :return: The event_source of this QueueCreatedEvent.  # noqa: E501
        :rtype: object
        """
        return self._event_source

    @event_source.setter
    def event_source(self, event_source):
        """Sets the event_source of this QueueCreatedEvent.


        :param event_source: The event_source of this QueueCreatedEvent.  # noqa: E501
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
        if issubclass(QueueCreatedEvent, dict):
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
        if not isinstance(other, QueueCreatedEvent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QueueCreatedEvent):
            return True

        return self.to_dict() != other.to_dict()
