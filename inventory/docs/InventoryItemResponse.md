# InventoryItemResponse

This type is used by the response of the <strong>bulkCreateOrReplaceInventoryItem</strong> method to indicate the success or failure of creating and/or updating each inventory item record. The <strong>sku</strong> value in this type identifies each inventory item record.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[Error]**](Error.md) | This container will be returned if there were one or more errors associated with the creation or update to the inventory item record. | [optional] 
**locale** | **str** | This field returns the natural language that was provided in the field values of the request payload (i.e., en_AU, en_GB or de_DE). For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/inventory/types/slr:LocaleEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**sku** | **str** | The seller-defined Stock-Keeping Unit (SKU) of the inventory item. The seller should have a unique SKU value for every product that they sell. | [optional] 
**status_code** | **int** | The HTTP status code returned in this field indicates the success or failure of creating or updating the inventory item record for the inventory item indicated in the &lt;strong&gt;sku&lt;/strong&gt; field. See the &lt;strong&gt;HTTP status codes&lt;/strong&gt; table to see which each status code indicates. | [optional] 
**warnings** | [**List[Error]**](Error.md) | This container will be returned if there were one or more warnings associated with the creation or update to the inventory item record. | [optional] 

## Example

```python
from ebayinventory.models.inventory_item_response import InventoryItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryItemResponse from a JSON string
inventory_item_response_instance = InventoryItemResponse.from_json(json)
# print the JSON string representation of the object
print(InventoryItemResponse.to_json())

# convert the object into a dict
inventory_item_response_dict = inventory_item_response_instance.to_dict()
# create an instance of InventoryItemResponse from a dict
inventory_item_response_from_dict = InventoryItemResponse.from_dict(inventory_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


