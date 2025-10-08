# GetInventoryItemResponse

This type is used by the response of the <strong>bulkGetInventoryItem</strong> method to give the status of each inventory item record that the user tried to retrieve.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[Error]**](Error.md) | This container will be returned if there were one or more errors associated with retrieving the inventory item record. | [optional] 
**inventory_item** | [**InventoryItemWithSkuLocaleGroupKeys**](InventoryItemWithSkuLocaleGroupKeys.md) |  | [optional] 
**sku** | **str** | The seller-defined Stock-Keeping Unit (SKU) of the inventory item. The seller should have a unique SKU value for every product that they sell. | [optional] 
**status_code** | **int** | The HTTP status code returned in this field indicates the success or failure of retrieving the inventory item record for the inventory item specified in the &lt;strong&gt;sku&lt;/strong&gt; field. See the &lt;strong&gt;HTTP status codes&lt;/strong&gt; table to see which each status code indicates. | [optional] 
**warnings** | [**List[Error]**](Error.md) | This container will be returned if there were one or more warnings associated with retrieving the inventory item record. | [optional] 

## Example

```python
from ebayinventory.models.get_inventory_item_response import GetInventoryItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetInventoryItemResponse from a JSON string
get_inventory_item_response_instance = GetInventoryItemResponse.from_json(json)
# print the JSON string representation of the object
print(GetInventoryItemResponse.to_json())

# convert the object into a dict
get_inventory_item_response_dict = get_inventory_item_response_instance.to_dict()
# create an instance of GetInventoryItemResponse from a dict
get_inventory_item_response_from_dict = GetInventoryItemResponse.from_dict(get_inventory_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


