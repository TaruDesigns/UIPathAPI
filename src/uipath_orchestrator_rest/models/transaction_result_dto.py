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


class TransactionResultDto(object):
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
        'is_successful': 'bool',
        'processing_exception': 'ProcessingExceptionDto',
        'defer_date': 'datetime',
        'due_date': 'datetime',
        'output': 'dict(str, object)',
        'analytics': 'dict(str, object)',
        'progress': 'str',
        'operation_id': 'str'
    }

    attribute_map = {
        'is_successful': 'IsSuccessful',
        'processing_exception': 'ProcessingException',
        'defer_date': 'DeferDate',
        'due_date': 'DueDate',
        'output': 'Output',
        'analytics': 'Analytics',
        'progress': 'Progress',
        'operation_id': 'OperationId'
    }

    def __init__(self, is_successful=None, processing_exception=None, defer_date=None, due_date=None, output=None, analytics=None, progress=None, operation_id=None, _configuration=None):  # noqa: E501
        """TransactionResultDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._is_successful = None
        self._processing_exception = None
        self._defer_date = None
        self._due_date = None
        self._output = None
        self._analytics = None
        self._progress = None
        self._operation_id = None
        self.discriminator = None

        if is_successful is not None:
            self.is_successful = is_successful
        if processing_exception is not None:
            self.processing_exception = processing_exception
        if defer_date is not None:
            self.defer_date = defer_date
        if due_date is not None:
            self.due_date = due_date
        if output is not None:
            self.output = output
        if analytics is not None:
            self.analytics = analytics
        if progress is not None:
            self.progress = progress
        if operation_id is not None:
            self.operation_id = operation_id

    @property
    def is_successful(self):
        """Gets the is_successful of this TransactionResultDto.  # noqa: E501

        States if the processing was successful or not.  # noqa: E501

        :return: The is_successful of this TransactionResultDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_successful

    @is_successful.setter
    def is_successful(self, is_successful):
        """Sets the is_successful of this TransactionResultDto.

        States if the processing was successful or not.  # noqa: E501

        :param is_successful: The is_successful of this TransactionResultDto.  # noqa: E501
        :type: bool
        """

        self._is_successful = is_successful

    @property
    def processing_exception(self):
        """Gets the processing_exception of this TransactionResultDto.  # noqa: E501


        :return: The processing_exception of this TransactionResultDto.  # noqa: E501
        :rtype: ProcessingExceptionDto
        """
        return self._processing_exception

    @processing_exception.setter
    def processing_exception(self, processing_exception):
        """Sets the processing_exception of this TransactionResultDto.


        :param processing_exception: The processing_exception of this TransactionResultDto.  # noqa: E501
        :type: ProcessingExceptionDto
        """

        self._processing_exception = processing_exception

    @property
    def defer_date(self):
        """Gets the defer_date of this TransactionResultDto.  # noqa: E501

        The earliest date and time at which the item is available for processing. If empty the item can be processed as soon as possible.  # noqa: E501

        :return: The defer_date of this TransactionResultDto.  # noqa: E501
        :rtype: datetime
        """
        return self._defer_date

    @defer_date.setter
    def defer_date(self, defer_date):
        """Sets the defer_date of this TransactionResultDto.

        The earliest date and time at which the item is available for processing. If empty the item can be processed as soon as possible.  # noqa: E501

        :param defer_date: The defer_date of this TransactionResultDto.  # noqa: E501
        :type: datetime
        """

        self._defer_date = defer_date

    @property
    def due_date(self):
        """Gets the due_date of this TransactionResultDto.  # noqa: E501

        The latest date and time at which the item should be processed. If empty the item can be processed at any given time.  # noqa: E501

        :return: The due_date of this TransactionResultDto.  # noqa: E501
        :rtype: datetime
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this TransactionResultDto.

        The latest date and time at which the item should be processed. If empty the item can be processed at any given time.  # noqa: E501

        :param due_date: The due_date of this TransactionResultDto.  # noqa: E501
        :type: datetime
        """

        self._due_date = due_date

    @property
    def output(self):
        """Gets the output of this TransactionResultDto.  # noqa: E501

        A collection of key value pairs containing custom data resulted after successful processing.  # noqa: E501

        :return: The output of this TransactionResultDto.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this TransactionResultDto.

        A collection of key value pairs containing custom data resulted after successful processing.  # noqa: E501

        :param output: The output of this TransactionResultDto.  # noqa: E501
        :type: dict(str, object)
        """

        self._output = output

    @property
    def analytics(self):
        """Gets the analytics of this TransactionResultDto.  # noqa: E501

        A collection of key value pairs containing custom data for further analytics processing.  # noqa: E501

        :return: The analytics of this TransactionResultDto.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._analytics

    @analytics.setter
    def analytics(self, analytics):
        """Sets the analytics of this TransactionResultDto.

        A collection of key value pairs containing custom data for further analytics processing.  # noqa: E501

        :param analytics: The analytics of this TransactionResultDto.  # noqa: E501
        :type: dict(str, object)
        """

        self._analytics = analytics

    @property
    def progress(self):
        """Gets the progress of this TransactionResultDto.  # noqa: E501

        String field which is used to keep track of the business flow progress.  # noqa: E501

        :return: The progress of this TransactionResultDto.  # noqa: E501
        :rtype: str
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this TransactionResultDto.

        String field which is used to keep track of the business flow progress.  # noqa: E501

        :param progress: The progress of this TransactionResultDto.  # noqa: E501
        :type: str
        """

        self._progress = progress

    @property
    def operation_id(self):
        """Gets the operation_id of this TransactionResultDto.  # noqa: E501

        The operation id which finished the queue item. Will be saved only if queue item is in final state  # noqa: E501

        :return: The operation_id of this TransactionResultDto.  # noqa: E501
        :rtype: str
        """
        return self._operation_id

    @operation_id.setter
    def operation_id(self, operation_id):
        """Sets the operation_id of this TransactionResultDto.

        The operation id which finished the queue item. Will be saved only if queue item is in final state  # noqa: E501

        :param operation_id: The operation_id of this TransactionResultDto.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                operation_id is not None and len(operation_id) > 128):
            raise ValueError("Invalid value for `operation_id`, length must be less than or equal to `128`")  # noqa: E501

        self._operation_id = operation_id

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
        if issubclass(TransactionResultDto, dict):
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
        if not isinstance(other, TransactionResultDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransactionResultDto):
            return True

        return self.to_dict() != other.to_dict()
