# BulkInventoryItemResponse

This type is used by the base response of the <strong>bulkCreateOrReplaceInventoryItem</strong> method.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**responses** | [**List[InventoryItemResponse]**](InventoryItemResponse.md) | This is the base container of the &lt;strong&gt;bulkCreateOrReplaceInventoryItem&lt;/strong&gt; response. The results of each attempted inventory item creation/update is captured under this container. | [optional] 

## Example

```python
from ebayinventory.models.bulk_inventory_item_response import BulkInventoryItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkInventoryItemResponse from a JSON string
bulk_inventory_item_response_instance = BulkInventoryItemResponse.from_json(json)
# print the JSON string representation of the object
print(BulkInventoryItemResponse.to_json())

# convert the object into a dict
bulk_inventory_item_response_dict = bulk_inventory_item_response_instance.to_dict()
# create an instance of BulkInventoryItemResponse from a dict
bulk_inventory_item_response_from_dict = BulkInventoryItemResponse.from_dict(bulk_inventory_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


