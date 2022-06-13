# swagger_client.ClaimApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_claim_collection**](ClaimApi.md#get_claim_collection) | **GET** /api/teamww/get-claim | Gets collection of Team WorldWide Claims
[**get_claim_item**](ClaimApi.md#get_claim_item) | **GET** /api/teamww/get-single-claim/{id} | Gets a single Team WorldWide Claim
[**post_claim_collection**](ClaimApi.md#post_claim_collection) | **POST** /api/teamww/post-claim | File a single Team WorldWide Claim
[**update_claim_item**](ClaimApi.md#update_claim_item) | **PATCH** /api/teamww/update-claim/{id} | Update an existing Team WorldWide Claim

# **get_claim_collection**
> InlineResponse2002 get_claim_collection(page=page)

Gets collection of Team WorldWide Claims

Retrieves the collection of Claim resources.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClaimApi()
page = 1 # int | The collection page number (optional) (default to 1)

try:
    # Gets collection of Team WorldWide Claims
    api_response = api_instance.get_claim_collection(page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClaimApi->get_claim_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The collection page number | [optional] [default to 1]

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_claim_item**
> ClaimClaimsResponseJsonldClaimCollectionReadRead get_claim_item(id)

Gets a single Team WorldWide Claim

Retrieves a Claim resource.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClaimApi()
id = 'id_example' # str | Resource identifier

try:
    # Gets a single Team WorldWide Claim
    api_response = api_instance.get_claim_item(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClaimApi->get_claim_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Resource identifier | 

### Return type

[**ClaimClaimsResponseJsonldClaimCollectionReadRead**](ClaimClaimsResponseJsonldClaimCollectionReadRead.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_claim_collection**
> ClaimClaimsResponseJsonldClaimCollectionReadRead post_claim_collection(body)

File a single Team WorldWide Claim

Creates a Claim resource.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClaimApi()
body = swagger_client.ClaimJsonldClaimCollectionWriteWrite() # ClaimJsonldClaimCollectionWriteWrite | The new Claim resource

try:
    # File a single Team WorldWide Claim
    api_response = api_instance.post_claim_collection(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClaimApi->post_claim_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClaimJsonldClaimCollectionWriteWrite**](ClaimJsonldClaimCollectionWriteWrite.md)| The new Claim resource | 

### Return type

[**ClaimClaimsResponseJsonldClaimCollectionReadRead**](ClaimClaimsResponseJsonldClaimCollectionReadRead.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/ld+json, application/json, text/html
 - **Accept**: application/ld+json, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_claim_item**
> ClaimClaimsResponseJsonldClaimCollectionReadRead update_claim_item(body, id)

Update an existing Team WorldWide Claim

Updates the Claim resource.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClaimApi()
body = swagger_client.ClaimClaimCollectionWriteWrite() # ClaimClaimCollectionWriteWrite | The updated Claim resource
id = 'id_example' # str | Resource identifier

try:
    # Update an existing Team WorldWide Claim
    api_response = api_instance.update_claim_item(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClaimApi->update_claim_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClaimClaimCollectionWriteWrite**](ClaimClaimCollectionWriteWrite.md)| The updated Claim resource | 
 **id** | **str**| Resource identifier | 

### Return type

[**ClaimClaimsResponseJsonldClaimCollectionReadRead**](ClaimClaimsResponseJsonldClaimCollectionReadRead.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/ld+json, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

