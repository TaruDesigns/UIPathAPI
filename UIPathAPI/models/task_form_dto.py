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


class TaskFormDto(object):
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
        'form_layout': 'object',
        'form_layout_id': 'int',
        'bulk_form_layout_id': 'int',
        'action_label': 'str',
        'status': 'str',
        'data': 'object',
        'action': 'str',
        'wait_job_state': 'str',
        'organization_unit_fully_qualified_name': 'str',
        'tags': 'list[TagDto]',
        'assigned_to_user': 'UserLoginInfoDto',
        'title': 'str',
        'type': 'str',
        'priority': 'str',
        'assigned_to_user_id': 'int',
        'organization_unit_id': 'int',
        'external_tag': 'str',
        'creator_job_key': 'str',
        'wait_job_key': 'str',
        'last_assigned_time': 'datetime',
        'completion_time': 'datetime',
        'is_deleted': 'bool',
        'deleter_user_id': 'int',
        'deletion_time': 'datetime',
        'last_modification_time': 'datetime',
        'last_modifier_user_id': 'int',
        'creation_time': 'datetime',
        'creator_user_id': 'int',
        'id': 'int'
    }

    attribute_map = {
        'form_layout': 'formLayout',
        'form_layout_id': 'formLayoutId',
        'bulk_form_layout_id': 'bulkFormLayoutId',
        'action_label': 'actionLabel',
        'status': 'status',
        'data': 'data',
        'action': 'action',
        'wait_job_state': 'waitJobState',
        'organization_unit_fully_qualified_name': 'organizationUnitFullyQualifiedName',
        'tags': 'tags',
        'assigned_to_user': 'assignedToUser',
        'title': 'title',
        'type': 'type',
        'priority': 'priority',
        'assigned_to_user_id': 'assignedToUserId',
        'organization_unit_id': 'organizationUnitId',
        'external_tag': 'externalTag',
        'creator_job_key': 'creatorJobKey',
        'wait_job_key': 'waitJobKey',
        'last_assigned_time': 'lastAssignedTime',
        'completion_time': 'completionTime',
        'is_deleted': 'isDeleted',
        'deleter_user_id': 'deleterUserId',
        'deletion_time': 'deletionTime',
        'last_modification_time': 'lastModificationTime',
        'last_modifier_user_id': 'lastModifierUserId',
        'creation_time': 'creationTime',
        'creator_user_id': 'creatorUserId',
        'id': 'id'
    }

    def __init__(self, form_layout=None, form_layout_id=None, bulk_form_layout_id=None, action_label=None, status=None, data=None, action=None, wait_job_state=None, organization_unit_fully_qualified_name=None, tags=None, assigned_to_user=None, title=None, type=None, priority=None, assigned_to_user_id=None, organization_unit_id=None, external_tag=None, creator_job_key=None, wait_job_key=None, last_assigned_time=None, completion_time=None, is_deleted=None, deleter_user_id=None, deletion_time=None, last_modification_time=None, last_modifier_user_id=None, creation_time=None, creator_user_id=None, id=None, _configuration=None):  # noqa: E501
        """TaskFormDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._form_layout = None
        self._form_layout_id = None
        self._bulk_form_layout_id = None
        self._action_label = None
        self._status = None
        self._data = None
        self._action = None
        self._wait_job_state = None
        self._organization_unit_fully_qualified_name = None
        self._tags = None
        self._assigned_to_user = None
        self._title = None
        self._type = None
        self._priority = None
        self._assigned_to_user_id = None
        self._organization_unit_id = None
        self._external_tag = None
        self._creator_job_key = None
        self._wait_job_key = None
        self._last_assigned_time = None
        self._completion_time = None
        self._is_deleted = None
        self._deleter_user_id = None
        self._deletion_time = None
        self._last_modification_time = None
        self._last_modifier_user_id = None
        self._creation_time = None
        self._creator_user_id = None
        self._id = None
        self.discriminator = None

        if form_layout is not None:
            self.form_layout = form_layout
        if form_layout_id is not None:
            self.form_layout_id = form_layout_id
        if bulk_form_layout_id is not None:
            self.bulk_form_layout_id = bulk_form_layout_id
        if action_label is not None:
            self.action_label = action_label
        if status is not None:
            self.status = status
        if data is not None:
            self.data = data
        if action is not None:
            self.action = action
        if wait_job_state is not None:
            self.wait_job_state = wait_job_state
        if organization_unit_fully_qualified_name is not None:
            self.organization_unit_fully_qualified_name = organization_unit_fully_qualified_name
        if tags is not None:
            self.tags = tags
        if assigned_to_user is not None:
            self.assigned_to_user = assigned_to_user
        if title is not None:
            self.title = title
        if type is not None:
            self.type = type
        if priority is not None:
            self.priority = priority
        if assigned_to_user_id is not None:
            self.assigned_to_user_id = assigned_to_user_id
        if organization_unit_id is not None:
            self.organization_unit_id = organization_unit_id
        if external_tag is not None:
            self.external_tag = external_tag
        if creator_job_key is not None:
            self.creator_job_key = creator_job_key
        if wait_job_key is not None:
            self.wait_job_key = wait_job_key
        if last_assigned_time is not None:
            self.last_assigned_time = last_assigned_time
        if completion_time is not None:
            self.completion_time = completion_time
        if is_deleted is not None:
            self.is_deleted = is_deleted
        if deleter_user_id is not None:
            self.deleter_user_id = deleter_user_id
        if deletion_time is not None:
            self.deletion_time = deletion_time
        if last_modification_time is not None:
            self.last_modification_time = last_modification_time
        if last_modifier_user_id is not None:
            self.last_modifier_user_id = last_modifier_user_id
        if creation_time is not None:
            self.creation_time = creation_time
        if creator_user_id is not None:
            self.creator_user_id = creator_user_id
        if id is not None:
            self.id = id

    @property
    def form_layout(self):
        """Gets the form_layout of this TaskFormDto.  # noqa: E501

        Task Form Layout json  # noqa: E501

        :return: The form_layout of this TaskFormDto.  # noqa: E501
        :rtype: object
        """
        return self._form_layout

    @form_layout.setter
    def form_layout(self, form_layout):
        """Sets the form_layout of this TaskFormDto.

        Task Form Layout json  # noqa: E501

        :param form_layout: The form_layout of this TaskFormDto.  # noqa: E501
        :type: object
        """

        self._form_layout = form_layout

    @property
    def form_layout_id(self):
        """Gets the form_layout_id of this TaskFormDto.  # noqa: E501

        Task Form Layout Id  # noqa: E501

        :return: The form_layout_id of this TaskFormDto.  # noqa: E501
        :rtype: int
        """
        return self._form_layout_id

    @form_layout_id.setter
    def form_layout_id(self, form_layout_id):
        """Sets the form_layout_id of this TaskFormDto.

        Task Form Layout Id  # noqa: E501

        :param form_layout_id: The form_layout_id of this TaskFormDto.  # noqa: E501
        :type: int
        """

        self._form_layout_id = form_layout_id

    @property
    def bulk_form_layout_id(self):
        """Gets the bulk_form_layout_id of this TaskFormDto.  # noqa: E501

        Task Form Layout Id  # noqa: E501

        :return: The bulk_form_layout_id of this TaskFormDto.  # noqa: E501
        :rtype: int
        """
        return self._bulk_form_layout_id

    @bulk_form_layout_id.setter
    def bulk_form_layout_id(self, bulk_form_layout_id):
        """Sets the bulk_form_layout_id of this TaskFormDto.

        Task Form Layout Id  # noqa: E501

        :param bulk_form_layout_id: The bulk_form_layout_id of this TaskFormDto.  # noqa: E501
        :type: int
        """

        self._bulk_form_layout_id = bulk_form_layout_id

    @property
    def action_label(self):
        """Gets the action_label of this TaskFormDto.  # noqa: E501

        Task form action label  # noqa: E501

        :return: The action_label of this TaskFormDto.  # noqa: E501
        :rtype: str
        """
        return self._action_label

    @action_label.setter
    def action_label(self, action_label):
        """Sets the action_label of this TaskFormDto.

        Task form action label  # noqa: E501

        :param action_label: The action_label of this TaskFormDto.  # noqa: E501
        :type: str
        """

        self._action_label = action_label

    @property
    def status(self):
        """Gets the status of this TaskFormDto.  # noqa: E501

        Task status  # noqa: E501

        :return: The status of this TaskFormDto.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TaskFormDto.

        Task status  # noqa: E501

        :param status: The status of this TaskFormDto.  # noqa: E501
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
    def data(self):
        """Gets the data of this TaskFormDto.  # noqa: E501

        Task form data json  # noqa: E501

        :return: The data of this TaskFormDto.  # noqa: E501
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this TaskFormDto.

        Task form data json  # noqa: E501

        :param data: The data of this TaskFormDto.  # noqa: E501
        :type: object
        """

        self._data = data

    @property
    def action(self):
        """Gets the action of this TaskFormDto.  # noqa: E501

        Task form action  # noqa: E501

        :return: The action of this TaskFormDto.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this TaskFormDto.

        Task form action  # noqa: E501

        :param action: The action of this TaskFormDto.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def wait_job_state(self):
        """Gets the wait_job_state of this TaskFormDto.  # noqa: E501

        State of the job(if any) waiting on the current task  # noqa: E501

        :return: The wait_job_state of this TaskFormDto.  # noqa: E501
        :rtype: str
        """
        return self._wait_job_state

    @wait_job_state.setter
    def wait_job_state(self, wait_job_state):
        """Sets the wait_job_state of this TaskFormDto.

        State of the job(if any) waiting on the current task  # noqa: E501

        :param wait_job_state: The wait_job_state of this TaskFormDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["Pending", "Running", "Stopping", "Terminating", "Faulted", "Successful", "Stopped", "Suspended", "Resumed"]  # noqa: E501
        if (self._configuration.client_side_validation and
                wait_job_state not in allowed_values):
            raise ValueError(
                "Invalid value for `wait_job_state` ({0}), must be one of {1}"  # noqa: E501
                .format(wait_job_state, allowed_values)
            )

        self._wait_job_state = wait_job_state

    @property
    def organization_unit_fully_qualified_name(self):
        """Gets the organization_unit_fully_qualified_name of this TaskFormDto.  # noqa: E501

        Fully qualified folder name  # noqa: E501

        :return: The organization_unit_fully_qualified_name of this TaskFormDto.  # noqa: E501
        :rtype: str
        """
        return self._organization_unit_fully_qualified_name

    @organization_unit_fully_qualified_name.setter
    def organization_unit_fully_qualified_name(self, organization_unit_fully_qualified_name):
        """Sets the organization_unit_fully_qualified_name of this TaskFormDto.

        Fully qualified folder name  # noqa: E501

        :param organization_unit_fully_qualified_name: The organization_unit_fully_qualified_name of this TaskFormDto.  # noqa: E501
        :type: str
        """

        self._organization_unit_fully_qualified_name = organization_unit_fully_qualified_name

    @property
    def tags(self):
        """Gets the tags of this TaskFormDto.  # noqa: E501

        List of tags associated to the task.  # noqa: E501

        :return: The tags of this TaskFormDto.  # noqa: E501
        :rtype: list[TagDto]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this TaskFormDto.

        List of tags associated to the task.  # noqa: E501

        :param tags: The tags of this TaskFormDto.  # noqa: E501
        :type: list[TagDto]
        """

        self._tags = tags

    @property
    def assigned_to_user(self):
        """Gets the assigned_to_user of this TaskFormDto.  # noqa: E501


        :return: The assigned_to_user of this TaskFormDto.  # noqa: E501
        :rtype: UserLoginInfoDto
        """
        return self._assigned_to_user

    @assigned_to_user.setter
    def assigned_to_user(self, assigned_to_user):
        """Sets the assigned_to_user of this TaskFormDto.


        :param assigned_to_user: The assigned_to_user of this TaskFormDto.  # noqa: E501
        :type: UserLoginInfoDto
        """

        self._assigned_to_user = assigned_to_user

    @property
    def title(self):
        """Gets the title of this TaskFormDto.  # noqa: E501

        Gets or sets title of this task.  # noqa: E501

        :return: The title of this TaskFormDto.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this TaskFormDto.

        Gets or sets title of this task.  # noqa: E501

        :param title: The title of this TaskFormDto.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def type(self):
        """Gets the type of this TaskFormDto.  # noqa: E501

        Gets or sets type of this task.  # noqa: E501

        :return: The type of this TaskFormDto.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TaskFormDto.

        Gets or sets type of this task.  # noqa: E501

        :param type: The type of this TaskFormDto.  # noqa: E501
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
        """Gets the priority of this TaskFormDto.  # noqa: E501

        Gets or sets priority of this task.  # noqa: E501

        :return: The priority of this TaskFormDto.  # noqa: E501
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this TaskFormDto.

        Gets or sets priority of this task.  # noqa: E501

        :param priority: The priority of this TaskFormDto.  # noqa: E501
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
    def assigned_to_user_id(self):
        """Gets the assigned_to_user_id of this TaskFormDto.  # noqa: E501

        Gets the id of the actual assigned user, if any.  # noqa: E501

        :return: The assigned_to_user_id of this TaskFormDto.  # noqa: E501
        :rtype: int
        """
        return self._assigned_to_user_id

    @assigned_to_user_id.setter
    def assigned_to_user_id(self, assigned_to_user_id):
        """Sets the assigned_to_user_id of this TaskFormDto.

        Gets the id of the actual assigned user, if any.  # noqa: E501

        :param assigned_to_user_id: The assigned_to_user_id of this TaskFormDto.  # noqa: E501
        :type: int
        """

        self._assigned_to_user_id = assigned_to_user_id

    @property
    def organization_unit_id(self):
        """Gets the organization_unit_id of this TaskFormDto.  # noqa: E501

        Gets or sets the folder/organization-unit id.  # noqa: E501

        :return: The organization_unit_id of this TaskFormDto.  # noqa: E501
        :rtype: int
        """
        return self._organization_unit_id

    @organization_unit_id.setter
    def organization_unit_id(self, organization_unit_id):
        """Sets the organization_unit_id of this TaskFormDto.

        Gets or sets the folder/organization-unit id.  # noqa: E501

        :param organization_unit_id: The organization_unit_id of this TaskFormDto.  # noqa: E501
        :type: int
        """

        self._organization_unit_id = organization_unit_id

    @property
    def external_tag(self):
        """Gets the external_tag of this TaskFormDto.  # noqa: E501

        Identifier of external system where this task is handled  # noqa: E501

        :return: The external_tag of this TaskFormDto.  # noqa: E501
        :rtype: str
        """
        return self._external_tag

    @external_tag.setter
    def external_tag(self, external_tag):
        """Sets the external_tag of this TaskFormDto.

        Identifier of external system where this task is handled  # noqa: E501

        :param external_tag: The external_tag of this TaskFormDto.  # noqa: E501
        :type: str
        """

        self._external_tag = external_tag

    @property
    def creator_job_key(self):
        """Gets the creator_job_key of this TaskFormDto.  # noqa: E501

        Key of the job which created this task  # noqa: E501

        :return: The creator_job_key of this TaskFormDto.  # noqa: E501
        :rtype: str
        """
        return self._creator_job_key

    @creator_job_key.setter
    def creator_job_key(self, creator_job_key):
        """Sets the creator_job_key of this TaskFormDto.

        Key of the job which created this task  # noqa: E501

        :param creator_job_key: The creator_job_key of this TaskFormDto.  # noqa: E501
        :type: str
        """

        self._creator_job_key = creator_job_key

    @property
    def wait_job_key(self):
        """Gets the wait_job_key of this TaskFormDto.  # noqa: E501

        Key job which is waiting on this task  # noqa: E501

        :return: The wait_job_key of this TaskFormDto.  # noqa: E501
        :rtype: str
        """
        return self._wait_job_key

    @wait_job_key.setter
    def wait_job_key(self, wait_job_key):
        """Sets the wait_job_key of this TaskFormDto.

        Key job which is waiting on this task  # noqa: E501

        :param wait_job_key: The wait_job_key of this TaskFormDto.  # noqa: E501
        :type: str
        """

        self._wait_job_key = wait_job_key

    @property
    def last_assigned_time(self):
        """Gets the last_assigned_time of this TaskFormDto.  # noqa: E501

        Datetime when task was last assigned.  # noqa: E501

        :return: The last_assigned_time of this TaskFormDto.  # noqa: E501
        :rtype: datetime
        """
        return self._last_assigned_time

    @last_assigned_time.setter
    def last_assigned_time(self, last_assigned_time):
        """Sets the last_assigned_time of this TaskFormDto.

        Datetime when task was last assigned.  # noqa: E501

        :param last_assigned_time: The last_assigned_time of this TaskFormDto.  # noqa: E501
        :type: datetime
        """

        self._last_assigned_time = last_assigned_time

    @property
    def completion_time(self):
        """Gets the completion_time of this TaskFormDto.  # noqa: E501

        Datetime when task was completed.  # noqa: E501

        :return: The completion_time of this TaskFormDto.  # noqa: E501
        :rtype: datetime
        """
        return self._completion_time

    @completion_time.setter
    def completion_time(self, completion_time):
        """Sets the completion_time of this TaskFormDto.

        Datetime when task was completed.  # noqa: E501

        :param completion_time: The completion_time of this TaskFormDto.  # noqa: E501
        :type: datetime
        """

        self._completion_time = completion_time

    @property
    def is_deleted(self):
        """Gets the is_deleted of this TaskFormDto.  # noqa: E501


        :return: The is_deleted of this TaskFormDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        """Sets the is_deleted of this TaskFormDto.


        :param is_deleted: The is_deleted of this TaskFormDto.  # noqa: E501
        :type: bool
        """

        self._is_deleted = is_deleted

    @property
    def deleter_user_id(self):
        """Gets the deleter_user_id of this TaskFormDto.  # noqa: E501


        :return: The deleter_user_id of this TaskFormDto.  # noqa: E501
        :rtype: int
        """
        return self._deleter_user_id

    @deleter_user_id.setter
    def deleter_user_id(self, deleter_user_id):
        """Sets the deleter_user_id of this TaskFormDto.


        :param deleter_user_id: The deleter_user_id of this TaskFormDto.  # noqa: E501
        :type: int
        """

        self._deleter_user_id = deleter_user_id

    @property
    def deletion_time(self):
        """Gets the deletion_time of this TaskFormDto.  # noqa: E501


        :return: The deletion_time of this TaskFormDto.  # noqa: E501
        :rtype: datetime
        """
        return self._deletion_time

    @deletion_time.setter
    def deletion_time(self, deletion_time):
        """Sets the deletion_time of this TaskFormDto.


        :param deletion_time: The deletion_time of this TaskFormDto.  # noqa: E501
        :type: datetime
        """

        self._deletion_time = deletion_time

    @property
    def last_modification_time(self):
        """Gets the last_modification_time of this TaskFormDto.  # noqa: E501


        :return: The last_modification_time of this TaskFormDto.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modification_time

    @last_modification_time.setter
    def last_modification_time(self, last_modification_time):
        """Sets the last_modification_time of this TaskFormDto.


        :param last_modification_time: The last_modification_time of this TaskFormDto.  # noqa: E501
        :type: datetime
        """

        self._last_modification_time = last_modification_time

    @property
    def last_modifier_user_id(self):
        """Gets the last_modifier_user_id of this TaskFormDto.  # noqa: E501


        :return: The last_modifier_user_id of this TaskFormDto.  # noqa: E501
        :rtype: int
        """
        return self._last_modifier_user_id

    @last_modifier_user_id.setter
    def last_modifier_user_id(self, last_modifier_user_id):
        """Sets the last_modifier_user_id of this TaskFormDto.


        :param last_modifier_user_id: The last_modifier_user_id of this TaskFormDto.  # noqa: E501
        :type: int
        """

        self._last_modifier_user_id = last_modifier_user_id

    @property
    def creation_time(self):
        """Gets the creation_time of this TaskFormDto.  # noqa: E501


        :return: The creation_time of this TaskFormDto.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this TaskFormDto.


        :param creation_time: The creation_time of this TaskFormDto.  # noqa: E501
        :type: datetime
        """

        self._creation_time = creation_time

    @property
    def creator_user_id(self):
        """Gets the creator_user_id of this TaskFormDto.  # noqa: E501


        :return: The creator_user_id of this TaskFormDto.  # noqa: E501
        :rtype: int
        """
        return self._creator_user_id

    @creator_user_id.setter
    def creator_user_id(self, creator_user_id):
        """Sets the creator_user_id of this TaskFormDto.


        :param creator_user_id: The creator_user_id of this TaskFormDto.  # noqa: E501
        :type: int
        """

        self._creator_user_id = creator_user_id

    @property
    def id(self):
        """Gets the id of this TaskFormDto.  # noqa: E501


        :return: The id of this TaskFormDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TaskFormDto.


        :param id: The id of this TaskFormDto.  # noqa: E501
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
        if issubclass(TaskFormDto, dict):
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
        if not isinstance(other, TaskFormDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TaskFormDto):
            return True

        return self.to_dict() != other.to_dict()
