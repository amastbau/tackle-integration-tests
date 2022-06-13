# swagger_client.GetApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addons_get**](GetApi.md#addons_get) | **GET** /addons | List all addons.
[**addons_name_get**](GetApi.md#addons_name_get) | **GET** /addons/{name} | Get an addon by name.
[**application_inventory_application_id_identities_get**](GetApi.md#application_inventory_application_id_identities_get) | **GET** /application-inventory/application/{id}/identities | List identities for an application.
[**application_inventory_application_import_id_get**](GetApi.md#application_inventory_application_import_id_get) | **GET** /application-inventory/application-import/{id} | Get an import by ID.
[**application_inventory_import_summary_id_get**](GetApi.md#application_inventory_import_summary_id_get) | **GET** /application-inventory/import-summary/{id} | Get an import summary by ID.
[**applications_id_get**](GetApi.md#applications_id_get) | **GET** /applications/{id} | Get an application by ID.
[**applications_id_tasks_id_content_wildcard_get**](GetApi.md#applications_id_tasks_id_content_wildcard_get) | **GET** /applications/{id}/tasks/{id}/content/{wildcard} | Get bucket content by ID and path.
[**bucket_id_content_wildcard_post**](GetApi.md#bucket_id_content_wildcard_post) | **POST** /bucket/{id}/content/{wildcard} | Upload bucket content by task ID and path.
[**businessservices_id_get**](GetApi.md#businessservices_id_get) | **GET** /businessservices/{id} | Get a business service by ID.
[**dependencies_id_get**](GetApi.md#dependencies_id_get) | **GET** /dependencies/{id} | Get a dependency by ID.
[**identities_get**](GetApi.md#identities_get) | **GET** /identities | List all identities.
[**identities_id_get**](GetApi.md#identities_id_get) | **GET** /identities/{id} | Get an identity by ID.
[**jobfunctions_get**](GetApi.md#jobfunctions_get) | **GET** /jobfunctions | List all job functions.
[**jobfunctions_id_get**](GetApi.md#jobfunctions_id_get) | **GET** /jobfunctions/{id} | Get a job function by ID.
[**proxies_get**](GetApi.md#proxies_get) | **GET** /proxies | List all proxies.
[**proxies_id_get**](GetApi.md#proxies_id_get) | **GET** /proxies/{id} | Get an proxy by ID.
[**reviews_get**](GetApi.md#reviews_get) | **GET** /reviews | List all reviews.
[**reviews_id_get**](GetApi.md#reviews_id_get) | **GET** /reviews/{id} | Get a review by ID.
[**settings_key_get**](GetApi.md#settings_key_get) | **GET** /settings/{key} | Get a setting by its key.
[**stakeholdergroups_get**](GetApi.md#stakeholdergroups_get) | **GET** /stakeholdergroups | List all stakeholder groups.
[**stakeholdergroups_id_get**](GetApi.md#stakeholdergroups_id_get) | **GET** /stakeholdergroups/{id} | Get a stakeholder group by ID.
[**stakeholders_get**](GetApi.md#stakeholders_get) | **GET** /stakeholders | List all stakeholders.
[**stakeholders_id_get**](GetApi.md#stakeholders_id_get) | **GET** /stakeholders/{id} | Get a stakeholder by ID.
[**tags_get**](GetApi.md#tags_get) | **GET** /tags | List all tags.
[**tags_id_get**](GetApi.md#tags_id_get) | **GET** /tags/{id} | Get a tag by ID.
[**tagtypes_get**](GetApi.md#tagtypes_get) | **GET** /tagtypes | List all tag types.
[**tagtypes_id_get**](GetApi.md#tagtypes_id_get) | **GET** /tagtypes/{id} | Get a tag type by ID.
[**taskgroups_get**](GetApi.md#taskgroups_get) | **GET** /taskgroups | List all task groups.
[**taskgroups_id_bucket_wildcard_get**](GetApi.md#taskgroups_id_bucket_wildcard_get) | **GET** /taskgroups/{id}/bucket/{wildcard} | Get bucket content by ID and path.
[**taskgroups_id_get**](GetApi.md#taskgroups_id_get) | **GET** /taskgroups/{id} | Get a task group by ID.
[**tasks_get**](GetApi.md#tasks_get) | **GET** /tasks | List all tasks.
[**tasks_id_bucket_wildcard_get**](GetApi.md#tasks_id_bucket_wildcard_get) | **GET** /tasks/{id}/bucket/{wildcard} | Get bucket content by ID and path.
[**tasks_id_bucket_wildcard_post**](GetApi.md#tasks_id_bucket_wildcard_post) | **POST** /tasks/{id}/bucket/{wildcard} | Upload bucket content by task ID and path.
[**tasks_id_get**](GetApi.md#tasks_id_get) | **GET** /tasks/{id} | Get a task by ID.


# **addons_get**
> list[ApiAddon] addons_get()

List all addons.

List all addons.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetApi()

try:
    # List all addons.
    api_response = api_instance.addons_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetApi->addons_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ApiAddon]**](ApiAddon.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addons_name_get**
> ApiAddon addons_name_get(name)

Get an addon by name.

Get an addon by name.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetApi()
name = 'name_example' # str | Addon name

try:
    # Get an addon by name.
    api_response = api_instance.addons_name_get(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetApi->addons_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Addon name | 

### Return type

[**ApiAddon**](ApiAddon.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_inventory_application_id_identities_get**
> list[ApiIdentity] application_inventory_application_id_identities_get(id)

List identities for an application.

List identities for an application.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetApi()
id = 56 # int | Application ID

try:
    # List identities for an application.
    api_response = api_instance.application_inventory_application_id_identities_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetApi->application_inventory_application_id_identities_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Application ID | 

### Return type

[**list[ApiIdentity]**](ApiIdentity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_inventory_application_import_id_get**
> ApiImport application_inventory_application_import_id_get(id)

Get an import by ID.

Get an import by ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetApi()
id = 'id_example' # str | Import ID

try:
    # Get an import by ID.
    api_response = api_instance.application_inventory_application_import_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetApi->application_inventory_application_import_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Import ID | 

### Return type

[**ApiImport**](ApiImport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_inventory_import_summary_id_get**
> ApiImportSummary application_inventory_import_summary_id_get(id)

Get an import summary by ID.

Get an import by ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetApi()
id = 'id_example' # str | ImportSummary ID

try:
    # Get an import summary by ID.
    api_response = api_instance.application_inventory_import_summary_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetApi->application_inventory_import_summary_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ImportSummary ID | 

### Return type

[**ApiImportSummary**](ApiImportSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_id_get**
> ApiApplication applications_id_get(id)

Get an application by ID.

Get an application by ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetApi()
id = 56 # int | Application ID

try:
    # Get an application by ID.
    api_response = api_instance.applications_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetApi->applications_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Application ID | 

### Return type

[**ApiApplication**](ApiApplication.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_id_tasks_id_content_wildcard_get**
> applications_id_tasks_id_content_wildcard_get(id)

Get bucket content by ID and path.

Get bucket content by ID and path.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetApi()
id = 'id_example' # str | Task ID

try:
    # Get bucket content by ID and path.
    api_instance.applications_id_tasks_id_content_wildcard_get(id)
except ApiException as e:
    print("Exception when calling GetApi->applications_id_tasks_id_content_wildcard_get: %s\n" % e)
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
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bucket_id_content_wildcard_post**
> bucket_id_content_wildcard_post(id)

Upload bucket content by task ID and path.

Upload bucket content by task ID and path.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetApi()
id = 'id_example' # str | Bucket ID

try:
    # Upload bucket content by task ID and path.
    api_instance.bucket_id_content_wildcard_post(id)
except ApiException as e:
    print("Exception when calling GetApi->bucket_id_content_wildcard_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Bucket ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **businessservices_id_get**
> ApiBusinessService businessservices_id_get(id)

Get a business service by ID.

Get a business service by ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetApi()
id = 'id_example' # str | Business Service ID

try:
    # Get a business service by ID.
    api_response = api_instance.businessservices_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetApi->businessservices_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Business Service ID | 

### Return type

[**ApiBusinessService**](ApiBusinessService.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dependencies_id_get**
> ApiDependency dependencies_id_get(id)

Get a dependency by ID.

Get a dependency by ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetApi()
id = 'id_example' # str | Dependency ID

try:
    # Get a dependency by ID.
    api_response = api_instance.dependencies_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetApi->dependencies_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Dependency ID | 

### Return type

[**ApiDependency**](ApiDependency.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **identities_get**
> list[ApiIdentity] identities_get()

List all identities.

List all identities.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetApi()

try:
    # List all identities.
    api_response = api_instance.identities_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetApi->identities_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ApiIdentity]**](ApiIdentity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **identities_id_get**
> ApiIdentity identities_id_get(id)

Get an identity by ID.

Get an identity by ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetApi()
id = 'id_example' # str | Identity ID

try:
    # Get an identity by ID.
    api_response = api_instance.identities_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetApi->identities_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identity ID | 

### Return type

[**ApiIdentity**](ApiIdentity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobfunctions_get**
> list[ApiJobFunction] jobfunctions_get()

List all job functions.

List all job functions.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetApi()

try:
    # List all job functions.
    api_response = api_instance.jobfunctions_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetApi->jobfunctions_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ApiJobFunction]**](ApiJobFunction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobfunctions_id_get**
> list[ApiJobFunction] jobfunctions_id_get(id)

Get a job function by ID.

Get a job function by ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetApi()
id = 'id_example' # str | Job Function ID

try:
    # Get a job function by ID.
    api_response = api_instance.jobfunctions_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetApi->jobfunctions_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Job Function ID | 

### Return type

[**list[ApiJobFunction]**](ApiJobFunction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxies_get**
> list[ApiProxy] proxies_get()

List all proxies.

List all proxies.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetApi()

try:
    # List all proxies.
    api_response = api_instance.proxies_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetApi->proxies_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ApiProxy]**](ApiProxy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxies_id_get**
> ApiProxy proxies_id_get(id)

Get an proxy by ID.

Get an proxy by ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetApi()
id = 'id_example' # str | Proxy ID

try:
    # Get an proxy by ID.
    api_response = api_instance.proxies_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetApi->proxies_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Proxy ID | 

### Return type

[**ApiProxy**](ApiProxy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reviews_get**
> list[ApiReview] reviews_get()

List all reviews.

List all reviews.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetApi()

try:
    # List all reviews.
    api_response = api_instance.reviews_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetApi->reviews_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ApiReview]**](ApiReview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reviews_id_get**
> list[ApiReview] reviews_id_get(id)

Get a review by ID.

Get a review by ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetApi()
id = 'id_example' # str | Review ID

try:
    # Get a review by ID.
    api_response = api_instance.reviews_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetApi->reviews_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Review ID | 

### Return type

[**list[ApiReview]**](ApiReview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

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
api_instance = swagger_client.GetApi()
key = 'key_example' # str | Key

try:
    # Get a setting by its key.
    api_response = api_instance.settings_key_get(key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetApi->settings_key_get: %s\n" % e)
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

# **stakeholdergroups_get**
> list[ApiStakeholderGroup] stakeholdergroups_get()

List all stakeholder groups.

List all stakeholder groups.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetApi()

try:
    # List all stakeholder groups.
    api_response = api_instance.stakeholdergroups_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetApi->stakeholdergroups_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ApiStakeholderGroup]**](ApiStakeholderGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stakeholdergroups_id_get**
> ApiStakeholderGroup stakeholdergroups_id_get(id)

Get a stakeholder group by ID.

Get a stakeholder group by ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetApi()
id = 'id_example' # str | Stakeholder Group ID

try:
    # Get a stakeholder group by ID.
    api_response = api_instance.stakeholdergroups_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetApi->stakeholdergroups_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Stakeholder Group ID | 

### Return type

[**ApiStakeholderGroup**](ApiStakeholderGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stakeholders_get**
> list[ApiStakeholder] stakeholders_get()

List all stakeholders.

List all stakeholders.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetApi()

try:
    # List all stakeholders.
    api_response = api_instance.stakeholders_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetApi->stakeholders_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ApiStakeholder]**](ApiStakeholder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stakeholders_id_get**
> ApiStakeholder stakeholders_id_get(id)

Get a stakeholder by ID.

Get a stakeholder by ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetApi()
id = 'id_example' # str | Stakeholder ID

try:
    # Get a stakeholder by ID.
    api_response = api_instance.stakeholders_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetApi->stakeholders_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Stakeholder ID | 

### Return type

[**ApiStakeholder**](ApiStakeholder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_get**
> list[ApiTag] tags_get()

List all tags.

List all tags.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetApi()

try:
    # List all tags.
    api_response = api_instance.tags_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetApi->tags_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ApiTag]**](ApiTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_id_get**
> ApiTag tags_id_get(id)

Get a tag by ID.

Get a tag by ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetApi()
id = 'id_example' # str | Tag ID

try:
    # Get a tag by ID.
    api_response = api_instance.tags_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetApi->tags_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tag ID | 

### Return type

[**ApiTag**](ApiTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tagtypes_get**
> list[ApiTagType] tagtypes_get()

List all tag types.

List all tag types.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetApi()

try:
    # List all tag types.
    api_response = api_instance.tagtypes_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetApi->tagtypes_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ApiTagType]**](ApiTagType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tagtypes_id_get**
> ApiTagType tagtypes_id_get(id)

Get a tag type by ID.

Get a tag type by ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetApi()
id = 'id_example' # str | Tag Type ID

try:
    # Get a tag type by ID.
    api_response = api_instance.tagtypes_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetApi->tagtypes_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tag Type ID | 

### Return type

[**ApiTagType**](ApiTagType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **taskgroups_get**
> list[ApiTaskGroup] taskgroups_get()

List all task groups.

List all task groups.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetApi()

try:
    # List all task groups.
    api_response = api_instance.taskgroups_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetApi->taskgroups_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ApiTaskGroup]**](ApiTaskGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **taskgroups_id_bucket_wildcard_get**
> taskgroups_id_bucket_wildcard_get(id)

Get bucket content by ID and path.

Get bucket content by ID and path.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetApi()
id = 'id_example' # str | TaskGroup ID

try:
    # Get bucket content by ID and path.
    api_instance.taskgroups_id_bucket_wildcard_get(id)
except ApiException as e:
    print("Exception when calling GetApi->taskgroups_id_bucket_wildcard_get: %s\n" % e)
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
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **taskgroups_id_get**
> ApiTaskGroup taskgroups_id_get(id)

Get a task group by ID.

Get a task group by ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetApi()
id = 'id_example' # str | TaskGroup ID

try:
    # Get a task group by ID.
    api_response = api_instance.taskgroups_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetApi->taskgroups_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| TaskGroup ID | 

### Return type

[**ApiTaskGroup**](ApiTaskGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_get**
> list[ApiTask] tasks_get()

List all tasks.

List all tasks.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetApi()

try:
    # List all tasks.
    api_response = api_instance.tasks_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetApi->tasks_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ApiTask]**](ApiTask.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_id_bucket_wildcard_get**
> tasks_id_bucket_wildcard_get(id)

Get bucket content by ID and path.

Get bucket content by ID and path.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetApi()
id = 'id_example' # str | Task ID

try:
    # Get bucket content by ID and path.
    api_instance.tasks_id_bucket_wildcard_get(id)
except ApiException as e:
    print("Exception when calling GetApi->tasks_id_bucket_wildcard_get: %s\n" % e)
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
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_id_bucket_wildcard_post**
> tasks_id_bucket_wildcard_post(id)

Upload bucket content by task ID and path.

Upload bucket content by task ID and path.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetApi()
id = 'id_example' # str | Bucket ID

try:
    # Upload bucket content by task ID and path.
    api_instance.tasks_id_bucket_wildcard_post(id)
except ApiException as e:
    print("Exception when calling GetApi->tasks_id_bucket_wildcard_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Bucket ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_id_get**
> ApiTask tasks_id_get(id)

Get a task by ID.

Get a task by ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetApi()
id = 'id_example' # str | Task ID

try:
    # Get a task by ID.
    api_response = api_instance.tasks_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetApi->tasks_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Task ID | 

### Return type

[**ApiTask**](ApiTask.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

