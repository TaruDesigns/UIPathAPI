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


class LibraryDto(object):
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
        'created': 'datetime',
        'last_updated': 'datetime',
        'owners': 'str',
        'icon_url': 'str',
        'summary': 'str',
        'package_size': 'int',
        'is_prerelease': 'bool',
        'title': 'str',
        'version': 'str',
        'key': 'str',
        'description': 'str',
        'published': 'datetime',
        'is_latest_version': 'bool',
        'old_version': 'str',
        'release_notes': 'str',
        'authors': 'str',
        'project_type': 'str',
        'tags': 'str',
        'is_compiled': 'bool',
        'license_url': 'str',
        'project_url': 'str',
        'resource_tags': 'list[TagDto]',
        'id': 'str'
    }

    attribute_map = {
        'created': 'Created',
        'last_updated': 'LastUpdated',
        'owners': 'Owners',
        'icon_url': 'IconUrl',
        'summary': 'Summary',
        'package_size': 'PackageSize',
        'is_prerelease': 'IsPrerelease',
        'title': 'Title',
        'version': 'Version',
        'key': 'Key',
        'description': 'Description',
        'published': 'Published',
        'is_latest_version': 'IsLatestVersion',
        'old_version': 'OldVersion',
        'release_notes': 'ReleaseNotes',
        'authors': 'Authors',
        'project_type': 'ProjectType',
        'tags': 'Tags',
        'is_compiled': 'IsCompiled',
        'license_url': 'LicenseUrl',
        'project_url': 'ProjectUrl',
        'resource_tags': 'ResourceTags',
        'id': 'Id'
    }

    def __init__(self, created=None, last_updated=None, owners=None, icon_url=None, summary=None, package_size=None, is_prerelease=None, title=None, version=None, key=None, description=None, published=None, is_latest_version=None, old_version=None, release_notes=None, authors=None, project_type=None, tags=None, is_compiled=None, license_url=None, project_url=None, resource_tags=None, id=None, _configuration=None):  # noqa: E501
        """LibraryDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._created = None
        self._last_updated = None
        self._owners = None
        self._icon_url = None
        self._summary = None
        self._package_size = None
        self._is_prerelease = None
        self._title = None
        self._version = None
        self._key = None
        self._description = None
        self._published = None
        self._is_latest_version = None
        self._old_version = None
        self._release_notes = None
        self._authors = None
        self._project_type = None
        self._tags = None
        self._is_compiled = None
        self._license_url = None
        self._project_url = None
        self._resource_tags = None
        self._id = None
        self.discriminator = None

        if created is not None:
            self.created = created
        if last_updated is not None:
            self.last_updated = last_updated
        if owners is not None:
            self.owners = owners
        if icon_url is not None:
            self.icon_url = icon_url
        if summary is not None:
            self.summary = summary
        if package_size is not None:
            self.package_size = package_size
        if is_prerelease is not None:
            self.is_prerelease = is_prerelease
        if title is not None:
            self.title = title
        if version is not None:
            self.version = version
        if key is not None:
            self.key = key
        if description is not None:
            self.description = description
        if published is not None:
            self.published = published
        if is_latest_version is not None:
            self.is_latest_version = is_latest_version
        if old_version is not None:
            self.old_version = old_version
        if release_notes is not None:
            self.release_notes = release_notes
        if authors is not None:
            self.authors = authors
        if project_type is not None:
            self.project_type = project_type
        if tags is not None:
            self.tags = tags
        if is_compiled is not None:
            self.is_compiled = is_compiled
        if license_url is not None:
            self.license_url = license_url
        if project_url is not None:
            self.project_url = project_url
        if resource_tags is not None:
            self.resource_tags = resource_tags
        if id is not None:
            self.id = id

    @property
    def created(self):
        """Gets the created of this LibraryDto.  # noqa: E501


        :return: The created of this LibraryDto.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this LibraryDto.


        :param created: The created of this LibraryDto.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def last_updated(self):
        """Gets the last_updated of this LibraryDto.  # noqa: E501


        :return: The last_updated of this LibraryDto.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this LibraryDto.


        :param last_updated: The last_updated of this LibraryDto.  # noqa: E501
        :type: datetime
        """

        self._last_updated = last_updated

    @property
    def owners(self):
        """Gets the owners of this LibraryDto.  # noqa: E501


        :return: The owners of this LibraryDto.  # noqa: E501
        :rtype: str
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """Sets the owners of this LibraryDto.


        :param owners: The owners of this LibraryDto.  # noqa: E501
        :type: str
        """

        self._owners = owners

    @property
    def icon_url(self):
        """Gets the icon_url of this LibraryDto.  # noqa: E501


        :return: The icon_url of this LibraryDto.  # noqa: E501
        :rtype: str
        """
        return self._icon_url

    @icon_url.setter
    def icon_url(self, icon_url):
        """Sets the icon_url of this LibraryDto.


        :param icon_url: The icon_url of this LibraryDto.  # noqa: E501
        :type: str
        """

        self._icon_url = icon_url

    @property
    def summary(self):
        """Gets the summary of this LibraryDto.  # noqa: E501


        :return: The summary of this LibraryDto.  # noqa: E501
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this LibraryDto.


        :param summary: The summary of this LibraryDto.  # noqa: E501
        :type: str
        """

        self._summary = summary

    @property
    def package_size(self):
        """Gets the package_size of this LibraryDto.  # noqa: E501


        :return: The package_size of this LibraryDto.  # noqa: E501
        :rtype: int
        """
        return self._package_size

    @package_size.setter
    def package_size(self, package_size):
        """Sets the package_size of this LibraryDto.


        :param package_size: The package_size of this LibraryDto.  # noqa: E501
        :type: int
        """

        self._package_size = package_size

    @property
    def is_prerelease(self):
        """Gets the is_prerelease of this LibraryDto.  # noqa: E501


        :return: The is_prerelease of this LibraryDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_prerelease

    @is_prerelease.setter
    def is_prerelease(self, is_prerelease):
        """Sets the is_prerelease of this LibraryDto.


        :param is_prerelease: The is_prerelease of this LibraryDto.  # noqa: E501
        :type: bool
        """

        self._is_prerelease = is_prerelease

    @property
    def title(self):
        """Gets the title of this LibraryDto.  # noqa: E501

        The custom name of the package.  # noqa: E501

        :return: The title of this LibraryDto.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this LibraryDto.

        The custom name of the package.  # noqa: E501

        :param title: The title of this LibraryDto.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def version(self):
        """Gets the version of this LibraryDto.  # noqa: E501

        The current version of the given package.  # noqa: E501

        :return: The version of this LibraryDto.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this LibraryDto.

        The current version of the given package.  # noqa: E501

        :param version: The version of this LibraryDto.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def key(self):
        """Gets the key of this LibraryDto.  # noqa: E501

        The unique identifier for the package.  # noqa: E501

        :return: The key of this LibraryDto.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this LibraryDto.

        The unique identifier for the package.  # noqa: E501

        :param key: The key of this LibraryDto.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def description(self):
        """Gets the description of this LibraryDto.  # noqa: E501

        Used to add additional information about a package in order to better identify it.  # noqa: E501

        :return: The description of this LibraryDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LibraryDto.

        Used to add additional information about a package in order to better identify it.  # noqa: E501

        :param description: The description of this LibraryDto.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def published(self):
        """Gets the published of this LibraryDto.  # noqa: E501

        The date and time when the package was published or uploaded.  # noqa: E501

        :return: The published of this LibraryDto.  # noqa: E501
        :rtype: datetime
        """
        return self._published

    @published.setter
    def published(self, published):
        """Sets the published of this LibraryDto.

        The date and time when the package was published or uploaded.  # noqa: E501

        :param published: The published of this LibraryDto.  # noqa: E501
        :type: datetime
        """

        self._published = published

    @property
    def is_latest_version(self):
        """Gets the is_latest_version of this LibraryDto.  # noqa: E501

        Specifies whether the current version is the latest of the given package.  # noqa: E501

        :return: The is_latest_version of this LibraryDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_latest_version

    @is_latest_version.setter
    def is_latest_version(self, is_latest_version):
        """Sets the is_latest_version of this LibraryDto.

        Specifies whether the current version is the latest of the given package.  # noqa: E501

        :param is_latest_version: The is_latest_version of this LibraryDto.  # noqa: E501
        :type: bool
        """

        self._is_latest_version = is_latest_version

    @property
    def old_version(self):
        """Gets the old_version of this LibraryDto.  # noqa: E501

        Specifies the last version before the current one.  # noqa: E501

        :return: The old_version of this LibraryDto.  # noqa: E501
        :rtype: str
        """
        return self._old_version

    @old_version.setter
    def old_version(self, old_version):
        """Sets the old_version of this LibraryDto.

        Specifies the last version before the current one.  # noqa: E501

        :param old_version: The old_version of this LibraryDto.  # noqa: E501
        :type: str
        """

        self._old_version = old_version

    @property
    def release_notes(self):
        """Gets the release_notes of this LibraryDto.  # noqa: E501

        Package release notes.  # noqa: E501

        :return: The release_notes of this LibraryDto.  # noqa: E501
        :rtype: str
        """
        return self._release_notes

    @release_notes.setter
    def release_notes(self, release_notes):
        """Sets the release_notes of this LibraryDto.

        Package release notes.  # noqa: E501

        :param release_notes: The release_notes of this LibraryDto.  # noqa: E501
        :type: str
        """

        self._release_notes = release_notes

    @property
    def authors(self):
        """Gets the authors of this LibraryDto.  # noqa: E501

        Package authors.  # noqa: E501

        :return: The authors of this LibraryDto.  # noqa: E501
        :rtype: str
        """
        return self._authors

    @authors.setter
    def authors(self, authors):
        """Sets the authors of this LibraryDto.

        Package authors.  # noqa: E501

        :param authors: The authors of this LibraryDto.  # noqa: E501
        :type: str
        """

        self._authors = authors

    @property
    def project_type(self):
        """Gets the project_type of this LibraryDto.  # noqa: E501

        Package project type.  # noqa: E501

        :return: The project_type of this LibraryDto.  # noqa: E501
        :rtype: str
        """
        return self._project_type

    @project_type.setter
    def project_type(self, project_type):
        """Sets the project_type of this LibraryDto.

        Package project type.  # noqa: E501

        :param project_type: The project_type of this LibraryDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["Undefined", "Process", "ProcessLibrary", "BusinessProcess", "BusinessProcessLibrary", "TestAutomationProcess"]  # noqa: E501
        if (self._configuration.client_side_validation and
                project_type not in allowed_values):
            raise ValueError(
                "Invalid value for `project_type` ({0}), must be one of {1}"  # noqa: E501
                .format(project_type, allowed_values)
            )

        self._project_type = project_type

    @property
    def tags(self):
        """Gets the tags of this LibraryDto.  # noqa: E501

        Package tags.  # noqa: E501

        :return: The tags of this LibraryDto.  # noqa: E501
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this LibraryDto.

        Package tags.  # noqa: E501

        :param tags: The tags of this LibraryDto.  # noqa: E501
        :type: str
        """

        self._tags = tags

    @property
    def is_compiled(self):
        """Gets the is_compiled of this LibraryDto.  # noqa: E501

        Disable explore packages for compiled processes  # noqa: E501

        :return: The is_compiled of this LibraryDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_compiled

    @is_compiled.setter
    def is_compiled(self, is_compiled):
        """Sets the is_compiled of this LibraryDto.

        Disable explore packages for compiled processes  # noqa: E501

        :param is_compiled: The is_compiled of this LibraryDto.  # noqa: E501
        :type: bool
        """

        self._is_compiled = is_compiled

    @property
    def license_url(self):
        """Gets the license_url of this LibraryDto.  # noqa: E501

        License URL  # noqa: E501

        :return: The license_url of this LibraryDto.  # noqa: E501
        :rtype: str
        """
        return self._license_url

    @license_url.setter
    def license_url(self, license_url):
        """Sets the license_url of this LibraryDto.

        License URL  # noqa: E501

        :param license_url: The license_url of this LibraryDto.  # noqa: E501
        :type: str
        """

        self._license_url = license_url

    @property
    def project_url(self):
        """Gets the project_url of this LibraryDto.  # noqa: E501

        Project URL  # noqa: E501

        :return: The project_url of this LibraryDto.  # noqa: E501
        :rtype: str
        """
        return self._project_url

    @project_url.setter
    def project_url(self, project_url):
        """Sets the project_url of this LibraryDto.

        Project URL  # noqa: E501

        :param project_url: The project_url of this LibraryDto.  # noqa: E501
        :type: str
        """

        self._project_url = project_url

    @property
    def resource_tags(self):
        """Gets the resource_tags of this LibraryDto.  # noqa: E501

        Tags set up by orchestrator  # noqa: E501

        :return: The resource_tags of this LibraryDto.  # noqa: E501
        :rtype: list[TagDto]
        """
        return self._resource_tags

    @resource_tags.setter
    def resource_tags(self, resource_tags):
        """Sets the resource_tags of this LibraryDto.

        Tags set up by orchestrator  # noqa: E501

        :param resource_tags: The resource_tags of this LibraryDto.  # noqa: E501
        :type: list[TagDto]
        """

        self._resource_tags = resource_tags

    @property
    def id(self):
        """Gets the id of this LibraryDto.  # noqa: E501


        :return: The id of this LibraryDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LibraryDto.


        :param id: The id of this LibraryDto.  # noqa: E501
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
        if issubclass(LibraryDto, dict):
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
        if not isinstance(other, LibraryDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LibraryDto):
            return True

        return self.to_dict() != other.to_dict()
