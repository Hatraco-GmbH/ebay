# BulkMigrateListingResponse

This type is used by the response payload of the <strong>bulkMigrateListings</strong> call.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**responses** | [**List[MigrateListingResponse]**](MigrateListingResponse.md) | This is the base container of the response payload of the &lt;strong&gt;bulkMigrateListings&lt;/strong&gt; call. The results of each attempted listing migration is captured under this container. | [optional] 

## Example

```python
from ebayinventory.models.bulk_migrate_listing_response import BulkMigrateListingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkMigrateListingResponse from a JSON string
bulk_migrate_listing_response_instance = BulkMigrateListingResponse.from_json(json)
# print the JSON string representation of the object
print(BulkMigrateListingResponse.to_json())

# convert the object into a dict
bulk_migrate_listing_response_dict = bulk_migrate_listing_response_instance.to_dict()
# create an instance of BulkMigrateListingResponse from a dict
bulk_migrate_listing_response_from_dict = BulkMigrateListingResponse.from_dict(bulk_migrate_listing_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


