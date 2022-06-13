# swagger_client.UpdateApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**applications_id_put**](UpdateApi.md#applications_id_put) | **PUT** /applications/{id} | Update an application.
[**businessservices_id_put**](UpdateApi.md#businessservices_id_put) | **PUT** /businessservices/{id} | Update a business service.
[**identities_id_put**](UpdateApi.md#identities_id_put) | **PUT** /identities/{id} | Update an identity.
[**jobfunctions_id_put**](UpdateApi.md#jobfunctions_id_put) | **PUT** /jobfunctions/{id} | Update a job function.
[**proxies_id_put**](UpdateApi.md#proxies_id_put) | **PUT** /proxies/{id} | Update an proxy.
[**reviews_id_put**](UpdateApi.md#reviews_id_put) | **PUT** /reviews/{id} | Update a review.
[**settings_key_put**](UpdateApi.md#settings_key_put) | **PUT** /settings/{key} | Update a setting.
[**stakeholdergroups_id_put**](UpdateApi.md#stakeholdergroups_id_put) | **PUT** /stakeholdergroups/{id} | Update a stakeholder group.
[**stakeholders_id_put**](UpdateApi.md#stakeholders_id_put) | **PUT** /stakeholders/{id} | Update a stakeholder.
[**tags_id_put**](UpdateApi.md#tags_id_put) | **PUT** /tags/{id} | Update a tag.
[**tagtypes_id_put**](UpdateApi.md#tagtypes_id_put) | **PUT** /tagtypes/{id} | Update a tag type.
[**taskgroups_id_submit_put**](UpdateApi.md#taskgroups_id_submit_put) | **PUT** /taskgroups/{id}/submit | Submit a task group.
[**tasks_id_put**](UpdateApi.md#tasks_id_put) | **PUT** /tasks/{id} | Update a task group.
[**tasks_id_report_delete**](UpdateApi.md#tasks_id_report_delete) | **DELETE** /tasks/{id}/report | Delete a task report.
[**tasks_id_report_post**](UpdateApi.md#tasks_id_report_post) | **POST** /tasks/{id}/report | Create a task report.
[**tasks_id_report_put**](UpdateApi.md#tasks_id_report_put) | **PUT** /tasks/{id}/report | Update a task report.
[**tasks_id_submit_put**](UpdateApi.md#tasks_id_submit_put) | **PUT** /tasks/{id}/submit | Submit a task.


# **applications_id_put**
> applications_id_put(id, application)

Update an application.

Update an application.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UpdateApi()
id = 56 # int | Application id
application = swagger_client.ApiApplication() # ApiApplication | Application data

try:
    # Update an application.
    api_instance.applications_id_put(id, application)
except ApiException as e:
    print("Exception when calling UpdateApi->applications_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Application id | 
 **application** | [**ApiApplication**](ApiApplication.md)| Application data | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **businessservices_id_put**
> businessservices_id_put(id, business_service)

Update a business service.

Update a business service.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UpdateApi()
id = 'id_example' # str | Business service ID
business_service = swagger_client.ApiBusinessService() # ApiBusinessService | Business service data

try:
    # Update a business service.
    api_instance.businessservices_id_put(id, business_service)
except ApiException as e:
    print("Exception when calling UpdateApi->businessservices_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Business service ID | 
 **business_service** | [**ApiBusinessService**](ApiBusinessService.md)| Business service data | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **identities_id_put**
> identities_id_put(id, identity)

Update an identity.

Update an identity.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UpdateApi()
id = 'id_example' # str | Identity ID
identity = swagger_client.ApiIdentity() # ApiIdentity | Identity data

try:
    # Update an identity.
    api_instance.identities_id_put(id, identity)
except ApiException as e:
    print("Exception when calling UpdateApi->identities_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identity ID | 
 **identity** | [**ApiIdentity**](ApiIdentity.md)| Identity data | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobfunctions_id_put**
> jobfunctions_id_put(id, job_function)

Update a job function.

Update a job function.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UpdateApi()
id = 'id_example' # str | Job Function ID
job_function = swagger_client.ApiJobFunction() # ApiJobFunction | Job Function data

try:
    # Update a job function.
    api_instance.jobfunctions_id_put(id, job_function)
except ApiException as e:
    print("Exception when calling UpdateApi->jobfunctions_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Job Function ID | 
 **job_function** | [**ApiJobFunction**](ApiJobFunction.md)| Job Function data | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxies_id_put**
> proxies_id_put(id, proxy)

Update an proxy.

Update an proxy.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UpdateApi()
id = 'id_example' # str | Proxy ID
proxy = swagger_client.ApiProxy() # ApiProxy | Proxy data

try:
    # Update an proxy.
    api_instance.proxies_id_put(id, proxy)
except ApiException as e:
    print("Exception when calling UpdateApi->proxies_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Proxy ID | 
 **proxy** | [**ApiProxy**](ApiProxy.md)| Proxy data | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reviews_id_put**
> reviews_id_put(id, review)

Update a review.

Update a review.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UpdateApi()
id = 'id_example' # str | Review ID
review = swagger_client.ApiReview() # ApiReview | Review data

try:
    # Update a review.
    api_instance.reviews_id_put(id, review)
except ApiException as e:
    print("Exception when calling UpdateApi->reviews_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Review ID | 
 **review** | [**ApiReview**](ApiReview.md)| Review data | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

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
api_instance = swagger_client.UpdateApi()
key = 'key_example' # str | Key

try:
    # Update a setting.
    api_instance.settings_key_put(key)
except ApiException as e:
    print("Exception when calling UpdateApi->settings_key_put: %s\n" % e)
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

# **stakeholdergroups_id_put**
> stakeholdergroups_id_put(id, stakeholder_group)

Update a stakeholder group.

Update a stakeholder group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UpdateApi()
id = 'id_example' # str | Stakeholder Group ID
stakeholder_group = swagger_client.ApiStakeholderGroup() # ApiStakeholderGroup | Stakeholder Group data

try:
    # Update a stakeholder group.
    api_instance.stakeholdergroups_id_put(id, stakeholder_group)
except ApiException as e:
    print("Exception when calling UpdateApi->stakeholdergroups_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Stakeholder Group ID | 
 **stakeholder_group** | [**ApiStakeholderGroup**](ApiStakeholderGroup.md)| Stakeholder Group data | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stakeholders_id_put**
> stakeholders_id_put(id, stakeholder)

Update a stakeholder.

Update a stakeholder.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UpdateApi()
id = 'id_example' # str | Stakeholder ID
stakeholder = swagger_client.ApiStakeholder() # ApiStakeholder | Stakeholder data

try:
    # Update a stakeholder.
    api_instance.stakeholders_id_put(id, stakeholder)
except ApiException as e:
    print("Exception when calling UpdateApi->stakeholders_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Stakeholder ID | 
 **stakeholder** | [**ApiStakeholder**](ApiStakeholder.md)| Stakeholder data | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_id_put**
> tags_id_put(id, tag)

Update a tag.

Update a tag.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UpdateApi()
id = 'id_example' # str | Tag ID
tag = swagger_client.ApiTag() # ApiTag | Tag data

try:
    # Update a tag.
    api_instance.tags_id_put(id, tag)
except ApiException as e:
    print("Exception when calling UpdateApi->tags_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tag ID | 
 **tag** | [**ApiTag**](ApiTag.md)| Tag data | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tagtypes_id_put**
> tagtypes_id_put(id, tag_type)

Update a tag type.

Update a tag type.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UpdateApi()
id = 'id_example' # str | Tag Type ID
tag_type = swagger_client.ApiTagType() # ApiTagType | Tag Type data

try:
    # Update a tag type.
    api_instance.tagtypes_id_put(id, tag_type)
except ApiException as e:
    print("Exception when calling UpdateApi->tagtypes_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tag Type ID | 
 **tag_type** | [**ApiTagType**](ApiTagType.md)| Tag Type data | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **taskgroups_id_submit_put**
> taskgroups_id_submit_put(id)

Submit a task group.

Submit a task group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UpdateApi()
id = 'id_example' # str | TaskGroup ID

try:
    # Submit a task group.
    api_instance.taskgroups_id_submit_put(id)
except ApiException as e:
    print("Exception when calling UpdateApi->taskgroups_id_submit_put: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_id_put**
> tasks_id_put(id, task)

Update a task group.

Update a task group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UpdateApi()
id = 'id_example' # str | Task ID
task = swagger_client.ApiTask() # ApiTask | Task data

try:
    # Update a task group.
    api_instance.tasks_id_put(id, task)
except ApiException as e:
    print("Exception when calling UpdateApi->tasks_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Task ID | 
 **task** | [**ApiTask**](ApiTask.md)| Task data | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_id_report_delete**
> tasks_id_report_delete(id)

Delete a task report.

Delete a task report.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UpdateApi()
id = 'id_example' # str | Task ID

try:
    # Delete a task report.
    api_instance.tasks_id_report_delete(id)
except ApiException as e:
    print("Exception when calling UpdateApi->tasks_id_report_delete: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_id_report_post**
> ApiTaskReport tasks_id_report_post(id, task)

Create a task report.

Update a task report.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UpdateApi()
id = 'id_example' # str | Task ID
task = swagger_client.ApiTaskReport() # ApiTaskReport | TaskReport data

try:
    # Create a task report.
    api_response = api_instance.tasks_id_report_post(id, task)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpdateApi->tasks_id_report_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Task ID | 
 **task** | [**ApiTaskReport**](ApiTaskReport.md)| TaskReport data | 

### Return type

[**ApiTaskReport**](ApiTaskReport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_id_report_put**
> ApiTaskReport tasks_id_report_put(id, task)

Update a task report.

Update a task report.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UpdateApi()
id = 'id_example' # str | Task ID
task = swagger_client.ApiTaskReport() # ApiTaskReport | TaskReport data

try:
    # Update a task report.
    api_response = api_instance.tasks_id_report_put(id, task)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpdateApi->tasks_id_report_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Task ID | 
 **task** | [**ApiTaskReport**](ApiTaskReport.md)| TaskReport data | 

### Return type

[**ApiTaskReport**](ApiTaskReport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_id_submit_put**
> tasks_id_submit_put(id)

Submit a task.

Submit a task.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UpdateApi()
id = 'id_example' # str | Task ID

try:
    # Submit a task.
    api_instance.tasks_id_submit_put(id)
except ApiException as e:
    print("Exception when calling UpdateApi->tasks_id_submit_put: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

