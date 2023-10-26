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


class ReleaseRetentionApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def release_retention_delete_by_id(self, key, **kwargs):  # noqa: E501
        """release_retention_delete_by_id  # noqa: E501

        OAuth required scopes: OR.Execution or OR.Execution.Write.  Required permissions: Processes.Edit.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.release_retention_delete_by_id(key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int key: (required)
        :param int x_uipath_organization_unit_id: Folder/OrganizationUnit Id
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.release_retention_delete_by_id_with_http_info(key, **kwargs)  # noqa: E501
        else:
            (data) = self.release_retention_delete_by_id_with_http_info(key, **kwargs)  # noqa: E501
            return data

    def release_retention_delete_by_id_with_http_info(self, key, **kwargs):  # noqa: E501
        """release_retention_delete_by_id  # noqa: E501

        OAuth required scopes: OR.Execution or OR.Execution.Write.  Required permissions: Processes.Edit.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.release_retention_delete_by_id_with_http_info(key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int key: (required)
        :param int x_uipath_organization_unit_id: Folder/OrganizationUnit Id
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['key', 'x_uipath_organization_unit_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method release_retention_delete_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'key' is set
        if self.api_client.client_side_validation and ('key' not in params or
                                                       params['key'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `key` when calling `release_retention_delete_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'key' in params:
            path_params['key'] = params['key']  # noqa: E501

        query_params = []

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
            '/odata/ReleaseRetention({key})', 'DELETE',
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

    def release_retention_get(self, **kwargs):  # noqa: E501
        """release_retention_get  # noqa: E501

        OAuth required scopes: OR.Execution or OR.Execution.Read.  Required permissions: Processes.View.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.release_retention_get(async_req=True)
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
        :return: ODataValueOfIEnumerableOfReleaseRetentionSettingDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.release_retention_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.release_retention_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def release_retention_get_with_http_info(self, **kwargs):  # noqa: E501
        """release_retention_get  # noqa: E501

        OAuth required scopes: OR.Execution or OR.Execution.Read.  Required permissions: Processes.View.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.release_retention_get_with_http_info(async_req=True)
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
        :return: ODataValueOfIEnumerableOfReleaseRetentionSettingDto
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
                    " to method release_retention_get" % key
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
            '/odata/ReleaseRetention', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ODataValueOfIEnumerableOfReleaseRetentionSettingDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def release_retention_get_by_id(self, key, **kwargs):  # noqa: E501
        """release_retention_get_by_id  # noqa: E501

        OAuth required scopes: OR.Execution or OR.Execution.Read.  Required permissions: Processes.View.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.release_retention_get_by_id(key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int key: (required)
        :param str expand: Indicates the related entities to be represented inline. The maximum depth is 2.
        :param str select: Limits the properties returned in the result.
        :param int x_uipath_organization_unit_id: Folder/OrganizationUnit Id
        :return: ReleaseRetentionSettingDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.release_retention_get_by_id_with_http_info(key, **kwargs)  # noqa: E501
        else:
            (data) = self.release_retention_get_by_id_with_http_info(key, **kwargs)  # noqa: E501
            return data

    def release_retention_get_by_id_with_http_info(self, key, **kwargs):  # noqa: E501
        """release_retention_get_by_id  # noqa: E501

        OAuth required scopes: OR.Execution or OR.Execution.Read.  Required permissions: Processes.View.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.release_retention_get_by_id_with_http_info(key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int key: (required)
        :param str expand: Indicates the related entities to be represented inline. The maximum depth is 2.
        :param str select: Limits the properties returned in the result.
        :param int x_uipath_organization_unit_id: Folder/OrganizationUnit Id
        :return: ReleaseRetentionSettingDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['key', 'expand', 'select', 'x_uipath_organization_unit_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method release_retention_get_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'key' is set
        if self.api_client.client_side_validation and ('key' not in params or
                                                       params['key'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `key` when calling `release_retention_get_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'key' in params:
            path_params['key'] = params['key']  # noqa: E501

        query_params = []
        if 'expand' in params:
            query_params.append(('$expand', params['expand']))  # noqa: E501
        if 'select' in params:
            query_params.append(('$select', params['select']))  # noqa: E501

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
            '/odata/ReleaseRetention({key})', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReleaseRetentionSettingDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def release_retention_put_by_id(self, key, **kwargs):  # noqa: E501
        """release_retention_put_by_id  # noqa: E501

        OAuth required scopes: OR.Execution or OR.Execution.Write.  Required permissions: Processes.Edit.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.release_retention_put_by_id(key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int key: (required)
        :param ReleaseRetentionSettingDto body:
        :param int x_uipath_organization_unit_id: Folder/OrganizationUnit Id
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.release_retention_put_by_id_with_http_info(key, **kwargs)  # noqa: E501
        else:
            (data) = self.release_retention_put_by_id_with_http_info(key, **kwargs)  # noqa: E501
            return data

    def release_retention_put_by_id_with_http_info(self, key, **kwargs):  # noqa: E501
        """release_retention_put_by_id  # noqa: E501

        OAuth required scopes: OR.Execution or OR.Execution.Write.  Required permissions: Processes.Edit.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.release_retention_put_by_id_with_http_info(key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int key: (required)
        :param ReleaseRetentionSettingDto body:
        :param int x_uipath_organization_unit_id: Folder/OrganizationUnit Id
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['key', 'body', 'x_uipath_organization_unit_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method release_retention_put_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'key' is set
        if self.api_client.client_side_validation and ('key' not in params or
                                                       params['key'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `key` when calling `release_retention_put_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'key' in params:
            path_params['key'] = params['key']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_uipath_organization_unit_id' in params:
            header_params['X-UIPATH-OrganizationUnitId'] = params['x_uipath_organization_unit_id']  # noqa: E501

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
            '/odata/ReleaseRetention({key})', 'PUT',
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
