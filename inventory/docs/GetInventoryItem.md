# GetInventoryItem

The seller-defined Stock-Keeping Unit (SKU) of each inventory item that the user wants to retrieve is passed in the request of the <strong>bulkGetInventoryItem</strong> method.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sku** | **str** | An array of SKU values are passed in under the &lt;strong&gt;sku&lt;/strong&gt; container to retrieve up to 25 inventory item records.&lt;br&gt;&lt;br&gt;Use the &lt;a href&#x3D;\&quot;/api-docs/sell/inventory/resources/inventory_item/methods/getInventoryItems\&quot; target&#x3D;\&quot;_blank \&quot;&gt;getInventoryItems&lt;/a&gt; method to retrieve SKU values. | [optional] 

## Example

```python
from ebayinventory.models.get_inventory_item import GetInventoryItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetInventoryItem from a JSON string
get_inventory_item_instance = GetInventoryItem.from_json(json)
# print the JSON string representation of the object
print(GetInventoryItem.to_json())

# convert the object into a dict
get_inventory_item_dict = get_inventory_item_instance.to_dict()
# create an instance of GetInventoryItem from a dict
get_inventory_item_from_dict = GetInventoryItem.from_dict(get_inventory_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


