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


class SessionEventData(object):
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
        'session_id': 'int',
        'robot_id': 'int',
        'machine_id': 'int',
        'machine_key': 'str',
        'host_machine_name': 'str',
        'service_username': 'str',
        'state': 'str',
        'reporting_time': 'datetime',
        'is_unresponsive': 'bool',
        'license_error_code': 'str'
    }

    attribute_map = {
        'session_id': 'SessionId',
        'robot_id': 'RobotId',
        'machine_id': 'MachineId',
        'machine_key': 'MachineKey',
        'host_machine_name': 'HostMachineName',
        'service_username': 'ServiceUsername',
        'state': 'State',
        'reporting_time': 'ReportingTime',
        'is_unresponsive': 'IsUnresponsive',
        'license_error_code': 'LicenseErrorCode'
    }

    def __init__(self, session_id=None, robot_id=None, machine_id=None, machine_key=None, host_machine_name=None, service_username=None, state=None, reporting_time=None, is_unresponsive=None, license_error_code=None, _configuration=None):  # noqa: E501
        """SessionEventData - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._session_id = None
        self._robot_id = None
        self._machine_id = None
        self._machine_key = None
        self._host_machine_name = None
        self._service_username = None
        self._state = None
        self._reporting_time = None
        self._is_unresponsive = None
        self._license_error_code = None
        self.discriminator = None

        if session_id is not None:
            self.session_id = session_id
        if robot_id is not None:
            self.robot_id = robot_id
        if machine_id is not None:
            self.machine_id = machine_id
        if machine_key is not None:
            self.machine_key = machine_key
        if host_machine_name is not None:
            self.host_machine_name = host_machine_name
        if service_username is not None:
            self.service_username = service_username
        if state is not None:
            self.state = state
        if reporting_time is not None:
            self.reporting_time = reporting_time
        if is_unresponsive is not None:
            self.is_unresponsive = is_unresponsive
        if license_error_code is not None:
            self.license_error_code = license_error_code

    @property
    def session_id(self):
        """Gets the session_id of this SessionEventData.  # noqa: E501


        :return: The session_id of this SessionEventData.  # noqa: E501
        :rtype: int
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this SessionEventData.


        :param session_id: The session_id of this SessionEventData.  # noqa: E501
        :type: int
        """

        self._session_id = session_id

    @property
    def robot_id(self):
        """Gets the robot_id of this SessionEventData.  # noqa: E501


        :return: The robot_id of this SessionEventData.  # noqa: E501
        :rtype: int
        """
        return self._robot_id

    @robot_id.setter
    def robot_id(self, robot_id):
        """Sets the robot_id of this SessionEventData.


        :param robot_id: The robot_id of this SessionEventData.  # noqa: E501
        :type: int
        """

        self._robot_id = robot_id

    @property
    def machine_id(self):
        """Gets the machine_id of this SessionEventData.  # noqa: E501


        :return: The machine_id of this SessionEventData.  # noqa: E501
        :rtype: int
        """
        return self._machine_id

    @machine_id.setter
    def machine_id(self, machine_id):
        """Sets the machine_id of this SessionEventData.


        :param machine_id: The machine_id of this SessionEventData.  # noqa: E501
        :type: int
        """

        self._machine_id = machine_id

    @property
    def machine_key(self):
        """Gets the machine_key of this SessionEventData.  # noqa: E501


        :return: The machine_key of this SessionEventData.  # noqa: E501
        :rtype: str
        """
        return self._machine_key

    @machine_key.setter
    def machine_key(self, machine_key):
        """Sets the machine_key of this SessionEventData.


        :param machine_key: The machine_key of this SessionEventData.  # noqa: E501
        :type: str
        """

        self._machine_key = machine_key

    @property
    def host_machine_name(self):
        """Gets the host_machine_name of this SessionEventData.  # noqa: E501


        :return: The host_machine_name of this SessionEventData.  # noqa: E501
        :rtype: str
        """
        return self._host_machine_name

    @host_machine_name.setter
    def host_machine_name(self, host_machine_name):
        """Sets the host_machine_name of this SessionEventData.


        :param host_machine_name: The host_machine_name of this SessionEventData.  # noqa: E501
        :type: str
        """

        self._host_machine_name = host_machine_name

    @property
    def service_username(self):
        """Gets the service_username of this SessionEventData.  # noqa: E501


        :return: The service_username of this SessionEventData.  # noqa: E501
        :rtype: str
        """
        return self._service_username

    @service_username.setter
    def service_username(self, service_username):
        """Sets the service_username of this SessionEventData.


        :param service_username: The service_username of this SessionEventData.  # noqa: E501
        :type: str
        """

        self._service_username = service_username

    @property
    def state(self):
        """Gets the state of this SessionEventData.  # noqa: E501


        :return: The state of this SessionEventData.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this SessionEventData.


        :param state: The state of this SessionEventData.  # noqa: E501
        :type: str
        """
        allowed_values = ["Available", "Busy", "Disconnected", "Unknown"]  # noqa: E501
        if (self._configuration.client_side_validation and
                state not in allowed_values):
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def reporting_time(self):
        """Gets the reporting_time of this SessionEventData.  # noqa: E501


        :return: The reporting_time of this SessionEventData.  # noqa: E501
        :rtype: datetime
        """
        return self._reporting_time

    @reporting_time.setter
    def reporting_time(self, reporting_time):
        """Sets the reporting_time of this SessionEventData.


        :param reporting_time: The reporting_time of this SessionEventData.  # noqa: E501
        :type: datetime
        """

        self._reporting_time = reporting_time

    @property
    def is_unresponsive(self):
        """Gets the is_unresponsive of this SessionEventData.  # noqa: E501


        :return: The is_unresponsive of this SessionEventData.  # noqa: E501
        :rtype: bool
        """
        return self._is_unresponsive

    @is_unresponsive.setter
    def is_unresponsive(self, is_unresponsive):
        """Sets the is_unresponsive of this SessionEventData.


        :param is_unresponsive: The is_unresponsive of this SessionEventData.  # noqa: E501
        :type: bool
        """

        self._is_unresponsive = is_unresponsive

    @property
    def license_error_code(self):
        """Gets the license_error_code of this SessionEventData.  # noqa: E501


        :return: The license_error_code of this SessionEventData.  # noqa: E501
        :rtype: str
        """
        return self._license_error_code

    @license_error_code.setter
    def license_error_code(self, license_error_code):
        """Sets the license_error_code of this SessionEventData.


        :param license_error_code: The license_error_code of this SessionEventData.  # noqa: E501
        :type: str
        """
        allowed_values = ["NoLicense", "LicenseExpired", "LicenseUnregistered", "NoAvailableLicenses", "NotEnoughAvailableSlots", "NotEnoughRuntimeLicenses", "LicenseIsAlreadyInUse", "InvalidRequest", "SlotsExceedLicenseLimit", "RuntimeDisabled", "ExternalNotSupported", "UsageExceedsLicenseLimit", "LicenseNotCompatible"]  # noqa: E501
        if (self._configuration.client_side_validation and
                license_error_code not in allowed_values):
            raise ValueError(
                "Invalid value for `license_error_code` ({0}), must be one of {1}"  # noqa: E501
                .format(license_error_code, allowed_values)
            )

        self._license_error_code = license_error_code

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
        if issubclass(SessionEventData, dict):
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
        if not isinstance(other, SessionEventData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SessionEventData):
            return True

        return self.to_dict() != other.to_dict()
