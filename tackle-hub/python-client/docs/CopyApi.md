# swagger_client.CopyApi

All URIs are relative to *http://192.168.39.186/hub*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reviews_copy_post**](CopyApi.md#reviews_copy_post) | **POST** /reviews/copy | Copy a review from one application to others.


# **reviews_copy_post**
> reviews_copy_post(copy_request)

Copy a review from one application to others.

Copy a review from one application to others.

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
api_instance = swagger_client.CopyApi(swagger_client.ApiClient(configuration))
copy_request = swagger_client.ApiCopyRequest() # ApiCopyRequest | Review copy request data

try:
    # Copy a review from one application to others.
    api_instance.reviews_copy_post(copy_request)
except ApiException as e:
    print("Exception when calling CopyApi->reviews_copy_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **copy_request** | [**ApiCopyRequest**](ApiCopyRequest.md)| Review copy request data | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

