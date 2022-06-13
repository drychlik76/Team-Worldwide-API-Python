# BookShipmentTeamBookShipmentCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quote_id** | **int** |  | [optional] 
**house_bill** | **str** | Reserve a house bill from either /api/teamww/get-house-bill or get one from /api/team-book/get-quote/{rateId} | 
**bol_prefix** | **str** | Leave this null. This is used in special cases. | [optional] 
**insurance_addon** | **bool** |  | [optional] 
**third_party_reference_number** | **str** |  | [optional] 
**pro_number** | **str** |  | [optional] 
**team_book_shipper** | [**TeamBookShipperTeamBookShipmentCreate**](TeamBookShipperTeamBookShipmentCreate.md) |  | [optional] 
**team_book_consignee** | [**TeamBookConsigneeTeamBookShipmentCreate**](TeamBookConsigneeTeamBookShipmentCreate.md) |  | [optional] 
**broker_information** | **AnyOfBookShipmentTeamBookShipmentCreateBrokerInformation** |  | [optional] 
**instructions** | **str** |  | [optional] 
**shipment_notes** | **str** |  | [optional] 
**emergency_contact** | **str** | Emergency Contact. Required if a shipment has hazardous materials. | [optional] 
**emergency_phone** | **str** | Emergency Phone Number. Required if a shipment has hazardous materials. | [optional] 
**unit_of_measure** | **str** | Unit of Measure. Valid values: US (lbs/in) - METRIC (kgs/cm) - MIXED (kgs/cms) | [optional] [default to 'US']
**shipment_reference1** | **str** |  | [optional] 
**shipment_reference2** | **str** |  | [optional] 
**pickup** | [**PickupTeamBookShipmentCreate**](PickupTeamBookShipmentCreate.md) |  | 
**delivery** | **AnyOfBookShipmentTeamBookShipmentCreateDelivery** |  | [optional] 
**team_book_accessorials** | **list[str]** | Array of accessorial codes. Refer to enabledAccessorials returned in /api/team-book/get-accessorials. Provide the code. | [optional] 
**freight** | [**list[FreightTeamBookShipmentCreate]**](FreightTeamBookShipmentCreate.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

