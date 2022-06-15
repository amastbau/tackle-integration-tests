# swagger_client.ListApi

All URIs are relative to *http://192.168.39.186/hub*

Method | HTTP request | Description
------------- | ------------- | -------------
[**application_inventory_application_import_get**](ListApi.md#application_inventory_application_import_get) | **GET** /application-inventory/application-import | List imports.
[**application_inventory_import_summary_get**](ListApi.md#application_inventory_import_summary_get) | **GET** /application-inventory/import-summary | List import summaries.
[**applications_get**](ListApi.md#applications_get) | **GET** /applications | List all applications.
[**businessservices_get**](ListApi.md#businessservices_get) | **GET** /businessservices | List all business services.
[**dependencies_get**](ListApi.md#dependencies_get) | **GET** /dependencies | List all dependencies.
[**settings_get**](ListApi.md#settings_get) | **GET** /settings | List all settings.


# **application_inventory_application_import_get**
> list[ApiImport] application_inventory_application_import_get()

List imports.

List imports.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearerAuth
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ListApi(swagger_client.ApiClient(configuration))

try:
    # List imports.
    api_response = api_instance.application_inventory_application_import_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListApi->application_inventory_application_import_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ApiImport]**](ApiImport.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_inventory_import_summary_get**
> list[ApiImportSummary] application_inventory_import_summary_get()

List import summaries.

List import summaries.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearerAuth
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ListApi(swagger_client.ApiClient(configuration))

try:
    # List import summaries.
    api_response = api_instance.application_inventory_import_summary_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListApi->application_inventory_import_summary_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ApiImportSummary]**](ApiImportSummary.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_get**
> list[ApiApplication] applications_get()

List all applications.

List all applications.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearerAuth
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ListApi(swagger_client.ApiClient(configuration))

try:
    # List all applications.
    api_response = api_instance.applications_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListApi->applications_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ApiApplication]**](ApiApplication.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **businessservices_get**
> ApiBusinessService businessservices_get()

List all business services.

List all business services.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearerAuth
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ListApi(swagger_client.ApiClient(configuration))

try:
    # List all business services.
    api_response = api_instance.businessservices_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListApi->businessservices_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiBusinessService**](ApiBusinessService.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dependencies_get**
> list[ApiDependency] dependencies_get()

List all dependencies.

List all dependencies.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearerAuth
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ListApi(swagger_client.ApiClient(configuration))

try:
    # List all dependencies.
    api_response = api_instance.dependencies_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListApi->dependencies_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ApiDependency]**](ApiDependency.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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

# Configure API key authorization: bearerAuth
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ListApi(swagger_client.ApiClient(configuration))

try:
    # List all settings.
    api_response = api_instance.settings_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListApi->settings_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ApiSetting]**](ApiSetting.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

