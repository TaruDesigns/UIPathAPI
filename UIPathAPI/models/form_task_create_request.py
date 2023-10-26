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


class FormTaskCreateRequest(object):
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
        'title': 'str',
        'priority': 'str',
        'data': 'object',
        'task_catalog_name': 'str',
        'external_tag': 'str',
        'tags': 'list[TagDto]'
    }

    attribute_map = {
        'form_layout': 'formLayout',
        'form_layout_id': 'formLayoutId',
        'bulk_form_layout_id': 'bulkFormLayoutId',
        'title': 'title',
        'priority': 'priority',
        'data': 'data',
        'task_catalog_name': 'taskCatalogName',
        'external_tag': 'externalTag',
        'tags': 'tags'
    }

    def __init__(self, form_layout=None, form_layout_id=None, bulk_form_layout_id=None, title=None, priority=None, data=None, task_catalog_name=None, external_tag=None, tags=None, _configuration=None):  # noqa: E501
        """FormTaskCreateRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._form_layout = None
        self._form_layout_id = None
        self._bulk_form_layout_id = None
        self._title = None
        self._priority = None
        self._data = None
        self._task_catalog_name = None
        self._external_tag = None
        self._tags = None
        self.discriminator = None

        if form_layout is not None:
            self.form_layout = form_layout
        if form_layout_id is not None:
            self.form_layout_id = form_layout_id
        if bulk_form_layout_id is not None:
            self.bulk_form_layout_id = bulk_form_layout_id
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
    def form_layout(self):
        """Gets the form_layout of this FormTaskCreateRequest.  # noqa: E501

        Text representing the form layout schema  # noqa: E501

        :return: The form_layout of this FormTaskCreateRequest.  # noqa: E501
        :rtype: object
        """
        return self._form_layout

    @form_layout.setter
    def form_layout(self, form_layout):
        """Sets the form_layout of this FormTaskCreateRequest.

        Text representing the form layout schema  # noqa: E501

        :param form_layout: The form_layout of this FormTaskCreateRequest.  # noqa: E501
        :type: object
        """

        self._form_layout = form_layout

    @property
    def form_layout_id(self):
        """Gets the form_layout_id of this FormTaskCreateRequest.  # noqa: E501

        Unique FormLayoutId for a form layout  # noqa: E501

        :return: The form_layout_id of this FormTaskCreateRequest.  # noqa: E501
        :rtype: int
        """
        return self._form_layout_id

    @form_layout_id.setter
    def form_layout_id(self, form_layout_id):
        """Sets the form_layout_id of this FormTaskCreateRequest.

        Unique FormLayoutId for a form layout  # noqa: E501

        :param form_layout_id: The form_layout_id of this FormTaskCreateRequest.  # noqa: E501
        :type: int
        """

        self._form_layout_id = form_layout_id

    @property
    def bulk_form_layout_id(self):
        """Gets the bulk_form_layout_id of this FormTaskCreateRequest.  # noqa: E501

        Unique BulkFormLayoutId for a form layout  # noqa: E501

        :return: The bulk_form_layout_id of this FormTaskCreateRequest.  # noqa: E501
        :rtype: int
        """
        return self._bulk_form_layout_id

    @bulk_form_layout_id.setter
    def bulk_form_layout_id(self, bulk_form_layout_id):
        """Sets the bulk_form_layout_id of this FormTaskCreateRequest.

        Unique BulkFormLayoutId for a form layout  # noqa: E501

        :param bulk_form_layout_id: The bulk_form_layout_id of this FormTaskCreateRequest.  # noqa: E501
        :type: int
        """

        self._bulk_form_layout_id = bulk_form_layout_id

    @property
    def title(self):
        """Gets the title of this FormTaskCreateRequest.  # noqa: E501

        Gets or sets title of this task.  # noqa: E501

        :return: The title of this FormTaskCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this FormTaskCreateRequest.

        Gets or sets title of this task.  # noqa: E501

        :param title: The title of this FormTaskCreateRequest.  # noqa: E501
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
        """Gets the priority of this FormTaskCreateRequest.  # noqa: E501

        Gets or sets priority of this task.  # noqa: E501

        :return: The priority of this FormTaskCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this FormTaskCreateRequest.

        Gets or sets priority of this task.  # noqa: E501

        :param priority: The priority of this FormTaskCreateRequest.  # noqa: E501
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
        """Gets the data of this FormTaskCreateRequest.  # noqa: E501

        Task data  # noqa: E501

        :return: The data of this FormTaskCreateRequest.  # noqa: E501
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this FormTaskCreateRequest.

        Task data  # noqa: E501

        :param data: The data of this FormTaskCreateRequest.  # noqa: E501
        :type: object
        """

        self._data = data

    @property
    def task_catalog_name(self):
        """Gets the task_catalog_name of this FormTaskCreateRequest.  # noqa: E501

        Gets or sets the task catalog/category of the task  # noqa: E501

        :return: The task_catalog_name of this FormTaskCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._task_catalog_name

    @task_catalog_name.setter
    def task_catalog_name(self, task_catalog_name):
        """Sets the task_catalog_name of this FormTaskCreateRequest.

        Gets or sets the task catalog/category of the task  # noqa: E501

        :param task_catalog_name: The task_catalog_name of this FormTaskCreateRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                task_catalog_name is not None and len(task_catalog_name) > 50):
            raise ValueError("Invalid value for `task_catalog_name`, length must be less than or equal to `50`")  # noqa: E501

        self._task_catalog_name = task_catalog_name

    @property
    def external_tag(self):
        """Gets the external_tag of this FormTaskCreateRequest.  # noqa: E501

        Reference or name of external system  # noqa: E501

        :return: The external_tag of this FormTaskCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._external_tag

    @external_tag.setter
    def external_tag(self, external_tag):
        """Sets the external_tag of this FormTaskCreateRequest.

        Reference or name of external system  # noqa: E501

        :param external_tag: The external_tag of this FormTaskCreateRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                external_tag is not None and len(external_tag) > 128):
            raise ValueError("Invalid value for `external_tag`, length must be less than or equal to `128`")  # noqa: E501

        self._external_tag = external_tag

    @property
    def tags(self):
        """Gets the tags of this FormTaskCreateRequest.  # noqa: E501

        List of tags associated to the task.  # noqa: E501

        :return: The tags of this FormTaskCreateRequest.  # noqa: E501
        :rtype: list[TagDto]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this FormTaskCreateRequest.

        List of tags associated to the task.  # noqa: E501

        :param tags: The tags of this FormTaskCreateRequest.  # noqa: E501
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
        if issubclass(FormTaskCreateRequest, dict):
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
        if not isinstance(other, FormTaskCreateRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FormTaskCreateRequest):
            return True

        return self.to_dict() != other.to_dict()
