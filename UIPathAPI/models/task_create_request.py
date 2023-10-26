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


class TaskCreateRequest(object):
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
        'title': 'str',
        'priority': 'str',
        'data': 'object',
        'task_catalog_name': 'str',
        'external_tag': 'str',
        'tags': 'list[TagDto]'
    }

    attribute_map = {
        'type': 'type',
        'title': 'title',
        'priority': 'priority',
        'data': 'data',
        'task_catalog_name': 'taskCatalogName',
        'external_tag': 'externalTag',
        'tags': 'tags'
    }

    def __init__(self, type=None, title=None, priority=None, data=None, task_catalog_name=None, external_tag=None, tags=None, _configuration=None):  # noqa: E501
        """TaskCreateRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._type = None
        self._title = None
        self._priority = None
        self._data = None
        self._task_catalog_name = None
        self._external_tag = None
        self._tags = None
        self.discriminator = None

        if type is not None:
            self.type = type
        self.title = title
        if priority is not None:
            self.priority = priority
        if data is not None:
            self.data = data
        if task_catalog_name is not None:
            self.task_catalog_name = task_catalog_name
        if external_tag is not None:
            self.external_tag = external_tag
        if tags is not None:
            self.tags = tags

    @property
    def type(self):
        """Gets the type of this TaskCreateRequest.  # noqa: E501

        Gets or sets type of this task, allowed type is 'ExternalTask'.  # noqa: E501

        :return: The type of this TaskCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TaskCreateRequest.

        Gets or sets type of this task, allowed type is 'ExternalTask'.  # noqa: E501

        :param type: The type of this TaskCreateRequest.  # noqa: E501
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
    def title(self):
        """Gets the title of this TaskCreateRequest.  # noqa: E501

        Gets or sets title of this task.  # noqa: E501

        :return: The title of this TaskCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this TaskCreateRequest.

        Gets or sets title of this task.  # noqa: E501

        :param title: The title of this TaskCreateRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                title is not None and len(title) > 512):
            raise ValueError("Invalid value for `title`, length must be less than or equal to `512`")  # noqa: E501
        if (self._configuration.client_side_validation and
                title is not None and len(title) < 0):
            raise ValueError("Invalid value for `title`, length must be greater than or equal to `0`")  # noqa: E501

        self._title = title

    @property
    def priority(self):
        """Gets the priority of this TaskCreateRequest.  # noqa: E501

        Gets or sets priority of this task.  # noqa: E501

        :return: The priority of this TaskCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this TaskCreateRequest.

        Gets or sets priority of this task.  # noqa: E501

        :param priority: The priority of this TaskCreateRequest.  # noqa: E501
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
    def data(self):
        """Gets the data of this TaskCreateRequest.  # noqa: E501

        Task data  # noqa: E501

        :return: The data of this TaskCreateRequest.  # noqa: E501
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this TaskCreateRequest.

        Task data  # noqa: E501

        :param data: The data of this TaskCreateRequest.  # noqa: E501
        :type: object
        """

        self._data = data

    @property
    def task_catalog_name(self):
        """Gets the task_catalog_name of this TaskCreateRequest.  # noqa: E501

        Gets or sets the task catalog/category of the task  # noqa: E501

        :return: The task_catalog_name of this TaskCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._task_catalog_name

    @task_catalog_name.setter
    def task_catalog_name(self, task_catalog_name):
        """Sets the task_catalog_name of this TaskCreateRequest.

        Gets or sets the task catalog/category of the task  # noqa: E501

        :param task_catalog_name: The task_catalog_name of this TaskCreateRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                task_catalog_name is not None and len(task_catalog_name) > 50):
            raise ValueError("Invalid value for `task_catalog_name`, length must be less than or equal to `50`")  # noqa: E501

        self._task_catalog_name = task_catalog_name

    @property
    def external_tag(self):
        """Gets the external_tag of this TaskCreateRequest.  # noqa: E501

        Reference or name of external system  # noqa: E501

        :return: The external_tag of this TaskCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._external_tag

    @external_tag.setter
    def external_tag(self, external_tag):
        """Sets the external_tag of this TaskCreateRequest.

        Reference or name of external system  # noqa: E501

        :param external_tag: The external_tag of this TaskCreateRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                external_tag is not None and len(external_tag) > 128):
            raise ValueError("Invalid value for `external_tag`, length must be less than or equal to `128`")  # noqa: E501

        self._external_tag = external_tag

    @property
    def tags(self):
        """Gets the tags of this TaskCreateRequest.  # noqa: E501

        List of tags associated to the task.  # noqa: E501

        :return: The tags of this TaskCreateRequest.  # noqa: E501
        :rtype: list[TagDto]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this TaskCreateRequest.

        List of tags associated to the task.  # noqa: E501

        :param tags: The tags of this TaskCreateRequest.  # noqa: E501
        :type: list[TagDto]
        """

        self._tags = tags

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
        if issubclass(TaskCreateRequest, dict):
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
        if not isinstance(other, TaskCreateRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TaskCreateRequest):
            return True

        return self.to_dict() != other.to_dict()
