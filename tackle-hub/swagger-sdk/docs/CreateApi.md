# swagger_client.CreateApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**applications_post**](CreateApi.md#applications_post) | **POST** /applications | Create an application.
[**businessservices_post**](CreateApi.md#businessservices_post) | **POST** /businessservices | Create a business service.
[**dependencies_post**](CreateApi.md#dependencies_post) | **POST** /dependencies | Create a dependency.
[**identities_post**](CreateApi.md#identities_post) | **POST** /identities | Create an identity.
[**jobfunctions_post**](CreateApi.md#jobfunctions_post) | **POST** /jobfunctions | Create a job function.
[**proxies_post**](CreateApi.md#proxies_post) | **POST** /proxies | Create an proxy.
[**reviews_post**](CreateApi.md#reviews_post) | **POST** /reviews | Create a review.
[**settings_post**](CreateApi.md#settings_post) | **POST** /settings | Create a setting.
[**stakeholdergroups_post**](CreateApi.md#stakeholdergroups_post) | **POST** /stakeholdergroups | Create a stakeholder group.
[**stakeholders_post**](CreateApi.md#stakeholders_post) | **POST** /stakeholders | Create a stakeholder.
[**tags_post**](CreateApi.md#tags_post) | **POST** /tags | Create a tag.
[**tagtypes_post**](CreateApi.md#tagtypes_post) | **POST** /tagtypes | Create a tag type.
[**taskgroups_post**](CreateApi.md#taskgroups_post) | **POST** /taskgroups | Create a task group.
[**tasks_post**](CreateApi.md#tasks_post) | **POST** /tasks | Create a task.


# **applications_post**
> ApiApplication applications_post(application)

Create an application.

Create an application.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreateApi()
application = swagger_client.ApiApplication() # ApiApplication | Application data

try:
    # Create an application.
    api_response = api_instance.applications_post(application)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateApi->applications_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | [**ApiApplication**](ApiApplication.md)| Application data | 

### Return type

[**ApiApplication**](ApiApplication.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **businessservices_post**
> ApiBusinessService businessservices_post(business_service)

Create a business service.

Create a business service.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreateApi()
business_service = swagger_client.ApiBusinessService() # ApiBusinessService | Business service data

try:
    # Create a business service.
    api_response = api_instance.businessservices_post(business_service)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateApi->businessservices_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_service** | [**ApiBusinessService**](ApiBusinessService.md)| Business service data | 

### Return type

[**ApiBusinessService**](ApiBusinessService.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dependencies_post**
> ApiDependency dependencies_post(applications_dependency)

Create a dependency.

Create a dependency.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreateApi()
applications_dependency = swagger_client.ApiDependency() # ApiDependency | Dependency data

try:
    # Create a dependency.
    api_response = api_instance.dependencies_post(applications_dependency)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateApi->dependencies_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applications_dependency** | [**ApiDependency**](ApiDependency.md)| Dependency data | 

### Return type

[**ApiDependency**](ApiDependency.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **identities_post**
> ApiIdentity identities_post(identity)

Create an identity.

Create an identity.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreateApi()
identity = swagger_client.ApiIdentity() # ApiIdentity | Identity data

try:
    # Create an identity.
    api_response = api_instance.identities_post(identity)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateApi->identities_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity** | [**ApiIdentity**](ApiIdentity.md)| Identity data | 

### Return type

[**ApiIdentity**](ApiIdentity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobfunctions_post**
> ApiJobFunction jobfunctions_post(job_function)

Create a job function.

Create a job function.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreateApi()
job_function = swagger_client.ApiJobFunction() # ApiJobFunction | Job Function data

try:
    # Create a job function.
    api_response = api_instance.jobfunctions_post(job_function)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateApi->jobfunctions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_function** | [**ApiJobFunction**](ApiJobFunction.md)| Job Function data | 

### Return type

[**ApiJobFunction**](ApiJobFunction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxies_post**
> ApiProxy proxies_post(proxy)

Create an proxy.

Create an proxy.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreateApi()
proxy = swagger_client.ApiProxy() # ApiProxy | Proxy data

try:
    # Create an proxy.
    api_response = api_instance.proxies_post(proxy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateApi->proxies_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proxy** | [**ApiProxy**](ApiProxy.md)| Proxy data | 

### Return type

[**ApiProxy**](ApiProxy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reviews_post**
> ApiReview reviews_post(review)

Create a review.

Create a review.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreateApi()
review = swagger_client.ApiReview() # ApiReview | Review data

try:
    # Create a review.
    api_response = api_instance.reviews_post(review)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateApi->reviews_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **review** | [**ApiReview**](ApiReview.md)| Review data | 

### Return type

[**ApiReview**](ApiReview.md)

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
api_instance = swagger_client.CreateApi()
setting = swagger_client.ApiSetting() # ApiSetting | Setting data

try:
    # Create a setting.
    api_response = api_instance.settings_post(setting)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateApi->settings_post: %s\n" % e)
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

# **stakeholdergroups_post**
> ApiStakeholderGroup stakeholdergroups_post(stakeholder_group)

Create a stakeholder group.

Create a stakeholder group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreateApi()
stakeholder_group = swagger_client.ApiStakeholderGroup() # ApiStakeholderGroup | Stakeholder Group data

try:
    # Create a stakeholder group.
    api_response = api_instance.stakeholdergroups_post(stakeholder_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateApi->stakeholdergroups_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stakeholder_group** | [**ApiStakeholderGroup**](ApiStakeholderGroup.md)| Stakeholder Group data | 

### Return type

[**ApiStakeholderGroup**](ApiStakeholderGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stakeholders_post**
> ApiStakeholder stakeholders_post(stakeholder)

Create a stakeholder.

Create a stakeholder.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreateApi()
stakeholder = swagger_client.ApiStakeholder() # ApiStakeholder | Stakeholder data

try:
    # Create a stakeholder.
    api_response = api_instance.stakeholders_post(stakeholder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateApi->stakeholders_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stakeholder** | [**ApiStakeholder**](ApiStakeholder.md)| Stakeholder data | 

### Return type

[**ApiStakeholder**](ApiStakeholder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_post**
> ApiTag tags_post(tag)

Create a tag.

Create a tag.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreateApi()
tag = swagger_client.ApiTag() # ApiTag | Tag data

try:
    # Create a tag.
    api_response = api_instance.tags_post(tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateApi->tags_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | [**ApiTag**](ApiTag.md)| Tag data | 

### Return type

[**ApiTag**](ApiTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tagtypes_post**
> ApiTagType tagtypes_post(tag_type)

Create a tag type.

Create a tag type.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreateApi()
tag_type = swagger_client.ApiTagType() # ApiTagType | Tag Type data

try:
    # Create a tag type.
    api_response = api_instance.tagtypes_post(tag_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateApi->tagtypes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_type** | [**ApiTagType**](ApiTagType.md)| Tag Type data | 

### Return type

[**ApiTagType**](ApiTagType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **taskgroups_post**
> ApiTaskGroup taskgroups_post(taskgroup)

Create a task group.

Create a task group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreateApi()
taskgroup = swagger_client.ApiTaskGroup() # ApiTaskGroup | TaskGroup data

try:
    # Create a task group.
    api_response = api_instance.taskgroups_post(taskgroup)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateApi->taskgroups_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taskgroup** | [**ApiTaskGroup**](ApiTaskGroup.md)| TaskGroup data | 

### Return type

[**ApiTaskGroup**](ApiTaskGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_post**
> ApiTask tasks_post(task)

Create a task.

Create a task.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreateApi()
task = swagger_client.ApiTask() # ApiTask | Task data

try:
    # Create a task.
    api_response = api_instance.tasks_post(task)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateApi->tasks_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task** | [**ApiTask**](ApiTask.md)| Task data | 

### Return type

[**ApiTask**](ApiTask.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

