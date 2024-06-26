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


class BulkTasksCompletionRequest(object):
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
        'action': 'str',
        'task_ids': 'list[int]',
        'data': 'object',
        'title': 'str',
        'task_catalog_id': 'int',
        'unset_task_catalog': 'bool',
        'priority': 'str',
        'note_text': 'str'
    }

    attribute_map = {
        'action': 'action',
        'task_ids': 'taskIds',
        'data': 'data',
        'title': 'title',
        'task_catalog_id': 'taskCatalogId',
        'unset_task_catalog': 'unsetTaskCatalog',
        'priority': 'priority',
        'note_text': 'noteText'
    }

    def __init__(self, action=None, task_ids=None, data=None, title=None, task_catalog_id=None, unset_task_catalog=None, priority=None, note_text=None, _configuration=None):  # noqa: E501
        """BulkTasksCompletionRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._action = None
        self._task_ids = None
        self._data = None
        self._title = None
        self._task_catalog_id = None
        self._unset_task_catalog = None
        self._priority = None
        self._note_text = None
        self.discriminator = None

        self.action = action
        self.task_ids = task_ids
        self.data = data
        if title is not None:
            self.title = title
        if task_catalog_id is not None:
            self.task_catalog_id = task_catalog_id
        if unset_task_catalog is not None:
            self.unset_task_catalog = unset_task_catalog
        if priority is not None:
            self.priority = priority
        if note_text is not None:
            self.note_text = note_text

    @property
    def action(self):
        """Gets the action of this BulkTasksCompletionRequest.  # noqa: E501

        Action taken on this task  # noqa: E501

        :return: The action of this BulkTasksCompletionRequest.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this BulkTasksCompletionRequest.

        Action taken on this task  # noqa: E501

        :param action: The action of this BulkTasksCompletionRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and action is None:
            raise ValueError("Invalid value for `action`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                action is not None and len(action) < 1):
            raise ValueError("Invalid value for `action`, length must be greater than or equal to `1`")  # noqa: E501

        self._action = action

    @property
    def task_ids(self):
        """Gets the task_ids of this BulkTasksCompletionRequest.  # noqa: E501

        List of Task Ids which have to be Bulk edited  # noqa: E501

        :return: The task_ids of this BulkTasksCompletionRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._task_ids

    @task_ids.setter
    def task_ids(self, task_ids):
        """Sets the task_ids of this BulkTasksCompletionRequest.

        List of Task Ids which have to be Bulk edited  # noqa: E501

        :param task_ids: The task_ids of this BulkTasksCompletionRequest.  # noqa: E501
        :type: list[int]
        """
        if self._configuration.client_side_validation and task_ids is None:
            raise ValueError("Invalid value for `task_ids`, must not be `None`")  # noqa: E501

        self._task_ids = task_ids

    @property
    def data(self):
        """Gets the data of this BulkTasksCompletionRequest.  # noqa: E501

        Task data json  # noqa: E501

        :return: The data of this BulkTasksCompletionRequest.  # noqa: E501
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this BulkTasksCompletionRequest.

        Task data json  # noqa: E501

        :param data: The data of this BulkTasksCompletionRequest.  # noqa: E501
        :type: object
        """
        if self._configuration.client_side_validation and data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def title(self):
        """Gets the title of this BulkTasksCompletionRequest.  # noqa: E501

        Title of tasks  # noqa: E501

        :return: The title of this BulkTasksCompletionRequest.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this BulkTasksCompletionRequest.

        Title of tasks  # noqa: E501

        :param title: The title of this BulkTasksCompletionRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                title is not None and len(title) > 512):
            raise ValueError("Invalid value for `title`, length must be less than or equal to `512`")  # noqa: E501

        self._title = title

    @property
    def task_catalog_id(self):
        """Gets the task_catalog_id of this BulkTasksCompletionRequest.  # noqa: E501

        Action Catalog to be associated with the tasks  # noqa: E501

        :return: The task_catalog_id of this BulkTasksCompletionRequest.  # noqa: E501
        :rtype: int
        """
        return self._task_catalog_id

    @task_catalog_id.setter
    def task_catalog_id(self, task_catalog_id):
        """Sets the task_catalog_id of this BulkTasksCompletionRequest.

        Action Catalog to be associated with the tasks  # noqa: E501

        :param task_catalog_id: The task_catalog_id of this BulkTasksCompletionRequest.  # noqa: E501
        :type: int
        """

        self._task_catalog_id = task_catalog_id

    @property
    def unset_task_catalog(self):
        """Gets the unset_task_catalog of this BulkTasksCompletionRequest.  # noqa: E501

        Unset/Unassociate action catalogs with the tasks  Set to true for unassociating catalog  # noqa: E501

        :return: The unset_task_catalog of this BulkTasksCompletionRequest.  # noqa: E501
        :rtype: bool
        """
        return self._unset_task_catalog

    @unset_task_catalog.setter
    def unset_task_catalog(self, unset_task_catalog):
        """Sets the unset_task_catalog of this BulkTasksCompletionRequest.

        Unset/Unassociate action catalogs with the tasks  Set to true for unassociating catalog  # noqa: E501

        :param unset_task_catalog: The unset_task_catalog of this BulkTasksCompletionRequest.  # noqa: E501
        :type: bool
        """

        self._unset_task_catalog = unset_task_catalog

    @property
    def priority(self):
        """Gets the priority of this BulkTasksCompletionRequest.  # noqa: E501

        Priority of tasks  # noqa: E501

        :return: The priority of this BulkTasksCompletionRequest.  # noqa: E501
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this BulkTasksCompletionRequest.

        Priority of tasks  # noqa: E501

        :param priority: The priority of this BulkTasksCompletionRequest.  # noqa: E501
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
    def note_text(self):
        """Gets the note_text of this BulkTasksCompletionRequest.  # noqa: E501

        Comment to be added while doing the bulk operation  # noqa: E501

        :return: The note_text of this BulkTasksCompletionRequest.  # noqa: E501
        :rtype: str
        """
        return self._note_text

    @note_text.setter
    def note_text(self, note_text):
        """Sets the note_text of this BulkTasksCompletionRequest.

        Comment to be added while doing the bulk operation  # noqa: E501

        :param note_text: The note_text of this BulkTasksCompletionRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                note_text is not None and len(note_text) > 512):
            raise ValueError("Invalid value for `note_text`, length must be less than or equal to `512`")  # noqa: E501

        self._note_text = note_text

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
        if issubclass(BulkTasksCompletionRequest, dict):
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
        if not isinstance(other, BulkTasksCompletionRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BulkTasksCompletionRequest):
            return True

        return self.to_dict() != other.to_dict()
