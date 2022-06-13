# swagger_client.PostApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**application_inventory_file_upload_post**](PostApi.md#application_inventory_file_upload_post) | **POST** /application-inventory/file/upload | Upload a CSV containing applications and dependencies to import.


# **application_inventory_file_upload_post**
> ApiImportSummary application_inventory_file_upload_post()

Upload a CSV containing applications and dependencies to import.

Upload a CSV containing applications and dependencies to import.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PostApi()

try:
    # Upload a CSV containing applications and dependencies to import.
    api_response = api_instance.application_inventory_file_upload_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PostApi->application_inventory_file_upload_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiImportSummary**](ApiImportSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

