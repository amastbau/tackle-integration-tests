# swagger_client.SettingApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**settings_get**](SettingApi.md#settings_get) | **GET** /settings | List all settings.
[**settings_key_delete**](SettingApi.md#settings_key_delete) | **DELETE** /settings/{key} | Delete a setting.
[**settings_key_get**](SettingApi.md#settings_key_get) | **GET** /settings/{key} | Get a setting by its key.
[**settings_key_put**](SettingApi.md#settings_key_put) | **PUT** /settings/{key} | Update a setting.
[**settings_post**](SettingApi.md#settings_post) | **POST** /settings | Create a setting.


# **settings_get**
> list[ApiSetting] settings_get()

List all settings.

List all settings.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SettingApi()

try:
    # List all settings.
    api_response = api_instance.settings_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingApi->settings_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ApiSetting]**](ApiSetting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_key_delete**
> settings_key_delete(key)

Delete a setting.

Delete a setting.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SettingApi()
key = 'key_example' # str | Key

try:
    # Delete a setting.
    api_instance.settings_key_delete(key)
except ApiException as e:
    print("Exception when calling SettingApi->settings_key_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Key | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_key_get**
> object settings_key_get(key)

Get a setting by its key.

Get a setting by its key.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SettingApi()
key = 'key_example' # str | Key

try:
    # Get a setting by its key.
    api_response = api_instance.settings_key_get(key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingApi->settings_key_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Key | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_key_put**
> settings_key_put(key)

Update a setting.

Update a setting.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SettingApi()
key = 'key_example' # str | Key

try:
    # Update a setting.
    api_instance.settings_key_put(key)
except ApiException as e:
    print("Exception when calling SettingApi->settings_key_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Key | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_post**
> ApiSetting settings_post(setting)

Create a setting.

Create a setting.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SettingApi()
setting = swagger_client.ApiSetting() # ApiSetting | Setting data

try:
    # Create a setting.
    api_response = api_instance.settings_post(setting)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingApi->settings_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting** | [**ApiSetting**](ApiSetting.md)| Setting data | 

### Return type

[**ApiSetting**](ApiSetting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

