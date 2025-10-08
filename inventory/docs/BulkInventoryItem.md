# BulkInventoryItem

The base request of the <strong>bulkCreateOrReplaceInventoryItem</strong> method.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**List[InventoryItemWithSkuLocale]**](InventoryItemWithSkuLocale.md) | The details of each inventory item that is being created or updated is passed in under this container. Up to 25 inventory item records can be created and/or updated with one &lt;strong&gt;bulkCreateOrReplaceInventoryItem&lt;/strong&gt; call. | [optional] 

## Example

```python
from ebayinventory.models.bulk_inventory_item import BulkInventoryItem

# TODO update the JSON string below
json = "{}"
# create an instance of BulkInventoryItem from a JSON string
bulk_inventory_item_instance = BulkInventoryItem.from_json(json)
# print the JSON string representation of the object
print(BulkInventoryItem.to_json())

# convert the object into a dict
bulk_inventory_item_dict = bulk_inventory_item_instance.to_dict()
# create an instance of BulkInventoryItem from a dict
bulk_inventory_item_from_dict = BulkInventoryItem.from_dict(bulk_inventory_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


