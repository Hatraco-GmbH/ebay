# MigrateListing

This type is used to specify one to five eBay listings that will be migrated to the new Inventory model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**listing_id** | **str** | The unique identifier of the eBay listing to migrate to the new Inventory model. In the Trading API, this field is known as the &lt;strong&gt;ItemID&lt;/strong&gt;.&lt;br&gt;&lt;br&gt;Up to five unique eBay listings may be specified here in separate &lt;strong&gt;listingId&lt;/strong&gt; fields. The seller should make sure that each of these listings meet the requirements that are stated at the top of this Call Reference page. | [optional] 

## Example

```python
from ebayinventory.models.migrate_listing import MigrateListing

# TODO update the JSON string below
json = "{}"
# create an instance of MigrateListing from a JSON string
migrate_listing_instance = MigrateListing.from_json(json)
# print the JSON string representation of the object
print(MigrateListing.to_json())

# convert the object into a dict
migrate_listing_dict = migrate_listing_instance.to_dict()
# create an instance of MigrateListing from a dict
migrate_listing_from_dict = MigrateListing.from_dict(migrate_listing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


