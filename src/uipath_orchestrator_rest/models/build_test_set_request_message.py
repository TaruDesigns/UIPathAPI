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


class BuildTestSetRequestMessage(object):
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
        'release_id': 'int',
        'version_number': 'str',
        'test_case_unique_ids': 'list[str]',
        'enable_coverage': 'bool',
        'mask_build_version': 'bool'
    }

    attribute_map = {
        'release_id': 'releaseId',
        'version_number': 'versionNumber',
        'test_case_unique_ids': 'testCaseUniqueIds',
        'enable_coverage': 'enableCoverage',
        'mask_build_version': 'maskBuildVersion'
    }

    def __init__(self, release_id=None, version_number=None, test_case_unique_ids=None, enable_coverage=None, mask_build_version=None, _configuration=None):  # noqa: E501
        """BuildTestSetRequestMessage - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._release_id = None
        self._version_number = None
        self._test_case_unique_ids = None
        self._enable_coverage = None
        self._mask_build_version = None
        self.discriminator = None

        self.release_id = release_id
        self.version_number = version_number
        if test_case_unique_ids is not None:
            self.test_case_unique_ids = test_case_unique_ids
        if enable_coverage is not None:
            self.enable_coverage = enable_coverage
        if mask_build_version is not None:
            self.mask_build_version = mask_build_version

    @property
    def release_id(self):
        """Gets the release_id of this BuildTestSetRequestMessage.  # noqa: E501


        :return: The release_id of this BuildTestSetRequestMessage.  # noqa: E501
        :rtype: int
        """
        return self._release_id

    @release_id.setter
    def release_id(self, release_id):
        """Sets the release_id of this BuildTestSetRequestMessage.


        :param release_id: The release_id of this BuildTestSetRequestMessage.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and release_id is None:
            raise ValueError("Invalid value for `release_id`, must not be `None`")  # noqa: E501

        self._release_id = release_id

    @property
    def version_number(self):
        """Gets the version_number of this BuildTestSetRequestMessage.  # noqa: E501


        :return: The version_number of this BuildTestSetRequestMessage.  # noqa: E501
        :rtype: str
        """
        return self._version_number

    @version_number.setter
    def version_number(self, version_number):
        """Sets the version_number of this BuildTestSetRequestMessage.


        :param version_number: The version_number of this BuildTestSetRequestMessage.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and version_number is None:
            raise ValueError("Invalid value for `version_number`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                version_number is not None and len(version_number) < 1):
            raise ValueError("Invalid value for `version_number`, length must be greater than or equal to `1`")  # noqa: E501

        self._version_number = version_number

    @property
    def test_case_unique_ids(self):
        """Gets the test_case_unique_ids of this BuildTestSetRequestMessage.  # noqa: E501


        :return: The test_case_unique_ids of this BuildTestSetRequestMessage.  # noqa: E501
        :rtype: list[str]
        """
        return self._test_case_unique_ids

    @test_case_unique_ids.setter
    def test_case_unique_ids(self, test_case_unique_ids):
        """Sets the test_case_unique_ids of this BuildTestSetRequestMessage.


        :param test_case_unique_ids: The test_case_unique_ids of this BuildTestSetRequestMessage.  # noqa: E501
        :type: list[str]
        """

        self._test_case_unique_ids = test_case_unique_ids

    @property
    def enable_coverage(self):
        """Gets the enable_coverage of this BuildTestSetRequestMessage.  # noqa: E501


        :return: The enable_coverage of this BuildTestSetRequestMessage.  # noqa: E501
        :rtype: bool
        """
        return self._enable_coverage

    @enable_coverage.setter
    def enable_coverage(self, enable_coverage):
        """Sets the enable_coverage of this BuildTestSetRequestMessage.


        :param enable_coverage: The enable_coverage of this BuildTestSetRequestMessage.  # noqa: E501
        :type: bool
        """

        self._enable_coverage = enable_coverage

    @property
    def mask_build_version(self):
        """Gets the mask_build_version of this BuildTestSetRequestMessage.  # noqa: E501


        :return: The mask_build_version of this BuildTestSetRequestMessage.  # noqa: E501
        :rtype: bool
        """
        return self._mask_build_version

    @mask_build_version.setter
    def mask_build_version(self, mask_build_version):
        """Sets the mask_build_version of this BuildTestSetRequestMessage.


        :param mask_build_version: The mask_build_version of this BuildTestSetRequestMessage.  # noqa: E501
        :type: bool
        """

        self._mask_build_version = mask_build_version

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
        if issubclass(BuildTestSetRequestMessage, dict):
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
        if not isinstance(other, BuildTestSetRequestMessage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BuildTestSetRequestMessage):
            return True

        return self.to_dict() != other.to_dict()
