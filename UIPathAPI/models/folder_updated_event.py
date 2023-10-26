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


class FolderUpdatedEvent(object):
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
        'display_name': 'str',
        'description': 'str',
        'code': 'str',
        'path': 'str',
        'fully_qualified_name': 'str',
        'type': 'str',
        'event_time': 'datetime',
        'event_source': 'object'
    }

    attribute_map = {
        'id': 'id',
        'key': 'key',
        'display_name': 'displayName',
        'description': 'description',
        'code': 'code',
        'path': 'path',
        'fully_qualified_name': 'fullyQualifiedName',
        'type': 'type',
        'event_time': 'eventTime',
        'event_source': 'eventSource'
    }

    def __init__(self, id=None, key=None, display_name=None, description=None, code=None, path=None, fully_qualified_name=None, type=None, event_time=None, event_source=None, _configuration=None):  # noqa: E501
        """FolderUpdatedEvent - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._key = None
        self._display_name = None
        self._description = None
        self._code = None
        self._path = None
        self._fully_qualified_name = None
        self._type = None
        self._event_time = None
        self._event_source = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if key is not None:
            self.key = key
        if display_name is not None:
            self.display_name = display_name
        if description is not None:
            self.description = description
        if code is not None:
            self.code = code
        if path is not None:
            self.path = path
        if fully_qualified_name is not None:
            self.fully_qualified_name = fully_qualified_name
        if type is not None:
            self.type = type
        if event_time is not None:
            self.event_time = event_time
        if event_source is not None:
            self.event_source = event_source

    @property
    def id(self):
        """Gets the id of this FolderUpdatedEvent.  # noqa: E501


        :return: The id of this FolderUpdatedEvent.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FolderUpdatedEvent.


        :param id: The id of this FolderUpdatedEvent.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def key(self):
        """Gets the key of this FolderUpdatedEvent.  # noqa: E501


        :return: The key of this FolderUpdatedEvent.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this FolderUpdatedEvent.


        :param key: The key of this FolderUpdatedEvent.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def display_name(self):
        """Gets the display_name of this FolderUpdatedEvent.  # noqa: E501


        :return: The display_name of this FolderUpdatedEvent.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this FolderUpdatedEvent.


        :param display_name: The display_name of this FolderUpdatedEvent.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this FolderUpdatedEvent.  # noqa: E501


        :return: The description of this FolderUpdatedEvent.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FolderUpdatedEvent.


        :param description: The description of this FolderUpdatedEvent.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def code(self):
        """Gets the code of this FolderUpdatedEvent.  # noqa: E501


        :return: The code of this FolderUpdatedEvent.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this FolderUpdatedEvent.


        :param code: The code of this FolderUpdatedEvent.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def path(self):
        """Gets the path of this FolderUpdatedEvent.  # noqa: E501


        :return: The path of this FolderUpdatedEvent.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this FolderUpdatedEvent.


        :param path: The path of this FolderUpdatedEvent.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def fully_qualified_name(self):
        """Gets the fully_qualified_name of this FolderUpdatedEvent.  # noqa: E501


        :return: The fully_qualified_name of this FolderUpdatedEvent.  # noqa: E501
        :rtype: str
        """
        return self._fully_qualified_name

    @fully_qualified_name.setter
    def fully_qualified_name(self, fully_qualified_name):
        """Sets the fully_qualified_name of this FolderUpdatedEvent.


        :param fully_qualified_name: The fully_qualified_name of this FolderUpdatedEvent.  # noqa: E501
        :type: str
        """

        self._fully_qualified_name = fully_qualified_name

    @property
    def type(self):
        """Gets the type of this FolderUpdatedEvent.  # noqa: E501


        :return: The type of this FolderUpdatedEvent.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FolderUpdatedEvent.


        :param type: The type of this FolderUpdatedEvent.  # noqa: E501
        :type: str
        """
        allowed_values = ["Standard", "Personal", "Virtual", "Solution"]  # noqa: E501
        if (self._configuration.client_side_validation and
                type not in allowed_values):
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def event_time(self):
        """Gets the event_time of this FolderUpdatedEvent.  # noqa: E501


        :return: The event_time of this FolderUpdatedEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._event_time

    @event_time.setter
    def event_time(self, event_time):
        """Sets the event_time of this FolderUpdatedEvent.


        :param event_time: The event_time of this FolderUpdatedEvent.  # noqa: E501
        :type: datetime
        """

        self._event_time = event_time

    @property
    def event_source(self):
        """Gets the event_source of this FolderUpdatedEvent.  # noqa: E501


        :return: The event_source of this FolderUpdatedEvent.  # noqa: E501
        :rtype: object
        """
        return self._event_source

    @event_source.setter
    def event_source(self, event_source):
        """Sets the event_source of this FolderUpdatedEvent.


        :param event_source: The event_source of this FolderUpdatedEvent.  # noqa: E501
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
        if issubclass(FolderUpdatedEvent, dict):
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
        if not isinstance(other, FolderUpdatedEvent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FolderUpdatedEvent):
            return True

        return self.to_dict() != other.to_dict()
