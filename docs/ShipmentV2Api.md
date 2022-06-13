# swagger_client.ShipmentV2Api

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_get_shipment_status_collection**](ShipmentV2Api.md#get_get_shipment_status_collection) | **GET** /api/teamww/get-shipment-statuses | Gets the shipment status by house bill.
[**get_house_bill_get_house_bill_collection**](ShipmentV2Api.md#get_house_bill_get_house_bill_collection) | **GET** /api/teamww/get-house-bill | Gets and Reserves a Team WorldWide HouseBill.
[**post_create_shipment_booking_shipment_booking_v2_collection**](ShipmentV2Api.md#post_create_shipment_booking_shipment_booking_v2_collection) | **POST** /api/teamww/create/shipmentBooking | Book shipments to Team Worldwide.
[**post_create_shipment_shipment_v2_collection**](ShipmentV2Api.md#post_create_shipment_shipment_v2_collection) | **POST** /api/teamww/create/shipment | Book a single shipment to Team Worldwide.
[**put_add_new_shipment_note_shipment_note_resource_item**](ShipmentV2Api.md#put_add_new_shipment_note_shipment_note_resource_item) | **PUT** /api/teamww/create/new/{houseBill}/note | Add Shipment Note.
[**put_update_team_booking_update_team_booking_item**](ShipmentV2Api.md#put_update_team_booking_update_team_booking_item) | **PATCH** /api/teamww/update/updateShipmentBooking/{teamBookingNumber} | Update Booking.

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
api_instance = swagger_client.ShipmentV2Api()
house_bill = 'house_bill_example' # str |  (optional)

try:
    # Gets the shipment status by house bill.
    api_response = api_instance.get_get_shipment_status_collection(house_bill=house_bill)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentV2Api->get_get_shipment_status_collection: %s\n" % e)
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

# **get_house_bill_get_house_bill_collection**
> InlineResponse2003 get_house_bill_get_house_bill_collection()

Gets and Reserves a Team WorldWide HouseBill.

Retrieves the collection of GetHouseBill resources.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ShipmentV2Api()

try:
    # Gets and Reserves a Team WorldWide HouseBill.
    api_response = api_instance.get_house_bill_get_house_bill_collection()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentV2Api->get_house_bill_get_house_bill_collection: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_create_shipment_booking_shipment_booking_v2_collection**
> ShipmentBookingV2ShipmentBookingCreatedJsonld post_create_shipment_booking_shipment_booking_v2_collection(body)

Book shipments to Team Worldwide.

Creates a ShipmentBookingV2 resource.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ShipmentV2Api()
body = swagger_client.ShipmentBookingV2JsonldShipmentBookingCreate() # ShipmentBookingV2JsonldShipmentBookingCreate | The new ShipmentBookingV2 resource

try:
    # Book shipments to Team Worldwide.
    api_response = api_instance.post_create_shipment_booking_shipment_booking_v2_collection(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentV2Api->post_create_shipment_booking_shipment_booking_v2_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ShipmentBookingV2JsonldShipmentBookingCreate**](ShipmentBookingV2JsonldShipmentBookingCreate.md)| The new ShipmentBookingV2 resource | 

### Return type

[**ShipmentBookingV2ShipmentBookingCreatedJsonld**](ShipmentBookingV2ShipmentBookingCreatedJsonld.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/ld+json, application/json, text/html
 - **Accept**: application/ld+json, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_create_shipment_shipment_v2_collection**
> ShipmentV2ShipmentCreatedJsonld post_create_shipment_shipment_v2_collection(body)

Book a single shipment to Team Worldwide.

Creates a ShipmentV2 resource.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ShipmentV2Api()
body = swagger_client.ShipmentV2ShipmentJsonldShipmentCreate() # ShipmentV2ShipmentJsonldShipmentCreate | The new ShipmentV2 resource

try:
    # Book a single shipment to Team Worldwide.
    api_response = api_instance.post_create_shipment_shipment_v2_collection(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentV2Api->post_create_shipment_shipment_v2_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ShipmentV2ShipmentJsonldShipmentCreate**](ShipmentV2ShipmentJsonldShipmentCreate.md)| The new ShipmentV2 resource | 

### Return type

[**ShipmentV2ShipmentCreatedJsonld**](ShipmentV2ShipmentCreatedJsonld.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/ld+json, application/json, text/html
 - **Accept**: application/ld+json, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_add_new_shipment_note_shipment_note_resource_item**
> ShipmentNoteResourceJsonld put_add_new_shipment_note_shipment_note_resource_item(body, house_bill)

Add Shipment Note.

Replaces the ShipmentNoteResource resource.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ShipmentV2Api()
body = swagger_client.ShipmentNoteResourceJsonldShipmentNoteResourceJsonldShipmentCreate() # ShipmentNoteResourceJsonldShipmentNoteResourceJsonldShipmentCreate | The updated ShipmentNoteResource resource
house_bill = 'house_bill_example' # str | Resource identifier

try:
    # Add Shipment Note.
    api_response = api_instance.put_add_new_shipment_note_shipment_note_resource_item(body, house_bill)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentV2Api->put_add_new_shipment_note_shipment_note_resource_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ShipmentNoteResourceJsonldShipmentNoteResourceJsonldShipmentCreate**](ShipmentNoteResourceJsonldShipmentNoteResourceJsonldShipmentCreate.md)| The updated ShipmentNoteResource resource | 
 **house_bill** | **str**| Resource identifier | 

### Return type

[**ShipmentNoteResourceJsonld**](ShipmentNoteResourceJsonld.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/ld+json, application/json, text/html
 - **Accept**: application/ld+json, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_update_team_booking_update_team_booking_item**
> UpdateTeamBookingJsonldGetShipmentBookingCollectionGetRead put_update_team_booking_update_team_booking_item(body, team_booking_number)

Update Booking.

Updates the UpdateTeamBooking resource.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ShipmentV2Api()
body = swagger_client.UpdateTeamBookingUpdateTeamBooking() # UpdateTeamBookingUpdateTeamBooking | The updated UpdateTeamBooking resource
team_booking_number = 'team_booking_number_example' # str | Resource identifier

try:
    # Update Booking.
    api_response = api_instance.put_update_team_booking_update_team_booking_item(body, team_booking_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentV2Api->put_update_team_booking_update_team_booking_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateTeamBookingUpdateTeamBooking**](UpdateTeamBookingUpdateTeamBooking.md)| The updated UpdateTeamBooking resource | 
 **team_booking_number** | **str**| Resource identifier | 

### Return type

[**UpdateTeamBookingJsonldGetShipmentBookingCollectionGetRead**](UpdateTeamBookingJsonldGetShipmentBookingCollectionGetRead.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/ld+json, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

