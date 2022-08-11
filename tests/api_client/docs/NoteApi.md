# swagger_client.NoteApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_note_id_view**](NoteApi.md#delete_note_id_view) | **DELETE** /note/{id} | 
[**get_note_view**](NoteApi.md#get_note_view) | **GET** /note | 
[**post_folder_note_view**](NoteApi.md#post_folder_note_view) | **POST** /folder/{folder_id}/note | 
[**put_note_id_view**](NoteApi.md#put_note_id_view) | **PUT** /note/{id} | 


# **delete_note_id_view**
> delete_note_id_view(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.NoteApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    api_instance.delete_note_id_view(id)
except ApiException as e:
    print("Exception when calling NoteApi->delete_note_id_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_note_view**
> NotePaging get_note_view(perpage=perpage, page=page, sortdesc=sortdesc, sort=sort, notetext=notetext, ispublic=ispublic, folderid=folderid, x_fields=x_fields)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.NoteApi(swagger_client.ApiClient(configuration))
perpage = 56 # int | Show specific number of items per page. (optional)
page = 56 # int | Show specific page. (optional)
sortdesc = 'sortdesc_example' # str | Turn on descending order. (optional)
sort = 'sort_example' # str | Sort by possible options [shared, heading] (optional)
notetext = 'notetext_example' # str | Search for text in notes. (optional)
ispublic = 'ispublic_example' # str | Public or private visibility [true, false]         When not specified user can see all of his notes, either private         or public. (optional)
folderid = 56 # int | Filter by specific folder. (optional)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_note_view(perpage=perpage, page=page, sortdesc=sortdesc, sort=sort, notetext=notetext, ispublic=ispublic, folderid=folderid, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NoteApi->get_note_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **perpage** | **int**| Show specific number of items per page. | [optional] 
 **page** | **int**| Show specific page. | [optional] 
 **sortdesc** | **str**| Turn on descending order. | [optional] 
 **sort** | **str**| Sort by possible options [shared, heading] | [optional] 
 **notetext** | **str**| Search for text in notes. | [optional] 
 **ispublic** | **str**| Public or private visibility [true, false]         When not specified user can see all of his notes, either private         or public. | [optional] 
 **folderid** | **int**| Filter by specific folder. | [optional] 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**NotePaging**](NotePaging.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_folder_note_view**
> Note post_folder_note_view(folder_id, payload, x_fields=x_fields)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.NoteApi(swagger_client.ApiClient(configuration))
folder_id = 56 # int | 
payload = swagger_client.NotePost() # NotePost | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.post_folder_note_view(folder_id, payload, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NoteApi->post_folder_note_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **int**|  | 
 **payload** | [**NotePost**](NotePost.md)|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**Note**](Note.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_note_id_view**
> Note put_note_id_view(id, payload, x_fields=x_fields)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.NoteApi(swagger_client.ApiClient(configuration))
id = 56 # int | 
payload = swagger_client.Note() # Note | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.put_note_id_view(id, payload, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NoteApi->put_note_id_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **payload** | [**Note**](Note.md)|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**Note**](Note.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

