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


class TaskAssignmentRequest(object):
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
        'task_id': 'int',
        'user_id': 'int',
        'user_name_or_email': 'str'
    }

    attribute_map = {
        'task_id': 'TaskId',
        'user_id': 'UserId',
        'user_name_or_email': 'UserNameOrEmail'
    }

    def __init__(self, task_id=None, user_id=None, user_name_or_email=None, _configuration=None):  # noqa: E501
        """TaskAssignmentRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._task_id = None
        self._user_id = None
        self._user_name_or_email = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if user_id is not None:
            self.user_id = user_id
        if user_name_or_email is not None:
            self.user_name_or_email = user_name_or_email

    @property
    def task_id(self):
        """Gets the task_id of this TaskAssignmentRequest.  # noqa: E501

        Gets or sets the taskId for this task assignment.  # noqa: E501

        :return: The task_id of this TaskAssignmentRequest.  # noqa: E501
        :rtype: int
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this TaskAssignmentRequest.

        Gets or sets the taskId for this task assignment.  # noqa: E501

        :param task_id: The task_id of this TaskAssignmentRequest.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                task_id is not None and task_id < 1):  # noqa: E501
            raise ValueError("Invalid value for `task_id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._task_id = task_id

    @property
    def user_id(self):
        """Gets the user_id of this TaskAssignmentRequest.  # noqa: E501

        Gets or sets the userId for this task assignment.  # noqa: E501

        :return: The user_id of this TaskAssignmentRequest.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this TaskAssignmentRequest.

        Gets or sets the userId for this task assignment.  # noqa: E501

        :param user_id: The user_id of this TaskAssignmentRequest.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def user_name_or_email(self):
        """Gets the user_name_or_email of this TaskAssignmentRequest.  # noqa: E501

        Gets or sets the UserName or Email for this task assignment. If UserId is provided, this property is ignored.  # noqa: E501

        :return: The user_name_or_email of this TaskAssignmentRequest.  # noqa: E501
        :rtype: str
        """
        return self._user_name_or_email

    @user_name_or_email.setter
    def user_name_or_email(self, user_name_or_email):
        """Sets the user_name_or_email of this TaskAssignmentRequest.

        Gets or sets the UserName or Email for this task assignment. If UserId is provided, this property is ignored.  # noqa: E501

        :param user_name_or_email: The user_name_or_email of this TaskAssignmentRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                user_name_or_email is not None and len(user_name_or_email) > 256):
            raise ValueError("Invalid value for `user_name_or_email`, length must be less than or equal to `256`")  # noqa: E501

        self._user_name_or_email = user_name_or_email

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
        if issubclass(TaskAssignmentRequest, dict):
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
        if not isinstance(other, TaskAssignmentRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TaskAssignmentRequest):
            return True

        return self.to_dict() != other.to_dict()
