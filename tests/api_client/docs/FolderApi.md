# swagger_client.FolderApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_folder_id_view**](FolderApi.md#delete_folder_id_view) | **DELETE** /folder/{id} | 
[**get_folder_view**](FolderApi.md#get_folder_view) | **GET** /folder | 
[**post_folder_view**](FolderApi.md#post_folder_view) | **POST** /folder | 
[**put_folder_id_view**](FolderApi.md#put_folder_id_view) | **PUT** /folder/{id} | 


# **delete_folder_id_view**
> delete_folder_id_view(id)



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
api_instance = swagger_client.FolderApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    api_instance.delete_folder_id_view(id)
except ApiException as e:
    print("Exception when calling FolderApi->delete_folder_id_view: %s\n" % e)
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

# **get_folder_view**
> list[Folder] get_folder_view(x_fields=x_fields)



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
api_instance = swagger_client.FolderApi(swagger_client.ApiClient(configuration))
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_folder_view(x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FolderApi->get_folder_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**list[Folder]**](Folder.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_folder_view**
> Folder post_folder_view(payload, x_fields=x_fields)



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
api_instance = swagger_client.FolderApi(swagger_client.ApiClient(configuration))
payload = swagger_client.FolderPost() # FolderPost | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.post_folder_view(payload, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FolderApi->post_folder_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**FolderPost**](FolderPost.md)|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**Folder**](Folder.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_folder_id_view**
> Folder put_folder_id_view(id, payload, x_fields=x_fields)



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
api_instance = swagger_client.FolderApi(swagger_client.ApiClient(configuration))
id = 56 # int | 
payload = swagger_client.FolderPost() # FolderPost | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.put_folder_id_view(id, payload, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FolderApi->put_folder_id_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **payload** | [**FolderPost**](FolderPost.md)|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**Folder**](Folder.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

