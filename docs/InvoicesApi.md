# swagger_client.InvoicesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_get_invoice_item**](InvoicesApi.md#get_get_invoice_item) | **GET** /api/teamww/invoice/get/{houseBill} | Get invoice by house bill

# **get_get_invoice_item**
> GetInvoiceInvoiceJsonldInvoiceItemGetRead get_get_invoice_item(house_bill)

Get invoice by house bill

Retrieves a GetInvoice resource.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
house_bill = 'house_bill_example' # str | Resource identifier

try:
    # Get invoice by house bill
    api_response = api_instance.get_get_invoice_item(house_bill)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_get_invoice_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **house_bill** | **str**| Resource identifier | 

### Return type

[**GetInvoiceInvoiceJsonldInvoiceItemGetRead**](GetInvoiceInvoiceJsonldInvoiceItemGetRead.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

