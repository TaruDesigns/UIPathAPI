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


class TestDataQueueSetItemsConsumedDto(object):
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
        'item_ids': 'list[int]',
        'is_consumed': 'bool'
    }

    attribute_map = {
        'item_ids': 'itemIds',
        'is_consumed': 'isConsumed'
    }

    def __init__(self, item_ids=None, is_consumed=None, _configuration=None):  # noqa: E501
        """TestDataQueueSetItemsConsumedDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._item_ids = None
        self._is_consumed = None
        self.discriminator = None

        self.item_ids = item_ids
        self.is_consumed = is_consumed

    @property
    def item_ids(self):
        """Gets the item_ids of this TestDataQueueSetItemsConsumedDto.  # noqa: E501


        :return: The item_ids of this TestDataQueueSetItemsConsumedDto.  # noqa: E501
        :rtype: list[int]
        """
        return self._item_ids

    @item_ids.setter
    def item_ids(self, item_ids):
        """Sets the item_ids of this TestDataQueueSetItemsConsumedDto.


        :param item_ids: The item_ids of this TestDataQueueSetItemsConsumedDto.  # noqa: E501
        :type: list[int]
        """
        if self._configuration.client_side_validation and item_ids is None:
            raise ValueError("Invalid value for `item_ids`, must not be `None`")  # noqa: E501

        self._item_ids = item_ids

    @property
    def is_consumed(self):
        """Gets the is_consumed of this TestDataQueueSetItemsConsumedDto.  # noqa: E501


        :return: The is_consumed of this TestDataQueueSetItemsConsumedDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_consumed

    @is_consumed.setter
    def is_consumed(self, is_consumed):
        """Sets the is_consumed of this TestDataQueueSetItemsConsumedDto.


        :param is_consumed: The is_consumed of this TestDataQueueSetItemsConsumedDto.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and is_consumed is None:
            raise ValueError("Invalid value for `is_consumed`, must not be `None`")  # noqa: E501

        self._is_consumed = is_consumed

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
        if issubclass(TestDataQueueSetItemsConsumedDto, dict):
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
        if not isinstance(other, TestDataQueueSetItemsConsumedDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TestDataQueueSetItemsConsumedDto):
            return True

        return self.to_dict() != other.to_dict()
