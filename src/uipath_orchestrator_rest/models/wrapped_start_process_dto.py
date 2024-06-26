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


class WrappedStartProcessDto(object):
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
        'release_key': 'str',
        'strategy': 'str',
        'robot_ids': 'list[int]',
        'jobs_count': 'int',
        'source': 'str'
    }

    attribute_map = {
        'release_key': 'ReleaseKey',
        'strategy': 'Strategy',
        'robot_ids': 'RobotIds',
        'jobs_count': 'JobsCount',
        'source': 'Source'
    }

    def __init__(self, release_key=None, strategy=None, robot_ids=None, jobs_count=None, source=None, _configuration=None):  # noqa: E501
        """WrappedStartProcessDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._release_key = None
        self._strategy = None
        self._robot_ids = None
        self._jobs_count = None
        self._source = None
        self.discriminator = None

        if release_key is not None:
            self.release_key = release_key
        if strategy is not None:
            self.strategy = strategy
        if robot_ids is not None:
            self.robot_ids = robot_ids
        if jobs_count is not None:
            self.jobs_count = jobs_count
        if source is not None:
            self.source = source

    @property
    def release_key(self):
        """Gets the release_key of this WrappedStartProcessDto.  # noqa: E501

        The unique key of the release associated with the process.  # noqa: E501

        :return: The release_key of this WrappedStartProcessDto.  # noqa: E501
        :rtype: str
        """
        return self._release_key

    @release_key.setter
    def release_key(self, release_key):
        """Sets the release_key of this WrappedStartProcessDto.

        The unique key of the release associated with the process.  # noqa: E501

        :param release_key: The release_key of this WrappedStartProcessDto.  # noqa: E501
        :type: str
        """

        self._release_key = release_key

    @property
    def strategy(self):
        """Gets the strategy of this WrappedStartProcessDto.  # noqa: E501

        States which robots from the environment are being run by the process.  # noqa: E501

        :return: The strategy of this WrappedStartProcessDto.  # noqa: E501
        :rtype: str
        """
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        """Sets the strategy of this WrappedStartProcessDto.

        States which robots from the environment are being run by the process.  # noqa: E501

        :param strategy: The strategy of this WrappedStartProcessDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["All", "Specific", "RobotCount", "JobsCount", "ModernJobsCount"]  # noqa: E501
        if (self._configuration.client_side_validation and
                strategy not in allowed_values):
            raise ValueError(
                "Invalid value for `strategy` ({0}), must be one of {1}"  # noqa: E501
                .format(strategy, allowed_values)
            )

        self._strategy = strategy

    @property
    def robot_ids(self):
        """Gets the robot_ids of this WrappedStartProcessDto.  # noqa: E501

        The collection of ids of specific robots selected to be run by the current process. This collection must be empty only if the start strategy is not Specific.  # noqa: E501

        :return: The robot_ids of this WrappedStartProcessDto.  # noqa: E501
        :rtype: list[int]
        """
        return self._robot_ids

    @robot_ids.setter
    def robot_ids(self, robot_ids):
        """Sets the robot_ids of this WrappedStartProcessDto.

        The collection of ids of specific robots selected to be run by the current process. This collection must be empty only if the start strategy is not Specific.  # noqa: E501

        :param robot_ids: The robot_ids of this WrappedStartProcessDto.  # noqa: E501
        :type: list[int]
        """

        self._robot_ids = robot_ids

    @property
    def jobs_count(self):
        """Gets the jobs_count of this WrappedStartProcessDto.  # noqa: E501

        Number of pending jobs to be created in the environment, for the current process. This number must be greater than 0 only if the start strategy is JobsCount.  # noqa: E501

        :return: The jobs_count of this WrappedStartProcessDto.  # noqa: E501
        :rtype: int
        """
        return self._jobs_count

    @jobs_count.setter
    def jobs_count(self, jobs_count):
        """Sets the jobs_count of this WrappedStartProcessDto.

        Number of pending jobs to be created in the environment, for the current process. This number must be greater than 0 only if the start strategy is JobsCount.  # noqa: E501

        :param jobs_count: The jobs_count of this WrappedStartProcessDto.  # noqa: E501
        :type: int
        """

        self._jobs_count = jobs_count

    @property
    def source(self):
        """Gets the source of this WrappedStartProcessDto.  # noqa: E501

        The Source of the job starting the current process.  # noqa: E501

        :return: The source of this WrappedStartProcessDto.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this WrappedStartProcessDto.

        The Source of the job starting the current process.  # noqa: E501

        :param source: The source of this WrappedStartProcessDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["Manual", "Schedule", "Queue", "StudioWeb", "IntegrationTrigger", "StudioDesktop", "AutomationOpsPipelines", "Apps", "SAP", "HttpTrigger", "HttpTriggerWithCallback", "RobotAPI", "Assistant", "CommandLine", "RobotNetAPI"]  # noqa: E501
        if (self._configuration.client_side_validation and
                source not in allowed_values):
            raise ValueError(
                "Invalid value for `source` ({0}), must be one of {1}"  # noqa: E501
                .format(source, allowed_values)
            )

        self._source = source

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
        if issubclass(WrappedStartProcessDto, dict):
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
        if not isinstance(other, WrappedStartProcessDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WrappedStartProcessDto):
            return True

        return self.to_dict() != other.to_dict()
