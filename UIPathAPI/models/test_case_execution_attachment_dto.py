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


class TestCaseExecutionAttachmentDto(object):
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
        'test_case_execution_id': 'int',
        'file_name': 'str',
        'mime_type': 'str',
        'creation_time': 'datetime',
        'tags': 'list[str]',
        'id': 'int'
    }

    attribute_map = {
        'test_case_execution_id': 'TestCaseExecutionId',
        'file_name': 'FileName',
        'mime_type': 'MimeType',
        'creation_time': 'CreationTime',
        'tags': 'Tags',
        'id': 'Id'
    }

    def __init__(self, test_case_execution_id=None, file_name=None, mime_type=None, creation_time=None, tags=None, id=None, _configuration=None):  # noqa: E501
        """TestCaseExecutionAttachmentDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._test_case_execution_id = None
        self._file_name = None
        self._mime_type = None
        self._creation_time = None
        self._tags = None
        self._id = None
        self.discriminator = None

        if test_case_execution_id is not None:
            self.test_case_execution_id = test_case_execution_id
        if file_name is not None:
            self.file_name = file_name
        if mime_type is not None:
            self.mime_type = mime_type
        if creation_time is not None:
            self.creation_time = creation_time
        if tags is not None:
            self.tags = tags
        if id is not None:
            self.id = id

    @property
    def test_case_execution_id(self):
        """Gets the test_case_execution_id of this TestCaseExecutionAttachmentDto.  # noqa: E501


        :return: The test_case_execution_id of this TestCaseExecutionAttachmentDto.  # noqa: E501
        :rtype: int
        """
        return self._test_case_execution_id

    @test_case_execution_id.setter
    def test_case_execution_id(self, test_case_execution_id):
        """Sets the test_case_execution_id of this TestCaseExecutionAttachmentDto.


        :param test_case_execution_id: The test_case_execution_id of this TestCaseExecutionAttachmentDto.  # noqa: E501
        :type: int
        """

        self._test_case_execution_id = test_case_execution_id

    @property
    def file_name(self):
        """Gets the file_name of this TestCaseExecutionAttachmentDto.  # noqa: E501


        :return: The file_name of this TestCaseExecutionAttachmentDto.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this TestCaseExecutionAttachmentDto.


        :param file_name: The file_name of this TestCaseExecutionAttachmentDto.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def mime_type(self):
        """Gets the mime_type of this TestCaseExecutionAttachmentDto.  # noqa: E501


        :return: The mime_type of this TestCaseExecutionAttachmentDto.  # noqa: E501
        :rtype: str
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        """Sets the mime_type of this TestCaseExecutionAttachmentDto.


        :param mime_type: The mime_type of this TestCaseExecutionAttachmentDto.  # noqa: E501
        :type: str
        """

        self._mime_type = mime_type

    @property
    def creation_time(self):
        """Gets the creation_time of this TestCaseExecutionAttachmentDto.  # noqa: E501


        :return: The creation_time of this TestCaseExecutionAttachmentDto.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this TestCaseExecutionAttachmentDto.


        :param creation_time: The creation_time of this TestCaseExecutionAttachmentDto.  # noqa: E501
        :type: datetime
        """

        self._creation_time = creation_time

    @property
    def tags(self):
        """Gets the tags of this TestCaseExecutionAttachmentDto.  # noqa: E501


        :return: The tags of this TestCaseExecutionAttachmentDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this TestCaseExecutionAttachmentDto.


        :param tags: The tags of this TestCaseExecutionAttachmentDto.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def id(self):
        """Gets the id of this TestCaseExecutionAttachmentDto.  # noqa: E501


        :return: The id of this TestCaseExecutionAttachmentDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TestCaseExecutionAttachmentDto.


        :param id: The id of this TestCaseExecutionAttachmentDto.  # noqa: E501
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
        if issubclass(TestCaseExecutionAttachmentDto, dict):
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
        if not isinstance(other, TestCaseExecutionAttachmentDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TestCaseExecutionAttachmentDto):
            return True

        return self.to_dict() != other.to_dict()
