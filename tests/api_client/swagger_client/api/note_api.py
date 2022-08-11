# coding: utf-8

"""
    Notes API

    Manage your notes in a simple way.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class NoteApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_note_id_view(self, id, **kwargs):  # noqa: E501
        """delete_note_id_view  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_note_id_view(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_note_id_view_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_note_id_view_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def delete_note_id_view_with_http_info(self, id, **kwargs):  # noqa: E501
        """delete_note_id_view  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_note_id_view_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_note_id_view" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `delete_note_id_view`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic_auth']  # noqa: E501

        return self.api_client.call_api(
            '/note/{id}', 'DELETE',
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

    def get_note_view(self, **kwargs):  # noqa: E501
        """get_note_view  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_note_view(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int perpage: Show specific number of items per page.
        :param int page: Show specific page.
        :param str sortdesc: Turn on descending order.
        :param str sort: Sort by possible options [shared, heading]
        :param str notetext: Search for text in notes.
        :param str ispublic: Public or private visibility [true, false]         When not specified user can see all of his notes, either private         or public.
        :param int folderid: Filter by specific folder.
        :param str x_fields: An optional fields mask
        :return: NotePaging
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_note_view_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_note_view_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_note_view_with_http_info(self, **kwargs):  # noqa: E501
        """get_note_view  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_note_view_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int perpage: Show specific number of items per page.
        :param int page: Show specific page.
        :param str sortdesc: Turn on descending order.
        :param str sort: Sort by possible options [shared, heading]
        :param str notetext: Search for text in notes.
        :param str ispublic: Public or private visibility [true, false]         When not specified user can see all of his notes, either private         or public.
        :param int folderid: Filter by specific folder.
        :param str x_fields: An optional fields mask
        :return: NotePaging
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['perpage', 'page', 'sortdesc', 'sort', 'notetext', 'ispublic', 'folderid', 'x_fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_note_view" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'perpage' in params:
            query_params.append(('perpage', params['perpage']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'sortdesc' in params:
            query_params.append(('sortdesc', params['sortdesc']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'notetext' in params:
            query_params.append(('notetext', params['notetext']))  # noqa: E501
        if 'ispublic' in params:
            query_params.append(('ispublic', params['ispublic']))  # noqa: E501
        if 'folderid' in params:
            query_params.append(('folderid', params['folderid']))  # noqa: E501

        header_params = {}
        if 'x_fields' in params:
            header_params['X-Fields'] = params['x_fields']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic_auth']  # noqa: E501

        return self.api_client.call_api(
            '/note', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NotePaging',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_folder_note_view(self, folder_id, payload, **kwargs):  # noqa: E501
        """post_folder_note_view  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_folder_note_view(folder_id, payload, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int folder_id: (required)
        :param NotePost payload: (required)
        :param str x_fields: An optional fields mask
        :return: Note
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_folder_note_view_with_http_info(folder_id, payload, **kwargs)  # noqa: E501
        else:
            (data) = self.post_folder_note_view_with_http_info(folder_id, payload, **kwargs)  # noqa: E501
            return data

    def post_folder_note_view_with_http_info(self, folder_id, payload, **kwargs):  # noqa: E501
        """post_folder_note_view  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_folder_note_view_with_http_info(folder_id, payload, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int folder_id: (required)
        :param NotePost payload: (required)
        :param str x_fields: An optional fields mask
        :return: Note
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['folder_id', 'payload', 'x_fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_folder_note_view" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'folder_id' is set
        if self.api_client.client_side_validation and ('folder_id' not in params or
                                                       params['folder_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `folder_id` when calling `post_folder_note_view`")  # noqa: E501
        # verify the required parameter 'payload' is set
        if self.api_client.client_side_validation and ('payload' not in params or
                                                       params['payload'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `payload` when calling `post_folder_note_view`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'folder_id' in params:
            path_params['folder_id'] = params['folder_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_fields' in params:
            header_params['X-Fields'] = params['x_fields']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'payload' in params:
            body_params = params['payload']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic_auth']  # noqa: E501

        return self.api_client.call_api(
            '/folder/{folder_id}/note', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Note',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_note_id_view(self, id, payload, **kwargs):  # noqa: E501
        """put_note_id_view  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_note_id_view(id, payload, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :param Note payload: (required)
        :param str x_fields: An optional fields mask
        :return: Note
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.put_note_id_view_with_http_info(id, payload, **kwargs)  # noqa: E501
        else:
            (data) = self.put_note_id_view_with_http_info(id, payload, **kwargs)  # noqa: E501
            return data

    def put_note_id_view_with_http_info(self, id, payload, **kwargs):  # noqa: E501
        """put_note_id_view  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_note_id_view_with_http_info(id, payload, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :param Note payload: (required)
        :param str x_fields: An optional fields mask
        :return: Note
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'payload', 'x_fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_note_id_view" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `put_note_id_view`")  # noqa: E501
        # verify the required parameter 'payload' is set
        if self.api_client.client_side_validation and ('payload' not in params or
                                                       params['payload'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `payload` when calling `put_note_id_view`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_fields' in params:
            header_params['X-Fields'] = params['x_fields']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'payload' in params:
            body_params = params['payload']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic_auth']  # noqa: E501

        return self.api_client.call_api(
            '/note/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Note',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
