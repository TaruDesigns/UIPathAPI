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


class QueueSetItemReviewStatusRequest(object):
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
        'queue_items': 'list[LongVersionedEntity]'
    }

    attribute_map = {
        'status': 'status',
        'queue_items': 'queueItems'
    }

    def __init__(self, status=None, queue_items=None, _configuration=None):  # noqa: E501
        """QueueSetItemReviewStatusRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._status = None
        self._queue_items = None
        self.discriminator = None

        self.status = status
        self.queue_items = queue_items

    @property
    def status(self):
        """Gets the status of this QueueSetItemReviewStatusRequest.  # noqa: E501


        :return: The status of this QueueSetItemReviewStatusRequest.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this QueueSetItemReviewStatusRequest.


        :param status: The status of this QueueSetItemReviewStatusRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                status is not None and len(status) < 1):
            raise ValueError("Invalid value for `status`, length must be greater than or equal to `1`")  # noqa: E501

        self._status = status

    @property
    def queue_items(self):
        """Gets the queue_items of this QueueSetItemReviewStatusRequest.  # noqa: E501


        :return: The queue_items of this QueueSetItemReviewStatusRequest.  # noqa: E501
        :rtype: list[LongVersionedEntity]
        """
        return self._queue_items

    @queue_items.setter
    def queue_items(self, queue_items):
        """Sets the queue_items of this QueueSetItemReviewStatusRequest.


        :param queue_items: The queue_items of this QueueSetItemReviewStatusRequest.  # noqa: E501
        :type: list[LongVersionedEntity]
        """
        if self._configuration.client_side_validation and queue_items is None:
            raise ValueError("Invalid value for `queue_items`, must not be `None`")  # noqa: E501

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
        if issubclass(QueueSetItemReviewStatusRequest, dict):
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
        if not isinstance(other, QueueSetItemReviewStatusRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QueueSetItemReviewStatusRequest):
            return True

        return self.to_dict() != other.to_dict()