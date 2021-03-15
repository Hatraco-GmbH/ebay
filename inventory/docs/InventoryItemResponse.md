# InventoryItemResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**list[Error]**](Error.md) | This container will be returned if there were one or more errors associated with the creation or update to the inventory item record. | [optional] 
**locale** | **str** | This field is for future use only. For implementation help, refer to &lt;a href&#x3D;&#x27;https://developer.ebay.com/api-docs/sell/inventory/types/slr:LocaleEnum&#x27;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**sku** | **str** | The seller-defined Stock-Keeping Unit (SKU) of the inventory item. The seller should have a unique SKU value for every product that they sell. | [optional] 
**status_code** | **int** | The HTTP status code returned in this field indicates the success or failure of creating or updating the inventory item record for the inventory item indicated in the sku field. See the HTTP status codes table to see which each status code indicates. | [optional] 
**warnings** | [**list[Error]**](Error.md) | This container will be returned if there were one or more warnings associated with the creation or update to the inventory item record. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

