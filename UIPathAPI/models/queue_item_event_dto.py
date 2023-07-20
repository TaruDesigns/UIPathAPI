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


class QueueItemEventDto(object):
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
        'queue_item_id': 'int',
        'timestamp': 'datetime',
        'action': 'str',
        'data': 'str',
        'user_id': 'int',
        'user_name': 'str',
        'status': 'str',
        'review_status': 'str',
        'reviewer_user_id': 'int',
        'reviewer_user_name': 'str',
        'external_client_id': 'str',
        'id': 'int'
    }

    attribute_map = {
        'queue_item_id': 'QueueItemId',
        'timestamp': 'Timestamp',
        'action': 'Action',
        'data': 'Data',
        'user_id': 'UserId',
        'user_name': 'UserName',
        'status': 'Status',
        'review_status': 'ReviewStatus',
        'reviewer_user_id': 'ReviewerUserId',
        'reviewer_user_name': 'ReviewerUserName',
        'external_client_id': 'ExternalClientId',
        'id': 'Id'
    }

    def __init__(self, queue_item_id=None, timestamp=None, action=None, data=None, user_id=None, user_name=None, status=None, review_status=None, reviewer_user_id=None, reviewer_user_name=None, external_client_id=None, id=None, _configuration=None):  # noqa: E501
        """QueueItemEventDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._queue_item_id = None
        self._timestamp = None
        self._action = None
        self._data = None
        self._user_id = None
        self._user_name = None
        self._status = None
        self._review_status = None
        self._reviewer_user_id = None
        self._reviewer_user_name = None
        self._external_client_id = None
        self._id = None
        self.discriminator = None

        if queue_item_id is not None:
            self.queue_item_id = queue_item_id
        if timestamp is not None:
            self.timestamp = timestamp
        if action is not None:
            self.action = action
        if data is not None:
            self.data = data
        if user_id is not None:
            self.user_id = user_id
        if user_name is not None:
            self.user_name = user_name
        if status is not None:
            self.status = status
        if review_status is not None:
            self.review_status = review_status
        if reviewer_user_id is not None:
            self.reviewer_user_id = reviewer_user_id
        if reviewer_user_name is not None:
            self.reviewer_user_name = reviewer_user_name
        if external_client_id is not None:
            self.external_client_id = external_client_id
        if id is not None:
            self.id = id

    @property
    def queue_item_id(self):
        """Gets the queue_item_id of this QueueItemEventDto.  # noqa: E501

        The Id of a Queue Item that the current item is connected to.  # noqa: E501

        :return: The queue_item_id of this QueueItemEventDto.  # noqa: E501
        :rtype: int
        """
        return self._queue_item_id

    @queue_item_id.setter
    def queue_item_id(self, queue_item_id):
        """Sets the queue_item_id of this QueueItemEventDto.

        The Id of a Queue Item that the current item is connected to.  # noqa: E501

        :param queue_item_id: The queue_item_id of this QueueItemEventDto.  # noqa: E501
        :type: int
        """

        self._queue_item_id = queue_item_id

    @property
    def timestamp(self):
        """Gets the timestamp of this QueueItemEventDto.  # noqa: E501

        The Date and Time when the event occured.  # noqa: E501

        :return: The timestamp of this QueueItemEventDto.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this QueueItemEventDto.

        The Date and Time when the event occured.  # noqa: E501

        :param timestamp: The timestamp of this QueueItemEventDto.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def action(self):
        """Gets the action of this QueueItemEventDto.  # noqa: E501

        The Action that caused the event.  # noqa: E501

        :return: The action of this QueueItemEventDto.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this QueueItemEventDto.

        The Action that caused the event.  # noqa: E501

        :param action: The action of this QueueItemEventDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["Create", "Edit", "Delete", "Status", "Retry"]  # noqa: E501
        if (self._configuration.client_side_validation and
                action not in allowed_values):
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def data(self):
        """Gets the data of this QueueItemEventDto.  # noqa: E501

        The Data associated to the event.  # noqa: E501

        :return: The data of this QueueItemEventDto.  # noqa: E501
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this QueueItemEventDto.

        The Data associated to the event.  # noqa: E501

        :param data: The data of this QueueItemEventDto.  # noqa: E501
        :type: str
        """

        self._data = data

    @property
    def user_id(self):
        """Gets the user_id of this QueueItemEventDto.  # noqa: E501

        The Id of the User that caused the event.  # noqa: E501

        :return: The user_id of this QueueItemEventDto.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this QueueItemEventDto.

        The Id of the User that caused the event.  # noqa: E501

        :param user_id: The user_id of this QueueItemEventDto.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def user_name(self):
        """Gets the user_name of this QueueItemEventDto.  # noqa: E501

        The Name of the User that caused the event.  # noqa: E501

        :return: The user_name of this QueueItemEventDto.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this QueueItemEventDto.

        The Name of the User that caused the event.  # noqa: E501

        :param user_name: The user_name of this QueueItemEventDto.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def status(self):
        """Gets the status of this QueueItemEventDto.  # noqa: E501

        Processing Status when event snapshot was taken.  # noqa: E501

        :return: The status of this QueueItemEventDto.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this QueueItemEventDto.

        Processing Status when event snapshot was taken.  # noqa: E501

        :param status: The status of this QueueItemEventDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["New", "InProgress", "Failed", "Successful", "Abandoned", "Retried", "Deleted"]  # noqa: E501
        if (self._configuration.client_side_validation and
                status not in allowed_values):
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def review_status(self):
        """Gets the review_status of this QueueItemEventDto.  # noqa: E501

        Review Status when event snapshot was taken.  # noqa: E501

        :return: The review_status of this QueueItemEventDto.  # noqa: E501
        :rtype: str
        """
        return self._review_status

    @review_status.setter
    def review_status(self, review_status):
        """Sets the review_status of this QueueItemEventDto.

        Review Status when event snapshot was taken.  # noqa: E501

        :param review_status: The review_status of this QueueItemEventDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "InReview", "Verified", "Retried"]  # noqa: E501
        if (self._configuration.client_side_validation and
                review_status not in allowed_values):
            raise ValueError(
                "Invalid value for `review_status` ({0}), must be one of {1}"  # noqa: E501
                .format(review_status, allowed_values)
            )

        self._review_status = review_status

    @property
    def reviewer_user_id(self):
        """Gets the reviewer_user_id of this QueueItemEventDto.  # noqa: E501

        Reviewer User Id when event snapshot was taken.  # noqa: E501

        :return: The reviewer_user_id of this QueueItemEventDto.  # noqa: E501
        :rtype: int
        """
        return self._reviewer_user_id

    @reviewer_user_id.setter
    def reviewer_user_id(self, reviewer_user_id):
        """Sets the reviewer_user_id of this QueueItemEventDto.

        Reviewer User Id when event snapshot was taken.  # noqa: E501

        :param reviewer_user_id: The reviewer_user_id of this QueueItemEventDto.  # noqa: E501
        :type: int
        """

        self._reviewer_user_id = reviewer_user_id

    @property
    def reviewer_user_name(self):
        """Gets the reviewer_user_name of this QueueItemEventDto.  # noqa: E501

        Reviewer User Name when event snapshot was taken.  # noqa: E501

        :return: The reviewer_user_name of this QueueItemEventDto.  # noqa: E501
        :rtype: str
        """
        return self._reviewer_user_name

    @reviewer_user_name.setter
    def reviewer_user_name(self, reviewer_user_name):
        """Sets the reviewer_user_name of this QueueItemEventDto.

        Reviewer User Name when event snapshot was taken.  # noqa: E501

        :param reviewer_user_name: The reviewer_user_name of this QueueItemEventDto.  # noqa: E501
        :type: str
        """

        self._reviewer_user_name = reviewer_user_name

    @property
    def external_client_id(self):
        """Gets the external_client_id of this QueueItemEventDto.  # noqa: E501

        The External client identifier that caused the event. Example: OAuth 3rd party app identifier that called Orchestrator.  # noqa: E501

        :return: The external_client_id of this QueueItemEventDto.  # noqa: E501
        :rtype: str
        """
        return self._external_client_id

    @external_client_id.setter
    def external_client_id(self, external_client_id):
        """Sets the external_client_id of this QueueItemEventDto.

        The External client identifier that caused the event. Example: OAuth 3rd party app identifier that called Orchestrator.  # noqa: E501

        :param external_client_id: The external_client_id of this QueueItemEventDto.  # noqa: E501
        :type: str
        """

        self._external_client_id = external_client_id

    @property
    def id(self):
        """Gets the id of this QueueItemEventDto.  # noqa: E501


        :return: The id of this QueueItemEventDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this QueueItemEventDto.


        :param id: The id of this QueueItemEventDto.  # noqa: E501
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
        if issubclass(QueueItemEventDto, dict):
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
        if not isinstance(other, QueueItemEventDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QueueItemEventDto):
            return True

        return self.to_dict() != other.to_dict()
