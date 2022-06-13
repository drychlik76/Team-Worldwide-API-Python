# ShipmentGoodsShipmentCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**pieces** | **int** |  | [default to 1]
**length** | **float** |  | [optional] 
**height** | **float** |  | [optional] 
**width** | **float** |  | [optional] 
**item_weight** | **float** |  | [optional] 
**is_dangerous_goods** | **bool** | Need to know if this a dangerous goods shipment | 
**dangerous_goods_description** | **str** | If is dangerous goods, a description is required | [optional] 
**package_type** | **str** |            [P] Piece,           [G] Bag,           [B] Box,           [K] Case,           [T] Tube,           [C] Crate,           [L] Loose,           [E] Pallet,           [S] Skid,           [U] Tub,           [D] Drum,           [N] Container          | 
**container_type** | **str** | Container Type | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

