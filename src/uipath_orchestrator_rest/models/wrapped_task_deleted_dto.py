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


class WrappedTaskDeletedDto(object):
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
        'title': 'str',
        'type': 'str',
        'priority': 'str',
        'status': 'str',
        'creation_time': 'datetime',
        'task_catalog_name': 'str',
        'id': 'int',
        'organization_unit_id': 'int',
        'assigned_to_user_id': 'int',
        'action': 'str',
        'deleter_user_id': 'int',
        'deletion_time': 'datetime'
    }

    attribute_map = {
        'title': 'Title',
        'type': 'Type',
        'priority': 'Priority',
        'status': 'Status',
        'creation_time': 'CreationTime',
        'task_catalog_name': 'TaskCatalogName',
        'id': 'Id',
        'organization_unit_id': 'OrganizationUnitId',
        'assigned_to_user_id': 'AssignedToUserId',
        'action': 'Action',
        'deleter_user_id': 'DeleterUserId',
        'deletion_time': 'DeletionTime'
    }

    def __init__(self, title=None, type=None, priority=None, status=None, creation_time=None, task_catalog_name=None, id=None, organization_unit_id=None, assigned_to_user_id=None, action=None, deleter_user_id=None, deletion_time=None, _configuration=None):  # noqa: E501
        """WrappedTaskDeletedDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._title = None
        self._type = None
        self._priority = None
        self._status = None
        self._creation_time = None
        self._task_catalog_name = None
        self._id = None
        self._organization_unit_id = None
        self._assigned_to_user_id = None
        self._action = None
        self._deleter_user_id = None
        self._deletion_time = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if type is not None:
            self.type = type
        if priority is not None:
            self.priority = priority
        if status is not None:
            self.status = status
        if creation_time is not None:
            self.creation_time = creation_time
        if task_catalog_name is not None:
            self.task_catalog_name = task_catalog_name
        if id is not None:
            self.id = id
        if organization_unit_id is not None:
            self.organization_unit_id = organization_unit_id
        if assigned_to_user_id is not None:
            self.assigned_to_user_id = assigned_to_user_id
        if action is not None:
            self.action = action
        if deleter_user_id is not None:
            self.deleter_user_id = deleter_user_id
        if deletion_time is not None:
            self.deletion_time = deletion_time

    @property
    def title(self):
        """Gets the title of this WrappedTaskDeletedDto.  # noqa: E501


        :return: The title of this WrappedTaskDeletedDto.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this WrappedTaskDeletedDto.


        :param title: The title of this WrappedTaskDeletedDto.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def type(self):
        """Gets the type of this WrappedTaskDeletedDto.  # noqa: E501


        :return: The type of this WrappedTaskDeletedDto.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WrappedTaskDeletedDto.


        :param type: The type of this WrappedTaskDeletedDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["FormTask", "ExternalTask", "DocumentValidationTask", "DocumentClassificationTask", "DataLabelingTask", "AppTask"]  # noqa: E501
        if (self._configuration.client_side_validation and
                type not in allowed_values):
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def priority(self):
        """Gets the priority of this WrappedTaskDeletedDto.  # noqa: E501


        :return: The priority of this WrappedTaskDeletedDto.  # noqa: E501
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this WrappedTaskDeletedDto.


        :param priority: The priority of this WrappedTaskDeletedDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["Low", "Medium", "High", "Critical"]  # noqa: E501
        if (self._configuration.client_side_validation and
                priority not in allowed_values):
            raise ValueError(
                "Invalid value for `priority` ({0}), must be one of {1}"  # noqa: E501
                .format(priority, allowed_values)
            )

        self._priority = priority

    @property
    def status(self):
        """Gets the status of this WrappedTaskDeletedDto.  # noqa: E501


        :return: The status of this WrappedTaskDeletedDto.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this WrappedTaskDeletedDto.


        :param status: The status of this WrappedTaskDeletedDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["Unassigned", "Pending", "Completed"]  # noqa: E501
        if (self._configuration.client_side_validation and
                status not in allowed_values):
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def creation_time(self):
        """Gets the creation_time of this WrappedTaskDeletedDto.  # noqa: E501


        :return: The creation_time of this WrappedTaskDeletedDto.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this WrappedTaskDeletedDto.


        :param creation_time: The creation_time of this WrappedTaskDeletedDto.  # noqa: E501
        :type: datetime
        """

        self._creation_time = creation_time

    @property
    def task_catalog_name(self):
        """Gets the task_catalog_name of this WrappedTaskDeletedDto.  # noqa: E501


        :return: The task_catalog_name of this WrappedTaskDeletedDto.  # noqa: E501
        :rtype: str
        """
        return self._task_catalog_name

    @task_catalog_name.setter
    def task_catalog_name(self, task_catalog_name):
        """Sets the task_catalog_name of this WrappedTaskDeletedDto.


        :param task_catalog_name: The task_catalog_name of this WrappedTaskDeletedDto.  # noqa: E501
        :type: str
        """

        self._task_catalog_name = task_catalog_name

    @property
    def id(self):
        """Gets the id of this WrappedTaskDeletedDto.  # noqa: E501


        :return: The id of this WrappedTaskDeletedDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WrappedTaskDeletedDto.


        :param id: The id of this WrappedTaskDeletedDto.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def organization_unit_id(self):
        """Gets the organization_unit_id of this WrappedTaskDeletedDto.  # noqa: E501


        :return: The organization_unit_id of this WrappedTaskDeletedDto.  # noqa: E501
        :rtype: int
        """
        return self._organization_unit_id

    @organization_unit_id.setter
    def organization_unit_id(self, organization_unit_id):
        """Sets the organization_unit_id of this WrappedTaskDeletedDto.


        :param organization_unit_id: The organization_unit_id of this WrappedTaskDeletedDto.  # noqa: E501
        :type: int
        """

        self._organization_unit_id = organization_unit_id

    @property
    def assigned_to_user_id(self):
        """Gets the assigned_to_user_id of this WrappedTaskDeletedDto.  # noqa: E501


        :return: The assigned_to_user_id of this WrappedTaskDeletedDto.  # noqa: E501
        :rtype: int
        """
        return self._assigned_to_user_id

    @assigned_to_user_id.setter
    def assigned_to_user_id(self, assigned_to_user_id):
        """Sets the assigned_to_user_id of this WrappedTaskDeletedDto.


        :param assigned_to_user_id: The assigned_to_user_id of this WrappedTaskDeletedDto.  # noqa: E501
        :type: int
        """

        self._assigned_to_user_id = assigned_to_user_id

    @property
    def action(self):
        """Gets the action of this WrappedTaskDeletedDto.  # noqa: E501

        Action taken while completing the task  # noqa: E501

        :return: The action of this WrappedTaskDeletedDto.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this WrappedTaskDeletedDto.

        Action taken while completing the task  # noqa: E501

        :param action: The action of this WrappedTaskDeletedDto.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def deleter_user_id(self):
        """Gets the deleter_user_id of this WrappedTaskDeletedDto.  # noqa: E501

        User who deleted this task  # noqa: E501

        :return: The deleter_user_id of this WrappedTaskDeletedDto.  # noqa: E501
        :rtype: int
        """
        return self._deleter_user_id

    @deleter_user_id.setter
    def deleter_user_id(self, deleter_user_id):
        """Sets the deleter_user_id of this WrappedTaskDeletedDto.

        User who deleted this task  # noqa: E501

        :param deleter_user_id: The deleter_user_id of this WrappedTaskDeletedDto.  # noqa: E501
        :type: int
        """

        self._deleter_user_id = deleter_user_id

    @property
    def deletion_time(self):
        """Gets the deletion_time of this WrappedTaskDeletedDto.  # noqa: E501

        Deletion time of this task  # noqa: E501

        :return: The deletion_time of this WrappedTaskDeletedDto.  # noqa: E501
        :rtype: datetime
        """
        return self._deletion_time

    @deletion_time.setter
    def deletion_time(self, deletion_time):
        """Sets the deletion_time of this WrappedTaskDeletedDto.

        Deletion time of this task  # noqa: E501

        :param deletion_time: The deletion_time of this WrappedTaskDeletedDto.  # noqa: E501
        :type: datetime
        """

        self._deletion_time = deletion_time

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
        if issubclass(WrappedTaskDeletedDto, dict):
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
        if not isinstance(other, WrappedTaskDeletedDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WrappedTaskDeletedDto):
            return True

        return self.to_dict() != other.to_dict()