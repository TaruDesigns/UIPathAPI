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


class OrganizationUnitDto(object):
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
        'display_name': 'str',
        'id': 'int'
    }

    attribute_map = {
        'display_name': 'DisplayName',
        'id': 'Id'
    }

    def __init__(self, display_name=None, id=None, _configuration=None):  # noqa: E501
        """OrganizationUnitDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._display_name = None
        self._id = None
        self.discriminator = None

        self.display_name = display_name
        if id is not None:
            self.id = id

    @property
    def display_name(self):
        """Gets the display_name of this OrganizationUnitDto.  # noqa: E501

        The name of the organization unit.  # noqa: E501

        :return: The display_name of this OrganizationUnitDto.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this OrganizationUnitDto.

        The name of the organization unit.  # noqa: E501

        :param display_name: The display_name of this OrganizationUnitDto.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                display_name is not None and len(display_name) > 128):
            raise ValueError("Invalid value for `display_name`, length must be less than or equal to `128`")  # noqa: E501
        if (self._configuration.client_side_validation and
                display_name is not None and len(display_name) < 1):
            raise ValueError("Invalid value for `display_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._display_name = display_name

    @property
    def id(self):
        """Gets the id of this OrganizationUnitDto.  # noqa: E501


        :return: The id of this OrganizationUnitDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrganizationUnitDto.


        :param id: The id of this OrganizationUnitDto.  # noqa: E501
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
        if issubclass(OrganizationUnitDto, dict):
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
        if not isinstance(other, OrganizationUnitDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrganizationUnitDto):
            return True

        return self.to_dict() != other.to_dict()
