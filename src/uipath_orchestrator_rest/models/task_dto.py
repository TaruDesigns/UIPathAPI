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


class TaskDto(object):
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
        'status': 'str',
        'assigned_to_user': 'UserLoginInfoDto',
        'creator_user': 'UserLoginInfoDto',
        'last_modifier_user': 'UserLoginInfoDto',
        'task_catalog_name': 'str',
        'is_completed': 'bool',
        'bulk_form_layout_id': 'int',
        'form_layout_id': 'int',
        'encrypted': 'bool',
        'tags': 'list[TagDto]',
        'action': 'str',
        'activities': 'list[TaskActivityDto]',
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
        'parent_operation_id': 'str',
        'key': 'str',
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
        'status': 'Status',
        'assigned_to_user': 'AssignedToUser',
        'creator_user': 'CreatorUser',
        'last_modifier_user': 'LastModifierUser',
        'task_catalog_name': 'TaskCatalogName',
        'is_completed': 'IsCompleted',
        'bulk_form_layout_id': 'BulkFormLayoutId',
        'form_layout_id': 'FormLayoutId',
        'encrypted': 'Encrypted',
        'tags': 'Tags',
        'action': 'Action',
        'activities': 'Activities',
        'title': 'Title',
        'type': 'Type',
        'priority': 'Priority',
        'assigned_to_user_id': 'AssignedToUserId',
        'organization_unit_id': 'OrganizationUnitId',
        'external_tag': 'ExternalTag',
        'creator_job_key': 'CreatorJobKey',
        'wait_job_key': 'WaitJobKey',
        'last_assigned_time': 'LastAssignedTime',
        'completion_time': 'CompletionTime',
        'parent_operation_id': 'ParentOperationId',
        'key': 'Key',
        'is_deleted': 'IsDeleted',
        'deleter_user_id': 'DeleterUserId',
        'deletion_time': 'DeletionTime',
        'last_modification_time': 'LastModificationTime',
        'last_modifier_user_id': 'LastModifierUserId',
        'creation_time': 'CreationTime',
        'creator_user_id': 'CreatorUserId',
        'id': 'Id'
    }

    def __init__(self, status=None, assigned_to_user=None, creator_user=None, last_modifier_user=None, task_catalog_name=None, is_completed=None, bulk_form_layout_id=None, form_layout_id=None, encrypted=None, tags=None, action=None, activities=None, title=None, type=None, priority=None, assigned_to_user_id=None, organization_unit_id=None, external_tag=None, creator_job_key=None, wait_job_key=None, last_assigned_time=None, completion_time=None, parent_operation_id=None, key=None, is_deleted=None, deleter_user_id=None, deletion_time=None, last_modification_time=None, last_modifier_user_id=None, creation_time=None, creator_user_id=None, id=None, _configuration=None):  # noqa: E501
        """TaskDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._status = None
        self._assigned_to_user = None
        self._creator_user = None
        self._last_modifier_user = None
        self._task_catalog_name = None
        self._is_completed = None
        self._bulk_form_layout_id = None
        self._form_layout_id = None
        self._encrypted = None
        self._tags = None
        self._action = None
        self._activities = None
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
        self._parent_operation_id = None
        self._key = None
        self._is_deleted = None
        self._deleter_user_id = None
        self._deletion_time = None
        self._last_modification_time = None
        self._last_modifier_user_id = None
        self._creation_time = None
        self._creator_user_id = None
        self._id = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if assigned_to_user is not None:
            self.assigned_to_user = assigned_to_user
        if creator_user is not None:
            self.creator_user = creator_user
        if last_modifier_user is not None:
            self.last_modifier_user = last_modifier_user
        if task_catalog_name is not None:
            self.task_catalog_name = task_catalog_name
        if is_completed is not None:
            self.is_completed = is_completed
        if bulk_form_layout_id is not None:
            self.bulk_form_layout_id = bulk_form_layout_id
        if form_layout_id is not None:
            self.form_layout_id = form_layout_id
        if encrypted is not None:
            self.encrypted = encrypted
        if tags is not None:
            self.tags = tags
        if action is not None:
            self.action = action
        if activities is not None:
            self.activities = activities
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
        if parent_operation_id is not None:
            self.parent_operation_id = parent_operation_id
        if key is not None:
            self.key = key
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
    def status(self):
        """Gets the status of this TaskDto.  # noqa: E501

        Gets or sets the status of this task.  # noqa: E501

        :return: The status of this TaskDto.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TaskDto.

        Gets or sets the status of this task.  # noqa: E501

        :param status: The status of this TaskDto.  # noqa: E501
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
    def assigned_to_user(self):
        """Gets the assigned_to_user of this TaskDto.  # noqa: E501


        :return: The assigned_to_user of this TaskDto.  # noqa: E501
        :rtype: UserLoginInfoDto
        """
        return self._assigned_to_user

    @assigned_to_user.setter
    def assigned_to_user(self, assigned_to_user):
        """Sets the assigned_to_user of this TaskDto.


        :param assigned_to_user: The assigned_to_user of this TaskDto.  # noqa: E501
        :type: UserLoginInfoDto
        """

        self._assigned_to_user = assigned_to_user

    @property
    def creator_user(self):
        """Gets the creator_user of this TaskDto.  # noqa: E501


        :return: The creator_user of this TaskDto.  # noqa: E501
        :rtype: UserLoginInfoDto
        """
        return self._creator_user

    @creator_user.setter
    def creator_user(self, creator_user):
        """Sets the creator_user of this TaskDto.


        :param creator_user: The creator_user of this TaskDto.  # noqa: E501
        :type: UserLoginInfoDto
        """

        self._creator_user = creator_user

    @property
    def last_modifier_user(self):
        """Gets the last_modifier_user of this TaskDto.  # noqa: E501


        :return: The last_modifier_user of this TaskDto.  # noqa: E501
        :rtype: UserLoginInfoDto
        """
        return self._last_modifier_user

    @last_modifier_user.setter
    def last_modifier_user(self, last_modifier_user):
        """Sets the last_modifier_user of this TaskDto.


        :param last_modifier_user: The last_modifier_user of this TaskDto.  # noqa: E501
        :type: UserLoginInfoDto
        """

        self._last_modifier_user = last_modifier_user

    @property
    def task_catalog_name(self):
        """Gets the task_catalog_name of this TaskDto.  # noqa: E501

        Gets or sets the task catalog/category of the task  # noqa: E501

        :return: The task_catalog_name of this TaskDto.  # noqa: E501
        :rtype: str
        """
        return self._task_catalog_name

    @task_catalog_name.setter
    def task_catalog_name(self, task_catalog_name):
        """Sets the task_catalog_name of this TaskDto.

        Gets or sets the task catalog/category of the task  # noqa: E501

        :param task_catalog_name: The task_catalog_name of this TaskDto.  # noqa: E501
        :type: str
        """

        self._task_catalog_name = task_catalog_name

    @property
    def is_completed(self):
        """Gets the is_completed of this TaskDto.  # noqa: E501


        :return: The is_completed of this TaskDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_completed

    @is_completed.setter
    def is_completed(self, is_completed):
        """Sets the is_completed of this TaskDto.


        :param is_completed: The is_completed of this TaskDto.  # noqa: E501
        :type: bool
        """

        self._is_completed = is_completed

    @property
    def bulk_form_layout_id(self):
        """Gets the bulk_form_layout_id of this TaskDto.  # noqa: E501

        Gets or sets the bulkFormLayoutId of the task  # noqa: E501

        :return: The bulk_form_layout_id of this TaskDto.  # noqa: E501
        :rtype: int
        """
        return self._bulk_form_layout_id

    @bulk_form_layout_id.setter
    def bulk_form_layout_id(self, bulk_form_layout_id):
        """Sets the bulk_form_layout_id of this TaskDto.

        Gets or sets the bulkFormLayoutId of the task  # noqa: E501

        :param bulk_form_layout_id: The bulk_form_layout_id of this TaskDto.  # noqa: E501
        :type: int
        """

        self._bulk_form_layout_id = bulk_form_layout_id

    @property
    def form_layout_id(self):
        """Gets the form_layout_id of this TaskDto.  # noqa: E501

        Gets or sets the formLayoutId of the task  # noqa: E501

        :return: The form_layout_id of this TaskDto.  # noqa: E501
        :rtype: int
        """
        return self._form_layout_id

    @form_layout_id.setter
    def form_layout_id(self, form_layout_id):
        """Sets the form_layout_id of this TaskDto.

        Gets or sets the formLayoutId of the task  # noqa: E501

        :param form_layout_id: The form_layout_id of this TaskDto.  # noqa: E501
        :type: int
        """

        self._form_layout_id = form_layout_id

    @property
    def encrypted(self):
        """Gets the encrypted of this TaskDto.  # noqa: E501

        Indicates if the task Data field is stored in an encrypted form.  # noqa: E501

        :return: The encrypted of this TaskDto.  # noqa: E501
        :rtype: bool
        """
        return self._encrypted

    @encrypted.setter
    def encrypted(self, encrypted):
        """Sets the encrypted of this TaskDto.

        Indicates if the task Data field is stored in an encrypted form.  # noqa: E501

        :param encrypted: The encrypted of this TaskDto.  # noqa: E501
        :type: bool
        """

        self._encrypted = encrypted

    @property
    def tags(self):
        """Gets the tags of this TaskDto.  # noqa: E501

        List of tags associated to the task.  # noqa: E501

        :return: The tags of this TaskDto.  # noqa: E501
        :rtype: list[TagDto]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this TaskDto.

        List of tags associated to the task.  # noqa: E501

        :param tags: The tags of this TaskDto.  # noqa: E501
        :type: list[TagDto]
        """

        self._tags = tags

    @property
    def action(self):
        """Gets the action of this TaskDto.  # noqa: E501

        Gets or sets the action performed on the task  # noqa: E501

        :return: The action of this TaskDto.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this TaskDto.

        Gets or sets the action performed on the task  # noqa: E501

        :param action: The action of this TaskDto.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def activities(self):
        """Gets the activities of this TaskDto.  # noqa: E501

        Gets the associated task activities for the task  # noqa: E501

        :return: The activities of this TaskDto.  # noqa: E501
        :rtype: list[TaskActivityDto]
        """
        return self._activities

    @activities.setter
    def activities(self, activities):
        """Sets the activities of this TaskDto.

        Gets the associated task activities for the task  # noqa: E501

        :param activities: The activities of this TaskDto.  # noqa: E501
        :type: list[TaskActivityDto]
        """

        self._activities = activities

    @property
    def title(self):
        """Gets the title of this TaskDto.  # noqa: E501

        Gets or sets title of this task.  # noqa: E501

        :return: The title of this TaskDto.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this TaskDto.

        Gets or sets title of this task.  # noqa: E501

        :param title: The title of this TaskDto.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def type(self):
        """Gets the type of this TaskDto.  # noqa: E501

        Gets or sets type of this task.  # noqa: E501

        :return: The type of this TaskDto.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TaskDto.

        Gets or sets type of this task.  # noqa: E501

        :param type: The type of this TaskDto.  # noqa: E501
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
        """Gets the priority of this TaskDto.  # noqa: E501

        Gets or sets priority of this task.  # noqa: E501

        :return: The priority of this TaskDto.  # noqa: E501
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this TaskDto.

        Gets or sets priority of this task.  # noqa: E501

        :param priority: The priority of this TaskDto.  # noqa: E501
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
        """Gets the assigned_to_user_id of this TaskDto.  # noqa: E501

        Gets the id of the actual assigned user, if any.  # noqa: E501

        :return: The assigned_to_user_id of this TaskDto.  # noqa: E501
        :rtype: int
        """
        return self._assigned_to_user_id

    @assigned_to_user_id.setter
    def assigned_to_user_id(self, assigned_to_user_id):
        """Sets the assigned_to_user_id of this TaskDto.

        Gets the id of the actual assigned user, if any.  # noqa: E501

        :param assigned_to_user_id: The assigned_to_user_id of this TaskDto.  # noqa: E501
        :type: int
        """

        self._assigned_to_user_id = assigned_to_user_id

    @property
    def organization_unit_id(self):
        """Gets the organization_unit_id of this TaskDto.  # noqa: E501

        Gets or sets the folder/organization-unit id.  # noqa: E501

        :return: The organization_unit_id of this TaskDto.  # noqa: E501
        :rtype: int
        """
        return self._organization_unit_id

    @organization_unit_id.setter
    def organization_unit_id(self, organization_unit_id):
        """Sets the organization_unit_id of this TaskDto.

        Gets or sets the folder/organization-unit id.  # noqa: E501

        :param organization_unit_id: The organization_unit_id of this TaskDto.  # noqa: E501
        :type: int
        """

        self._organization_unit_id = organization_unit_id

    @property
    def external_tag(self):
        """Gets the external_tag of this TaskDto.  # noqa: E501

        Identifier of external system where this task is handled  # noqa: E501

        :return: The external_tag of this TaskDto.  # noqa: E501
        :rtype: str
        """
        return self._external_tag

    @external_tag.setter
    def external_tag(self, external_tag):
        """Sets the external_tag of this TaskDto.

        Identifier of external system where this task is handled  # noqa: E501

        :param external_tag: The external_tag of this TaskDto.  # noqa: E501
        :type: str
        """

        self._external_tag = external_tag

    @property
    def creator_job_key(self):
        """Gets the creator_job_key of this TaskDto.  # noqa: E501

        Key of the job which created this task  # noqa: E501

        :return: The creator_job_key of this TaskDto.  # noqa: E501
        :rtype: str
        """
        return self._creator_job_key

    @creator_job_key.setter
    def creator_job_key(self, creator_job_key):
        """Sets the creator_job_key of this TaskDto.

        Key of the job which created this task  # noqa: E501

        :param creator_job_key: The creator_job_key of this TaskDto.  # noqa: E501
        :type: str
        """

        self._creator_job_key = creator_job_key

    @property
    def wait_job_key(self):
        """Gets the wait_job_key of this TaskDto.  # noqa: E501

        Key job which is waiting on this task  # noqa: E501

        :return: The wait_job_key of this TaskDto.  # noqa: E501
        :rtype: str
        """
        return self._wait_job_key

    @wait_job_key.setter
    def wait_job_key(self, wait_job_key):
        """Sets the wait_job_key of this TaskDto.

        Key job which is waiting on this task  # noqa: E501

        :param wait_job_key: The wait_job_key of this TaskDto.  # noqa: E501
        :type: str
        """

        self._wait_job_key = wait_job_key

    @property
    def last_assigned_time(self):
        """Gets the last_assigned_time of this TaskDto.  # noqa: E501

        Datetime when task was last assigned.  # noqa: E501

        :return: The last_assigned_time of this TaskDto.  # noqa: E501
        :rtype: datetime
        """
        return self._last_assigned_time

    @last_assigned_time.setter
    def last_assigned_time(self, last_assigned_time):
        """Sets the last_assigned_time of this TaskDto.

        Datetime when task was last assigned.  # noqa: E501

        :param last_assigned_time: The last_assigned_time of this TaskDto.  # noqa: E501
        :type: datetime
        """

        self._last_assigned_time = last_assigned_time

    @property
    def completion_time(self):
        """Gets the completion_time of this TaskDto.  # noqa: E501

        Datetime when task was completed.  # noqa: E501

        :return: The completion_time of this TaskDto.  # noqa: E501
        :rtype: datetime
        """
        return self._completion_time

    @completion_time.setter
    def completion_time(self, completion_time):
        """Sets the completion_time of this TaskDto.

        Datetime when task was completed.  # noqa: E501

        :param completion_time: The completion_time of this TaskDto.  # noqa: E501
        :type: datetime
        """

        self._completion_time = completion_time

    @property
    def parent_operation_id(self):
        """Gets the parent_operation_id of this TaskDto.  # noqa: E501

        Operation id which created the task.  # noqa: E501

        :return: The parent_operation_id of this TaskDto.  # noqa: E501
        :rtype: str
        """
        return self._parent_operation_id

    @parent_operation_id.setter
    def parent_operation_id(self, parent_operation_id):
        """Sets the parent_operation_id of this TaskDto.

        Operation id which created the task.  # noqa: E501

        :param parent_operation_id: The parent_operation_id of this TaskDto.  # noqa: E501
        :type: str
        """

        self._parent_operation_id = parent_operation_id

    @property
    def key(self):
        """Gets the key of this TaskDto.  # noqa: E501

        The unique Task identifier.  # noqa: E501

        :return: The key of this TaskDto.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this TaskDto.

        The unique Task identifier.  # noqa: E501

        :param key: The key of this TaskDto.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def is_deleted(self):
        """Gets the is_deleted of this TaskDto.  # noqa: E501


        :return: The is_deleted of this TaskDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        """Sets the is_deleted of this TaskDto.


        :param is_deleted: The is_deleted of this TaskDto.  # noqa: E501
        :type: bool
        """

        self._is_deleted = is_deleted

    @property
    def deleter_user_id(self):
        """Gets the deleter_user_id of this TaskDto.  # noqa: E501


        :return: The deleter_user_id of this TaskDto.  # noqa: E501
        :rtype: int
        """
        return self._deleter_user_id

    @deleter_user_id.setter
    def deleter_user_id(self, deleter_user_id):
        """Sets the deleter_user_id of this TaskDto.


        :param deleter_user_id: The deleter_user_id of this TaskDto.  # noqa: E501
        :type: int
        """

        self._deleter_user_id = deleter_user_id

    @property
    def deletion_time(self):
        """Gets the deletion_time of this TaskDto.  # noqa: E501


        :return: The deletion_time of this TaskDto.  # noqa: E501
        :rtype: datetime
        """
        return self._deletion_time

    @deletion_time.setter
    def deletion_time(self, deletion_time):
        """Sets the deletion_time of this TaskDto.


        :param deletion_time: The deletion_time of this TaskDto.  # noqa: E501
        :type: datetime
        """

        self._deletion_time = deletion_time

    @property
    def last_modification_time(self):
        """Gets the last_modification_time of this TaskDto.  # noqa: E501


        :return: The last_modification_time of this TaskDto.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modification_time

    @last_modification_time.setter
    def last_modification_time(self, last_modification_time):
        """Sets the last_modification_time of this TaskDto.


        :param last_modification_time: The last_modification_time of this TaskDto.  # noqa: E501
        :type: datetime
        """

        self._last_modification_time = last_modification_time

    @property
    def last_modifier_user_id(self):
        """Gets the last_modifier_user_id of this TaskDto.  # noqa: E501


        :return: The last_modifier_user_id of this TaskDto.  # noqa: E501
        :rtype: int
        """
        return self._last_modifier_user_id

    @last_modifier_user_id.setter
    def last_modifier_user_id(self, last_modifier_user_id):
        """Sets the last_modifier_user_id of this TaskDto.


        :param last_modifier_user_id: The last_modifier_user_id of this TaskDto.  # noqa: E501
        :type: int
        """

        self._last_modifier_user_id = last_modifier_user_id

    @property
    def creation_time(self):
        """Gets the creation_time of this TaskDto.  # noqa: E501


        :return: The creation_time of this TaskDto.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this TaskDto.


        :param creation_time: The creation_time of this TaskDto.  # noqa: E501
        :type: datetime
        """

        self._creation_time = creation_time

    @property
    def creator_user_id(self):
        """Gets the creator_user_id of this TaskDto.  # noqa: E501


        :return: The creator_user_id of this TaskDto.  # noqa: E501
        :rtype: int
        """
        return self._creator_user_id

    @creator_user_id.setter
    def creator_user_id(self, creator_user_id):
        """Sets the creator_user_id of this TaskDto.


        :param creator_user_id: The creator_user_id of this TaskDto.  # noqa: E501
        :type: int
        """

        self._creator_user_id = creator_user_id

    @property
    def id(self):
        """Gets the id of this TaskDto.  # noqa: E501


        :return: The id of this TaskDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TaskDto.


        :param id: The id of this TaskDto.  # noqa: E501
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
        if issubclass(TaskDto, dict):
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
        if not isinstance(other, TaskDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TaskDto):
            return True

        return self.to_dict() != other.to_dict()
