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


class TestCaseAssertionDto(object):
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
        'message': 'str',
        'payload': 'str',
        'succeeded': 'bool',
        'test_case_execution_id': 'int',
        'has_screenshot': 'bool',
        'creation_time': 'datetime',
        'id': 'int'
    }

    attribute_map = {
        'message': 'Message',
        'payload': 'Payload',
        'succeeded': 'Succeeded',
        'test_case_execution_id': 'TestCaseExecutionId',
        'has_screenshot': 'HasScreenshot',
        'creation_time': 'CreationTime',
        'id': 'Id'
    }

    def __init__(self, message=None, payload=None, succeeded=None, test_case_execution_id=None, has_screenshot=None, creation_time=None, id=None, _configuration=None):  # noqa: E501
        """TestCaseAssertionDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._message = None
        self._payload = None
        self._succeeded = None
        self._test_case_execution_id = None
        self._has_screenshot = None
        self._creation_time = None
        self._id = None
        self.discriminator = None

        if message is not None:
            self.message = message
        if payload is not None:
            self.payload = payload
        if succeeded is not None:
            self.succeeded = succeeded
        if test_case_execution_id is not None:
            self.test_case_execution_id = test_case_execution_id
        if has_screenshot is not None:
            self.has_screenshot = has_screenshot
        if creation_time is not None:
            self.creation_time = creation_time
        if id is not None:
            self.id = id

    @property
    def message(self):
        """Gets the message of this TestCaseAssertionDto.  # noqa: E501


        :return: The message of this TestCaseAssertionDto.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this TestCaseAssertionDto.


        :param message: The message of this TestCaseAssertionDto.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def payload(self):
        """Gets the payload of this TestCaseAssertionDto.  # noqa: E501


        :return: The payload of this TestCaseAssertionDto.  # noqa: E501
        :rtype: str
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this TestCaseAssertionDto.


        :param payload: The payload of this TestCaseAssertionDto.  # noqa: E501
        :type: str
        """

        self._payload = payload

    @property
    def succeeded(self):
        """Gets the succeeded of this TestCaseAssertionDto.  # noqa: E501


        :return: The succeeded of this TestCaseAssertionDto.  # noqa: E501
        :rtype: bool
        """
        return self._succeeded

    @succeeded.setter
    def succeeded(self, succeeded):
        """Sets the succeeded of this TestCaseAssertionDto.


        :param succeeded: The succeeded of this TestCaseAssertionDto.  # noqa: E501
        :type: bool
        """

        self._succeeded = succeeded

    @property
    def test_case_execution_id(self):
        """Gets the test_case_execution_id of this TestCaseAssertionDto.  # noqa: E501


        :return: The test_case_execution_id of this TestCaseAssertionDto.  # noqa: E501
        :rtype: int
        """
        return self._test_case_execution_id

    @test_case_execution_id.setter
    def test_case_execution_id(self, test_case_execution_id):
        """Sets the test_case_execution_id of this TestCaseAssertionDto.


        :param test_case_execution_id: The test_case_execution_id of this TestCaseAssertionDto.  # noqa: E501
        :type: int
        """

        self._test_case_execution_id = test_case_execution_id

    @property
    def has_screenshot(self):
        """Gets the has_screenshot of this TestCaseAssertionDto.  # noqa: E501


        :return: The has_screenshot of this TestCaseAssertionDto.  # noqa: E501
        :rtype: bool
        """
        return self._has_screenshot

    @has_screenshot.setter
    def has_screenshot(self, has_screenshot):
        """Sets the has_screenshot of this TestCaseAssertionDto.


        :param has_screenshot: The has_screenshot of this TestCaseAssertionDto.  # noqa: E501
        :type: bool
        """

        self._has_screenshot = has_screenshot

    @property
    def creation_time(self):
        """Gets the creation_time of this TestCaseAssertionDto.  # noqa: E501


        :return: The creation_time of this TestCaseAssertionDto.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this TestCaseAssertionDto.


        :param creation_time: The creation_time of this TestCaseAssertionDto.  # noqa: E501
        :type: datetime
        """

        self._creation_time = creation_time

    @property
    def id(self):
        """Gets the id of this TestCaseAssertionDto.  # noqa: E501


        :return: The id of this TestCaseAssertionDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TestCaseAssertionDto.


        :param id: The id of this TestCaseAssertionDto.  # noqa: E501
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
        if issubclass(TestCaseAssertionDto, dict):
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
        if not isinstance(other, TestCaseAssertionDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TestCaseAssertionDto):
            return True

        return self.to_dict() != other.to_dict()