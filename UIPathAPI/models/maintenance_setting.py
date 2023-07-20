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


class MaintenanceSetting(object):
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
        'state': 'str',
        'maintenance_logs': 'list[MaintenanceStateLog]',
        'job_stops_attempted': 'int',
        'job_kills_attempted': 'int',
        'triggers_skipped': 'int',
        'system_triggers_skipped': 'int'
    }

    attribute_map = {
        'state': 'state',
        'maintenance_logs': 'maintenanceLogs',
        'job_stops_attempted': 'jobStopsAttempted',
        'job_kills_attempted': 'jobKillsAttempted',
        'triggers_skipped': 'triggersSkipped',
        'system_triggers_skipped': 'systemTriggersSkipped'
    }

    def __init__(self, state=None, maintenance_logs=None, job_stops_attempted=None, job_kills_attempted=None, triggers_skipped=None, system_triggers_skipped=None, _configuration=None):  # noqa: E501
        """MaintenanceSetting - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._state = None
        self._maintenance_logs = None
        self._job_stops_attempted = None
        self._job_kills_attempted = None
        self._triggers_skipped = None
        self._system_triggers_skipped = None
        self.discriminator = None

        if state is not None:
            self.state = state
        if maintenance_logs is not None:
            self.maintenance_logs = maintenance_logs
        if job_stops_attempted is not None:
            self.job_stops_attempted = job_stops_attempted
        if job_kills_attempted is not None:
            self.job_kills_attempted = job_kills_attempted
        if triggers_skipped is not None:
            self.triggers_skipped = triggers_skipped
        if system_triggers_skipped is not None:
            self.system_triggers_skipped = system_triggers_skipped

    @property
    def state(self):
        """Gets the state of this MaintenanceSetting.  # noqa: E501


        :return: The state of this MaintenanceSetting.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this MaintenanceSetting.


        :param state: The state of this MaintenanceSetting.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "Draining", "Suspended"]  # noqa: E501
        if (self._configuration.client_side_validation and
                state not in allowed_values):
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def maintenance_logs(self):
        """Gets the maintenance_logs of this MaintenanceSetting.  # noqa: E501


        :return: The maintenance_logs of this MaintenanceSetting.  # noqa: E501
        :rtype: list[MaintenanceStateLog]
        """
        return self._maintenance_logs

    @maintenance_logs.setter
    def maintenance_logs(self, maintenance_logs):
        """Sets the maintenance_logs of this MaintenanceSetting.


        :param maintenance_logs: The maintenance_logs of this MaintenanceSetting.  # noqa: E501
        :type: list[MaintenanceStateLog]
        """

        self._maintenance_logs = maintenance_logs

    @property
    def job_stops_attempted(self):
        """Gets the job_stops_attempted of this MaintenanceSetting.  # noqa: E501


        :return: The job_stops_attempted of this MaintenanceSetting.  # noqa: E501
        :rtype: int
        """
        return self._job_stops_attempted

    @job_stops_attempted.setter
    def job_stops_attempted(self, job_stops_attempted):
        """Sets the job_stops_attempted of this MaintenanceSetting.


        :param job_stops_attempted: The job_stops_attempted of this MaintenanceSetting.  # noqa: E501
        :type: int
        """

        self._job_stops_attempted = job_stops_attempted

    @property
    def job_kills_attempted(self):
        """Gets the job_kills_attempted of this MaintenanceSetting.  # noqa: E501


        :return: The job_kills_attempted of this MaintenanceSetting.  # noqa: E501
        :rtype: int
        """
        return self._job_kills_attempted

    @job_kills_attempted.setter
    def job_kills_attempted(self, job_kills_attempted):
        """Sets the job_kills_attempted of this MaintenanceSetting.


        :param job_kills_attempted: The job_kills_attempted of this MaintenanceSetting.  # noqa: E501
        :type: int
        """

        self._job_kills_attempted = job_kills_attempted

    @property
    def triggers_skipped(self):
        """Gets the triggers_skipped of this MaintenanceSetting.  # noqa: E501


        :return: The triggers_skipped of this MaintenanceSetting.  # noqa: E501
        :rtype: int
        """
        return self._triggers_skipped

    @triggers_skipped.setter
    def triggers_skipped(self, triggers_skipped):
        """Sets the triggers_skipped of this MaintenanceSetting.


        :param triggers_skipped: The triggers_skipped of this MaintenanceSetting.  # noqa: E501
        :type: int
        """

        self._triggers_skipped = triggers_skipped

    @property
    def system_triggers_skipped(self):
        """Gets the system_triggers_skipped of this MaintenanceSetting.  # noqa: E501


        :return: The system_triggers_skipped of this MaintenanceSetting.  # noqa: E501
        :rtype: int
        """
        return self._system_triggers_skipped

    @system_triggers_skipped.setter
    def system_triggers_skipped(self, system_triggers_skipped):
        """Sets the system_triggers_skipped of this MaintenanceSetting.


        :param system_triggers_skipped: The system_triggers_skipped of this MaintenanceSetting.  # noqa: E501
        :type: int
        """

        self._system_triggers_skipped = system_triggers_skipped

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
        if issubclass(MaintenanceSetting, dict):
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
        if not isinstance(other, MaintenanceSetting):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MaintenanceSetting):
            return True

        return self.to_dict() != other.to_dict()
