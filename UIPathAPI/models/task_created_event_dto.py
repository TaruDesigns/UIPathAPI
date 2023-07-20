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


class TaskCreatedEventDto(object):
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
        'type': 'str',
        'event_id': 'str',
        'entity_key': 'str',
        'timestamp': 'datetime',
        'tasks': 'list[WebhookTaskCreatedDto]',
        'event_time': 'datetime',
        'event_source_id': 'int',
        'tenant_id': 'int',
        'organization_unit_id': 'int',
        'organization_unit_key': 'str',
        'user_id': 'int'
    }

    attribute_map = {
        'type': 'Type',
        'event_id': 'EventId',
        'entity_key': 'EntityKey',
        'timestamp': 'Timestamp',
        'tasks': 'Tasks',
        'event_time': 'EventTime',
        'event_source_id': 'EventSourceId',
        'tenant_id': 'TenantId',
        'organization_unit_id': 'OrganizationUnitId',
        'organization_unit_key': 'OrganizationUnitKey',
        'user_id': 'UserId'
    }

    def __init__(self, type=None, event_id=None, entity_key=None, timestamp=None, tasks=None, event_time=None, event_source_id=None, tenant_id=None, organization_unit_id=None, organization_unit_key=None, user_id=None, _configuration=None):  # noqa: E501
        """TaskCreatedEventDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._type = None
        self._event_id = None
        self._entity_key = None
        self._timestamp = None
        self._tasks = None
        self._event_time = None
        self._event_source_id = None
        self._tenant_id = None
        self._organization_unit_id = None
        self._organization_unit_key = None
        self._user_id = None
        self.discriminator = None

        self.type = type
        self.event_id = event_id
        if entity_key is not None:
            self.entity_key = entity_key
        self.timestamp = timestamp
        if tasks is not None:
            self.tasks = tasks
        if event_time is not None:
            self.event_time = event_time
        if event_source_id is not None:
            self.event_source_id = event_source_id
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if organization_unit_id is not None:
            self.organization_unit_id = organization_unit_id
        if organization_unit_key is not None:
            self.organization_unit_key = organization_unit_key
        if user_id is not None:
            self.user_id = user_id

    @property
    def type(self):
        """Gets the type of this TaskCreatedEventDto.  # noqa: E501


        :return: The type of this TaskCreatedEventDto.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TaskCreatedEventDto.


        :param type: The type of this TaskCreatedEventDto.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                type is not None and len(type) < 1):
            raise ValueError("Invalid value for `type`, length must be greater than or equal to `1`")  # noqa: E501

        self._type = type

    @property
    def event_id(self):
        """Gets the event_id of this TaskCreatedEventDto.  # noqa: E501


        :return: The event_id of this TaskCreatedEventDto.  # noqa: E501
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this TaskCreatedEventDto.


        :param event_id: The event_id of this TaskCreatedEventDto.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and event_id is None:
            raise ValueError("Invalid value for `event_id`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                event_id is not None and len(event_id) > 50):
            raise ValueError("Invalid value for `event_id`, length must be less than or equal to `50`")  # noqa: E501
        if (self._configuration.client_side_validation and
                event_id is not None and len(event_id) < 0):
            raise ValueError("Invalid value for `event_id`, length must be greater than or equal to `0`")  # noqa: E501

        self._event_id = event_id

    @property
    def entity_key(self):
        """Gets the entity_key of this TaskCreatedEventDto.  # noqa: E501


        :return: The entity_key of this TaskCreatedEventDto.  # noqa: E501
        :rtype: str
        """
        return self._entity_key

    @entity_key.setter
    def entity_key(self, entity_key):
        """Sets the entity_key of this TaskCreatedEventDto.


        :param entity_key: The entity_key of this TaskCreatedEventDto.  # noqa: E501
        :type: str
        """

        self._entity_key = entity_key

    @property
    def timestamp(self):
        """Gets the timestamp of this TaskCreatedEventDto.  # noqa: E501


        :return: The timestamp of this TaskCreatedEventDto.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this TaskCreatedEventDto.


        :param timestamp: The timestamp of this TaskCreatedEventDto.  # noqa: E501
        :type: datetime
        """
        if self._configuration.client_side_validation and timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def tasks(self):
        """Gets the tasks of this TaskCreatedEventDto.  # noqa: E501


        :return: The tasks of this TaskCreatedEventDto.  # noqa: E501
        :rtype: list[WebhookTaskCreatedDto]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """Sets the tasks of this TaskCreatedEventDto.


        :param tasks: The tasks of this TaskCreatedEventDto.  # noqa: E501
        :type: list[WebhookTaskCreatedDto]
        """

        self._tasks = tasks

    @property
    def event_time(self):
        """Gets the event_time of this TaskCreatedEventDto.  # noqa: E501


        :return: The event_time of this TaskCreatedEventDto.  # noqa: E501
        :rtype: datetime
        """
        return self._event_time

    @event_time.setter
    def event_time(self, event_time):
        """Sets the event_time of this TaskCreatedEventDto.


        :param event_time: The event_time of this TaskCreatedEventDto.  # noqa: E501
        :type: datetime
        """

        self._event_time = event_time

    @property
    def event_source_id(self):
        """Gets the event_source_id of this TaskCreatedEventDto.  # noqa: E501


        :return: The event_source_id of this TaskCreatedEventDto.  # noqa: E501
        :rtype: int
        """
        return self._event_source_id

    @event_source_id.setter
    def event_source_id(self, event_source_id):
        """Sets the event_source_id of this TaskCreatedEventDto.


        :param event_source_id: The event_source_id of this TaskCreatedEventDto.  # noqa: E501
        :type: int
        """

        self._event_source_id = event_source_id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this TaskCreatedEventDto.  # noqa: E501


        :return: The tenant_id of this TaskCreatedEventDto.  # noqa: E501
        :rtype: int
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this TaskCreatedEventDto.


        :param tenant_id: The tenant_id of this TaskCreatedEventDto.  # noqa: E501
        :type: int
        """

        self._tenant_id = tenant_id

    @property
    def organization_unit_id(self):
        """Gets the organization_unit_id of this TaskCreatedEventDto.  # noqa: E501


        :return: The organization_unit_id of this TaskCreatedEventDto.  # noqa: E501
        :rtype: int
        """
        return self._organization_unit_id

    @organization_unit_id.setter
    def organization_unit_id(self, organization_unit_id):
        """Sets the organization_unit_id of this TaskCreatedEventDto.


        :param organization_unit_id: The organization_unit_id of this TaskCreatedEventDto.  # noqa: E501
        :type: int
        """

        self._organization_unit_id = organization_unit_id

    @property
    def organization_unit_key(self):
        """Gets the organization_unit_key of this TaskCreatedEventDto.  # noqa: E501


        :return: The organization_unit_key of this TaskCreatedEventDto.  # noqa: E501
        :rtype: str
        """
        return self._organization_unit_key

    @organization_unit_key.setter
    def organization_unit_key(self, organization_unit_key):
        """Sets the organization_unit_key of this TaskCreatedEventDto.


        :param organization_unit_key: The organization_unit_key of this TaskCreatedEventDto.  # noqa: E501
        :type: str
        """

        self._organization_unit_key = organization_unit_key

    @property
    def user_id(self):
        """Gets the user_id of this TaskCreatedEventDto.  # noqa: E501


        :return: The user_id of this TaskCreatedEventDto.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this TaskCreatedEventDto.


        :param user_id: The user_id of this TaskCreatedEventDto.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

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
        if issubclass(TaskCreatedEventDto, dict):
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
        if not isinstance(other, TaskCreatedEventDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TaskCreatedEventDto):
            return True

        return self.to_dict() != other.to_dict()
