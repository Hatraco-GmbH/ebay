# InventoryItemListing

This type is used by the <strong>inventoryItems</strong> container that is returned in the response of the <strong>bulkMigrateListing</strong> call. Up to five <strong>sku</strong>/<strong>offerId</strong> pairs may be returned under the <strong>inventoryItems</strong> container, dependent on how many eBay listings the seller is attempting to migrate to the inventory model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_id** | **str** | Upon a successful migration of a listing, eBay auto-generates this unique identifier, and this offer ID value will be used to retrieve and manage the newly-created offer object. This value will only be generated and returned if the eBay listing is migrated successfully. | [optional] 
**sku** | **str** | This is the seller-defined SKU value associated with the item(s) in a listing. This same SKU value will be used to retrieve and manage the newly-created inventory item object if the listing migration is successful. This SKU value will get returned even if the migration is not successful. | [optional] 

## Example

```python
from ebayinventory.models.inventory_item_listing import InventoryItemListing

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryItemListing from a JSON string
inventory_item_listing_instance = InventoryItemListing.from_json(json)
# print the JSON string representation of the object
print(InventoryItemListing.to_json())

# convert the object into a dict
inventory_item_listing_dict = inventory_item_listing_instance.to_dict()
# create an instance of InventoryItemListing from a dict
inventory_item_listing_from_dict = InventoryItemListing.from_dict(inventory_item_listing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


