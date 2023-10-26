# coding: utf-8

"""
    UiPath.WebApi 17.0

    Orchestrator API  # noqa: E501

    OpenAPI spec version: 17.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from UIPathAPI.api_client import ApiClient


class StatsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def stats_get_consumption_license_stats(self, **kwargs):  # noqa: E501
        """Gets the consumption licensing usage statistics  # noqa: E501

        OAuth required scopes: OR.Monitoring or OR.Monitoring.Read.  Required permissions: License.View.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stats_get_consumption_license_stats(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int tenant_id: The Tenant's Id - can be used when authenticated as Host
        :param int days: Number of reported license usage days
        :return: list[ConsumptionLicenseStatsModel]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.stats_get_consumption_license_stats_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.stats_get_consumption_license_stats_with_http_info(**kwargs)  # noqa: E501
            return data

    def stats_get_consumption_license_stats_with_http_info(self, **kwargs):  # noqa: E501
        """Gets the consumption licensing usage statistics  # noqa: E501

        OAuth required scopes: OR.Monitoring or OR.Monitoring.Read.  Required permissions: License.View.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stats_get_consumption_license_stats_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int tenant_id: The Tenant's Id - can be used when authenticated as Host
        :param int days: Number of reported license usage days
        :return: list[ConsumptionLicenseStatsModel]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tenant_id', 'days']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method stats_get_consumption_license_stats" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'tenant_id' in params:
            query_params.append(('tenantId', params['tenant_id']))  # noqa: E501
        if 'days' in params:
            query_params.append(('days', params['days']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/api/Stats/GetConsumptionLicenseStats', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ConsumptionLicenseStatsModel]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def stats_get_count_stats(self, **kwargs):  # noqa: E501
        """Gets the total number of various entities registered in Orchestrator  # noqa: E501

        OAuth required scopes: OR.Monitoring or OR.Monitoring.Read.  Requires authentication.  Returns the name and the total number of entities registered in Orchestrator for a set of entities.  All the counted entity types can be seen in the result below.       [             {               \"title\": \"Processes\",               \"count\": 1             },             {               \"title\": \"Assets\",               \"count\": 0             },             {               \"title\": \"Queues\",               \"count\": 0             },             {               \"title\": \"Schedules\",               \"count\": 0             }       ]  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stats_get_count_stats(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[CountStats]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.stats_get_count_stats_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.stats_get_count_stats_with_http_info(**kwargs)  # noqa: E501
            return data

    def stats_get_count_stats_with_http_info(self, **kwargs):  # noqa: E501
        """Gets the total number of various entities registered in Orchestrator  # noqa: E501

        OAuth required scopes: OR.Monitoring or OR.Monitoring.Read.  Requires authentication.  Returns the name and the total number of entities registered in Orchestrator for a set of entities.  All the counted entity types can be seen in the result below.       [             {               \"title\": \"Processes\",               \"count\": 1             },             {               \"title\": \"Assets\",               \"count\": 0             },             {               \"title\": \"Queues\",               \"count\": 0             },             {               \"title\": \"Schedules\",               \"count\": 0             }       ]  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stats_get_count_stats_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[CountStats]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method stats_get_count_stats" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/api/Stats/GetCountStats', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[CountStats]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def stats_get_jobs_stats(self, **kwargs):  # noqa: E501
        """Gets the total number of jobs aggregated by Job State  # noqa: E501

        OAuth required scopes: OR.Monitoring or OR.Monitoring.Read.  Required permissions: Jobs.View.  Returns the total number of Successful, Faulted and Canceled jobs respectively.  Example of returned result:      [            {              \"title\": \"Successful\",              \"count\": 0            },            {              \"title\": \"Faulted\",              \"count\": 0            },            {              \"title\": \"Canceled\",              \"count\": 0            }      ]  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stats_get_jobs_stats(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[CountStats]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.stats_get_jobs_stats_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.stats_get_jobs_stats_with_http_info(**kwargs)  # noqa: E501
            return data

    def stats_get_jobs_stats_with_http_info(self, **kwargs):  # noqa: E501
        """Gets the total number of jobs aggregated by Job State  # noqa: E501

        OAuth required scopes: OR.Monitoring or OR.Monitoring.Read.  Required permissions: Jobs.View.  Returns the total number of Successful, Faulted and Canceled jobs respectively.  Example of returned result:      [            {              \"title\": \"Successful\",              \"count\": 0            },            {              \"title\": \"Faulted\",              \"count\": 0            },            {              \"title\": \"Canceled\",              \"count\": 0            }      ]  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stats_get_jobs_stats_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[CountStats]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method stats_get_jobs_stats" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/api/Stats/GetJobsStats', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[CountStats]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def stats_get_license_stats(self, **kwargs):  # noqa: E501
        """Gets the licensing usage statistics  # noqa: E501

        OAuth required scopes: OR.Monitoring or OR.Monitoring.Read.  Required permissions: License.View.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stats_get_license_stats(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int tenant_id: The Tenant's Id - can be used when authenticated as Host
        :param int days: Number of reported license usage days
        :return: list[LicenseStatsModel]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.stats_get_license_stats_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.stats_get_license_stats_with_http_info(**kwargs)  # noqa: E501
            return data

    def stats_get_license_stats_with_http_info(self, **kwargs):  # noqa: E501
        """Gets the licensing usage statistics  # noqa: E501

        OAuth required scopes: OR.Monitoring or OR.Monitoring.Read.  Required permissions: License.View.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stats_get_license_stats_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int tenant_id: The Tenant's Id - can be used when authenticated as Host
        :param int days: Number of reported license usage days
        :return: list[LicenseStatsModel]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tenant_id', 'days']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method stats_get_license_stats" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'tenant_id' in params:
            query_params.append(('tenantId', params['tenant_id']))  # noqa: E501
        if 'days' in params:
            query_params.append(('days', params['days']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/api/Stats/GetLicenseStats', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[LicenseStatsModel]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def stats_get_sessions_stats(self, **kwargs):  # noqa: E501
        """Gets the total number of robots aggregated by Robot State  # noqa: E501

        OAuth required scopes: OR.Monitoring or OR.Monitoring.Read.  Required permissions: Robots.View.  Returns the total number of Available, Busy, Disconnected and Unresponsive robots respectively.  Example of returned result:      [            {              \"title\": \"Available\",              \"count\": 1            },            {              \"title\": \"Busy\",              \"count\": 0            },            {              \"title\": \"Disconnected\",              \"count\": 1            },            {              \"title\": \"Unresponsive\",              \"count\": 0            }      ]  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stats_get_sessions_stats(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[CountStats]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.stats_get_sessions_stats_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.stats_get_sessions_stats_with_http_info(**kwargs)  # noqa: E501
            return data

    def stats_get_sessions_stats_with_http_info(self, **kwargs):  # noqa: E501
        """Gets the total number of robots aggregated by Robot State  # noqa: E501

        OAuth required scopes: OR.Monitoring or OR.Monitoring.Read.  Required permissions: Robots.View.  Returns the total number of Available, Busy, Disconnected and Unresponsive robots respectively.  Example of returned result:      [            {              \"title\": \"Available\",              \"count\": 1            },            {              \"title\": \"Busy\",              \"count\": 0            },            {              \"title\": \"Disconnected\",              \"count\": 1            },            {              \"title\": \"Unresponsive\",              \"count\": 0            }      ]  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stats_get_sessions_stats_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[CountStats]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method stats_get_sessions_stats" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/api/Stats/GetSessionsStats', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[CountStats]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
