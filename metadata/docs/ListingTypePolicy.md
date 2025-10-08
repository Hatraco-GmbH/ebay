# ListingTypePolicy

This type contains the policies governing the listing type by category.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_id** | **str** | The unique identifier of the eBay leaf category for which metadata is being returned. | [optional] 
**category_tree_id** | **str** | The unique identifier of the category tree. | [optional] 
**digital_good_delivery_enabled** | **bool** | A &lt;code&gt;true&lt;/code&gt; value in this field indicates that the leaf category supports the listing of items (such as gift cards) that can be delivered electronically via a download link or sent to a buyer&#39;s email address. | [optional] 
**listing_durations** | [**List[ListingDuration]**](ListingDuration.md) | An array of eBay listing types and the supported durations for the corresponding leaf category. If a specific eBay listing type does not appear for a leaf category, it indicates that the category does not support that listing type. | [optional] 
**pickup_drop_off_enabled** | **bool** | A true value in this field indicates that items listed in the category (specified in the &lt;b&gt;listingTypePolicies.categoryId&lt;/b&gt; field) may be enabled with the &#39;Click and Collect&#39; feature. With the &#39;Click and Collect&#39; feature, a buyer can purchase certain items on an eBay site and collect them at a local store. Buyers are notified by eBay once their items are available. A false value in this field indicates that items listed in the category are not eligible for the &#39;Click and Collect&#39; feature. | [optional] 

## Example

```python
from ebaymetadata.models.listing_type_policy import ListingTypePolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ListingTypePolicy from a JSON string
listing_type_policy_instance = ListingTypePolicy.from_json(json)
# print the JSON string representation of the object
print(ListingTypePolicy.to_json())

# convert the object into a dict
listing_type_policy_dict = listing_type_policy_instance.to_dict()
# create an instance of ListingTypePolicy from a dict
listing_type_policy_from_dict = ListingTypePolicy.from_dict(listing_type_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


