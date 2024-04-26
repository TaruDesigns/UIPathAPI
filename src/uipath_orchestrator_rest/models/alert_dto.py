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


class AlertDto(object):
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
        'notification_name': 'str',
        'data': 'str',
        'component': 'str',
        'severity': 'str',
        'creation_time': 'datetime',
        'state': 'str',
        'user_notification_id': 'str',
        'deep_link_relative_url': 'str',
        'id': 'str'
    }

    attribute_map = {
        'notification_name': 'NotificationName',
        'data': 'Data',
        'component': 'Component',
        'severity': 'Severity',
        'creation_time': 'CreationTime',
        'state': 'State',
        'user_notification_id': 'UserNotificationId',
        'deep_link_relative_url': 'DeepLinkRelativeUrl',
        'id': 'Id'
    }

    def __init__(self, notification_name=None, data=None, component=None, severity=None, creation_time=None, state=None, user_notification_id=None, deep_link_relative_url=None, id=None, _configuration=None):  # noqa: E501
        """AlertDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._notification_name = None
        self._data = None
        self._component = None
        self._severity = None
        self._creation_time = None
        self._state = None
        self._user_notification_id = None
        self._deep_link_relative_url = None
        self._id = None
        self.discriminator = None

        if notification_name is not None:
            self.notification_name = notification_name
        if data is not None:
            self.data = data
        if component is not None:
            self.component = component
        self.severity = severity
        if creation_time is not None:
            self.creation_time = creation_time
        if state is not None:
            self.state = state
        if user_notification_id is not None:
            self.user_notification_id = user_notification_id
        if deep_link_relative_url is not None:
            self.deep_link_relative_url = deep_link_relative_url
        if id is not None:
            self.id = id

    @property
    def notification_name(self):
        """Gets the notification_name of this AlertDto.  # noqa: E501

        The name of a specific type of notification, e.g. Robot.StatusChanged.NotResponding.  # noqa: E501

        :return: The notification_name of this AlertDto.  # noqa: E501
        :rtype: str
        """
        return self._notification_name

    @notification_name.setter
    def notification_name(self, notification_name):
        """Sets the notification_name of this AlertDto.

        The name of a specific type of notification, e.g. Robot.StatusChanged.NotResponding.  # noqa: E501

        :param notification_name: The notification_name of this AlertDto.  # noqa: E501
        :type: str
        """

        self._notification_name = notification_name

    @property
    def data(self):
        """Gets the data of this AlertDto.  # noqa: E501

        Stores data about the context in which the event occurred, in JSON format.  # noqa: E501

        :return: The data of this AlertDto.  # noqa: E501
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this AlertDto.

        Stores data about the context in which the event occurred, in JSON format.  # noqa: E501

        :param data: The data of this AlertDto.  # noqa: E501
        :type: str
        """

        self._data = data

    @property
    def component(self):
        """Gets the component of this AlertDto.  # noqa: E501

        The component that raised the alert.  # noqa: E501

        :return: The component of this AlertDto.  # noqa: E501
        :rtype: str
        """
        return self._component

    @component.setter
    def component(self, component):
        """Sets the component of this AlertDto.

        The component that raised the alert.  # noqa: E501

        :param component: The component of this AlertDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["Robots", "Transactions", "Schedules", "Jobs", "Process", "Tasks", "Queues", "Folders", "PersonalWorkspaces", "TestAutomation", "Insights", "CloudRobots", "ConnectedTriggers", "Serverless", "Export"]  # noqa: E501
        if (self._configuration.client_side_validation and
                component not in allowed_values):
            raise ValueError(
                "Invalid value for `component` ({0}), must be one of {1}"  # noqa: E501
                .format(component, allowed_values)
            )

        self._component = component

    @property
    def severity(self):
        """Gets the severity of this AlertDto.  # noqa: E501

        The severity level of the alert.  # noqa: E501

        :return: The severity of this AlertDto.  # noqa: E501
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this AlertDto.

        The severity level of the alert.  # noqa: E501

        :param severity: The severity of this AlertDto.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and severity is None:
            raise ValueError("Invalid value for `severity`, must not be `None`")  # noqa: E501
        allowed_values = ["Info", "Success", "Warn", "Error", "Fatal"]  # noqa: E501
        if (self._configuration.client_side_validation and
                severity not in allowed_values):
            raise ValueError(
                "Invalid value for `severity` ({0}), must be one of {1}"  # noqa: E501
                .format(severity, allowed_values)
            )

        self._severity = severity

    @property
    def creation_time(self):
        """Gets the creation_time of this AlertDto.  # noqa: E501

        The date and time when the alert was generated.  # noqa: E501

        :return: The creation_time of this AlertDto.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this AlertDto.

        The date and time when the alert was generated.  # noqa: E501

        :param creation_time: The creation_time of this AlertDto.  # noqa: E501
        :type: datetime
        """

        self._creation_time = creation_time

    @property
    def state(self):
        """Gets the state of this AlertDto.  # noqa: E501

        Defines if a specified notification has been read or not.  <para />Members: Unread (0) - the specified notification has not been marked as read; Read (1) - the specified notification has been marked as read.  # noqa: E501

        :return: The state of this AlertDto.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this AlertDto.

        Defines if a specified notification has been read or not.  <para />Members: Unread (0) - the specified notification has not been marked as read; Read (1) - the specified notification has been marked as read.  # noqa: E501

        :param state: The state of this AlertDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["Unread", "Read"]  # noqa: E501
        if (self._configuration.client_side_validation and
                state not in allowed_values):
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def user_notification_id(self):
        """Gets the user_notification_id of this AlertDto.  # noqa: E501

        The database unique identifier for the alert notification sent to the current user.  # noqa: E501

        :return: The user_notification_id of this AlertDto.  # noqa: E501
        :rtype: str
        """
        return self._user_notification_id

    @user_notification_id.setter
    def user_notification_id(self, user_notification_id):
        """Sets the user_notification_id of this AlertDto.

        The database unique identifier for the alert notification sent to the current user.  # noqa: E501

        :param user_notification_id: The user_notification_id of this AlertDto.  # noqa: E501
        :type: str
        """

        self._user_notification_id = user_notification_id

    @property
    def deep_link_relative_url(self):
        """Gets the deep_link_relative_url of this AlertDto.  # noqa: E501

        Relative deep link for front-end usage.  e.g /alerts/deeplink/{alert_title}?{alert_param1}={alert_param1_value}&{alert_param2}={alert_param2_value}  # noqa: E501

        :return: The deep_link_relative_url of this AlertDto.  # noqa: E501
        :rtype: str
        """
        return self._deep_link_relative_url

    @deep_link_relative_url.setter
    def deep_link_relative_url(self, deep_link_relative_url):
        """Sets the deep_link_relative_url of this AlertDto.

        Relative deep link for front-end usage.  e.g /alerts/deeplink/{alert_title}?{alert_param1}={alert_param1_value}&{alert_param2}={alert_param2_value}  # noqa: E501

        :param deep_link_relative_url: The deep_link_relative_url of this AlertDto.  # noqa: E501
        :type: str
        """

        self._deep_link_relative_url = deep_link_relative_url

    @property
    def id(self):
        """Gets the id of this AlertDto.  # noqa: E501


        :return: The id of this AlertDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AlertDto.


        :param id: The id of this AlertDto.  # noqa: E501
        :type: str
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
        if issubclass(AlertDto, dict):
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
        if not isinstance(other, AlertDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AlertDto):
            return True

        return self.to_dict() != other.to_dict()