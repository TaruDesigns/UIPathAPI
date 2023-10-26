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


class TenantLicenseDto(object):
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
        'host_license_id': 'int',
        'creation_time': 'datetime',
        'code': 'str',
        'allowed': 'dict(str, int)',
        'id': 'int'
    }

    attribute_map = {
        'host_license_id': 'HostLicenseId',
        'creation_time': 'CreationTime',
        'code': 'Code',
        'allowed': 'Allowed',
        'id': 'Id'
    }

    def __init__(self, host_license_id=None, creation_time=None, code=None, allowed=None, id=None, _configuration=None):  # noqa: E501
        """TenantLicenseDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._host_license_id = None
        self._creation_time = None
        self._code = None
        self._allowed = None
        self._id = None
        self.discriminator = None

        if host_license_id is not None:
            self.host_license_id = host_license_id
        if creation_time is not None:
            self.creation_time = creation_time
        if code is not None:
            self.code = code
        if allowed is not None:
            self.allowed = allowed
        if id is not None:
            self.id = id

    @property
    def host_license_id(self):
        """Gets the host_license_id of this TenantLicenseDto.  # noqa: E501

        The host license Id.  # noqa: E501

        :return: The host_license_id of this TenantLicenseDto.  # noqa: E501
        :rtype: int
        """
        return self._host_license_id

    @host_license_id.setter
    def host_license_id(self, host_license_id):
        """Sets the host_license_id of this TenantLicenseDto.

        The host license Id.  # noqa: E501

        :param host_license_id: The host_license_id of this TenantLicenseDto.  # noqa: E501
        :type: int
        """

        self._host_license_id = host_license_id

    @property
    def creation_time(self):
        """Gets the creation_time of this TenantLicenseDto.  # noqa: E501

        The date it was uploaded.  # noqa: E501

        :return: The creation_time of this TenantLicenseDto.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this TenantLicenseDto.

        The date it was uploaded.  # noqa: E501

        :param creation_time: The creation_time of this TenantLicenseDto.  # noqa: E501
        :type: datetime
        """

        self._creation_time = creation_time

    @property
    def code(self):
        """Gets the code of this TenantLicenseDto.  # noqa: E501

        The license code.  # noqa: E501

        :return: The code of this TenantLicenseDto.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this TenantLicenseDto.

        The license code.  # noqa: E501

        :param code: The code of this TenantLicenseDto.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def allowed(self):
        """Gets the allowed of this TenantLicenseDto.  # noqa: E501

        Contains the number of allowed licenses for each type  # noqa: E501

        :return: The allowed of this TenantLicenseDto.  # noqa: E501
        :rtype: dict(str, int)
        """
        return self._allowed

    @allowed.setter
    def allowed(self, allowed):
        """Sets the allowed of this TenantLicenseDto.

        Contains the number of allowed licenses for each type  # noqa: E501

        :param allowed: The allowed of this TenantLicenseDto.  # noqa: E501
        :type: dict(str, int)
        """

        self._allowed = allowed

    @property
    def id(self):
        """Gets the id of this TenantLicenseDto.  # noqa: E501


        :return: The id of this TenantLicenseDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TenantLicenseDto.


        :param id: The id of this TenantLicenseDto.  # noqa: E501
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
        if issubclass(TenantLicenseDto, dict):
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
        if not isinstance(other, TenantLicenseDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TenantLicenseDto):
            return True

        return self.to_dict() != other.to_dict()
