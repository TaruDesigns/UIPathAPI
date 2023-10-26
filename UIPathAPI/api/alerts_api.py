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


class AlertsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def alerts_expand_current_user_group_alerts(self, **kwargs):  # noqa: E501
        """alerts_expand_current_user_group_alerts  # noqa: E501

        OAuth required scopes: OR.Monitoring or OR.Monitoring.Write.  Required permissions: Alerts.View.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.alerts_expand_current_user_group_alerts(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.alerts_expand_current_user_group_alerts_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.alerts_expand_current_user_group_alerts_with_http_info(**kwargs)  # noqa: E501
            return data

    def alerts_expand_current_user_group_alerts_with_http_info(self, **kwargs):  # noqa: E501
        """alerts_expand_current_user_group_alerts  # noqa: E501

        OAuth required scopes: OR.Monitoring or OR.Monitoring.Write.  Required permissions: Alerts.View.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.alerts_expand_current_user_group_alerts_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
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
                    " to method alerts_expand_current_user_group_alerts" % key
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
            '/odata/Alerts/UiPath.Server.Configuration.OData.ExpandCurrentUserGroupAlerts', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def alerts_get(self, **kwargs):  # noqa: E501
        """Gets alerts.  # noqa: E501

        OAuth required scopes: OR.Monitoring or OR.Monitoring.Read.  Required permissions: Alerts.View.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.alerts_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str expand: Indicates the related entities to be represented inline. The maximum depth is 2.
        :param str filter: Restricts the set of items returned. The maximum number of expressions is 100.
        :param str select: Limits the properties returned in the result.
        :param str orderby: Specifies the order in which items are returned. The maximum number of expressions is 5.
        :param int top: Limits the number of items returned from a collection. The maximum value is 1000.
        :param int skip: Excludes the specified number of items of the queried collection from the result.
        :param bool count: Indicates whether the total count of items within a collection are returned in the result.
        :return: ODataValueOfIEnumerableOfAlertDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.alerts_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.alerts_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def alerts_get_with_http_info(self, **kwargs):  # noqa: E501
        """Gets alerts.  # noqa: E501

        OAuth required scopes: OR.Monitoring or OR.Monitoring.Read.  Required permissions: Alerts.View.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.alerts_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str expand: Indicates the related entities to be represented inline. The maximum depth is 2.
        :param str filter: Restricts the set of items returned. The maximum number of expressions is 100.
        :param str select: Limits the properties returned in the result.
        :param str orderby: Specifies the order in which items are returned. The maximum number of expressions is 5.
        :param int top: Limits the number of items returned from a collection. The maximum value is 1000.
        :param int skip: Excludes the specified number of items of the queried collection from the result.
        :param bool count: Indicates whether the total count of items within a collection are returned in the result.
        :return: ODataValueOfIEnumerableOfAlertDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['expand', 'filter', 'select', 'orderby', 'top', 'skip', 'count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method alerts_get" % key
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

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/odata/Alerts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ODataValueOfIEnumerableOfAlertDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def alerts_get_unread_count(self, **kwargs):  # noqa: E501
        """Returns the total number of alerts, per tenant, that haven't been read by the current user.  # noqa: E501

        OAuth required scopes: OR.Monitoring or OR.Monitoring.Read.  Required permissions: Alerts.View.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.alerts_get_unread_count(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str expand: Indicates the related entities to be represented inline. The maximum depth is 2.
        :param str select: Limits the properties returned in the result.
        :return: ODataValueOfInt64
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.alerts_get_unread_count_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.alerts_get_unread_count_with_http_info(**kwargs)  # noqa: E501
            return data

    def alerts_get_unread_count_with_http_info(self, **kwargs):  # noqa: E501
        """Returns the total number of alerts, per tenant, that haven't been read by the current user.  # noqa: E501

        OAuth required scopes: OR.Monitoring or OR.Monitoring.Read.  Required permissions: Alerts.View.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.alerts_get_unread_count_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str expand: Indicates the related entities to be represented inline. The maximum depth is 2.
        :param str select: Limits the properties returned in the result.
        :return: ODataValueOfInt64
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['expand', 'select']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method alerts_get_unread_count" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'expand' in params:
            query_params.append(('$expand', params['expand']))  # noqa: E501
        if 'select' in params:
            query_params.append(('$select', params['select']))  # noqa: E501

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
            '/odata/Alerts/UiPath.Server.Configuration.OData.GetUnreadCount', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ODataValueOfInt64',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def alerts_mark_as_read(self, **kwargs):  # noqa: E501
        """Marks alerts as read and returns the remaining number of unread notifications.  # noqa: E501

        OAuth required scopes: OR.Monitoring or OR.Monitoring.Write.  Required permissions: Alerts.View.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.alerts_mark_as_read(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AlertsMarkAsReadRequest body: Collection containing the unique identifiers of the notifications that will be marked as read
        :param str expand: Indicates the related entities to be represented inline. The maximum depth is 2.
        :param str select: Limits the properties returned in the result.
        :return: ODataValueOfInt64
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.alerts_mark_as_read_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.alerts_mark_as_read_with_http_info(**kwargs)  # noqa: E501
            return data

    def alerts_mark_as_read_with_http_info(self, **kwargs):  # noqa: E501
        """Marks alerts as read and returns the remaining number of unread notifications.  # noqa: E501

        OAuth required scopes: OR.Monitoring or OR.Monitoring.Write.  Required permissions: Alerts.View.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.alerts_mark_as_read_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AlertsMarkAsReadRequest body: Collection containing the unique identifiers of the notifications that will be marked as read
        :param str expand: Indicates the related entities to be represented inline. The maximum depth is 2.
        :param str select: Limits the properties returned in the result.
        :return: ODataValueOfInt64
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'expand', 'select']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method alerts_mark_as_read" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'expand' in params:
            query_params.append(('$expand', params['expand']))  # noqa: E501
        if 'select' in params:
            query_params.append(('$select', params['select']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json;odata.metadata=minimal;odata.streaming=true', 'application/json;odata.metadata=minimal;odata.streaming=false', 'application/json;odata.metadata=minimal', 'application/json;odata.metadata=full;odata.streaming=true', 'application/json;odata.metadata=full;odata.streaming=false', 'application/json;odata.metadata=full', 'application/json;odata.metadata=none;odata.streaming=true', 'application/json;odata.metadata=none;odata.streaming=false', 'application/json;odata.metadata=none', 'application/json;odata.streaming=true', 'application/json;odata.streaming=false', 'application/json', 'application/json-patch+json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/odata/Alerts/UiPath.Server.Configuration.OData.MarkAsRead', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ODataValueOfInt64',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def alerts_raise_process_alert(self, **kwargs):  # noqa: E501
        """Creates a Process Alert  # noqa: E501

        OAuth required scopes: OR.Monitoring or OR.Monitoring.Write.  Required permissions: Alerts.Create.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.alerts_raise_process_alert(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RaiseProcessAlertRequest body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.alerts_raise_process_alert_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.alerts_raise_process_alert_with_http_info(**kwargs)  # noqa: E501
            return data

    def alerts_raise_process_alert_with_http_info(self, **kwargs):  # noqa: E501
        """Creates a Process Alert  # noqa: E501

        OAuth required scopes: OR.Monitoring or OR.Monitoring.Write.  Required permissions: Alerts.Create.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.alerts_raise_process_alert_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RaiseProcessAlertRequest body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method alerts_raise_process_alert" % key
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
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json;odata.metadata=minimal;odata.streaming=true', 'application/json;odata.metadata=minimal;odata.streaming=false', 'application/json;odata.metadata=minimal', 'application/json;odata.metadata=full;odata.streaming=true', 'application/json;odata.metadata=full;odata.streaming=false', 'application/json;odata.metadata=full', 'application/json;odata.metadata=none;odata.streaming=true', 'application/json;odata.metadata=none;odata.streaming=false', 'application/json;odata.metadata=none', 'application/json;odata.streaming=true', 'application/json;odata.streaming=false', 'application/json', 'application/json-patch+json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/odata/Alerts/UiPath.Server.Configuration.OData.RaiseProcessAlert', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
