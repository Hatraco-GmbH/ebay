# BulkGetInventoryItem

This type is used by the base request of the <strong>bulkGetInventoryItem</strong> method.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**List[GetInventoryItem]**](GetInventoryItem.md) | The seller passes in multiple SKU values under this container to retrieve multiple inventory item records. Up to 25 inventory item records can be retrieved at one time. | [optional] 

## Example

```python
from ebayinventory.models.bulk_get_inventory_item import BulkGetInventoryItem

# TODO update the JSON string below
json = "{}"
# create an instance of BulkGetInventoryItem from a JSON string
bulk_get_inventory_item_instance = BulkGetInventoryItem.from_json(json)
# print the JSON string representation of the object
print(BulkGetInventoryItem.to_json())

# convert the object into a dict
bulk_get_inventory_item_dict = bulk_get_inventory_item_instance.to_dict()
# create an instance of BulkGetInventoryItem from a dict
bulk_get_inventory_item_from_dict = BulkGetInventoryItem.from_dict(bulk_get_inventory_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


