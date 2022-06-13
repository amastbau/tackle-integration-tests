# swagger_client.ExportApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**application_inventory_csv_export_get**](ExportApi.md#application_inventory_csv_export_get) | **GET** /application-inventory/csv-export | Export the source CSV for a particular import summary.


# **application_inventory_csv_export_get**
> file application_inventory_csv_export_get(import_summary_id)

Export the source CSV for a particular import summary.

Export the source CSV for a particular import summary.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExportApi()
import_summary_id = 'import_summary_id_example' # str | ImportSummary ID

try:
    # Export the source CSV for a particular import summary.
    api_response = api_instance.application_inventory_csv_export_get(import_summary_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportApi->application_inventory_csv_export_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_summary_id** | **str**| ImportSummary ID | 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

