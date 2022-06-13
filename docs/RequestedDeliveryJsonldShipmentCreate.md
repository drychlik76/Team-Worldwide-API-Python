# RequestedDeliveryJsonldShipmentCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **OneOfRequestedDeliveryJsonldShipmentCreateContext** |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**type** | **str** |           [R] Regular Delivery,          [M] Must Delivery,          [S] Special Delivery,          [D] Direct to Consignee,          [H] Hold on Dock       | 
**_date** | **datetime** | Delivery date YYYY-MM-DD | 
**from_time** | **datetime** | Time between | 
**to_time** | **datetime** | Time between | 
**on_by** | **str** |           [O] On,           [B] By           | [default to '[B] By']
**notes** | **str** | Requested pickup related notes | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

