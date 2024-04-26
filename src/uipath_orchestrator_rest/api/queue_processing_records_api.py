# coding: utf-8

"""
    UiPath.WebApi 18.0

    Orchestrator API  # noqa: E501

    OpenAPI spec version: 18.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from uipath_orchestrator_rest.api_client import ApiClient


class QueueProcessingRecordsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def queue_processing_records_retrieve_last_days_processing_records_by_daysno_and_queuedefinitionid(self, days_no, queue_definition_id, **kwargs):  # noqa: E501
        """Returns the computed processing status for a given queue in the last specified days.  # noqa: E501

        OAuth required scopes: OR.Queues or OR.Queues.Read.  Required permissions: Queues.View and Transactions.View.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.queue_processing_records_retrieve_last_days_processing_records_by_daysno_and_queuedefinitionid(days_no, queue_definition_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int days_no: The number of days to go back from the present moment when calculating the report. If it is 0 the report will be computed for the last hour. (required)
        :param int queue_definition_id: The Id of the queue for which the report is computed. (required)
        :param str expand: Indicates the related entities to be represented inline. The maximum depth is 2.
        :param str filter: Restricts the set of items returned. The maximum number of expressions is 100.
        :param str select: Limits the properties returned in the result.
        :param str orderby: Specifies the order in which items are returned. The maximum number of expressions is 5.
        :param bool count: Indicates whether the total count of items within a collection are returned in the result.
        :param int x_uipath_organization_unit_id: Folder/OrganizationUnit Id
        :return: ODataValueOfIEnumerableOfQueueProcessingRecordDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.queue_processing_records_retrieve_last_days_processing_records_by_daysno_and_queuedefinitionid_with_http_info(days_no, queue_definition_id, **kwargs)  # noqa: E501
        else:
            (data) = self.queue_processing_records_retrieve_last_days_processing_records_by_daysno_and_queuedefinitionid_with_http_info(days_no, queue_definition_id, **kwargs)  # noqa: E501
            return data

    def queue_processing_records_retrieve_last_days_processing_records_by_daysno_and_queuedefinitionid_with_http_info(self, days_no, queue_definition_id, **kwargs):  # noqa: E501
        """Returns the computed processing status for a given queue in the last specified days.  # noqa: E501

        OAuth required scopes: OR.Queues or OR.Queues.Read.  Required permissions: Queues.View and Transactions.View.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.queue_processing_records_retrieve_last_days_processing_records_by_daysno_and_queuedefinitionid_with_http_info(days_no, queue_definition_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int days_no: The number of days to go back from the present moment when calculating the report. If it is 0 the report will be computed for the last hour. (required)
        :param int queue_definition_id: The Id of the queue for which the report is computed. (required)
        :param str expand: Indicates the related entities to be represented inline. The maximum depth is 2.
        :param str filter: Restricts the set of items returned. The maximum number of expressions is 100.
        :param str select: Limits the properties returned in the result.
        :param str orderby: Specifies the order in which items are returned. The maximum number of expressions is 5.
        :param bool count: Indicates whether the total count of items within a collection are returned in the result.
        :param int x_uipath_organization_unit_id: Folder/OrganizationUnit Id
        :return: ODataValueOfIEnumerableOfQueueProcessingRecordDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['days_no', 'queue_definition_id', 'expand', 'filter', 'select', 'orderby', 'count', 'x_uipath_organization_unit_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method queue_processing_records_retrieve_last_days_processing_records_by_daysno_and_queuedefinitionid" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'days_no' is set
        if self.api_client.client_side_validation and ('days_no' not in params or
                                                       params['days_no'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `days_no` when calling `queue_processing_records_retrieve_last_days_processing_records_by_daysno_and_queuedefinitionid`")  # noqa: E501
        # verify the required parameter 'queue_definition_id' is set
        if self.api_client.client_side_validation and ('queue_definition_id' not in params or
                                                       params['queue_definition_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `queue_definition_id` when calling `queue_processing_records_retrieve_last_days_processing_records_by_daysno_and_queuedefinitionid`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'days_no' in params:
            path_params['daysNo'] = params['days_no']  # noqa: E501
        if 'queue_definition_id' in params:
            path_params['queueDefinitionId'] = params['queue_definition_id']  # noqa: E501

        query_params = []
        if 'expand' in params:
            query_params.append(('$expand', params['expand']))  # noqa: E501
        if 'filter' in params:
            query_params.append(('$filter', params['filter']))  # noqa: E501
        if 'select' in params:
            query_params.append(('$select', params['select']))  # noqa: E501
        if 'orderby' in params:
            query_params.append(('$orderby', params['orderby']))  # noqa: E501
        if 'count' in params:
            query_params.append(('$count', params['count']))  # noqa: E501

        header_params = {}
        if 'x_uipath_organization_unit_id' in params:
            header_params['X-UIPATH-OrganizationUnitId'] = params['x_uipath_organization_unit_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/odata/QueueProcessingRecords/UiPathODataSvc.RetrieveLastDaysProcessingRecords(daysNo={daysNo},queueDefinitionId={queueDefinitionId})', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ODataValueOfIEnumerableOfQueueProcessingRecordDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def queue_processing_records_retrieve_queues_processing_status(self, **kwargs):  # noqa: E501
        """Returns the processing status for all queues. Allows odata query options.  # noqa: E501

        OAuth required scopes: OR.Queues or OR.Queues.Read.  Required permissions: Queues.View.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.queue_processing_records_retrieve_queues_processing_status(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str expand: Indicates the related entities to be represented inline. The maximum depth is 2.
        :param str filter: Restricts the set of items returned. The maximum number of expressions is 100.
        :param str select: Limits the properties returned in the result.
        :param str orderby: Specifies the order in which items are returned. The maximum number of expressions is 5.
        :param int top: Limits the number of items returned from a collection. The maximum value is 1000.
        :param int skip: Excludes the specified number of items of the queried collection from the result.
        :param bool count: Indicates whether the total count of items within a collection are returned in the result.
        :param int x_uipath_organization_unit_id: Folder/OrganizationUnit Id
        :return: ODataValueOfIEnumerableOfQueueProcessingStatusDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.queue_processing_records_retrieve_queues_processing_status_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.queue_processing_records_retrieve_queues_processing_status_with_http_info(**kwargs)  # noqa: E501
            return data

    def queue_processing_records_retrieve_queues_processing_status_with_http_info(self, **kwargs):  # noqa: E501
        """Returns the processing status for all queues. Allows odata query options.  # noqa: E501

        OAuth required scopes: OR.Queues or OR.Queues.Read.  Required permissions: Queues.View.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.queue_processing_records_retrieve_queues_processing_status_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str expand: Indicates the related entities to be represented inline. The maximum depth is 2.
        :param str filter: Restricts the set of items returned. The maximum number of expressions is 100.
        :param str select: Limits the properties returned in the result.
        :param str orderby: Specifies the order in which items are returned. The maximum number of expressions is 5.
        :param int top: Limits the number of items returned from a collection. The maximum value is 1000.
        :param int skip: Excludes the specified number of items of the queried collection from the result.
        :param bool count: Indicates whether the total count of items within a collection are returned in the result.
        :param int x_uipath_organization_unit_id: Folder/OrganizationUnit Id
        :return: ODataValueOfIEnumerableOfQueueProcessingStatusDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['expand', 'filter', 'select', 'orderby', 'top', 'skip', 'count', 'x_uipath_organization_unit_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method queue_processing_records_retrieve_queues_processing_status" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'expand' in params:
            query_params.append(('$expand', params['expand']))  # noqa: E501
        if 'filter' in params:
            query_params.append(('$filter', params['filter']))  # noqa: E501
        if 'select' in params:
            query_params.append(('$select', params['select']))  # noqa: E501
        if 'orderby' in params:
            query_params.append(('$orderby', params['orderby']))  # noqa: E501
        if 'top' in params:
            query_params.append(('$top', params['top']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('$skip', params['skip']))  # noqa: E501
        if 'count' in params:
            query_params.append(('$count', params['count']))  # noqa: E501

        header_params = {}
        if 'x_uipath_organization_unit_id' in params:
            header_params['X-UIPATH-OrganizationUnitId'] = params['x_uipath_organization_unit_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/odata/QueueProcessingRecords/UiPathODataSvc.RetrieveQueuesProcessingStatus', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ODataValueOfIEnumerableOfQueueProcessingStatusDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)