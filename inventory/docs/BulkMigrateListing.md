# BulkMigrateListing

This type is used by the base container of the <strong>bulkMigrateListings</strong> request payload.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**List[MigrateListing]**](MigrateListing.md) | This is the base container of the &lt;strong&gt;bulkMigrateListings&lt;/strong&gt; request payload. One to five eBay listings will be included under this container. | [optional] 

## Example

```python
from ebayinventory.models.bulk_migrate_listing import BulkMigrateListing

# TODO update the JSON string below
json = "{}"
# create an instance of BulkMigrateListing from a JSON string
bulk_migrate_listing_instance = BulkMigrateListing.from_json(json)
# print the JSON string representation of the object
print(BulkMigrateListing.to_json())

# convert the object into a dict
bulk_migrate_listing_dict = bulk_migrate_listing_instance.to_dict()
# create an instance of BulkMigrateListing from a dict
bulk_migrate_listing_from_dict = BulkMigrateListing.from_dict(bulk_migrate_listing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


