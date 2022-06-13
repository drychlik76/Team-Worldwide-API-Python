# GetRate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unique_id** | **str** |  | [optional] 
**origin_city** | **str** |  | 
**origin_state** | **str** |  | 
**origin_zip_code** | **str** |  | 
**origin_country** | **str** |  | 
**destination_city** | **str** |  | 
**destination_state** | **str** |  | 
**destination_zip_code** | **str** |  | 
**destination_country** | **str** |  | 
**freight** | [**list[Freight]**](Freight.md) |  | 
**unit_of_measure** | **str** |  | [default to 'US']
**team_book_accessorials** | **list[str]** | Array of accessorial codes. Refer to enabledAccessorials returned in /api/team-book/get-accessorials. Provide the code. | [optional] 
**pickup_date** | **datetime** |  | [optional] 
**rate_type_list** | **list[str]** |  | [optional] 
**equipment** | **str** |  | [optional] 
**insurance_add_on** | **bool** |  | [optional] 
**insure_freight** | **bool** |  | [optional] 
**insurance_amount** | **float** |  | [optional] 
**linear_feet** | **float** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

