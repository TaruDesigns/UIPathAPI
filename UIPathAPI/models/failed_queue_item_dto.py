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


class FailedQueueItemDto(object):
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
        'ordinal': 'int',
        'error_code': 'str',
        'error_message': 'str'
    }

    attribute_map = {
        'ordinal': 'Ordinal',
        'error_code': 'ErrorCode',
        'error_message': 'ErrorMessage'
    }

    def __init__(self, ordinal=None, error_code=None, error_message=None, _configuration=None):  # noqa: E501
        """FailedQueueItemDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._ordinal = None
        self._error_code = None
        self._error_message = None
        self.discriminator = None

        if ordinal is not None:
            self.ordinal = ordinal
        if error_code is not None:
            self.error_code = error_code
        if error_message is not None:
            self.error_message = error_message

    @property
    def ordinal(self):
        """Gets the ordinal of this FailedQueueItemDto.  # noqa: E501

        Ordinal of the item that failed.  A value of null means that offending item is unknown.  # noqa: E501

        :return: The ordinal of this FailedQueueItemDto.  # noqa: E501
        :rtype: int
        """
        return self._ordinal

    @ordinal.setter
    def ordinal(self, ordinal):
        """Sets the ordinal of this FailedQueueItemDto.

        Ordinal of the item that failed.  A value of null means that offending item is unknown.  # noqa: E501

        :param ordinal: The ordinal of this FailedQueueItemDto.  # noqa: E501
        :type: int
        """

        self._ordinal = ordinal

    @property
    def error_code(self):
        """Gets the error_code of this FailedQueueItemDto.  # noqa: E501

        Error code.  # noqa: E501

        :return: The error_code of this FailedQueueItemDto.  # noqa: E501
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this FailedQueueItemDto.

        Error code.  # noqa: E501

        :param error_code: The error_code of this FailedQueueItemDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["Unknown", "MultipleErrors", "InvalidODataRequest", "InvalidRequest", "NameAlreadyUsed", "ItemNotFound", "StringProtectFailed", "ItemAlreadyExists", "ErrorDeleting", "ErrorInserting", "ErrorUpdating", "ErrorSendingEmail", "InvalidArgument", "SqlAcquireLockFailure", "LibrariesFeedInUse", "HasDependentItems", "ItemIsInUse", "ParameterMissing", "ParameterInvalid", "DuplicateReference", "ForbiddenOperation", "InvalidUser", "FeatureDisabled", "OptimisticConcurrency", "EncryptionException", "CannotCreateOrMigrateTenantDb", "TenantIsRequired", "FieldNotEditable", "ServiceUnavailable", "SharedAccessSignatureFailure", "ProviderNotSupported", "EmailAlreadyUsed", "MaxSiblingsLimitReached", "InvalidAuditRelationship", "InvalidOrganizationUnit", "RequiredOrganizationUnit", "OrganizationUnitNotEditable", "NoOrganizationUnitWithPermissions", "MultipleOrganizationUnitsOnSession", "InvalidPermissionInCrossFolderRequest", "CannotCreateClassicEntities", "CannotEditClassicEntities", "RequiredPermissions", "CannotEditDuringMigration", "MachineAlreadyPairedWithDifferentLicenseKey", "NoAvailableLicenses", "HasAttachedRobots", "InvalidMachineKey", "MachineNameRequired", "UserNameRequired", "CannotDeleteBusyRobot", "MachineNameCannotChange", "MachineLicenseCannotChange", "CannotUpdateBusyRobot", "MachineTypeCannotChange", "UserNameInvalid", "SessionAlreadyActive", "CannotAssignMachineToFloatingRobot", "CannotUpdateRobotHostingType", "CannotAssignMachineTemplateToStandardRobot", "CannotUpdateActiveSession", "MachineTemplateUniqueLicenseKey", "InvalidMachineId", "InvalidNonProductionMachineSlots", "InvalidUnattendedMachineSlots", "DisconnectedRobot", "UnresponsiveRobot", "UnsupportedFloatingSessionRobotType", "UnsupportedStandardSessionRobotType", "RobotNotFoundUseInteractive", "MachineScopeProtected", "MachineKeyCannotChange", "TenantIdMismatch", "UserDoesNotHaveRobot", "RobotDisabled", "UnattendedRobotNotFound", "CannotPropagateMachineToSubfolders", "MachineRuntimeProtected", "IncompatibleOS", "IncompatibleRobotVersion", "MachineMaintenanceWindowDuration", "MachineMaintenanceTimeZoneId", "ClassicRobotNotFound", "ClassicRobotToUserMappingUsernameMissmatch", "UserMappedToRobotWithDifferentUsername", "RobotOnDifferentMachineMappedToSameUser", "ClassicRobotMappedToInvalidUser", "SameRobotUsernameMappedToDiferentUser", "ClassicCannotCleanNotFailedMigrations", "InvalidSlots", "RobotNotFoundByKey", "InvalidJobKey", "MachineSessionNotFound", "EnvironmentDeploymentConflict", "UnattendedRobotCredentialsNotFound", "ServerConflict", "ActionAlreadyPerformed", "UnavailableResources", "UserIsDeleted", "UserIsLockedOut", "ChangePassword", "PasswordExpired", "InvalidPassword", "CannotDeleteStaticRole", "UserNotEditable", "DomainUnreachable", "PasswordResetFailed", "ConfirmEmailFailed", "CannotUsePreviousPassword", "RoleIsNotEditable", "UserNotFoundInDomain", "CannotUpdateUsername", "InvalidLoginMethod", "InvalidUsernameOrPassword", "MultipleMatchingUsers", "CannotCallFromHost", "CreateNotAllowed", "ProvisionError", "EmptyDirectoryParam", "NotDirectoryUserOrGroup", "NoUsersFound", "CannotChangeRoleType", "InvalidTenantRole", "InvalidFolderRole", "HostTenantKeyNotFound", "CannotAssignFolderRolesToUser", "CannotAssignTenantRolesToFolder", "InvalidAuthenticationToken", "CannotDeleteLastAdmin", "CannotUnassignLastAdmin", "CannotInactivateLastAdmin", "UserNotInRole", "UserAlreadyInRole", "AdditionalPermissionsNotAllowed", "CredentialAssetEmptyPasswordForNewUser", "CredentialAssetEmptyForNewRobot", "AssetTypeNonUpdatable", "AssetNotAvailableForRobot", "AssetNotFound", "InvalidCron", "ScheduleWillNeverRun", "ScheduleMisfired", "InvalidScheduleKey", "ScheduleIsNotEnabled", "ScheduleNotAssociatedWithAQueue", "ScheduleCannotBeAssociatedWithAQueue", "UserIsAssignedToTriggers", "InvalidCronRecurrence", "DisabledDueToConsecutiveFailures", "MachineRobotHasAttachedTriggers", "UserHasAttachedTriggers", "MachineHasAttachedTriggers", "InvalidTimeZoneId", "DisabledDueToConsecutiveJobFailures", "ScheduleJobsNotCreated", "DownloadUnavailable", "CannotConnectToPackagesRepository", "NotSupportedByExternalFeeds", "ErrorDownloading", "InvalidPackageDetails", "TenantFeedInUse", "InvalidProcessKey", "JobTypeCannotBeStopped", "JobCannotBeCancelled", "JobCannotBeTerminated", "VersionNotFound", "ProcessNotFound", "HasAttachedProcesses", "InvalidExtension", "InvalidPackageCount", "PreviousVersionNotFound", "HasRunningJobs", "TenantNotFound", "PendingJobsAlreadyExist", "InvalidStartJobRobotIds", "UnregisteredCannotStartJobs", "LicenseExpiredCannotStartJobs", "InvalidReleaseKey", "InvalidPackageVersion", "TenantIsDisabled", "PackageNotFound", "NoRobotsAvailable", "PathTooLong", "JobExecutionFaulted", "InvalidJobIdOrRobotKey", "InvalidJobStateForSuspend", "JobNotFoundByPersistenceId", "SuspendJobStateNotFound", "ErrorPackagePublish", "ErrorSavingPackageDefinition", "MaxNumberJobsAlreadyExist", "HasSlaEnabedQueuesAssociated", "VersionsManagedAutomatically", "InaccessibleFeed", "TestAutomationJobExecutionNotSupported", "TestAutomationProcessAlreadyExists", "CannotRestartUnfinishedJob", "CyberArkEditPasswordNotAllowed", "LogMessageNotFound", "LogRobotNameNotFound", "InvalidElasticQuery", "EncryptionKeyNotFound", "EncryptionKeyIncorrectFormat", "AzureKeyVaultRetrieveIssue", "AzureKeyVaultStoreIssue", "EncryptionKeyUnavailable", "TransactionReferenceRequired", "InvalidTransactionProgressStatus", "TransactionNotStarted", "ReviewerNotAvailable", "QueueDefinitionParametersCannotChange", "QueueProcessingApplicationException", "QueueItemSchemaViolationException", "InvalidQueueSchemaDefinition", "InvalidQueueSchemaDefinitionChange", "InvalidQueueSchemaType", "QueueSchemaDefinitionNotFound", "SlaEnableQueueDefinitionFailure", "QueueSlaAtPredictedRisk", "QueueSlaPredictedBreach", "QueueItemContentSizeExceeded", "QueueItemInvalidTransitionFromFinalStatus", "QueueItemInvalidStatusForRetry", "LicenseNotFound", "LicenseExpired", "LicenseAlreadyInUse", "InvalidLicenseFormat", "LicenseLimitExceeded", "UnattendedLicenseLimitExceeded", "NonProductionLicenseLimitExceeded", "AttendedLicenseLimitExceeded", "DevelopmentLicenseLimitExceeded", "RobotFailedToAcquireLicense", "NonProductionSlotsLimitExceeded", "UnattendedSlotsLimitExceeded", "LicenseUnregistered", "LicenseNotAvailable", "NotEnoughAvailableSlots", "NotEnoughRuntimeLicenses", "SlotsExceedLicenseLimit", "NotEnoughAvailableLicenses", "HostLicenseLimitExceeded", "NoHostLicense", "LicenseNewInvalidArguments", "LicenseMachineDisabled", "CannotDisableBusyMachine", "HeadlessSlotsLimitExceeded", "HeadlessLicenseLimitExceeded", "TestAutomationSlotsLimitExceeded", "TestAutomationLicenseLimitExceeded", "LicenseNotCompatible", "AutomationCloudLicenseLimitExceeded", "AutomationExpressNotSupported", "StudioWebLocalRobotNotSupported", "ArgumentMetadataExtract", "ArgumentMetadataValidation", "ArgumentDefinitionExtract", "ArgumentValueExtract", "ArgumentValidation", "PackageMetadataExtract", "PackageMetadataValidation", "ProjectTypeChangedOnUpload", "EntryPointUniqueIdsAlreadyUsed", "EntryPointNotValidForRelease", "EntryPointNotAllowedForTestAutomationRelease", "UnknownWebhookEventType", "WebhookQuotaReached", "WebhookDuplicateName", "ExecutionMediaStorageUnavailable", "ExecutionMediaNotAvailableForJob", "ExecutionMediaContentNotAvailable", "JobNotAssignedToRobot", "JobAssignedToDifferentRobot", "JobNotCompleted", "JobVideoRecordingNotEnabled", "QueueItemVideoRecordingNotEnabled", "CannotDeleteDefaultCredentialStore", "CredentialStoreNotFound", "UnknownCredentialStoreType", "InvalidCredentialStoreConfiguration", "FailedToReadFromCredentialStore", "FailedToWriteToCredentialStore", "CannotDeleteNonEmptyCredentialStore", "FailedToDeleteFromCredentialStore", "InvalidCredentialStoreType", "TaskAssignmentError", "TaskCompletionError", "TaskAssigneeMismatchError", "TaskFormInvalidFormLayout", "TaskFormInvalidFormPayload", "TaskFormMultipleActions", "TaskFormNoAction", "TaskFormInvalidAction", "TasksNotAllowedInModernFolder", "NoFolderExistAsTaskAdmin", "NoFolderExistAsTaskUser", "TaskAlreadyCompletedBySameUser", "TaskTypeMistmatch", "TaskNotAlreadyAssigned", "TaskAssigneeNotPermitted", "TaskAssignerNotPermitted", "DuplicateTaskAssignment", "TaskAlreadyAssignedToSameUser", "TaskAlreadyAssignedToAnotherUser", "TaskAlreadyCompletedByAnotherUser", "TaskSaveError", "TaskFormNoData", "TaskForwardError", "TaskFormSubmitButtonMissing", "TaskDeletionGenericError", "TaskAlreadyDeletedBySameUser", "TaskAlreadyDeletedByAnotherUser", "TaskDeleterNotPermitted", "DuplicateTaskDelete", "NoFolderExistsWithTaskCatalogView", "TaskCatalogMultipleDistinctColumn", "TaskCatalogDistinctColumnInvalid", "TaskFormLayoutAndIdMissing", "TaskFormDuplicateFormLayoutGuid", "TaskFormFormLayoutGuidNotFound", "TaskFormLayoutOrGuidMissing", "TaskFormLayoutAndIdBothNotSupported", "TaskFormLayoutIdNotFound", "TaskFormLayoutOutOfSize", "TaskCatalogHaveActiveTasks", "TasksBulkFormLayoutIdsNotSameOrNull", "EmptyTasksBulkOperationRequest", "TaskMaximumBulkOperationLimitExceeded", "TasksBulkOperationError", "TasksBulkOperationInvalidCatalog", "TasksBulkUpdateWithTaskCatalogAndUnsetIsInvalid", "EditTaskNotFound", "TasksEditMetadataWithTaskCatalogAndUnsetIsInvalid", "TasksEditMetadataOperationInvalidCatalog", "TasksEditMetadataCatalogInEncryptedTaskIsInvalid", "TaskCatalogNotFound", "TaskCatalogEncrypted", "TasksSummaryDateDiffOutOfRange", "TasksSummaryEndDateShouldBeGreater", "TaskDefinitionPropertiesRequired", "TaskDefinitionNotFound", "TaskDefinitionVersionNotFound", "AppTaskNoAction", "AppTaskInvalidPayload", "AppTaskNoData", "TaskProviderInvalidModifiedDate", "TaskProviderInvalidTaskUrn", "TaskDefinitionAllowedActionsRequired", "AppTaskDataItemViolatesContentJsonSchema", "TaskDefinitionSchemaNotAnObject", "TaskDefinitionNameIsAlreadyUsed", "InvalidSecureStoreContext", "MailSmtpSettingsError", "CannotDeleteCalendarWhenUsedBySchedule", "InvalidExternalUrl", "HostMailSmtpSettingsError", "MandatoryPropertiesForRootFolderNotSpecified", "IncompatibleFolderProperties", "NoHierarchyAllowedForClassicFolders", "MaximumFolderHierarchyDepthReached", "CannotChangeRobotProvisionType", "CannotChangeFolderPermissionModel", "CannotEditFolderParent", "EntitiesRequiredForAssignmentNotFound", "CannotAssignRolesToNonFineGrainedFolders", "InvalidFolderDisplayName", "AssociationAlreadyExists", "UserDoesNotHaveAccessToFolder", "CannotChangeRobotUserFolderAssignments", "CannotAssignMachineToClassicFolder", "StrategyNotAvailableInModernFolder", "StrategyNotAvailableInClassicFolder", "ValidModernFolderIdRequired", "NoMachineAssociatedWithFolder", "ClassicFoldersCannotBeInvolvedInMoveOperation", "CannotMoveToDescendantFolder", "CannotDisableTriggersInHierarchy", "CannotKillJobsInHierarchy", "CannotDeleteEntitiesInHierarchy", "NotInFinalStateJobsExist", "ModernFoldersCannotInheritRolesFromTenant", "CannotChangeFolderFeedType", "CannotCreatePersonalWorkspace", "CannotSetMachineRobots", "FolderNotFound", "CannotUnassignFromFolder", "MachineAssociatedWithFolderConflict", "CannotAssignMachineToFolder", "CannotAssignPersonalWorkspaceMachines", "CannotMoveFolder", "CannotMigrateClassicRelatedObjects", "NotSuccessfulEntityMigration", "FolderTypeMismatch", "ActionNotAllowedInClassicFolder", "CannotRenameSolutionFolder", "MaintenanceActive", "TenantMaintenanceActive", "TenantMaintenanceNotActive", "AnalyticsNotAuthorized", "AnalyticsTenantNotProvisioned", "AnalyticsUserIsHostUser", "AnalyticsUserHasNoEmail", "AnalyticsUserNotFound", "AnalyticsAdminEmailProhibited", "AnalyticsDbQueryFailure", "InvalidStorageProvider", "BucketIsReadOnly", "InvalidBlobFilePath", "UnavailableStorageProvider", "BucketDoesNotExists", "BucketSecretNotFoundInCredentialStore", "TestSetNotNewOnCreate", "TestAutomationKeyMismatch", "TestSetNewOnUpdate", "TestSetEmpty", "TestSetDuplicatePackages", "TestSetVersionMaskInvalid", "TestSetDefinitionNotFound", "TestSetTestCaseInvalid", "TestSetTestCaseVersionInvalid", "TestAutomationVersionInvalid", "TestSetExecutionEmptyTestSet", "TestSetExecutionCreateFailed", "TestSetExecutionDuplicateUniqueIds", "TestCaseAssertionScreenshotMimeTypeMissing", "TestCaseAssertionScreenshotMissing", "TestSetExecutionBatchExecutionKeyAlreadyExists", "TestDataQueueContentJsonSchemaInvalid", "TestDataQueueNameChangeNotAllowed", "TestDataQueueItemViolatesContentJsonSchema", "TestDataQueueItemsFromMultipleQueues", "TestDataQueueItemsBulkAddMixed", "TestDataQueueBulkOperationInProgress", "TestSetDuplicateInputArgument", "TestSetExecutionInvalidExecutionTarget", "AttachmentInvalid", "TestCasesReexecuteFailed", "TestSetTestCaseMissingReleaseVersion", "TestCaseDefinitionDuplicateIds", "TestCaseDefinitionInUse", "TestSetScheduleInvalidScheduleKey", "InvalidTenantMoveStatus", "TenantMoveIdConflict", "TenantMoveMigrationConflict", "MediaFileNotFound", "MediaFileNotFoundForKey", "InvalidMediaFilesUpload", "MediaFileTypeNotSupported", "CannotBeExploredByOwner", "AlreadyExploredByCurrentUser", "NotExploredCurrentUser", "CannotRemoveMachineFromPersonalWorkspace", "CannotToggleDebugMode", "CannotStartRemoteControl", "CannotStopRemoteControl", "CheckForUpdatesWithProductDuplicates", "AccountIdMissing", "AccountIdPartitionKeyMismatch", "IdentityKeyMissing", "InvalidDownloadUri", "InstallationIdMissing", "UpdateRequestRetryFailed", "InvalidProductVersion", "ProductVersionUpdateNotAllowed", "HostRetentionPolicyInvalidLicenseType", "TenantRetentionPolicyLicenseTypeNotSupported", "SWRobotCreationFailed", "SWRobotCreationNotEnabled", "SWPersonalWorkspaceCreationFailed", "SWPersonalWorkspacesNotEnabled", "SWMachineTemplateCreationFailed", "SWMachineTemplateAssignmentFailed", "SWMachineTemplateAssignmentMissingVirtualFolder", "SWRobotCreationNoLicense", "SWUserDoesNotHaveAnAttendedRobotOrProvisionNotEnabled", "SWUserInactive", "SWUserLicensingEnabledNoRobots", "SWUserLicensingEnabledRobotProvisionFailed", "SWUserLicensingEnabledAttendedLicense", "SWUserLicensingDisabledNoRobots", "SWUserLicensingDisabledRobotProvisionFailed", "SWUserLicensingDisabledAttendedLicense", "ConnectionsAvailableOnlyInPW", "ResourceOverwriteNotSupported", "ResourceNotOverwritable", "ResourceOverwriteNotSupportedInStandardFolders", "MultipleOverwritesForSameResourceKeyNotSupported", "PackageResourceNotFound", "InvalidConnectionId", "ConnectionNotFound", "InvalidConnectionType", "ConnectedEventTriggerNoConnection", "ConnectedEventTriggerCreateFailed", "ConnectedEventTriggerDeleteFailed", "MissingEventTriggerBinding", "VirtualTriggerCanNotHaveUser", "EventTriggerCreateFailedConnectionNotAvailable", "UserHasNoRobotToFireUserEventTrigger", "CredentialsProxyNotFound", "CannotDeleteCredentialsProxyInUse", "CredentialsProxyUrlMustBeHttps", "CredentialsProxyHostUrlUpdateRequiresSecretResubmission", "CredentialsProxyBadSecretFormat", "CredentialsProxyAuthHealthRequestFailed", "CredentialsProxyHealthRequestFailed", "CredentialsProxyRequestFailedInvalidCredentials", "CredentialsProxyConnectionRefused", "CredentialsProxyTypeCannotBeUpdated", "CredentialsProxyRequestFailedForbidden", "CredentialsProxyRequestFailedNotFound", "CredentialsProxyRequestFailedInternalServerError", "CredentialsProxyRequestFailedUnhandledError", "CredentialsProxyRequestFailedBadRequest", "CredentialsProxyTypeCannotBeCreated", "ServerlessCreateMachineTemplateErrorCode", "ServerlessUpdateMachineTemplateErrorCode", "ServerlessDeleteMachineTemplateErrorCode", "ServerlessUnkownActionMachineTemplateErrorCode", "ServerlessVpnInvalidCidr", "ServerlessVpnInvalidState", "ServerlessVpnNotFound", "ServerlessUnknownError", "ServerlessNoMachineTemplate", "ServerlessGenericWorkloadsNotEnabled", "ServerlessRobotJobTypeInvalid", "ServerlessServiceIsDisabledInTenant", "InvalidSolutionArchive", "CompatibilityCheckFail", "RollbackNotSupported", "SolutionsResourceNotFound", "SolutionsResourceNotSupported", "SolutionsResourcesNotFound", "FolderKeyRequired", "SolutionsCannotInstallInClassicFolder", "SolutionsCannotInstallInSolutionFolder", "SolutionIsNotInstalledAtPath", "SolutionFolderNotFound", "SolutionFolderHasJobsNotInFinalState", "SolutionFileNotFound", "SolutionPackageUrlIsInvalid", "SolutionInstallationFolderNotFound", "SolutionPackageNotInScope", "ExportTimeout", "InvalidMessageReceived", "IntegrationServiceApiFailure", "JobFaulted", "JobStopped", "JobUnknownFinalStatus", "MaxTriggersLimitReached", "CalendarNotFound", "ContentLengthTooLarge"]  # noqa: E501
        if (self._configuration.client_side_validation and
                error_code not in allowed_values):
            raise ValueError(
                "Invalid value for `error_code` ({0}), must be one of {1}"  # noqa: E501
                .format(error_code, allowed_values)
            )

        self._error_code = error_code

    @property
    def error_message(self):
        """Gets the error_message of this FailedQueueItemDto.  # noqa: E501

        Error message.  # noqa: E501

        :return: The error_message of this FailedQueueItemDto.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this FailedQueueItemDto.

        Error message.  # noqa: E501

        :param error_message: The error_message of this FailedQueueItemDto.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

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
        if issubclass(FailedQueueItemDto, dict):
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
        if not isinstance(other, FailedQueueItemDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FailedQueueItemDto):
            return True

        return self.to_dict() != other.to_dict()
