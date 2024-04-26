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


class UpdateInfoDto(object):
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
        'update_status': 'str',
        'reason': 'str',
        'target_update_version': 'str',
        'is_community': 'bool',
        'status_info': 'str'
    }

    attribute_map = {
        'update_status': 'updateStatus',
        'reason': 'reason',
        'target_update_version': 'targetUpdateVersion',
        'is_community': 'isCommunity',
        'status_info': 'statusInfo'
    }

    def __init__(self, update_status=None, reason=None, target_update_version=None, is_community=None, status_info=None, _configuration=None):  # noqa: E501
        """UpdateInfoDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._update_status = None
        self._reason = None
        self._target_update_version = None
        self._is_community = None
        self._status_info = None
        self.discriminator = None

        if update_status is not None:
            self.update_status = update_status
        if reason is not None:
            self.reason = reason
        if target_update_version is not None:
            self.target_update_version = target_update_version
        if is_community is not None:
            self.is_community = is_community
        if status_info is not None:
            self.status_info = status_info

    @property
    def update_status(self):
        """Gets the update_status of this UpdateInfoDto.  # noqa: E501


        :return: The update_status of this UpdateInfoDto.  # noqa: E501
        :rtype: str
        """
        return self._update_status

    @update_status.setter
    def update_status(self, update_status):
        """Sets the update_status of this UpdateInfoDto.


        :param update_status: The update_status of this UpdateInfoDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "InProgress", "Failed", "NonCompliant", "Compliant", "NotApplicable", "Scheduled", "FailedRescheduled"]  # noqa: E501
        if (self._configuration.client_side_validation and
                update_status not in allowed_values):
            raise ValueError(
                "Invalid value for `update_status` ({0}), must be one of {1}"  # noqa: E501
                .format(update_status, allowed_values)
            )

        self._update_status = update_status

    @property
    def reason(self):
        """Gets the reason of this UpdateInfoDto.  # noqa: E501


        :return: The reason of this UpdateInfoDto.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this UpdateInfoDto.


        :param reason: The reason of this UpdateInfoDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["NonCompliantWithDifferentVersion", "NonCompliantWithoutTargetVersion", "NotApplicableForOlderSessions", "NotApplicableForMachineType", "NotApplicableTemplateWithoutRobotSessions", "NotApplicableForPlatform", "NotApplicableForTargetFramework"]  # noqa: E501
        if (self._configuration.client_side_validation and
                reason not in allowed_values):
            raise ValueError(
                "Invalid value for `reason` ({0}), must be one of {1}"  # noqa: E501
                .format(reason, allowed_values)
            )

        self._reason = reason

    @property
    def target_update_version(self):
        """Gets the target_update_version of this UpdateInfoDto.  # noqa: E501


        :return: The target_update_version of this UpdateInfoDto.  # noqa: E501
        :rtype: str
        """
        return self._target_update_version

    @target_update_version.setter
    def target_update_version(self, target_update_version):
        """Sets the target_update_version of this UpdateInfoDto.


        :param target_update_version: The target_update_version of this UpdateInfoDto.  # noqa: E501
        :type: str
        """

        self._target_update_version = target_update_version

    @property
    def is_community(self):
        """Gets the is_community of this UpdateInfoDto.  # noqa: E501


        :return: The is_community of this UpdateInfoDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_community

    @is_community.setter
    def is_community(self, is_community):
        """Sets the is_community of this UpdateInfoDto.


        :param is_community: The is_community of this UpdateInfoDto.  # noqa: E501
        :type: bool
        """

        self._is_community = is_community

    @property
    def status_info(self):
        """Gets the status_info of this UpdateInfoDto.  # noqa: E501


        :return: The status_info of this UpdateInfoDto.  # noqa: E501
        :rtype: str
        """
        return self._status_info

    @status_info.setter
    def status_info(self, status_info):
        """Sets the status_info of this UpdateInfoDto.


        :param status_info: The status_info of this UpdateInfoDto.  # noqa: E501
        :type: str
        """

        self._status_info = status_info

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
        if issubclass(UpdateInfoDto, dict):
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
        if not isinstance(other, UpdateInfoDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateInfoDto):
            return True

        return self.to_dict() != other.to_dict()