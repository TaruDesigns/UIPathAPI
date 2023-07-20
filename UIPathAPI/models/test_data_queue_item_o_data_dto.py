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


class TestDataQueueItemODataDto(object):
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
        'test_data_queue_id': 'int',
        'content_json': 'str',
        'is_consumed': 'bool',
        'id': 'int'
    }

    attribute_map = {
        'test_data_queue_id': 'TestDataQueueId',
        'content_json': 'ContentJson',
        'is_consumed': 'IsConsumed',
        'id': 'Id'
    }

    def __init__(self, test_data_queue_id=None, content_json=None, is_consumed=None, id=None, _configuration=None):  # noqa: E501
        """TestDataQueueItemODataDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._test_data_queue_id = None
        self._content_json = None
        self._is_consumed = None
        self._id = None
        self.discriminator = None

        if test_data_queue_id is not None:
            self.test_data_queue_id = test_data_queue_id
        if content_json is not None:
            self.content_json = content_json
        if is_consumed is not None:
            self.is_consumed = is_consumed
        if id is not None:
            self.id = id

    @property
    def test_data_queue_id(self):
        """Gets the test_data_queue_id of this TestDataQueueItemODataDto.  # noqa: E501


        :return: The test_data_queue_id of this TestDataQueueItemODataDto.  # noqa: E501
        :rtype: int
        """
        return self._test_data_queue_id

    @test_data_queue_id.setter
    def test_data_queue_id(self, test_data_queue_id):
        """Sets the test_data_queue_id of this TestDataQueueItemODataDto.


        :param test_data_queue_id: The test_data_queue_id of this TestDataQueueItemODataDto.  # noqa: E501
        :type: int
        """

        self._test_data_queue_id = test_data_queue_id

    @property
    def content_json(self):
        """Gets the content_json of this TestDataQueueItemODataDto.  # noqa: E501


        :return: The content_json of this TestDataQueueItemODataDto.  # noqa: E501
        :rtype: str
        """
        return self._content_json

    @content_json.setter
    def content_json(self, content_json):
        """Sets the content_json of this TestDataQueueItemODataDto.


        :param content_json: The content_json of this TestDataQueueItemODataDto.  # noqa: E501
        :type: str
        """

        self._content_json = content_json

    @property
    def is_consumed(self):
        """Gets the is_consumed of this TestDataQueueItemODataDto.  # noqa: E501


        :return: The is_consumed of this TestDataQueueItemODataDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_consumed

    @is_consumed.setter
    def is_consumed(self, is_consumed):
        """Sets the is_consumed of this TestDataQueueItemODataDto.


        :param is_consumed: The is_consumed of this TestDataQueueItemODataDto.  # noqa: E501
        :type: bool
        """

        self._is_consumed = is_consumed

    @property
    def id(self):
        """Gets the id of this TestDataQueueItemODataDto.  # noqa: E501


        :return: The id of this TestDataQueueItemODataDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TestDataQueueItemODataDto.


        :param id: The id of this TestDataQueueItemODataDto.  # noqa: E501
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
        if issubclass(TestDataQueueItemODataDto, dict):
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
        if not isinstance(other, TestDataQueueItemODataDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TestDataQueueItemODataDto):
            return True

        return self.to_dict() != other.to_dict()
