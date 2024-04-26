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


class QueuesStartTransactionRequest(object):
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
        'transaction_data': 'TransactionDataDto'
    }

    attribute_map = {
        'transaction_data': 'transactionData'
    }

    def __init__(self, transaction_data=None, _configuration=None):  # noqa: E501
        """QueuesStartTransactionRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._transaction_data = None
        self.discriminator = None

        self.transaction_data = transaction_data

    @property
    def transaction_data(self):
        """Gets the transaction_data of this QueuesStartTransactionRequest.  # noqa: E501


        :return: The transaction_data of this QueuesStartTransactionRequest.  # noqa: E501
        :rtype: TransactionDataDto
        """
        return self._transaction_data

    @transaction_data.setter
    def transaction_data(self, transaction_data):
        """Sets the transaction_data of this QueuesStartTransactionRequest.


        :param transaction_data: The transaction_data of this QueuesStartTransactionRequest.  # noqa: E501
        :type: TransactionDataDto
        """
        if self._configuration.client_side_validation and transaction_data is None:
            raise ValueError("Invalid value for `transaction_data`, must not be `None`")  # noqa: E501

        self._transaction_data = transaction_data

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
        if issubclass(QueuesStartTransactionRequest, dict):
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
        if not isinstance(other, QueuesStartTransactionRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QueuesStartTransactionRequest):
            return True

        return self.to_dict() != other.to_dict()