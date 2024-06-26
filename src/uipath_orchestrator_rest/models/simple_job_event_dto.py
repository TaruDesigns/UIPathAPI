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


class SimpleJobEventDto(object):
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
        'id': 'int',
        'key': 'str',
        'type': 'str',
        'state': 'str',
        'start_time': 'datetime',
        'resume_time': 'datetime',
        'end_time': 'datetime',
        'creation_time': 'datetime',
        'info': 'str',
        'specific_priority_value': 'int',
        'runtime_type': 'str',
        'source_type': 'str',
        'output_arguments': 'object',
        'robot': 'SimpleRobotEventDto',
        'machine': 'SimpleMachineDto',
        'release': 'SimpleReleaseEventDto'
    }

    attribute_map = {
        'id': 'Id',
        'key': 'Key',
        'type': 'Type',
        'state': 'State',
        'start_time': 'StartTime',
        'resume_time': 'ResumeTime',
        'end_time': 'EndTime',
        'creation_time': 'CreationTime',
        'info': 'Info',
        'specific_priority_value': 'SpecificPriorityValue',
        'runtime_type': 'RuntimeType',
        'source_type': 'SourceType',
        'output_arguments': 'OutputArguments',
        'robot': 'Robot',
        'machine': 'Machine',
        'release': 'Release'
    }

    def __init__(self, id=None, key=None, type=None, state=None, start_time=None, resume_time=None, end_time=None, creation_time=None, info=None, specific_priority_value=None, runtime_type=None, source_type=None, output_arguments=None, robot=None, machine=None, release=None, _configuration=None):  # noqa: E501
        """SimpleJobEventDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._key = None
        self._type = None
        self._state = None
        self._start_time = None
        self._resume_time = None
        self._end_time = None
        self._creation_time = None
        self._info = None
        self._specific_priority_value = None
        self._runtime_type = None
        self._source_type = None
        self._output_arguments = None
        self._robot = None
        self._machine = None
        self._release = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if key is not None:
            self.key = key
        if type is not None:
            self.type = type
        if state is not None:
            self.state = state
        if start_time is not None:
            self.start_time = start_time
        if resume_time is not None:
            self.resume_time = resume_time
        if end_time is not None:
            self.end_time = end_time
        if creation_time is not None:
            self.creation_time = creation_time
        if info is not None:
            self.info = info
        if specific_priority_value is not None:
            self.specific_priority_value = specific_priority_value
        if runtime_type is not None:
            self.runtime_type = runtime_type
        if source_type is not None:
            self.source_type = source_type
        if output_arguments is not None:
            self.output_arguments = output_arguments
        if robot is not None:
            self.robot = robot
        if machine is not None:
            self.machine = machine
        if release is not None:
            self.release = release

    @property
    def id(self):
        """Gets the id of this SimpleJobEventDto.  # noqa: E501


        :return: The id of this SimpleJobEventDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SimpleJobEventDto.


        :param id: The id of this SimpleJobEventDto.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def key(self):
        """Gets the key of this SimpleJobEventDto.  # noqa: E501


        :return: The key of this SimpleJobEventDto.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this SimpleJobEventDto.


        :param key: The key of this SimpleJobEventDto.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def type(self):
        """Gets the type of this SimpleJobEventDto.  # noqa: E501


        :return: The type of this SimpleJobEventDto.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SimpleJobEventDto.


        :param type: The type of this SimpleJobEventDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["Unattended", "Attended", "ServerlessGeneric"]  # noqa: E501
        if (self._configuration.client_side_validation and
                type not in allowed_values):
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def state(self):
        """Gets the state of this SimpleJobEventDto.  # noqa: E501


        :return: The state of this SimpleJobEventDto.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this SimpleJobEventDto.


        :param state: The state of this SimpleJobEventDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["Pending", "Running", "Stopping", "Terminating", "Faulted", "Successful", "Stopped", "Suspended", "Resumed"]  # noqa: E501
        if (self._configuration.client_side_validation and
                state not in allowed_values):
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def start_time(self):
        """Gets the start_time of this SimpleJobEventDto.  # noqa: E501


        :return: The start_time of this SimpleJobEventDto.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this SimpleJobEventDto.


        :param start_time: The start_time of this SimpleJobEventDto.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def resume_time(self):
        """Gets the resume_time of this SimpleJobEventDto.  # noqa: E501


        :return: The resume_time of this SimpleJobEventDto.  # noqa: E501
        :rtype: datetime
        """
        return self._resume_time

    @resume_time.setter
    def resume_time(self, resume_time):
        """Sets the resume_time of this SimpleJobEventDto.


        :param resume_time: The resume_time of this SimpleJobEventDto.  # noqa: E501
        :type: datetime
        """

        self._resume_time = resume_time

    @property
    def end_time(self):
        """Gets the end_time of this SimpleJobEventDto.  # noqa: E501


        :return: The end_time of this SimpleJobEventDto.  # noqa: E501
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this SimpleJobEventDto.


        :param end_time: The end_time of this SimpleJobEventDto.  # noqa: E501
        :type: datetime
        """

        self._end_time = end_time

    @property
    def creation_time(self):
        """Gets the creation_time of this SimpleJobEventDto.  # noqa: E501


        :return: The creation_time of this SimpleJobEventDto.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this SimpleJobEventDto.


        :param creation_time: The creation_time of this SimpleJobEventDto.  # noqa: E501
        :type: datetime
        """

        self._creation_time = creation_time

    @property
    def info(self):
        """Gets the info of this SimpleJobEventDto.  # noqa: E501


        :return: The info of this SimpleJobEventDto.  # noqa: E501
        :rtype: str
        """
        return self._info

    @info.setter
    def info(self, info):
        """Sets the info of this SimpleJobEventDto.


        :param info: The info of this SimpleJobEventDto.  # noqa: E501
        :type: str
        """

        self._info = info

    @property
    def specific_priority_value(self):
        """Gets the specific_priority_value of this SimpleJobEventDto.  # noqa: E501


        :return: The specific_priority_value of this SimpleJobEventDto.  # noqa: E501
        :rtype: int
        """
        return self._specific_priority_value

    @specific_priority_value.setter
    def specific_priority_value(self, specific_priority_value):
        """Sets the specific_priority_value of this SimpleJobEventDto.


        :param specific_priority_value: The specific_priority_value of this SimpleJobEventDto.  # noqa: E501
        :type: int
        """

        self._specific_priority_value = specific_priority_value

    @property
    def runtime_type(self):
        """Gets the runtime_type of this SimpleJobEventDto.  # noqa: E501


        :return: The runtime_type of this SimpleJobEventDto.  # noqa: E501
        :rtype: str
        """
        return self._runtime_type

    @runtime_type.setter
    def runtime_type(self, runtime_type):
        """Sets the runtime_type of this SimpleJobEventDto.


        :param runtime_type: The runtime_type of this SimpleJobEventDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["NonProduction", "Attended", "Unattended", "Development", "Studio", "RpaDeveloper", "StudioX", "CitizenDeveloper", "Headless", "StudioPro", "RpaDeveloperPro", "TestAutomation", "AutomationCloud", "Serverless", "AutomationKit", "ServerlessTestAutomation", "AutomationCloudTestAutomation", "AttendedStudioWeb"]  # noqa: E501
        if (self._configuration.client_side_validation and
                runtime_type not in allowed_values):
            raise ValueError(
                "Invalid value for `runtime_type` ({0}), must be one of {1}"  # noqa: E501
                .format(runtime_type, allowed_values)
            )

        self._runtime_type = runtime_type

    @property
    def source_type(self):
        """Gets the source_type of this SimpleJobEventDto.  # noqa: E501


        :return: The source_type of this SimpleJobEventDto.  # noqa: E501
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this SimpleJobEventDto.


        :param source_type: The source_type of this SimpleJobEventDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["Manual", "Schedule", "Agent", "Queue", "StudioWeb", "IntegrationTrigger", "StudioDesktop", "AutomationOpsPipelines", "Apps", "SAP", "HttpTrigger", "HttpTriggerCallback", "RobotAPI", "CommandLine", "RobotNetAPI"]  # noqa: E501
        if (self._configuration.client_side_validation and
                source_type not in allowed_values):
            raise ValueError(
                "Invalid value for `source_type` ({0}), must be one of {1}"  # noqa: E501
                .format(source_type, allowed_values)
            )

        self._source_type = source_type

    @property
    def output_arguments(self):
        """Gets the output_arguments of this SimpleJobEventDto.  # noqa: E501


        :return: The output_arguments of this SimpleJobEventDto.  # noqa: E501
        :rtype: object
        """
        return self._output_arguments

    @output_arguments.setter
    def output_arguments(self, output_arguments):
        """Sets the output_arguments of this SimpleJobEventDto.


        :param output_arguments: The output_arguments of this SimpleJobEventDto.  # noqa: E501
        :type: object
        """

        self._output_arguments = output_arguments

    @property
    def robot(self):
        """Gets the robot of this SimpleJobEventDto.  # noqa: E501


        :return: The robot of this SimpleJobEventDto.  # noqa: E501
        :rtype: SimpleRobotEventDto
        """
        return self._robot

    @robot.setter
    def robot(self, robot):
        """Sets the robot of this SimpleJobEventDto.


        :param robot: The robot of this SimpleJobEventDto.  # noqa: E501
        :type: SimpleRobotEventDto
        """

        self._robot = robot

    @property
    def machine(self):
        """Gets the machine of this SimpleJobEventDto.  # noqa: E501


        :return: The machine of this SimpleJobEventDto.  # noqa: E501
        :rtype: SimpleMachineDto
        """
        return self._machine

    @machine.setter
    def machine(self, machine):
        """Sets the machine of this SimpleJobEventDto.


        :param machine: The machine of this SimpleJobEventDto.  # noqa: E501
        :type: SimpleMachineDto
        """

        self._machine = machine

    @property
    def release(self):
        """Gets the release of this SimpleJobEventDto.  # noqa: E501


        :return: The release of this SimpleJobEventDto.  # noqa: E501
        :rtype: SimpleReleaseEventDto
        """
        return self._release

    @release.setter
    def release(self, release):
        """Sets the release of this SimpleJobEventDto.


        :param release: The release of this SimpleJobEventDto.  # noqa: E501
        :type: SimpleReleaseEventDto
        """

        self._release = release

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
        if issubclass(SimpleJobEventDto, dict):
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
        if not isinstance(other, SimpleJobEventDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SimpleJobEventDto):
            return True

        return self.to_dict() != other.to_dict()
