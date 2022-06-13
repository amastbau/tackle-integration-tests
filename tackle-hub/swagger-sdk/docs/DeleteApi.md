# swagger_client.DeleteApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**application_inventory_application_import_id_delete**](DeleteApi.md#application_inventory_application_import_id_delete) | **DELETE** /application-inventory/application-import/{id} | Delete an import.
[**application_inventory_import_summary_id_delete**](DeleteApi.md#application_inventory_import_summary_id_delete) | **DELETE** /application-inventory/import-summary/{id} | Delete an import summary and associated import records.
[**applications_id_delete**](DeleteApi.md#applications_id_delete) | **DELETE** /applications/{id} | Delete an application.
[**businessservices_id_delete**](DeleteApi.md#businessservices_id_delete) | **DELETE** /businessservices/{id} | Delete a business service.
[**dependencies_id_delete**](DeleteApi.md#dependencies_id_delete) | **DELETE** /dependencies/{id} | Delete a dependency.
[**identities_id_delete**](DeleteApi.md#identities_id_delete) | **DELETE** /identities/{id} | Delete an identity.
[**jobfunctions_id_delete**](DeleteApi.md#jobfunctions_id_delete) | **DELETE** /jobfunctions/{id} | Delete a job function.
[**proxies_id_delete**](DeleteApi.md#proxies_id_delete) | **DELETE** /proxies/{id} | Delete an proxy.
[**reviews_id_delete**](DeleteApi.md#reviews_id_delete) | **DELETE** /reviews/{id} | Delete a review.
[**settings_key_delete**](DeleteApi.md#settings_key_delete) | **DELETE** /settings/{key} | Delete a setting.
[**stakeholdergroups_id_delete**](DeleteApi.md#stakeholdergroups_id_delete) | **DELETE** /stakeholdergroups/{id} | Delete a stakeholder group.
[**stakeholders_id_delete**](DeleteApi.md#stakeholders_id_delete) | **DELETE** /stakeholders/{id} | Delete a stakeholder.
[**tags_id_delete**](DeleteApi.md#tags_id_delete) | **DELETE** /tags/{id} | Delete a tag.
[**tagtypes_id_delete**](DeleteApi.md#tagtypes_id_delete) | **DELETE** /tagtypes/{id} | Delete a tag type.
[**taskgroups_id_delete**](DeleteApi.md#taskgroups_id_delete) | **DELETE** /taskgroups/{id} | Delete a task group.
[**tasks_id_delete**](DeleteApi.md#tasks_id_delete) | **DELETE** /tasks/{id} | Delete a task.


# **application_inventory_application_import_id_delete**
> application_inventory_application_import_id_delete(id)

Delete an import.

Delete an import. This leaves any created application or dependency.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeleteApi()
id = 'id_example' # str | Import ID

try:
    # Delete an import.
    api_instance.application_inventory_application_import_id_delete(id)
except ApiException as e:
    print("Exception when calling DeleteApi->application_inventory_application_import_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Import ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_inventory_import_summary_id_delete**
> application_inventory_import_summary_id_delete(id)

Delete an import summary and associated import records.

Delete an import summary and associated import records.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeleteApi()
id = 'id_example' # str | ImportSummary ID

try:
    # Delete an import summary and associated import records.
    api_instance.application_inventory_import_summary_id_delete(id)
except ApiException as e:
    print("Exception when calling DeleteApi->application_inventory_import_summary_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ImportSummary ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_id_delete**
> applications_id_delete(id)

Delete an application.

Delete an application.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeleteApi()
id = 56 # int | Application id

try:
    # Delete an application.
    api_instance.applications_id_delete(id)
except ApiException as e:
    print("Exception when calling DeleteApi->applications_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Application id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **businessservices_id_delete**
> businessservices_id_delete(id)

Delete a business service.

Delete a business service.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeleteApi()
id = 'id_example' # str | Business service ID

try:
    # Delete a business service.
    api_instance.businessservices_id_delete(id)
except ApiException as e:
    print("Exception when calling DeleteApi->businessservices_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Business service ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dependencies_id_delete**
> dependencies_id_delete(id)

Delete a dependency.

Delete a dependency.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeleteApi()
id = 'id_example' # str | Dependency id

try:
    # Delete a dependency.
    api_instance.dependencies_id_delete(id)
except ApiException as e:
    print("Exception when calling DeleteApi->dependencies_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Dependency id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **identities_id_delete**
> identities_id_delete(id)

Delete an identity.

Delete an identity.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeleteApi()
id = 'id_example' # str | Identity ID

try:
    # Delete an identity.
    api_instance.identities_id_delete(id)
except ApiException as e:
    print("Exception when calling DeleteApi->identities_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identity ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobfunctions_id_delete**
> jobfunctions_id_delete(id)

Delete a job function.

Delete a job function.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeleteApi()
id = 'id_example' # str | Job Function ID

try:
    # Delete a job function.
    api_instance.jobfunctions_id_delete(id)
except ApiException as e:
    print("Exception when calling DeleteApi->jobfunctions_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Job Function ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxies_id_delete**
> proxies_id_delete(id)

Delete an proxy.

Delete an proxy.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeleteApi()
id = 'id_example' # str | Proxy ID

try:
    # Delete an proxy.
    api_instance.proxies_id_delete(id)
except ApiException as e:
    print("Exception when calling DeleteApi->proxies_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Proxy ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reviews_id_delete**
> reviews_id_delete(id)

Delete a review.

Delete a review.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeleteApi()
id = 'id_example' # str | Review ID

try:
    # Delete a review.
    api_instance.reviews_id_delete(id)
except ApiException as e:
    print("Exception when calling DeleteApi->reviews_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Review ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

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
api_instance = swagger_client.DeleteApi()
key = 'key_example' # str | Key

try:
    # Delete a setting.
    api_instance.settings_key_delete(key)
except ApiException as e:
    print("Exception when calling DeleteApi->settings_key_delete: %s\n" % e)
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

# **stakeholdergroups_id_delete**
> stakeholdergroups_id_delete(id)

Delete a stakeholder group.

Delete a stakeholder group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeleteApi()
id = 'id_example' # str | Stakeholder Group ID

try:
    # Delete a stakeholder group.
    api_instance.stakeholdergroups_id_delete(id)
except ApiException as e:
    print("Exception when calling DeleteApi->stakeholdergroups_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Stakeholder Group ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stakeholders_id_delete**
> stakeholders_id_delete(id)

Delete a stakeholder.

Delete a stakeholder.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeleteApi()
id = 'id_example' # str | Stakeholder ID

try:
    # Delete a stakeholder.
    api_instance.stakeholders_id_delete(id)
except ApiException as e:
    print("Exception when calling DeleteApi->stakeholders_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Stakeholder ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_id_delete**
> tags_id_delete(id)

Delete a tag.

Delete a tag.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeleteApi()
id = 'id_example' # str | Tag ID

try:
    # Delete a tag.
    api_instance.tags_id_delete(id)
except ApiException as e:
    print("Exception when calling DeleteApi->tags_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tag ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tagtypes_id_delete**
> tagtypes_id_delete(id)

Delete a tag type.

Delete a tag type.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeleteApi()
id = 'id_example' # str | Tag Type ID

try:
    # Delete a tag type.
    api_instance.tagtypes_id_delete(id)
except ApiException as e:
    print("Exception when calling DeleteApi->tagtypes_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tag Type ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **taskgroups_id_delete**
> taskgroups_id_delete(id)

Delete a task group.

Delete a task group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeleteApi()
id = 'id_example' # str | TaskGroup ID

try:
    # Delete a task group.
    api_instance.taskgroups_id_delete(id)
except ApiException as e:
    print("Exception when calling DeleteApi->taskgroups_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TaskGroup ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_id_delete**
> tasks_id_delete(id)

Delete a task.

Delete a task.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeleteApi()
id = 'id_example' # str | Task ID

try:
    # Delete a task.
    api_instance.tasks_id_delete(id)
except ApiException as e:
    print("Exception when calling DeleteApi->tasks_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Task ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

