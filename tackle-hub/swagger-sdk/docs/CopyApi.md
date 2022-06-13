# swagger_client.CopyApi

All URIs are relative to *https://localhost*

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

# create an instance of the API class
api_instance = swagger_client.CopyApi()
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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

