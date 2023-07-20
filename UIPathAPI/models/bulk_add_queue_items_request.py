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


class BulkAddQueueItemsRequest(object):
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
        'queue_name': 'str',
        'commit_type': 'str',
        'queue_items': 'list[QueueItemDataDto]'
    }

    attribute_map = {
        'queue_name': 'queueName',
        'commit_type': 'commitType',
        'queue_items': 'queueItems'
    }

    def __init__(self, queue_name=None, commit_type=None, queue_items=None, _configuration=None):  # noqa: E501
        """BulkAddQueueItemsRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._queue_name = None
        self._commit_type = None
        self._queue_items = None
        self.discriminator = None

        self.queue_name = queue_name
        self.commit_type = commit_type
        if queue_items is not None:
            self.queue_items = queue_items

    @property
    def queue_name(self):
        """Gets the queue_name of this BulkAddQueueItemsRequest.  # noqa: E501


        :return: The queue_name of this BulkAddQueueItemsRequest.  # noqa: E501
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        """Sets the queue_name of this BulkAddQueueItemsRequest.


        :param queue_name: The queue_name of this BulkAddQueueItemsRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and queue_name is None:
            raise ValueError("Invalid value for `queue_name`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                queue_name is not None and len(queue_name) < 1):
            raise ValueError("Invalid value for `queue_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._queue_name = queue_name

    @property
    def commit_type(self):
        """Gets the commit_type of this BulkAddQueueItemsRequest.  # noqa: E501


        :return: The commit_type of this BulkAddQueueItemsRequest.  # noqa: E501
        :rtype: str
        """
        return self._commit_type

    @commit_type.setter
    def commit_type(self, commit_type):
        """Sets the commit_type of this BulkAddQueueItemsRequest.


        :param commit_type: The commit_type of this BulkAddQueueItemsRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and commit_type is None:
            raise ValueError("Invalid value for `commit_type`, must not be `None`")  # noqa: E501
        allowed_values = ["AllOrNothing", "StopOnFirstFailure", "ProcessAllIndependently"]  # noqa: E501
        if (self._configuration.client_side_validation and
                commit_type not in allowed_values):
            raise ValueError(
                "Invalid value for `commit_type` ({0}), must be one of {1}"  # noqa: E501
                .format(commit_type, allowed_values)
            )

        self._commit_type = commit_type

    @property
    def queue_items(self):
        """Gets the queue_items of this BulkAddQueueItemsRequest.  # noqa: E501


        :return: The queue_items of this BulkAddQueueItemsRequest.  # noqa: E501
        :rtype: list[QueueItemDataDto]
        """
        return self._queue_items

    @queue_items.setter
    def queue_items(self, queue_items):
        """Sets the queue_items of this BulkAddQueueItemsRequest.


        :param queue_items: The queue_items of this BulkAddQueueItemsRequest.  # noqa: E501
        :type: list[QueueItemDataDto]
        """

        self._queue_items = queue_items

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
        if issubclass(BulkAddQueueItemsRequest, dict):
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
        if not isinstance(other, BulkAddQueueItemsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BulkAddQueueItemsRequest):
            return True

        return self.to_dict() != other.to_dict()
