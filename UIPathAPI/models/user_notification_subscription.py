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


class UserNotificationSubscription(object):
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
        'queues': 'bool',
        'robots': 'bool',
        'jobs': 'bool',
        'schedules': 'bool',
        'tasks': 'bool',
        'queue_items': 'bool',
        'insights': 'bool',
        'cloud_robots': 'bool',
        'serverless': 'bool',
        'export': 'bool'
    }

    attribute_map = {
        'queues': 'Queues',
        'robots': 'Robots',
        'jobs': 'Jobs',
        'schedules': 'Schedules',
        'tasks': 'Tasks',
        'queue_items': 'QueueItems',
        'insights': 'Insights',
        'cloud_robots': 'CloudRobots',
        'serverless': 'Serverless',
        'export': 'Export'
    }

    def __init__(self, queues=None, robots=None, jobs=None, schedules=None, tasks=None, queue_items=None, insights=None, cloud_robots=None, serverless=None, export=None, _configuration=None):  # noqa: E501
        """UserNotificationSubscription - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._queues = None
        self._robots = None
        self._jobs = None
        self._schedules = None
        self._tasks = None
        self._queue_items = None
        self._insights = None
        self._cloud_robots = None
        self._serverless = None
        self._export = None
        self.discriminator = None

        if queues is not None:
            self.queues = queues
        if robots is not None:
            self.robots = robots
        if jobs is not None:
            self.jobs = jobs
        if schedules is not None:
            self.schedules = schedules
        if tasks is not None:
            self.tasks = tasks
        if queue_items is not None:
            self.queue_items = queue_items
        if insights is not None:
            self.insights = insights
        if cloud_robots is not None:
            self.cloud_robots = cloud_robots
        if serverless is not None:
            self.serverless = serverless
        if export is not None:
            self.export = export

    @property
    def queues(self):
        """Gets the queues of this UserNotificationSubscription.  # noqa: E501


        :return: The queues of this UserNotificationSubscription.  # noqa: E501
        :rtype: bool
        """
        return self._queues

    @queues.setter
    def queues(self, queues):
        """Sets the queues of this UserNotificationSubscription.


        :param queues: The queues of this UserNotificationSubscription.  # noqa: E501
        :type: bool
        """

        self._queues = queues

    @property
    def robots(self):
        """Gets the robots of this UserNotificationSubscription.  # noqa: E501


        :return: The robots of this UserNotificationSubscription.  # noqa: E501
        :rtype: bool
        """
        return self._robots

    @robots.setter
    def robots(self, robots):
        """Sets the robots of this UserNotificationSubscription.


        :param robots: The robots of this UserNotificationSubscription.  # noqa: E501
        :type: bool
        """

        self._robots = robots

    @property
    def jobs(self):
        """Gets the jobs of this UserNotificationSubscription.  # noqa: E501


        :return: The jobs of this UserNotificationSubscription.  # noqa: E501
        :rtype: bool
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        """Sets the jobs of this UserNotificationSubscription.


        :param jobs: The jobs of this UserNotificationSubscription.  # noqa: E501
        :type: bool
        """

        self._jobs = jobs

    @property
    def schedules(self):
        """Gets the schedules of this UserNotificationSubscription.  # noqa: E501


        :return: The schedules of this UserNotificationSubscription.  # noqa: E501
        :rtype: bool
        """
        return self._schedules

    @schedules.setter
    def schedules(self, schedules):
        """Sets the schedules of this UserNotificationSubscription.


        :param schedules: The schedules of this UserNotificationSubscription.  # noqa: E501
        :type: bool
        """

        self._schedules = schedules

    @property
    def tasks(self):
        """Gets the tasks of this UserNotificationSubscription.  # noqa: E501


        :return: The tasks of this UserNotificationSubscription.  # noqa: E501
        :rtype: bool
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """Sets the tasks of this UserNotificationSubscription.


        :param tasks: The tasks of this UserNotificationSubscription.  # noqa: E501
        :type: bool
        """

        self._tasks = tasks

    @property
    def queue_items(self):
        """Gets the queue_items of this UserNotificationSubscription.  # noqa: E501


        :return: The queue_items of this UserNotificationSubscription.  # noqa: E501
        :rtype: bool
        """
        return self._queue_items

    @queue_items.setter
    def queue_items(self, queue_items):
        """Sets the queue_items of this UserNotificationSubscription.


        :param queue_items: The queue_items of this UserNotificationSubscription.  # noqa: E501
        :type: bool
        """

        self._queue_items = queue_items

    @property
    def insights(self):
        """Gets the insights of this UserNotificationSubscription.  # noqa: E501


        :return: The insights of this UserNotificationSubscription.  # noqa: E501
        :rtype: bool
        """
        return self._insights

    @insights.setter
    def insights(self, insights):
        """Sets the insights of this UserNotificationSubscription.


        :param insights: The insights of this UserNotificationSubscription.  # noqa: E501
        :type: bool
        """

        self._insights = insights

    @property
    def cloud_robots(self):
        """Gets the cloud_robots of this UserNotificationSubscription.  # noqa: E501


        :return: The cloud_robots of this UserNotificationSubscription.  # noqa: E501
        :rtype: bool
        """
        return self._cloud_robots

    @cloud_robots.setter
    def cloud_robots(self, cloud_robots):
        """Sets the cloud_robots of this UserNotificationSubscription.


        :param cloud_robots: The cloud_robots of this UserNotificationSubscription.  # noqa: E501
        :type: bool
        """

        self._cloud_robots = cloud_robots

    @property
    def serverless(self):
        """Gets the serverless of this UserNotificationSubscription.  # noqa: E501


        :return: The serverless of this UserNotificationSubscription.  # noqa: E501
        :rtype: bool
        """
        return self._serverless

    @serverless.setter
    def serverless(self, serverless):
        """Sets the serverless of this UserNotificationSubscription.


        :param serverless: The serverless of this UserNotificationSubscription.  # noqa: E501
        :type: bool
        """

        self._serverless = serverless

    @property
    def export(self):
        """Gets the export of this UserNotificationSubscription.  # noqa: E501


        :return: The export of this UserNotificationSubscription.  # noqa: E501
        :rtype: bool
        """
        return self._export

    @export.setter
    def export(self, export):
        """Sets the export of this UserNotificationSubscription.


        :param export: The export of this UserNotificationSubscription.  # noqa: E501
        :type: bool
        """

        self._export = export

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
        if issubclass(UserNotificationSubscription, dict):
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
        if not isinstance(other, UserNotificationSubscription):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserNotificationSubscription):
            return True

        return self.to_dict() != other.to_dict()
