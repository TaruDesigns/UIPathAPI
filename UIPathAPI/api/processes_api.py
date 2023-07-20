# coding: utf-8

"""
    UiPath.WebApi 16.0

    Orchestrator API  # noqa: E501

    OpenAPI spec version: 16.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from UIPathAPI.api_client import ApiClient


class ProcessesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def processes_delete_by_id(self, key, **kwargs):  # noqa: E501
        """Deletes a package.  # noqa: E501

        OAuth required scopes: OR.Execution or OR.Execution.Write.  Required permissions: (Packages.Delete - Deletes a package in a Tenant Feed) and (FolderPackages.Delete - Deletes a package in a Folder Feed).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.processes_delete_by_id(key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str key:  (required)
        :param str feed_id: 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.processes_delete_by_id_with_http_info(key, **kwargs)  # noqa: E501
        else:
            (data) = self.processes_delete_by_id_with_http_info(key, **kwargs)  # noqa: E501
            return data

    def processes_delete_by_id_with_http_info(self, key, **kwargs):  # noqa: E501
        """Deletes a package.  # noqa: E501

        OAuth required scopes: OR.Execution or OR.Execution.Write.  Required permissions: (Packages.Delete - Deletes a package in a Tenant Feed) and (FolderPackages.Delete - Deletes a package in a Folder Feed).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.processes_delete_by_id_with_http_info(key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str key:  (required)
        :param str feed_id: 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['key', 'feed_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method processes_delete_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'key' is set
        if self.api_client.client_side_validation and ('key' not in params or
                                                       params['key'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `key` when calling `processes_delete_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'key' in params:
            path_params['key'] = params['key']  # noqa: E501

        query_params = []
        if 'feed_id' in params:
            query_params.append(('feedId', params['feed_id']))  # noqa: E501

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
            '/odata/Processes(\'{key}\')', 'DELETE',
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

    def processes_download_package_by_key(self, key, **kwargs):  # noqa: E501
        """Downloads the .nupkg file of a Package.  # noqa: E501

        OAuth required scopes: OR.Execution or OR.Execution.Read.  Required permissions: (Packages.View - Downloads a package from a Tenant Feed) and (FolderPackages.View - Downloads a package from a Folder Feed).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.processes_download_package_by_key(key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str key:  (required)
        :param str feed_id: 
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.processes_download_package_by_key_with_http_info(key, **kwargs)  # noqa: E501
        else:
            (data) = self.processes_download_package_by_key_with_http_info(key, **kwargs)  # noqa: E501
            return data

    def processes_download_package_by_key_with_http_info(self, key, **kwargs):  # noqa: E501
        """Downloads the .nupkg file of a Package.  # noqa: E501

        OAuth required scopes: OR.Execution or OR.Execution.Read.  Required permissions: (Packages.View - Downloads a package from a Tenant Feed) and (FolderPackages.View - Downloads a package from a Folder Feed).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.processes_download_package_by_key_with_http_info(key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str key:  (required)
        :param str feed_id: 
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['key', 'feed_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method processes_download_package_by_key" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'key' is set
        if self.api_client.client_side_validation and ('key' not in params or
                                                       params['key'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `key` when calling `processes_download_package_by_key`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'key' in params:
            path_params['key'] = params['key']  # noqa: E501

        query_params = []
        if 'feed_id' in params:
            query_params.append(('feedId', params['feed_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/odata/Processes/UiPath.Server.Configuration.OData.DownloadPackage(key=\'{key}\')', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def processes_get(self, **kwargs):  # noqa: E501
        """Gets the processes.  # noqa: E501

        OAuth required scopes: OR.Execution or OR.Execution.Read.  Required permissions: (Packages.View - Lists packages in a Tenant Feed) and (FolderPackages.View - Lists packages in a Folder Feed).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.processes_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_term: 
        :param str feed_id: 
        :param str expand: Indicates the related entities to be represented inline. The maximum depth is 2.
        :param str filter: Restricts the set of items returned. The maximum number of expressions is 100.
        :param str select: Limits the properties returned in the result.
        :param str orderby: Specifies the order in which items are returned. The maximum number of expressions is 5.
        :param int top: Limits the number of items returned from a collection. The maximum value is 1000.
        :param int skip: Excludes the specified number of items of the queried collection from the result.
        :param bool count: Indicates whether the total count of items within a collection are returned in the result.
        :return: ODataValueOfIEnumerableOfProcessDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.processes_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.processes_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def processes_get_with_http_info(self, **kwargs):  # noqa: E501
        """Gets the processes.  # noqa: E501

        OAuth required scopes: OR.Execution or OR.Execution.Read.  Required permissions: (Packages.View - Lists packages in a Tenant Feed) and (FolderPackages.View - Lists packages in a Folder Feed).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.processes_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_term: 
        :param str feed_id: 
        :param str expand: Indicates the related entities to be represented inline. The maximum depth is 2.
        :param str filter: Restricts the set of items returned. The maximum number of expressions is 100.
        :param str select: Limits the properties returned in the result.
        :param str orderby: Specifies the order in which items are returned. The maximum number of expressions is 5.
        :param int top: Limits the number of items returned from a collection. The maximum value is 1000.
        :param int skip: Excludes the specified number of items of the queried collection from the result.
        :param bool count: Indicates whether the total count of items within a collection are returned in the result.
        :return: ODataValueOfIEnumerableOfProcessDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['search_term', 'feed_id', 'expand', 'filter', 'select', 'orderby', 'top', 'skip', 'count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method processes_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'search_term' in params:
            query_params.append(('searchTerm', params['search_term']))  # noqa: E501
        if 'feed_id' in params:
            query_params.append(('feedId', params['feed_id']))  # noqa: E501
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
            '/odata/Processes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ODataValueOfIEnumerableOfProcessDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def processes_get_arguments_by_key(self, key, **kwargs):  # noqa: E501
        """Get process parameters  # noqa: E501

        OAuth required scopes: OR.Execution or OR.Execution.Read.  Required permissions: Packages.View.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.processes_get_arguments_by_key(key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str key:  (required)
        :param str expand: Indicates the related entities to be represented inline. The maximum depth is 2.
        :param str select: Limits the properties returned in the result.
        :return: ArgumentMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.processes_get_arguments_by_key_with_http_info(key, **kwargs)  # noqa: E501
        else:
            (data) = self.processes_get_arguments_by_key_with_http_info(key, **kwargs)  # noqa: E501
            return data

    def processes_get_arguments_by_key_with_http_info(self, key, **kwargs):  # noqa: E501
        """Get process parameters  # noqa: E501

        OAuth required scopes: OR.Execution or OR.Execution.Read.  Required permissions: Packages.View.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.processes_get_arguments_by_key_with_http_info(key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str key:  (required)
        :param str expand: Indicates the related entities to be represented inline. The maximum depth is 2.
        :param str select: Limits the properties returned in the result.
        :return: ArgumentMetadata
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['key', 'expand', 'select']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method processes_get_arguments_by_key" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'key' is set
        if self.api_client.client_side_validation and ('key' not in params or
                                                       params['key'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `key` when calling `processes_get_arguments_by_key`")  # noqa: E501

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

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/odata/Processes/UiPath.Server.Configuration.OData.GetArguments(key=\'{key}\')', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ArgumentMetadata',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def processes_get_process_versions_by_processid(self, process_id, **kwargs):  # noqa: E501
        """Returns a collection of all available versions of a given process. Allows odata query options.  # noqa: E501

        OAuth required scopes: OR.Execution or OR.Execution.Read.  Required permissions: (Packages.View - Lists versions of a package in a Tenant Feed) and (FolderPackages.View - Lists versions of a package in a Folder Feed).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.processes_get_process_versions_by_processid(process_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str process_id: The Id of the process for which the versions are fetched. (required)
        :param str feed_id: 
        :param str expand: Indicates the related entities to be represented inline. The maximum depth is 2.
        :param str filter: Restricts the set of items returned. The maximum number of expressions is 100.
        :param str select: Limits the properties returned in the result.
        :param str orderby: Specifies the order in which items are returned. The maximum number of expressions is 5.
        :param int top: Limits the number of items returned from a collection. The maximum value is 1000.
        :param int skip: Excludes the specified number of items of the queried collection from the result.
        :param bool count: Indicates whether the total count of items within a collection are returned in the result.
        :return: ODataValueOfIEnumerableOfProcessDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.processes_get_process_versions_by_processid_with_http_info(process_id, **kwargs)  # noqa: E501
        else:
            (data) = self.processes_get_process_versions_by_processid_with_http_info(process_id, **kwargs)  # noqa: E501
            return data

    def processes_get_process_versions_by_processid_with_http_info(self, process_id, **kwargs):  # noqa: E501
        """Returns a collection of all available versions of a given process. Allows odata query options.  # noqa: E501

        OAuth required scopes: OR.Execution or OR.Execution.Read.  Required permissions: (Packages.View - Lists versions of a package in a Tenant Feed) and (FolderPackages.View - Lists versions of a package in a Folder Feed).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.processes_get_process_versions_by_processid_with_http_info(process_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str process_id: The Id of the process for which the versions are fetched. (required)
        :param str feed_id: 
        :param str expand: Indicates the related entities to be represented inline. The maximum depth is 2.
        :param str filter: Restricts the set of items returned. The maximum number of expressions is 100.
        :param str select: Limits the properties returned in the result.
        :param str orderby: Specifies the order in which items are returned. The maximum number of expressions is 5.
        :param int top: Limits the number of items returned from a collection. The maximum value is 1000.
        :param int skip: Excludes the specified number of items of the queried collection from the result.
        :param bool count: Indicates whether the total count of items within a collection are returned in the result.
        :return: ODataValueOfIEnumerableOfProcessDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['process_id', 'feed_id', 'expand', 'filter', 'select', 'orderby', 'top', 'skip', 'count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method processes_get_process_versions_by_processid" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'process_id' is set
        if self.api_client.client_side_validation and ('process_id' not in params or
                                                       params['process_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `process_id` when calling `processes_get_process_versions_by_processid`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'process_id' in params:
            path_params['processId'] = params['process_id']  # noqa: E501

        query_params = []
        if 'feed_id' in params:
            query_params.append(('feedId', params['feed_id']))  # noqa: E501
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
            '/odata/Processes/UiPath.Server.Configuration.OData.GetProcessVersions(processId=\'{processId}\')', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ODataValueOfIEnumerableOfProcessDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def processes_set_arguments(self, **kwargs):  # noqa: E501
        """Saves process arguments  # noqa: E501

        OAuth required scopes: OR.Execution or OR.Execution.Write.  Required permissions: Packages.Edit.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.processes_set_arguments(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProcessesSetArgumentsRequest body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.processes_set_arguments_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.processes_set_arguments_with_http_info(**kwargs)  # noqa: E501
            return data

    def processes_set_arguments_with_http_info(self, **kwargs):  # noqa: E501
        """Saves process arguments  # noqa: E501

        OAuth required scopes: OR.Execution or OR.Execution.Write.  Required permissions: Packages.Edit.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.processes_set_arguments_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProcessesSetArgumentsRequest body:
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
                    " to method processes_set_arguments" % key
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
            '/odata/Processes/UiPath.Server.Configuration.OData.SetArguments', 'POST',
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

    def processes_upload_package(self, file, **kwargs):  # noqa: E501
        """Uploads a new package or a new version of an existing package. The content of the package is sent as a .nupkg file embedded in the HTTP request.  # noqa: E501

        OAuth required scopes: OR.Execution or OR.Execution.Write.  Required permissions: (Packages.Create - Uploads a package in a Tenant Feed) and (FolderPackages.Create - Uploads a package in a Folder Feed).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.processes_upload_package(file, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file file: (required)
        :param str feed_id:
        :param str expand: Indicates the related entities to be represented inline. The maximum depth is 2.
        :param str filter: Restricts the set of items returned. The maximum number of expressions is 100.
        :param str select: Limits the properties returned in the result.
        :param str orderby: Specifies the order in which items are returned. The maximum number of expressions is 5.
        :param bool count: Indicates whether the total count of items within a collection are returned in the result.
        :param file file1:
        :param file file2:
        :param file file3:
        :param file file4:
        :param file file5:
        :param file file6:
        :param file file7:
        :param file file8:
        :param file file9:
        :return: ODataValueOfIEnumerableOfBulkItemDtoOfString
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.processes_upload_package_with_http_info(file, **kwargs)  # noqa: E501
        else:
            (data) = self.processes_upload_package_with_http_info(file, **kwargs)  # noqa: E501
            return data

    def processes_upload_package_with_http_info(self, file, **kwargs):  # noqa: E501
        """Uploads a new package or a new version of an existing package. The content of the package is sent as a .nupkg file embedded in the HTTP request.  # noqa: E501

        OAuth required scopes: OR.Execution or OR.Execution.Write.  Required permissions: (Packages.Create - Uploads a package in a Tenant Feed) and (FolderPackages.Create - Uploads a package in a Folder Feed).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.processes_upload_package_with_http_info(file, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file file: (required)
        :param str feed_id:
        :param str expand: Indicates the related entities to be represented inline. The maximum depth is 2.
        :param str filter: Restricts the set of items returned. The maximum number of expressions is 100.
        :param str select: Limits the properties returned in the result.
        :param str orderby: Specifies the order in which items are returned. The maximum number of expressions is 5.
        :param bool count: Indicates whether the total count of items within a collection are returned in the result.
        :param file file1:
        :param file file2:
        :param file file3:
        :param file file4:
        :param file file5:
        :param file file6:
        :param file file7:
        :param file file8:
        :param file file9:
        :return: ODataValueOfIEnumerableOfBulkItemDtoOfString
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file', 'feed_id', 'expand', 'filter', 'select', 'orderby', 'count', 'file1', 'file2', 'file3', 'file4', 'file5', 'file6', 'file7', 'file8', 'file9']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method processes_upload_package" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file' is set
        if self.api_client.client_side_validation and ('file' not in params or
                                                       params['file'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `file` when calling `processes_upload_package`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'feed_id' in params:
            query_params.append(('feedId', params['feed_id']))  # noqa: E501
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

        form_params = []
        local_var_files = {}
        if 'file1' in params:
            local_var_files['file1'] = params['file1']  # noqa: E501
        if 'file2' in params:
            local_var_files['file2'] = params['file2']  # noqa: E501
        if 'file3' in params:
            local_var_files['file3'] = params['file3']  # noqa: E501
        if 'file4' in params:
            local_var_files['file4'] = params['file4']  # noqa: E501
        if 'file5' in params:
            local_var_files['file5'] = params['file5']  # noqa: E501
        if 'file6' in params:
            local_var_files['file6'] = params['file6']  # noqa: E501
        if 'file7' in params:
            local_var_files['file7'] = params['file7']  # noqa: E501
        if 'file8' in params:
            local_var_files['file8'] = params['file8']  # noqa: E501
        if 'file9' in params:
            local_var_files['file9'] = params['file9']  # noqa: E501
        if 'file' in params:
            local_var_files['file'] = params['file']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/odata/Processes/UiPath.Server.Configuration.OData.UploadPackage', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ODataValueOfIEnumerableOfBulkItemDtoOfString',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
