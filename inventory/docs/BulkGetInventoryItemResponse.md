# BulkGetInventoryItemResponse

This type is used by the base response of the <strong>bulkGetInventoryItem</strong> method.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**responses** | [**List[GetInventoryItemResponse]**](GetInventoryItemResponse.md) | This is the base container of the &lt;strong&gt;bulkGetInventoryItem&lt;/strong&gt; response. The results of each attempted inventory item retrieval is captured under this container. | [optional] 

## Example

```python
from ebayinventory.models.bulk_get_inventory_item_response import BulkGetInventoryItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkGetInventoryItemResponse from a JSON string
bulk_get_inventory_item_response_instance = BulkGetInventoryItemResponse.from_json(json)
# print the JSON string representation of the object
print(BulkGetInventoryItemResponse.to_json())

# convert the object into a dict
bulk_get_inventory_item_response_dict = bulk_get_inventory_item_response_instance.to_dict()
# create an instance of BulkGetInventoryItemResponse from a dict
bulk_get_inventory_item_response_from_dict = BulkGetInventoryItemResponse.from_dict(bulk_get_inventory_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


