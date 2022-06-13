# ShipmentV2ShipmentJsonldShipmentCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **OneOfShipmentV2ShipmentJsonldShipmentCreateContext** |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**is_test_shipment** | **bool** | Set true if this is a live shipment | [optional] 
**house_bill** | **str** | If your account is enabled to pre-reserve the house bill,               you must reserve a house bill from the /api/teamww/get-house-bill endpoint.  Leave this property blank and a house bill,              will be generated for you. | [optional] 
**control_branch** | **str** | Control branch.  Can be null. | [optional] 
**company** | **str** |                [01] TAE,               [02] TOS,               [03] TCB,               [05] TWC,               [21] LIB,               [25] PWJ,               [27] RAV           | [default to '[01] TAE']
**shipment_type** | **str** |               [1] Domestic Air,              [2] International Air Export,              [3] International Air Import,              [4] Ocean Export (FMC),              [5] Ocean Export (NVOCC),              [6] Ocean Import (FMC),              [7] Ocean Import (NVOCC),              [8] Domestic Truck,              [19] Domestic Warehouse,              [20] Ocean Warehouse,              [21] International Warehouse,              [22] Intl Customs Brokerage,              [23] Ocean Customs Brokerage,              [24] Ocean Import (Unregulated),              [25] Ocean Export (Unregulated),              [26] International Truck Import,              [27] International Truck Export,              [30] International Truck,              [31] International Air,              [32] Ocean Unregulated           | [default to '[8] Domestic Truck']
**service** | **str** |           [D] Same Day,          [N] Over The Counter,          [A] Overnight AM,          [P] Overnight PM,          [R] International Express,          [T] International Standard,          [M] International Economy,          [O] Other,          [Q] Charter,          [S] Standard,          [2] Standard 2 (2-day),          [3] Economy (3-day),          [5] Deferred (4-5 day),          [L] LTL,          [F] FTL,          [U] EUV/Hotshot | [default to '[3] Economy (3-day)']
**pickup_date** | **datetime** | Pickup date YYYY-MM-DD | 
**origin** | **str** | Origin location. Must be a valid Team Worldwide origin. | [optional] 
**destination** | **str** | Destination location.  Must be a valid Team Worldwide destination | [optional] 
**linear_units** | **str** | Acceptable values are IN and CM | [default to 'IN']
**weight_units** | **str** | Acceptable values are LB and KG | [default to 'LB']
**oversize** | **str** | Is the shipment oversize? | [optional] [default to 'N']
**goods_description** | **str** | Description of the goods | 
**weight** | **float** |  | [optional] 
**special_instructions** | **str** | Special instructions | [optional] 
**declared_value** | **float** | Declared value | [optional] 
**shipper** | [**ShipperJsonldShipmentCreate**](ShipperJsonldShipmentCreate.md) |  | 
**consignee** | [**ConsigneeJsonldShipmentCreate**](ConsigneeJsonldShipmentCreate.md) |  | 
**bill_to** | **AnyOfShipmentV2ShipmentJsonldShipmentCreateBillTo** | Billing party of this shipment | [optional] 
**requested_pickup** | **AnyOfShipmentV2ShipmentJsonldShipmentCreateRequestedPickup** | Requested pickup | [optional] 
**requested_delivery** | **AnyOfShipmentV2ShipmentJsonldShipmentCreateRequestedDelivery** | Request delivery | [optional] 
**shipment_goods** | [**list[ShipmentGoodsJsonldShipmentCreate]**](ShipmentGoodsJsonldShipmentCreate.md) | Shipment goods | [optional] 
**shipment_goods_handling** | [**list[ShipmentGoodsHandlingJsonldShipmentCreate]**](ShipmentGoodsHandlingJsonldShipmentCreate.md) | Shipment goods handling | [optional] 
**shipment_notes** | [**list[ShipmentNoteResourceJsonldShipmentCreate]**](ShipmentNoteResourceJsonldShipmentCreate.md) | Shipment notes | [optional] 
**additional_references** | [**list[ShipmentAdditionalReferencesJsonldShipmentCreate]**](ShipmentAdditionalReferencesJsonldShipmentCreate.md) | Any additional references for this shipment | [optional] 
**projected_expenses** | [**list[ProjectedExpenseJsonldShipmentCreate]**](ProjectedExpenseJsonldShipmentCreate.md) | Projected Expenses | [optional] 
**projected_customer_charges** | [**list[ProjectedCustomerChargeJsonldShipmentCreate]**](ProjectedCustomerChargeJsonldShipmentCreate.md) | Projected customer charges | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

