# swagger_client.TeamBookApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_get_accessorials_collection**](TeamBookApi.md#get_get_accessorials_collection) | **GET** /api/team-book/get-accessorials | Get TeamBook accessorials.
[**get_get_quote_item**](TeamBookApi.md#get_get_quote_item) | **GET** /api/team-book/get-quote/{rateId} | Get a Quote along with a reserved house bill.  Use a rateId from get-rates endpoint.
[**get_get_rate_collection**](TeamBookApi.md#get_get_rate_collection) | **GET** /api/team-book/get-rates | Get rates from the Team Book System.
[**get_get_shipment_status_collection**](TeamBookApi.md#get_get_shipment_status_collection) | **GET** /api/teamww/get-shipment-statuses | Gets the shipment status by house bill.
[**post_book_shipment_collection**](TeamBookApi.md#post_book_shipment_collection) | **POST** /api/team-book/book-shipment | Book and dispatch a shipment in the TeamBook system.

# **get_get_accessorials_collection**
> InlineResponse200 get_get_accessorials_collection()

Get TeamBook accessorials.

Retrieves the collection of GetAccessorials resources.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TeamBookApi()

try:
    # Get TeamBook accessorials.
    api_response = api_instance.get_get_accessorials_collection()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBookApi->get_get_accessorials_collection: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_get_quote_item**
> GetQuoteQuoteResponseJsonld get_get_quote_item(rate_id)

Get a Quote along with a reserved house bill.  Use a rateId from get-rates endpoint.

Retrieves a GetQuote resource.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TeamBookApi()
rate_id = 'rate_id_example' # str | Resource identifier

try:
    # Get a Quote along with a reserved house bill.  Use a rateId from get-rates endpoint.
    api_response = api_instance.get_get_quote_item(rate_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBookApi->get_get_quote_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rate_id** | **str**| Resource identifier | 

### Return type

[**GetQuoteQuoteResponseJsonld**](GetQuoteQuoteResponseJsonld.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_get_rate_collection**
> InlineResponse2001 get_get_rate_collection(origin_city, origin_state, origin_zip_code, origin_country, destination_city, destination_state, destination_zip_code, destination_country, unit_of_measure, pickup_date=pickup_date, insurance_add_on=insurance_add_on, insure_freight=insure_freight, insurance_amount=insurance_amount, linear_feet=linear_feet, equipment=equipment)

Get rates from the Team Book System.

Retrieves the collection of GetRate resources.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TeamBookApi()
origin_city = 'origin_city_example' # str | 
origin_state = 'origin_state_example' # str | 
origin_zip_code = 'origin_zip_code_example' # str | 
origin_country = 'origin_country_example' # str | 
destination_city = 'destination_city_example' # str | 
destination_state = 'destination_state_example' # str | 
destination_zip_code = 'destination_zip_code_example' # str | 
destination_country = 'destination_country_example' # str | 
unit_of_measure = 'unit_of_measure_example' # str | Unit of Measure. Valid values: US (lbs/in) - METRIC (kgs/cm) - MIXED (kgs/cms)
pickup_date = 'pickup_date_example' # str | Pickup Date. Format: YYYY-MM-DD (optional)
insurance_add_on = true # bool | Option to add 10% to the insurance value (optional)
insure_freight = true # bool | Used to tell the API to quote insurance. Your account must be setup for quoting insurance. (optional)
insurance_amount = 1.2 # float | This parameter refers to the extra value of 'Money' type accessorials like declared value. (optional)
linear_feet = 1.2 # float | Linear feet value. Helpful for some volume vendors to return a rate based on space needed in a truck. (optional)
equipment = 'equipment_example' # str | Used for volume vendors and rates they return. Valid values: All, Van, Flatbed (optional)

try:
    # Get rates from the Team Book System.
    api_response = api_instance.get_get_rate_collection(origin_city, origin_state, origin_zip_code, origin_country, destination_city, destination_state, destination_zip_code, destination_country, unit_of_measure, pickup_date=pickup_date, insurance_add_on=insurance_add_on, insure_freight=insure_freight, insurance_amount=insurance_amount, linear_feet=linear_feet, equipment=equipment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBookApi->get_get_rate_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **origin_city** | **str**|  | 
 **origin_state** | **str**|  | 
 **origin_zip_code** | **str**|  | 
 **origin_country** | **str**|  | 
 **destination_city** | **str**|  | 
 **destination_state** | **str**|  | 
 **destination_zip_code** | **str**|  | 
 **destination_country** | **str**|  | 
 **unit_of_measure** | **str**| Unit of Measure. Valid values: US (lbs/in) - METRIC (kgs/cm) - MIXED (kgs/cms) | 
 **pickup_date** | **str**| Pickup Date. Format: YYYY-MM-DD | [optional] 
 **insurance_add_on** | **bool**| Option to add 10% to the insurance value | [optional] 
 **insure_freight** | **bool**| Used to tell the API to quote insurance. Your account must be setup for quoting insurance. | [optional] 
 **insurance_amount** | **float**| This parameter refers to the extra value of &#x27;Money&#x27; type accessorials like declared value. | [optional] 
 **linear_feet** | **float**| Linear feet value. Helpful for some volume vendors to return a rate based on space needed in a truck. | [optional] 
 **equipment** | **str**| Used for volume vendors and rates they return. Valid values: All, Van, Flatbed | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_get_shipment_status_collection**
> InlineResponse2004 get_get_shipment_status_collection(house_bill=house_bill)

Gets the shipment status by house bill.

Retrieves the collection of GetShipmentStatus resources.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TeamBookApi()
house_bill = 'house_bill_example' # str |  (optional)

try:
    # Gets the shipment status by house bill.
    api_response = api_instance.get_get_shipment_status_collection(house_bill=house_bill)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBookApi->get_get_shipment_status_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **house_bill** | **str**|  | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_book_shipment_collection**
> BookShipmentTeamBookResponseJsonld post_book_shipment_collection(body)

Book and dispatch a shipment in the TeamBook system.

Creates a BookShipment resource.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TeamBookApi()
body = swagger_client.BookShipmentJsonldTeamBookShipmentCreate() # BookShipmentJsonldTeamBookShipmentCreate | The new BookShipment resource

try:
    # Book and dispatch a shipment in the TeamBook system.
    api_response = api_instance.post_book_shipment_collection(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamBookApi->post_book_shipment_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BookShipmentJsonldTeamBookShipmentCreate**](BookShipmentJsonldTeamBookShipmentCreate.md)| The new BookShipment resource | 

### Return type

[**BookShipmentTeamBookResponseJsonld**](BookShipmentTeamBookResponseJsonld.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/ld+json, application/json, text/html
 - **Accept**: application/ld+json, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

