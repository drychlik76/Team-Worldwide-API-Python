# ShipmentBookingV2ShipmentBookingCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**booked_date** | **datetime** |  | [optional] 
**shipping_mode** | **str** |           [DA] Domestic-Air,          [IA] International-Air,          [O] Ocean,          [T] Domestic/International Truck,          [TLN] Team Line Haul       | [default to '[T] Domestic/International Truck']
**carrier_name** | **str** |  | [optional] 
**origin_code** | **str** |  | [optional] 
**destination_code** | **str** |  | [optional] 
**vendor_code** | **str** |  | [optional] 
**carrier_booking_number** | **str** | Carrier master bill or booking number | [optional] 
**carrier_booking_number2** | **str** | Secondary carrier master bill or booking number | [optional] 
**service** | **str** |           [S] Standard,          [X] Express,          [F] Road Feeder,          [N] Over the Counter,          [W] Weekend,          [T] Truck/Line Haul,          [E] Economy,          [H] Hot Shot,          [K] Full Truck Load,          [L] Less Than Truck Load,          [U] Exclusive Use,          [R] Live Recovery,          [C] Local       | [default to '[S] Standard']
**direct_to_consignee** | **bool** | Ship direct to consignee | [optional] 
**override_measures** | **bool** | Override Pieces/Weight/Volume | [optional] 
**total_pieces** | **int** | Total number of pieces | [optional] 
**total_weight** | **float** | Total weight of all shipments | [optional] 
**departure_date** | **datetime** |  | [optional] 
**departure_time** | **datetime** |  | [optional] 
**arrival_date** | **datetime** |  | [optional] 
**arrival_time** | **datetime** |  | [optional] 
**booking_station** | **str** | The booking station or airport code.  Generally speaking it will be airport code | [optional] 
**general_notes** | **str** | General notes for the booking | [optional] 
**shipments** | [**list[ShipmentShipmentBookingCreate]**](ShipmentShipmentBookingCreate.md) | Shipments | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

