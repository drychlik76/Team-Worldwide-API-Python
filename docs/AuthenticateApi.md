# swagger_client.AuthenticateApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_credentials_item**](AuthenticateApi.md#post_credentials_item) | **POST** /api/authenticate | Authenticate to start session.

# **post_credentials_item**
> post_credentials_item(body=body)

Authenticate to start session.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticateApi()
body = swagger_client.Credentials() # Credentials | Start Session (optional)

try:
    # Authenticate to start session.
    api_instance.post_credentials_item(body=body)
except ApiException as e:
    print("Exception when calling AuthenticateApi->post_credentials_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Credentials**](Credentials.md)| Start Session | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

