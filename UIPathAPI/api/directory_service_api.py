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


class DirectoryServiceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def directory_service_get_directory_permissions(self, **kwargs):  # noqa: E501
        """Gets directory permissions  # noqa: E501

        OAuth required scopes: OR.Users or OR.Users.Read.  Required permissions: Users.View.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.directory_service_get_directory_permissions(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str username:
        :param str domain:
        :return: list[DirectoryPermissionDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.directory_service_get_directory_permissions_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.directory_service_get_directory_permissions_with_http_info(**kwargs)  # noqa: E501
            return data

    def directory_service_get_directory_permissions_with_http_info(self, **kwargs):  # noqa: E501
        """Gets directory permissions  # noqa: E501

        OAuth required scopes: OR.Users or OR.Users.Read.  Required permissions: Users.View.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.directory_service_get_directory_permissions_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str username:
        :param str domain:
        :return: list[DirectoryPermissionDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['username', 'domain']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method directory_service_get_directory_permissions" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'username' in params:
            query_params.append(('username', params['username']))  # noqa: E501
        if 'domain' in params:
            query_params.append(('domain', params['domain']))  # noqa: E501

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
            '/api/DirectoryService/GetDirectoryPermissions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[DirectoryPermissionDto]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def directory_service_get_domains(self, **kwargs):  # noqa: E501
        """Gets domains  # noqa: E501

        OAuth required scopes: OR.Users or OR.Users.Read.  Required permissions: (Users.View or Units.Edit or SubFolders.Edit).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.directory_service_get_domains(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[DomainDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.directory_service_get_domains_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.directory_service_get_domains_with_http_info(**kwargs)  # noqa: E501
            return data

    def directory_service_get_domains_with_http_info(self, **kwargs):  # noqa: E501
        """Gets domains  # noqa: E501

        OAuth required scopes: OR.Users or OR.Users.Read.  Required permissions: (Users.View or Units.Edit or SubFolders.Edit).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.directory_service_get_domains_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[DomainDto]
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
                    " to method directory_service_get_domains" % key
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
            '/api/DirectoryService/GetDomains', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[DomainDto]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def directory_service_search_for_users_and_groups(self, **kwargs):  # noqa: E501
        """Search users and groups  # noqa: E501

        OAuth required scopes: OR.Users or OR.Users.Read.  Required permissions: (Users.View or Units.Edit or SubFolders.Edit).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.directory_service_search_for_users_and_groups(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_context: 
        :param str domain: 
        :param str prefix: 
        :return: list[DirectoryObjectDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.directory_service_search_for_users_and_groups_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.directory_service_search_for_users_and_groups_with_http_info(**kwargs)  # noqa: E501
            return data

    def directory_service_search_for_users_and_groups_with_http_info(self, **kwargs):  # noqa: E501
        """Search users and groups  # noqa: E501

        OAuth required scopes: OR.Users or OR.Users.Read.  Required permissions: (Users.View or Units.Edit or SubFolders.Edit).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.directory_service_search_for_users_and_groups_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_context: 
        :param str domain: 
        :param str prefix: 
        :return: list[DirectoryObjectDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['search_context', 'domain', 'prefix']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method directory_service_search_for_users_and_groups" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'search_context' in params:
            query_params.append(('searchContext', params['search_context']))  # noqa: E501
        if 'domain' in params:
            query_params.append(('domain', params['domain']))  # noqa: E501
        if 'prefix' in params:
            query_params.append(('prefix', params['prefix']))  # noqa: E501

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
            '/api/DirectoryService/SearchForUsersAndGroups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[DirectoryObjectDto]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)