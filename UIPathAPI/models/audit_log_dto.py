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


class AuditLogDto(object):
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
        'service_name': 'str',
        'method_name': 'str',
        'parameters': 'str',
        'execution_time': 'datetime',
        'action': 'str',
        'component': 'str',
        'display_name': 'str',
        'entity_id': 'int',
        'operation_text': 'str',
        'user_name': 'str',
        'user_type': 'str',
        'entities': 'list[AuditLogEntityDto]',
        'external_client_id': 'str',
        'user_id': 'int',
        'user_is_deleted': 'bool',
        'id': 'int'
    }

    attribute_map = {
        'service_name': 'ServiceName',
        'method_name': 'MethodName',
        'parameters': 'Parameters',
        'execution_time': 'ExecutionTime',
        'action': 'Action',
        'component': 'Component',
        'display_name': 'DisplayName',
        'entity_id': 'EntityId',
        'operation_text': 'OperationText',
        'user_name': 'UserName',
        'user_type': 'UserType',
        'entities': 'Entities',
        'external_client_id': 'ExternalClientId',
        'user_id': 'UserId',
        'user_is_deleted': 'UserIsDeleted',
        'id': 'Id'
    }

    def __init__(self, service_name=None, method_name=None, parameters=None, execution_time=None, action=None, component=None, display_name=None, entity_id=None, operation_text=None, user_name=None, user_type=None, entities=None, external_client_id=None, user_id=None, user_is_deleted=None, id=None, _configuration=None):  # noqa: E501
        """AuditLogDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._service_name = None
        self._method_name = None
        self._parameters = None
        self._execution_time = None
        self._action = None
        self._component = None
        self._display_name = None
        self._entity_id = None
        self._operation_text = None
        self._user_name = None
        self._user_type = None
        self._entities = None
        self._external_client_id = None
        self._user_id = None
        self._user_is_deleted = None
        self._id = None
        self.discriminator = None

        if service_name is not None:
            self.service_name = service_name
        if method_name is not None:
            self.method_name = method_name
        if parameters is not None:
            self.parameters = parameters
        if execution_time is not None:
            self.execution_time = execution_time
        if action is not None:
            self.action = action
        if component is not None:
            self.component = component
        if display_name is not None:
            self.display_name = display_name
        if entity_id is not None:
            self.entity_id = entity_id
        if operation_text is not None:
            self.operation_text = operation_text
        if user_name is not None:
            self.user_name = user_name
        if user_type is not None:
            self.user_type = user_type
        if entities is not None:
            self.entities = entities
        if external_client_id is not None:
            self.external_client_id = external_client_id
        if user_id is not None:
            self.user_id = user_id
        if user_is_deleted is not None:
            self.user_is_deleted = user_is_deleted
        if id is not None:
            self.id = id

    @property
    def service_name(self):
        """Gets the service_name of this AuditLogDto.  # noqa: E501

        The name of the Orchestrator service that performed a given action in the system.  # noqa: E501

        :return: The service_name of this AuditLogDto.  # noqa: E501
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this AuditLogDto.

        The name of the Orchestrator service that performed a given action in the system.  # noqa: E501

        :param service_name: The service_name of this AuditLogDto.  # noqa: E501
        :type: str
        """

        self._service_name = service_name

    @property
    def method_name(self):
        """Gets the method_name of this AuditLogDto.  # noqa: E501

        The name of the service method that performed a given action in the system.  # noqa: E501

        :return: The method_name of this AuditLogDto.  # noqa: E501
        :rtype: str
        """
        return self._method_name

    @method_name.setter
    def method_name(self, method_name):
        """Sets the method_name of this AuditLogDto.

        The name of the service method that performed a given action in the system.  # noqa: E501

        :param method_name: The method_name of this AuditLogDto.  # noqa: E501
        :type: str
        """

        self._method_name = method_name

    @property
    def parameters(self):
        """Gets the parameters of this AuditLogDto.  # noqa: E501

        JSON representation of the method parameters and their values for the given action.  # noqa: E501

        :return: The parameters of this AuditLogDto.  # noqa: E501
        :rtype: str
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this AuditLogDto.

        JSON representation of the method parameters and their values for the given action.  # noqa: E501

        :param parameters: The parameters of this AuditLogDto.  # noqa: E501
        :type: str
        """

        self._parameters = parameters

    @property
    def execution_time(self):
        """Gets the execution_time of this AuditLogDto.  # noqa: E501

        The date and time when the action was performed.  # noqa: E501

        :return: The execution_time of this AuditLogDto.  # noqa: E501
        :rtype: datetime
        """
        return self._execution_time

    @execution_time.setter
    def execution_time(self, execution_time):
        """Sets the execution_time of this AuditLogDto.

        The date and time when the action was performed.  # noqa: E501

        :param execution_time: The execution_time of this AuditLogDto.  # noqa: E501
        :type: datetime
        """

        self._execution_time = execution_time

    @property
    def action(self):
        """Gets the action of this AuditLogDto.  # noqa: E501

        The action performed (create, update, delete etc)  # noqa: E501

        :return: The action of this AuditLogDto.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this AuditLogDto.

        The action performed (create, update, delete etc)  # noqa: E501

        :param action: The action of this AuditLogDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["Unknown", "Create", "Update", "Delete", "StartJob", "StopJob", "Associate", "Upload", "ChangeStatus", "Import", "ChangePassword", "Register", "Toggle", "ResetPassword", "PasswordResetAttempt", "Download", "Acknowledge", "Activate", "Assign", "BulkUpload", "UpdateFeature", "ResumeJob", "Start", "End", "Skip", "Unassign", "Deactivate", "CreateBlobFileSas", "DeleteBlobFile", "Move", "Set", "StartDelete", "ExploreStart", "ExploreEnd", "Save", "Convert", "Forward", "BulkComplete", "BulkSave", "ForceStopJob", "MigrateFolder", "EditTaskMetadata", "Archive", "StartMigrateFolders", "ToggleUserFolderSubscription", "StartUninstall", "StartInstall", "VideoAccess", "AutomaticallyExploreEnd", "InstallState", "FinishInstall", "FinishUninstall"]  # noqa: E501
        if (self._configuration.client_side_validation and
                action not in allowed_values):
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def component(self):
        """Gets the component of this AuditLogDto.  # noqa: E501

        The component for which the action was performed  # noqa: E501

        :return: The component of this AuditLogDto.  # noqa: E501
        :rtype: str
        """
        return self._component

    @component.setter
    def component(self, component):
        """Sets the component of this AuditLogDto.

        The component for which the action was performed  # noqa: E501

        :param component: The component of this AuditLogDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["Unknown", "Assets", "Environments", "Processes", "Queues", "Robots", "Roles", "Schedules", "Users", "Comments", "Units", "Jobs", "Settings", "Packages", "License", "Tenant", "Machines", "Libraries", "Webhooks", "ExecutionMedia", "Monitoring", "CredentialStores", "DefaultCredentialStores", "TaskCatalogs", "Tasks", "Maintenance", "Folders", "DirectoryService", "Buckets", "DataRetentionPolicies", "TenantMove", "Secrets", "PersonalWorkspaces", "CloudSubscriptions", "CloudSnapshots", "Sessions", "CredentialsProxies", "StudioWeb", "AutomationSolutions", "RemoteControl", "TaskSolutions", "TaskDefinitions", "HttpTriggers", "TestSets", "TestSetSchedules", "TestDataQueues", "TestDataQueueItems"]  # noqa: E501
        if (self._configuration.client_side_validation and
                component not in allowed_values):
            raise ValueError(
                "Invalid value for `component` ({0}), must be one of {1}"  # noqa: E501
                .format(component, allowed_values)
            )

        self._component = component

    @property
    def display_name(self):
        """Gets the display_name of this AuditLogDto.  # noqa: E501

        The display name of the resource acted on, usually Name  # noqa: E501

        :return: The display_name of this AuditLogDto.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this AuditLogDto.

        The display name of the resource acted on, usually Name  # noqa: E501

        :param display_name: The display_name of this AuditLogDto.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def entity_id(self):
        """Gets the entity_id of this AuditLogDto.  # noqa: E501

        The Id of the resource acted on  # noqa: E501

        :return: The entity_id of this AuditLogDto.  # noqa: E501
        :rtype: int
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this AuditLogDto.

        The Id of the resource acted on  # noqa: E501

        :param entity_id: The entity_id of this AuditLogDto.  # noqa: E501
        :type: int
        """

        self._entity_id = entity_id

    @property
    def operation_text(self):
        """Gets the operation_text of this AuditLogDto.  # noqa: E501

        User friendly description of the change, e.g. \"User X created robot Y\"  # noqa: E501

        :return: The operation_text of this AuditLogDto.  # noqa: E501
        :rtype: str
        """
        return self._operation_text

    @operation_text.setter
    def operation_text(self, operation_text):
        """Sets the operation_text of this AuditLogDto.

        User friendly description of the change, e.g. \"User X created robot Y\"  # noqa: E501

        :param operation_text: The operation_text of this AuditLogDto.  # noqa: E501
        :type: str
        """

        self._operation_text = operation_text

    @property
    def user_name(self):
        """Gets the user_name of this AuditLogDto.  # noqa: E501

        UserName that sent the request  # noqa: E501

        :return: The user_name of this AuditLogDto.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this AuditLogDto.

        UserName that sent the request  # noqa: E501

        :param user_name: The user_name of this AuditLogDto.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def user_type(self):
        """Gets the user_type of this AuditLogDto.  # noqa: E501

        The type of user that sent the request  # noqa: E501

        :return: The user_type of this AuditLogDto.  # noqa: E501
        :rtype: str
        """
        return self._user_type

    @user_type.setter
    def user_type(self, user_type):
        """Sets the user_type of this AuditLogDto.

        The type of user that sent the request  # noqa: E501

        :param user_type: The user_type of this AuditLogDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["User", "Robot", "DirectoryUser", "DirectoryGroup", "DirectoryRobot", "DirectoryExternalApplication"]  # noqa: E501
        if (self._configuration.client_side_validation and
                user_type not in allowed_values):
            raise ValueError(
                "Invalid value for `user_type` ({0}), must be one of {1}"  # noqa: E501
                .format(user_type, allowed_values)
            )

        self._user_type = user_type

    @property
    def entities(self):
        """Gets the entities of this AuditLogDto.  # noqa: E501

        Audit entity details collection  # noqa: E501

        :return: The entities of this AuditLogDto.  # noqa: E501
        :rtype: list[AuditLogEntityDto]
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """Sets the entities of this AuditLogDto.

        Audit entity details collection  # noqa: E501

        :param entities: The entities of this AuditLogDto.  # noqa: E501
        :type: list[AuditLogEntityDto]
        """

        self._entities = entities

    @property
    def external_client_id(self):
        """Gets the external_client_id of this AuditLogDto.  # noqa: E501

        External client identifier. Example: OAuth 3rd party app identifier that called Orchestrator.  # noqa: E501

        :return: The external_client_id of this AuditLogDto.  # noqa: E501
        :rtype: str
        """
        return self._external_client_id

    @external_client_id.setter
    def external_client_id(self, external_client_id):
        """Sets the external_client_id of this AuditLogDto.

        External client identifier. Example: OAuth 3rd party app identifier that called Orchestrator.  # noqa: E501

        :param external_client_id: The external_client_id of this AuditLogDto.  # noqa: E501
        :type: str
        """

        self._external_client_id = external_client_id

    @property
    def user_id(self):
        """Gets the user_id of this AuditLogDto.  # noqa: E501


        :return: The user_id of this AuditLogDto.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this AuditLogDto.


        :param user_id: The user_id of this AuditLogDto.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def user_is_deleted(self):
        """Gets the user_is_deleted of this AuditLogDto.  # noqa: E501

        Marks whether the users that did the action was deleted in the meantime  # noqa: E501

        :return: The user_is_deleted of this AuditLogDto.  # noqa: E501
        :rtype: bool
        """
        return self._user_is_deleted

    @user_is_deleted.setter
    def user_is_deleted(self, user_is_deleted):
        """Sets the user_is_deleted of this AuditLogDto.

        Marks whether the users that did the action was deleted in the meantime  # noqa: E501

        :param user_is_deleted: The user_is_deleted of this AuditLogDto.  # noqa: E501
        :type: bool
        """

        self._user_is_deleted = user_is_deleted

    @property
    def id(self):
        """Gets the id of this AuditLogDto.  # noqa: E501


        :return: The id of this AuditLogDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AuditLogDto.


        :param id: The id of this AuditLogDto.  # noqa: E501
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
        if issubclass(AuditLogDto, dict):
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
        if not isinstance(other, AuditLogDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AuditLogDto):
            return True

        return self.to_dict() != other.to_dict()
